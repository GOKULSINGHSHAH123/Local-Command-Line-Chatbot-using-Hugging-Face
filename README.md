# Local Command-Line Chatbot using Hugging Face

A simple yet powerful command-line chatbot built with Hugging Face Transformers, featuring conversation memory and local model execution.

## Features

- **Local Model Execution**: Runs entirely on your machine using Hugging Face models
- **Conversation Memory**: Maintains context with a sliding window of recent exchanges
- **Multiple Model Support**: Compatible with various Hugging Face seq2seq models
- **GPU/CPU Support**: Automatically detects and uses available hardware
- **Interactive Commands**: Built-in commands for better user experience
- **Memory Management**: Configurable conversation history window

## Project Structure

```
├── chat_memory.py      # Handles conversation history and context
├── model_loader.py     # Manages model loading and response generation
├── main.py            # Main chat interface and user interaction
└── requirements.txt   # Project dependencies
```

## Requirements

- Python 3.7+
- PyTorch
- Transformers library
- CUDA (optional, for GPU acceleration)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GOKULSINGHSHAH123/Local-Command-Line-Chatbot-using-Hugging-Face.git
   cd Local-Command-Line-Chatbot-using-Hugging-Face
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv chatbot_env
   source chatbot_env/bin/activate  # On Windows: chatbot_env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Run the chatbot with the default model:
```bash
python main.py
```

### Custom Model

You can modify the model in `main.py` or create a custom instance:
```python
chat = ChatInterface(model_name="google/flan-t5-base")  # Smaller model
# or
chat = ChatInterface(model_name="google/flan-t5-xl")    # Larger model
```

### Available Commands

While chatting, you can use these commands:

- `/exit` - Exit the chatbot
- `/clear` - Clear conversation memory
- `/help` - Show available commands

### Example Session

```
Loading model and tokenizer...
Using device: cuda
Model loaded successfully!

Chatbot started! Type '/exit' to quit, '/clear' to clear memory.

User: Hello, how are you?
Bot: I'm doing well, thank you for asking! How can I help you today?

User: What's the weather like?
Bot: I don't have access to real-time weather data, but I can help you with other questions or tasks.

User: /clear
Bot: Memory cleared. Let's start fresh!

User: /exit
Exiting chatbot. Goodbye!
```

## Configuration Options

### Memory Window Size

Adjust the conversation history window:
```python
chat = ChatInterface(memory_window=5)  # Remember last 5 exchanges
```

### Model Selection

Popular model options:
- `google/flan-t5-small` - Fastest, least memory
- `google/flan-t5-base` - Balanced performance
- `google/flan-t5-large` - Default, good quality
- `google/flan-t5-xl` - Best quality, more resources needed

### Generation Parameters

Modify response generation in `model_loader.py`:
```python
outputs = self.model.generate(
    **inputs,
    max_new_tokens=150,      # Maximum response length
    num_beams=5,             # Beam search width
    repetition_penalty=1.2   # Avoid repetitive responses
)
```

## System Requirements

### Minimum Requirements
- RAM: 4GB
- Storage: 2GB free space
- Python 3.7+

### Recommended Requirements
- RAM: 8GB+ (for larger models)
- GPU: NVIDIA GPU with 4GB+ VRAM (optional)
- Storage: 5GB+ free space

## Model Performance

| Model | Size | RAM Usage | Speed | Quality |
|-------|------|-----------|-------|---------|
| flan-t5-small | ~250MB | ~1GB | Fast | Basic |
| flan-t5-base | ~900MB | ~2GB | Medium | Good |
| flan-t5-large | ~3GB | ~4GB | Slower | Better |
| flan-t5-xl | ~11GB | ~12GB | Slowest | Best |

## Troubleshooting

### Common Issues

1. **CUDA Out of Memory**:
   - Switch to a smaller model
   - Use CPU instead: Set `CUDA_VISIBLE_DEVICES=""`

2. **Slow Response Times**:
   - Use a smaller model
   - Enable GPU acceleration
   - Reduce `max_new_tokens` parameter

3. **Model Loading Fails**:
   - Check internet connection (first download)
   - Ensure sufficient disk space
   - Try a different model

### Error Messages

- `"Failed to load model"` - Check model name and internet connection
- `"CUDA out of memory"` - Use smaller model or CPU
- `"Error generating response"` - Input may be too long

## Customization

### Adding New Models

To use different models, ensure they're compatible with `AutoModelForSeq2SeqLM`:
```python
# Examples of compatible models
"t5-small"
"t5-base" 
"google/flan-t5-base"
"facebook/blenderbot-400M-distill"
```

### Extending Functionality

You can extend the chatbot by:
- Adding new commands in `ChatInterface.start_chat()`
- Implementing different memory strategies in `ChatMemory`
- Adding response post-processing in `ModelLoader`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the repository for license details.

## Support

For issues and questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review Hugging Face documentation

## Acknowledgments

- Built with [Hugging Face Transformers](https://huggingface.co/transformers/)
- Uses Google's FLAN-T5 models
- Powered by PyTorch

---

**Note**: First-time model loading requires internet connection to download models from Hugging Face Hub. Subsequent runs can work offline.
