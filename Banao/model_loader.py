from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

class ModelLoader:
    def __init__(self, model_name="google/flan-t5-large"):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.device = None
        
    def load_model(self):
        """Load the model and tokenizer"""
        try:
            print("Loading model and tokenizer...")
            
            # Detect device
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            print(f"Using device: {self.device}")
            
            # Load tokenizer and model
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name).to(self.device)
            
            print("Model loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def generate_response(self, input_text, max_new_tokens=150):
        """Generate a response using the loaded model"""
        if not self.model or not self.tokenizer:
            return "Error: Model not loaded properly."
            
        try:
            # Format the input with a prompt template
            prompt = f"Answer the following question concisely: {input_text}"
            
            # Tokenize input
            inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True).to(self.device)
            
            # Generate response
            outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            num_beams=5,            # Beam search
            repetition_penalty=1.2  # Avoid repetition
        )

            
            # Decode the response
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response
            
        except Exception as e:
            return f"Error generating response: {e}"