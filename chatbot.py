import requests
from persona_data import personas_dict

url = "http://localhost:11434/api/chat"
model = "llama3"

# Persona selection
persona_choice = input("Choose a persona (healthcare, banking, personal_shopper, travel_agent): ").strip().lower()
prompt_stack = personas_dict.get(persona_choice, personas_dict["healthcare"])

chat_history = [{"role": "system", "content": prompt_stack}]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    chat_history.append({"role": "user", "content": user_input})

    response = requests.post(url, json={
        "model": model,
        "messages": chat_history,
        "stream": False
    })

    result = response.json()
    bot_message = result["message"]["content"]
    print("Bot:", bot_message)

    chat_history.append({"role": "assistant", "content": bot_message})
