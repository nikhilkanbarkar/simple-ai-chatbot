# 🤖 Simple AI Chat Assistant

A simple AI-powered chatbot built with **Python** and the **Google Gemini API**. The chatbot accepts user input, generates AI responses, maintains conversation history, and handles common errors gracefully.

This project was developed as part of a **Week 1 AI Internship Assignment**.

---

## 📌 Project Overview

The **Simple AI Chat Assistant** is a terminal-based conversational application that demonstrates how to integrate a Large Language Model (LLM) into a Python application.

The chatbot can:

* Accept user input
* Generate AI-powered responses
* Continue conversations using chat history
* Handle invalid inputs and API errors
* Store API keys securely using a `.env` file

---

## ✨ Features

* 🤖 AI-powered conversation using Google Gemini
* 💬 Multi-turn conversation with chat history
* 🔐 Secure API key management using `.env`
* ⚠️ Graceful error handling
* 🔄 Automatic retry mechanism for temporary server issues
* 🧹 Clear conversation history
* 🚪 Exit command
* 🧩 Clean and modular project structure

---

## 📂 Project Structure

```text
simple-ai-chatbot/
│
├── main.py              # Application entry point
├── chatbot.py           # Chatbot logic
├── config.py            # API configuration
├── .env                 # API key (Not pushed to GitHub)
├── .gitignore
├── requirements.txt
├── README.md
└── venv/
```

---

## 🛠️ Technologies Used

* Python 3.x
* Google Gemini API
* google-genai SDK
* python-dotenv

---

## 📋 Requirements

* Python 3.10 or above
* Google Gemini API Key

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nikhilkanbarkar/simple-ai-chatbot.git
```

### 2. Navigate to the Project

```bash
cd simple-ai-chatbot
```

### 3. Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Create a `.env` File

Create a file named `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your own Gemini API key.

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💻 Example

```text
============================================================
          🤖 SIMPLE AI CHAT ASSISTANT
============================================================

You : Hello

AI : Hello! How can I help you today?

You : Explain Machine Learning.

AI : Machine Learning is a field of Artificial Intelligence...

You : clear

AI : Conversation history cleared.

You : exit

AI : Goodbye!
```

---

## 🧠 Commands

| Command | Description                |
| ------- | -------------------------- |
| `exit`  | Exit the chatbot           |
| `clear` | Clear conversation history |

---

## 🔒 Security

The API key is stored securely using a `.env` file.

The `.env` file is excluded from GitHub using `.gitignore`.

Never share your API key publicly.

---

## ⚠️ Error Handling

The chatbot gracefully handles:

* Empty user input
* Invalid API configuration
* Invalid API key
* Network issues
* Gemini server busy (503)
* Unexpected runtime errors

---

## 📦 Dependencies

```text
google-genai
python-dotenv
```

---

## 🔮 Future Improvements

* Web interface using Streamlit
* Voice input and speech output
* Markdown response formatting
* Chat history export
* GUI version using Tkinter or PyQt
* Theme customization
* Streaming AI responses

---

---

## 👨‍💻 Author

**Nikhil Kanbarkar**

* **GitHub:** https://github.com/nikhilkanbarkar
* **LinkedIn:** https://www.linkedin.com/in/nikhil-kanbarkar

Feel free to connect with me for discussions on Artificial Intelligence, Machine Learning, Data Science, or Python development.

---

## 📄 License

This project is created for **educational and internship purposes**.

No official open-source license has been applied to this repository yet. You are welcome to explore the code, learn from it, and use it for personal learning. If you plan to reuse significant portions of this project publicly or commercially, please contact the author first.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

If you have ideas to improve this project, feel free to:

* Fork the repository
* Create a new branch
* Submit a Pull Request

---

## ⭐ Support

If you found this project helpful:

* ⭐ Star this repository
* 🍴 Fork it for your own learning
* 💬 Share your feedback or suggestions

If you have any questions or would like to discuss AI, Machine Learning, or Python development, feel free to connect with me on LinkedIn. I'm always happy to learn, collaborate, and help where I can.
