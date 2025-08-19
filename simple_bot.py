import cohere
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Load static context from text file
with open(
"file.txt", "r", encoding="utf-8") as f:
    context = f.read()

# Chat history
chat_history = []

# System message
system_msg = "You are a helpful assistant."

# Chat loop
print("Start chatting (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: successfully exit!")
        break
    if not user_input.strip():
        print("Bot: Please type something.")
        continue

    # Send to Cohere
    response = co.chat(
        model="command-r",
        message=user_input,
        temperature=0.6,
        documents=[{"text": context}],
        chat_history=chat_history,
        preamble=system_msg,
        
    )

    # Output and save to memory
    bot_reply = response.text.strip()
    print("Bot:", bot_reply)
    chat_history.append({"role": "USER", "message": user_input})
    chat_history.append({"role": "CHATBOT", "message": bot_reply})
