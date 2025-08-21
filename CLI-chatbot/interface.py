from model_loader import ModelLoader
from chat_memory import ChatMemory
import sys
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)



class ChatInterface:
    def __init__(self, model_name="google/flan-t5-large", memory_window=3):
        self.model_loader = ModelLoader(model_name)
        self.memory = ChatMemory(memory_window)
        self.is_running = False
        
    def start_chat(self):
        """Start the chat interface"""
        # Load the model
        if not self.model_loader.load_model():
            print("Failed to load model. Exiting.")
            return
            
        self.is_running = True
        print("\nChatbot started! Type '/exit' to quit, '/clear' to clear memory.\n")
        
        while self.is_running:
            try:
                # Get user input
                user_input = input("User: ").strip()
                
                # Check for exit command
                if user_input.lower() == "/exit":
                    self.stop_chat()
                    continue
                
                # Check for clear memory command
                if user_input.lower() == "/clear":
                    self.memory.clear_memory()
                    print("Bot: Memory cleared. Let's start fresh!\n")
                    continue
                
                # Check for help command
                if user_input.lower() == "/help":
                    print("Bot: Available commands:\n  /exit - Exit the chatbot\n  /clear - Clear conversation memory\n  /help - Show this help message\n")
                    continue
                
                # Generate response with context
                context = self.memory.get_context()
                
                # For FLAN-T5, we need to format the input appropriately
                if context:
                    full_input = f"{context}\n\nNew question: {user_input}"
                else:
                    full_input = user_input
                
                bot_response = self.model_loader.generate_response(full_input)
                
                # Print response
                print(f"Bot: {bot_response}\n")
                
                # Add to memory
                self.memory.add_exchange(user_input, bot_response)
                
            except KeyboardInterrupt:
                self.stop_chat()
            except Exception as e:
                print(f"Error: {e}")
    
    def stop_chat(self):
        """Stop the chat interface"""
        self.is_running = False
        print("\nExiting chatbot. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    # Use a smaller model if you have limited resources
    chat = ChatInterface(model_name="google/flan-t5-large")
    chat.start_chat()