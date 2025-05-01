import streamlit as st
import requests
import json

# Set up page config
st.set_page_config(page_title="AI Chatbot Personas", page_icon="🤖", layout="wide")

# Custom CSS for some extra spacing and clean visuals
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        border: 1px solid #ccc;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
    .stTextArea textarea {
        border: 1px solid #ccc;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Persona utilities
def load_personas():
    try:
        with open('personas.json', 'r') as f:
            data = json.load(f)
            return data.get('user_personas', {})
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_persona(persona_name, persona_description):
    personas = load_personas()
    personas[persona_name] = persona_description
    with open('personas.json', 'w') as f:
        json.dump({"user_personas": personas}, f, indent=4)

def edit_persona(persona_name, new_description):
    personas = load_personas()
    if persona_name in personas:
        personas[persona_name] = new_description
        with open('personas.json', 'w') as f:
            json.dump({"user_personas": personas}, f, indent=4)

def delete_persona(persona_name):
    personas = load_personas()
    if persona_name in personas:
        del personas[persona_name]
        with open('personas.json', 'w') as f:
            json.dump({"user_personas": personas}, f, indent=4)

# Load personas
personas = load_personas()

# Title & Introduction
st.title("🤖 AI Chatbot Personas")

# Persona Creator Section
with st.container():
    st.subheader("🎨 Create a New Persona")
    persona_name = st.text_input("Persona Name")
    persona_description = st.text_area("Persona Description")

    if st.button("Save Persona"):
        if persona_name and persona_description:
            save_persona(persona_name, persona_description)
            st.success(f"Persona '{persona_name}' created successfully!")
        else:
            st.error("Please provide both a name and description.")

st.markdown("---")  # Horizontal line

# Persona Selector
with st.container():
    st.subheader("🗂️ Select a Persona")

    all_personas = list(personas.keys()) + ["healthcare", "banking", "personal_shopper", "travel_agent"]
    persona_choice = st.selectbox("Available Personas:", all_personas)

    prompt_stack = personas.get(persona_choice, "Default persona")

st.markdown("---")

# Chat Interface
with st.container():
    st.subheader("💬 Chat with AI")

    chat_history = [{"role": "system", "content": prompt_stack}]
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        chat_history.append({"role": "user", "content": user_input})

        url = "http://localhost:11434/api/chat"
        model = "llama3"
        response = requests.post(url, json={
            "model": model,
            "messages": chat_history,
            "stream": False
        })

        result = response.json()
        bot_message = result.get("message", {}).get("content", "⚠️ No response received.")
        chat_history.append({"role": "assistant", "content": bot_message})

        st.markdown("### Conversation History")
        for message in chat_history:
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**Bot:** {message['content']}")

st.markdown("---")

# Edit & Delete Features
if persona_choice not in ["healthcare", "banking", "personal_shopper", "travel_agent"]:
    with st.container():
        st.subheader(f"✏️ Edit or ❌ Delete '{persona_choice}'")

        persona_edit_name = st.text_input(f"Edit '{persona_choice}' Description", personas.get(persona_choice, ""))

        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Save Edit for {persona_choice}"):
                if persona_edit_name:
                    edit_persona(persona_choice, persona_edit_name)
                    st.success(f"Persona '{persona_choice}' updated successfully!")
                else:
                    st.error("Please provide a new description.")
        with col2:
            if st.button(f"Delete {persona_choice}"):
                delete_persona(persona_choice)
                st.success(f"Persona '{persona_choice}' deleted successfully.")

