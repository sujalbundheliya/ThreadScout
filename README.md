# 🧵 ThreadScout

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/sujalbundheliya/ThreadScout.git)

## 📌 Overview

**ThreadScout** is a Python-based tool designed to streamline your research by fetching relevant threads and discussions from **Reddit** and **Twitter** based on your voice or text queries. It compiles results—including thread titles, URLs, and engagement metrics—into organized CSV files for convenient analysis and reference.

---

## ✨ Features

- ✅ **Voice or Text Input**: Flexibility to input queries via speech or text.
- ✅ **Reddit & Twitter Integration**: Retrieves the most relevant threads and posts.
- ✅ **CSV Output**: Automatically generates and saves results to uniquely named CSV files to prevent overwrites.
- ✅ **Simple Setup**: Easy-to-follow setup guide to get started quickly.

---

## 🚀 Quick Start Guide

Follow these easy steps to set up and run **ThreadScout** locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sujalbundheliya/ThreadScout.git
cd ThreadScout
```

### 2️⃣ Set Up Virtual Environment (Recommended)

- **For Windows:**

```powershell
python -m venv env
.\env\Scripts\activate
```

- **For macOS/Linux:**

```bash
python3 -m venv env
source env/bin/activate
```

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Your `.env` File

Create a `.env` file in the project's root directory to securely store your API credentials:

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_reddit_user_agent

TWITTER_BEARER_TOKEN=your_twitter_bearer_token
```

> **⚠️ Important:** Ensure your `.env` file is never uploaded to GitHub (it's ignored by default).

---

## ▶️ Running ThreadScout

Run the main Python script:

```bash
python main.py
```

You'll see a prompt:

```bash
Choose input method:
1: Voice Input
2: Text Input
Enter 1 or 2:
```

- **Voice Input:** Clearly speak your query.
- **Text Input:** Type your query manually.

ThreadScout will then fetch relevant posts from Reddit and Twitter, saving results in CSV format (e.g., `output.csv`, `output_1.csv`, etc.).

---

## 📂 Project Structure

```
ThreadScout/
├── csv_writer.py            # Logic to handle CSV output files
├── main.py                  # Main script to run the application
├── reddit_search.py         # Reddit API integration
├── twitter_search.py        # Twitter API integration
├── voice_input.py           # Handles voice-to-text input
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not included on GitHub)
└── README.md                # Project documentation
```

---

## 📦 Dependencies

- `praw` *(Reddit API)*
- `tweepy` *(Twitter API)*
- `speechrecognition` *(Voice input support)*
- `pyaudio` *(Audio input)*
- `python-dotenv` *(Environment variable management)*

All dependencies can be quickly installed via:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Troubleshooting

- **API Credentials Error**: Check that your `.env` file has correct API keys and IDs.
- **Voice Input Issue**: Ensure you have installed `pyaudio` correctly (see [PyAudio installation guide](https://people.csail.mit.edu/hubert/pyaudio/)).

---

## 📞 Support

For any questions, issues, or suggestions, open an [Issue](https://github.com/sujalbundheliya/ThreadScout/issues) or contact me directly via my GitHub profile.

---

## 📄 License

This project is open source. Feel free to use and modify it according to your needs.

---

## 👤 Author

- [Sujal Bundheliya](https://github.com/sujalbundheliya)

---

⭐ Don't forget to **star** this repository if you find it useful!

