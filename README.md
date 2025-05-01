# AI Chatbot with Customizable Personas 🤖

A simple AI chatbot built with Streamlit, allowing users to create, edit, delete, and chat with custom personas. Powered by a local LLaMA model API.

## Features:
- Create custom AI personas
- Edit and delete personas
- Chat interface with selectable personas
- Streamlit web UI

## Requirements:
- Python 3.9+
- Install dependencies via `pip install -r requirements.txt`

## Run Locally:
```bash
streamlit run app.py


---------------------------------------

🤖 AI Chatbot Personas
A customizable AI chatbot web application built with Python, Streamlit, and LLaMA 3 via a local Ollama API. This project allows users to interact with multiple predefined chatbot personas or create and manage their own unique personas for dynamic, tailored conversations.

📸 Project Preview
<!-- optional if you add a screenshot image to your repo -->

🚀 Features
Predefined Personas:

Healthcare Assistant

Travel Agent

Personal Shopper

Banking Advisor

Custom Persona Management:

Create new chatbot personas with unique instructions

Edit or delete existing custom personas

Personas stored persistently in a personas.json file

Interactive Chat Interface:

Live conversation with selected persona

Chat history displayed in real-time

Clear UI sections using Streamlit containers and layout separation

API Integration:

Connects to a locally hosted Ollama server running LLaMA 3

Sends chat messages via API requests and handles JSON responses

🛠️ Tech Stack
Python 3.10+

Streamlit

Ollama API (LLaMA 3)

JSON

Git & GitHub

📦 Installation
Clone the repository:

git clone https://github.com/Omojosh/ai-chatbot-personas.git
cd ai-chatbot-personas

Install dependencies:

pip install -r requirements.txt
Run your Ollama server with LLaMA 3:


ollama serve
Launch the Streamlit app:

streamlit run app.py

📑 Project Structure

ai-chatbot-personas/
├── app.py                # Main Streamlit application
├── personas.json         # Stores user-created personas
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore

✨ Demo
Coming soon…

📖 License
This project is open-source and available under the MIT License.