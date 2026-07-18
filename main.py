import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load environment configuration
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("⚠️ Environment Setup Error: GROQ_API_KEY environment variable not found.")

# Initialize the Groq inference engine client
client = Groq(api_key=my_api_key)

# Configure model hyperparameters 
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0.7

# Define the expert behavior system instructions 
SYSTEM_INSTRUCTION = {
    "role": "system",
    "content": (
        "You are an expert fashion brand manager and retail strategist. Your goal is to help "
        "the user build, name, and scale their clothing company. Provide precise, creative, "
        "and actionable business advice. When suggesting names, keep them sharp and modern."
    )
}

def generate_assistant_response(conversation_history):
    """Dispatches payload to Groq API and parses the token stream payload response."""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=conversation_history,
            temperature=TEMPERATURE
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🚨 API Execution Error: {str(e)}"

def run_assistant_loop():
    """Main execution thread maintaining chat session history via the terminal."""
    print("================================================================")
    print("🧥 Groq AI Clothing Brand Manager Active 🚀")
    print("Type 'exit' or 'quit' at any time to close the session.")
    print("================================================================")
    
    # Initialize the conversation architecture with system rules
    messages = [SYSTEM_INSTRUCTION]
    
    while True:
        user_prompt = input("\nYou: ").strip()
        
        # Check termination constraints
        if not user_prompt:
            continue
        if user_prompt.lower() in ['exit', 'quit']:
            print("\n👋 Closing brand manager session. Happy building!")
            break
            
        # Append latest interaction context to historical tracking array
        messages.append({"role": "user", "content": user_prompt})
        
        print("\nAssistant is thinking...")
        ai_response = generate_assistant_response(messages)
        
        # Display extracted response content stream
        print(f"\nAI Brand Manager:\n{ai_response}")
        
        # Store context window to retain conversation state memory
        messages.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    run_assistant_loop()
