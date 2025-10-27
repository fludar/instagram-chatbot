
<h1 align="center">

[![instagram](https://skillicons.dev/icons?i=instagram)](https://skillicons.dev)

  Instagram Chatbot
</h1>

<h4 align="center">An Instagram Chatbot that uses user predefined commands</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#build-instructions">Build Instructions</a> •
  <a href="#screenshot">Screenshot</a> •
  <a href="#credits">Credits</a> 
</p>



## 🧮 Key Features
 - Owner-only command management — only the claimed owner can add or remove custom commands.
 - Claim/unclaim ownership (anti-grief) — claim or release ownership so others can’t hijack the bot.
 - Purge setup messages — remove or mark setup DMs as seen to keep configuration private.
 - Runtime add/delete commands — create and remove command triggers on the fly via DM.
 - Persistent session storage — save session.json to avoid repeated logins and auth challenges.

## 🛠 Build Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/fludar/instagram-chatbot.git
   ```
2. Change into the project directory:
   ```bash
   cd instagram-chatbot
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your environment variables:

Linux / macOS:
```bash
export IG_USERNAME="your_username"
export IG_PASSWORD="your_password"
```

Windows (PowerShell):
```powershell
$env:IG_USERNAME="your_username"
$env:IG_PASSWORD="your_password"
```

## ▶️ Usage

From the repository root run:

```bash
python src/main.py
```

The script will log in (persisting session data to `session.json`) and poll unread direct message threads. When it receives an eligible message, it will respond according to the built-in or custom commands.

## 📸 Screenshot
<img src="https://raw.githubusercontent.com/fludar/instagram-chatbot/main/resources/demo.jpg" width="216" height="480" /> ![screenshot](https://raw.githubusercontent.com/fludar/instagram-chatbot/main/resources/demo.gif)



## 🙏 Credits

- [instagrapi](https://github.com/subzeroid/instagrapi) — private API client used to interact with Instagram.

## 📖 What did I learn?

- How to use instagrapi for basic DM handling and session management.  
- How to persist a login session to avoid repeated authentication.  
- How to implement owner-restricted commands and simple anti-griefing measures.  
