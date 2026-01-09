<h1 align="center">🎙️ Vinay's AI Voice Assistant</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20With-Python%20%26%20AI-blueviolet?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Voice-Aoede%20LLM-yellowgreen?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/LiveKit-Agent%20Voice-blue?style=for-the-badge&logo=livechat" />
</p>

<p align="center"> <b style="font-size:1.4em; color:#00ff7f;">Smart, Secure, and Emotionally Aware Voice Assistant</b><br> Your real-time AI companion that listens, understands, and responds like a supportive partner.<br> <i style="color:#a9a9a9;">Crafted for clarity, care, and productivity.</i> </p> <p align="center"> <img src="https://media.giphy.com/media/SWnYxeGC7ihwNFZobG/giphy.gif" width="70%" alt="AI Voice Assistant Demo"/> </p> <p align="center"> <img src="https://img.shields.io/badge/Real-Time-Voice%20Processing-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/Emotionally%20Aware-Yes-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/AI-Powered-purple?style=for-the-badge" /> <img src="https://img.shields.io/badge/Version-1.0.0-yellow?style=for-the-badge" /> </p> <p align="center"> <a href="#features" style="background-color:#00ff7f; color:#000; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold;">Explore Features</a> </p>

---

## 🌟 Features

🎙️ **Real-Time Voice Conversations**  
Chat naturally using your voice with human-like responses powered by **Google's Realtime LLM** and **LiveKit**.

🧠 **Mood Detection**  
Understands how you're feeling from your voice tone and responds with empathy.

🌐 **Multilingual Support**  
Speaks in both **English 🇺🇸** and **Kannada 🇮🇳**, with personalized greetings.

📅 **Calendar Integration**  
Provides daily event summaries and time-aware, mood-aware greetings.

🎯 **Smart Utilities**
- Reminders & Notes
- Weather Forecasts
- Web Search
- App Opening
- System Commands
- Email Sending
- Database Task Handling

🔒 **Security-First Design**  
Your data stays local, private, and protected. No unwanted tracking.

---

## 🛠️ Tech Stack

| Tool            | Purpose                      |
|-----------------|------------------------------|
| **Python**      | Core language                |
| **LiveKit**     | Real-time audio/video input  |
| **Google LLM**  | Voice AI generation (Aoede)  |
| **LangChain**   | Tool orchestration           |
| **SQLite**      | Local data storage           |
| **dotenv**      | Secure config management     |

---

## 📸 Preview

![AI Voice Assistant Demo](https://your-demo-link.png)

> Replace this with a screenshot or GIF of your assistant in action.

---

## 🧪 How It Works

1. 🎧 **Listens** to your voice and detects mood
2. 🌞 **Greets** you based on time, mood, and language
3. 🧠 **Understands** your intent
4. 🛠️ **Performs** the task (reminder, search, DB update, etc.)
5. 💬 **Responds** with a warm, natural voice

---

## 🚀 Getting Started

```bash
# 1. Clone this repository
git clone https://github.com/yourusername/ai-voice-assistant
cd ai-voice-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Add your API keys, Google credentials, and preferences

# 4. Run the assistant
python main.py
````

---

## 🗂️ Folder Structure

```
📁 ai-voice-assistant/
├── tools/                  # Task tools (weather, search, email, db)
├── prompts.py              # Personalized prompt instructions
├── config.py               # User settings (name, mood, language)
├── mood_tools.py           # Detects mood from voice
├── calendar_tools.py       # Calendar integration
├── main.py                 # Entry point & assistant setup
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🧪 Sample Commands

> Try saying:

* “What’s the weather like today?”
* “Remind me to call mom at 6 PM.”
* “Open Notepad.”
* “Add 'Buy groceries' to my tasks.”
* “Am I sounding tired today?”

---

## 🔐 Security Policy

Your privacy and data security are our top priorities. Here's how we keep your assistant safe:

### ✅ Local-First Execution

* All data operations (voice, calendar, DB) are processed **locally** unless explicitly using APIs (e.g., weather or search).

### ✅ Environment Variables

* Secrets (email, API keys) are stored securely in `.env` and **never hardcoded**.

### ✅ No Data Leaks

* No analytics, tracking, or external logs.
* Assistant only sends API requests **when required by you**.

### ✅ Optional Encryption

* You can extend to encrypt `.db` files using `cryptography` or `sqlitecipher`.

> **Tip:** Use strong passwords, app-specific email tokens, and enable 2FA on all integrated accounts.

---

## 🙌 Credits

Made with ❤️ by [Vinay](https://github.com/yourusername)
Voice model by **Google Realtime (Aoede)**
Framework powered by **LiveKit Agents**
Inspired by **JARVIS**, **Samantha (Her)**, and the idea of emotionally aware AI.

---

## 📬 Contact

Got feedback or collaboration ideas?

* 🌐 Portfolio: [yourwebsite.com](https://yourwebsite.com)
* 📫 Email: `youremail@example.com`
* 🔗 LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

---

## ⭐ Support the Project

If you love this assistant:

* ⭐ Star the repo
* 🍴 Fork it
* 🧑‍💻 Try it out and share your experience

> “A truly helpful assistant doesn’t just *respond* — it *connects*.” 💙

---

```


