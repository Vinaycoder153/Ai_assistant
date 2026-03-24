<h1 align="center">🎙️ Vinay's AI Voice Assistant</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20With-Python%20%26%20AI-blueviolet?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Voice-Aoede%20LLM-yellowgreen?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/LiveKit-Agent%20Voice-blue?style=for-the-badge&logo=livechat" />
</p>

<p align="center">
  <b style="font-size:1.4em; color:#00ff7f;">Smart, Secure, and Emotionally Aware Voice Assistant</b><br>
  Your real-time AI companion that listens, understands, and responds like a supportive partner.<br>
  <i style="color:#a9a9a9;">Crafted for clarity, care, and productivity.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Real-Time-Voice%20Processing-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Emotionally%20Aware-Yes-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-Powered-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Version-1.0.0-yellow?style=for-the-badge" />
</p>

<p align="center">
  <a href="#-features" style="background-color:#00ff7f; color:#000; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:bold;">Explore Features</a>
</p>

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

| Tool                       | Purpose                                           |
|----------------------------|---------------------------------------------------|
| **Python**                 | Core language                                     |
| **LiveKit Agents**         | Real-time audio/video pipeline & agent framework  |
| **Google LLM (Aoede)**     | Realtime voice AI generation                      |
| **LangChain / DuckDuckGo** | Web search tool integration                       |
| **Flask + Flask-CORS**     | HTTP token-generation server for LiveKit rooms    |
| **SQLite**                 | Local schedule/task storage (`assistant_data.db`) |
| **Google Calendar API**    | Fetching today's calendar events                  |
| **python-dotenv**          | Secure environment-variable management            |

---

## 📸 Preview

![AI Voice Assistant Demo](https://your-demo-link.png)

> Replace this with a screenshot or GIF of your assistant in action.

---

## 🧪 How It Works

1. 🎧 **`agent.py` starts** a LiveKit agent worker that listens to your voice in a room.
2. 🌞 **`prompts.py`** builds a dynamic greeting based on detected mood, time of day, and language preference (from `config.py`).
3. 🧠 **Google's Realtime LLM (Aoede)** interprets your intent and decides which tool to call.
4. 🛠️ **`tools.py`** executes the requested action — weather lookup, web search, email, schedule management, or system commands.
5. 💬 The assistant **responds** with a warm, natural voice back through LiveKit.
6. 🌐 **`server.py`** runs a separate Flask HTTP server that generates secure LiveKit access tokens for frontend clients joining rooms.

---

## 🚀 Getting Started

```bash
# 1. Clone this repository
git clone https://github.com/Vinaycoder153/Ai_assistant
cd Ai_assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env .env.local          # or create your own .env
# Fill in: LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET,
#          GMAIL_USER, GMAIL_APP_PASSWORD, and any other keys

# 4a. Start the LiveKit voice agent
python agent.py dev

# 4b. (Optional) Start the token server for frontend clients
python server.py
```

---

## 🗂️ Codebase Structure

```
📁 Ai_assistant/
├── agent.py            # LiveKit agent entry point — sets up the Assistant and connects to a room
├── server.py           # Flask HTTP server — generates LiveKit access tokens (/getToken endpoint)
├── tools.py            # All callable agent tools: weather, web search, email, time, app, commands, DB
├── prompts.py          # Dynamic prompt & greeting builder (mood + time + language aware)
├── config.py           # User profile settings (name, language, timezone, mood)
├── mood_tools.py       # Mood detection stub (returns current mood; ready for ML/API integration)
├── calendar_tools.py   # Google Calendar integration — fetches today's events
├── db_driver.py        # SQLite wrapper (PersonalAssistantDB) — stores and queries schedules
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API keys, credentials — never commit secrets)
├── assistant_data.db   # SQLite database file (auto-created on first run)
└── README.md
```

### Module Descriptions

| File | Role |
|------|------|
| `agent.py` | Defines the `Assistant` (subclass of LiveKit `Agent`) with all registered tools, and the async `entrypoint` that starts the session and sends the opening greeting. Run with `python agent.py dev`. |
| `server.py` | Lightweight Flask app with a single `GET /getToken` endpoint. Generates and returns a signed LiveKit JWT so browser/mobile clients can join a room. Run with `python server.py`. |
| `tools.py` | Eight `@function_tool` async functions exposed to the LLM: `get_weather`, `search_web`, `send_email`, `get_current_time`, `open_app`, `run_command`, `db_add_data`, `db_query_data`. |
| `prompts.py` | Builds `AGENT_INSTRUCTION` (static system prompt) and `SESSION_INSTRUCTION_FUNCTION` (async function that generates a personalised greeting). Imported by `agent.py`. |
| `config.py` | `USER_PROFILE` dict — single source of truth for the user's name, preferred language (`en` / `kn`), timezone, and default mood. |
| `mood_tools.py` | `detect_mood_from_voice()` — currently a stub returning `"happy"`. Intended hook for a future audio emotion model. |
| `calendar_tools.py` | `get_today_events()` — authenticates with Google Calendar via `token.json` and returns a list of today's events as formatted strings. |
| `db_driver.py` | `PersonalAssistantDB` class — wraps SQLite to create a `schedule` table and expose `add_schedule` / `get_all_schedules` methods used by the DB tools in `tools.py`. |

---

## 🧪 Sample Commands

> Try saying:

* "What's the weather like today?"
* "Remind me to call mom at 6 PM."
* "Open Notepad."
* "Add 'Buy groceries' to my tasks."
* "Am I sounding tired today?"

---

## 🔐 Security Policy

Your privacy and data security are our top priorities. Here's how we keep your assistant safe:

### ✅ Local-First Execution

* All data operations (voice, calendar, DB) are processed **locally** unless explicitly using APIs (e.g., weather or search).

### ✅ Environment Variables

* Secrets (email, API keys, LiveKit credentials) are stored in `.env` and **never hardcoded**.

### ✅ No Data Leaks

* No analytics, tracking, or external logs.
* Assistant only sends API requests **when required by you**.

### ✅ Optional Encryption

* You can extend to encrypt `.db` files using `cryptography` or `sqlitecipher`.

> **Tip:** Use strong passwords, app-specific email tokens, and enable 2FA on all integrated accounts.

---

## 🙌 Credits

Made with ❤️ by [Vinay](https://github.com/Vinaycoder153)
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

> "A truly helpful assistant doesn't just *respond* — it *connects*." 💙
