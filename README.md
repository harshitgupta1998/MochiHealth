# 📝 Mood of the Queue

**Mood of the Queue** is a simple internal tool built for support teams to track the emotional vibe of customer tickets throughout the day at Mochi Health.

Built with:
- **Streamlit** for the frontend.
- **Flask** for the backend API.
- **Google Sheets** as the data store.

---

## 🚀 Live Demo

🌐 ** (Streamlit App)**: [View Live Streamlit App](https://your-streamlit-app.streamlit.app)


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
<img width="510" alt="image" src="https://github.com/user-attachments/assets/84458380-3ea3-4008-877b-53de2ae35a9d" />


### 📊 Mood Visualization
<img width="591" alt="image" src="https://github.com/user-attachments/assets/b28a9db7-7a76-40f3-b414-22207cfa9571" />


---

## 🚀 Setup Instructions

### 1. Backend API (Flask)

- Clone the repo:
```bash
git clone https://github.com/your-username/mood-tracker-backend.git
cd mood-tracker-backend
```

###
1. 🔒 Block Future Dates
Prevent users from selecting future dates in the date picker — moods should only be logged or analyzed for today or past dates.

st.date_input("Select Date", datetime.now().date(), max_value=datetime.now().date())
✅ Prevents invalid data selection.

2. 🗓️ Restrict Logging Moods for Past Dates
Only allow mood logging for today — logging for past or future dates should not be possible.
Why: Moods should capture real-time emotions, not retrospective guesses.

3. 🛡️ Validate Inputs

Ensure mood is not empty (already drop-down controlled).

Limit note length (e.g., 200 characters) to prevent spammy input.

Sanitize any text input to avoid invalid or unsafe data.

4. 📉 Display Historical Mood Trends
Add a line chart over days/weeks to see mood trends over time.
Analyze team mood dynamics — are Mondays sadder? Fridays happier?

5. 📊 Percentage Breakdown
Show mood distribution in percentages using Pie or Donut charts.
Example: 50% Happy, 20% Angry, etc.

6. ⏳ Loading Indicators
Add a spinner while data is being fetched to improve user experience:

with st.spinner('Fetching mood data...'):
    response = requests.get(...)

7. 📥 Downloadable Reports
Allow users to download the mood data as a CSV for further analysis.
Use Streamlit's st.download_button.


8. 🎨 Dynamic Mood Emojis
Display the top mood of the day as a big emoji at the top.
Example: “Today’s Mood: 🎉 Celebratory”.

9. 🚨 Prevent Duplicate Mood Logs
Implement a mechanism to prevent multiple mood logs within a short time window (e.g., 5 minutes).
Add rate-limiting to ensure data quality.


