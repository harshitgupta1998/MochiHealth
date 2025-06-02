# 📝 Mood of the Queue

**Mood of the Queue** is a simple internal tool built for support teams to track the emotional vibe of customer tickets throughout the day at Mochi Health.

Built with:
- **Streamlit** for the frontend.
- **Flask** for the backend API.
- **Google Sheets** as the data store.

---

## 🚀 Live Demo

🌐 **Frontend (Streamlit App)**: [View Live Streamlit App](https://your-streamlit-app.streamlit.app)

🌐 **Backend API**: [Flask API on Render](https://mochihealth.onrender.com)

---

## 📚 Table of Contents
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Screenshots](#-screenshots)
- [Setup Instructions](#-setup-instructions)
- [Environment Variables](#-environment-variables)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

## ✨ Features

- 📝 **Log a Mood** — Select a mood from dropdown with an optional note.
- 📊 **Visualize Moods** — View mood trends over time with interactive bar charts.
- 🔄 **Auto-Refresh** — Auto-refreshes mood data every 60 seconds.
- 🗓️ **Filter by Date** — Easily pick a date to view moods logged on that day.
- 🔒 **Secure Google Sheets Integration** — Service account credentials are hidden using environment variables.

---

## 🛠️ Tech Stack

**Frontend**:
- Streamlit
- Plotly
- Pandas
- Streamlit-AutoRefresh

**Backend**:
- Flask
- gspread
- oauth2client

**Hosting**:
- Streamlit Cloud (Frontend)
- Render.com (Backend API)

**Storage**:
- Google Sheets (using Google Drive API)

---

## 📸 Screenshots

### 📝 Mood Logging
*(Add your mood logging screenshot here)*

### 📊 Mood Visualization
*(Add your mood trends screenshot here)*

---

## 🚀 Setup Instructions

### 1. Backend API (Flask)

- Clone the repo:
```bash
git clone https://github.com/your-username/mood-tracker-backend.git
cd mood-tracker-backend
