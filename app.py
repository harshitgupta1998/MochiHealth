import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

API_URL = "https://mochihealth.onrender.com" 

# Page config
st.set_page_config(
    page_title="Mood of the Queue",
    page_icon="😊",
    layout="centered"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    
    /* Text colors */
    h1, h2, h3, p, label {
        color: #FFFFFF !important;
    }
    
    .stSelectbox > div {
        background-color: #1E1E1E;
        border-radius: 8px;
        color: #FFFFFF;
        min-height: 45px;
        padding: 2px;
    }
    .stSelectbox > div > div {
        color: #FFFFFF;
        font-size: 18px;
    }

    .stTextInput > div > div > input {
        background-color: #1E1E1E;
        color: #FFFFFF;
        border-radius: 8px;
        font-size: 18px;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #4CAF50 !important;
        color: white !important;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    
    /* Date input styling */
    .stDateInput > div > div > input {
        background-color: #1E1E1E;
        color: #FFFFFF;
        border-radius: 8px;
    }
    
    /* Info messages */
    .stAlert {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }

    /* Dropdown list items */
    .stSelectbox > div > div[role="listbox"] {
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📝 Mood of the Queue")

# Log a Mood Section
st.header("Ops team capture your vibe")

# Moods List
moods = {
    "😊": "Happy",
    "😠": "Angry",
    "😕": "Confused",
    "🎉": "Celebratory",
    "😔": "Sad",
    "😎": "Cool"
}

# Dropdown for Mood
selected_mood_emoji = st.selectbox(
    "Select your mood",
    options=list(moods.keys()),
    format_func=lambda emoji: f"{emoji} {moods[emoji]}"
)

# Text Input for Note
note = st.text_input("Add a short note (optional)")

if st.button("Submit Mood"):
    payload = {
        "mood": selected_mood_emoji,
        "note": note
    }
    try:
        response = requests.post(f"{API_URL}/log_mood", json=payload)


        if response.status_code == 200:
            st.success("Mood logged successfully!")
        else:
            st.error(f"Failed to log mood. Server responded: {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")


# Auto-refresh every 60 seconds
count = st_autorefresh(interval=60 * 1000, key="datarefresh")

# Mood Visualization
st.header("Today's Mood Trends")

# Date Filter
selected_date = st.date_input("Select Date", datetime.now().date())

response = requests.get(f"{API_URL}/get_moods")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

    if not df.empty:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df_filtered = df[df['timestamp'].dt.date == selected_date]

        if not df_filtered.empty:
            mood_counts = df_filtered['mood'].value_counts().reset_index()
            mood_counts.columns = ['Mood', 'Count']

            fig = px.bar(
                mood_counts,
                x='Mood',
                y='Count',
                title=f"Mood Counts for {selected_date.strftime('%Y-%m-%d')}",
                text_auto=True,
                color='Mood',
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No mood entries for the selected date.")
    else:
        st.info("No mood data available yet.")
else:
    st.error("Failed to fetch mood data.")
