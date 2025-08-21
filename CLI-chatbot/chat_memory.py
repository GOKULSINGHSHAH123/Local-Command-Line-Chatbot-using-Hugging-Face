import warnings
warnings.filterwarnings("ignore", category=UserWarning)
class ChatMemory:
    def __init__(self, window_size=3):
        self.window_size = window_size
        self.conversation_history = []
        
    def add_exchange(self, user_input, bot_response):
        """Add a user-bot exchange to the history"""
        self.conversation_history.append({"user": user_input, "bot": bot_response})
        
        # Maintain the sliding window
        if len(self.conversation_history) > self.window_size:
            self.conversation_history.pop(0)
    
    def get_context(self):
        """Format the conversation history as context for the model"""
        if not self.conversation_history:
            return ""
            
        context = "Previous conversation:\n"
        for exchange in self.conversation_history:
            context += f"User: {exchange['user']}\nAssistant: {exchange['bot']}\n"
            
        return context.strip()
    
    def clear_memory(self):
        """Clear the conversation history"""
        self.conversation_history = []
        
    def get_history_length(self):
        """Return the number of exchanges in memory"""
        return len(self.conversation_history)