# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px
# from datetime import datetime
# from streamlit_autorefresh import st_autorefresh

# API_URL = "http://localhost:5000"  # Adjust if you deploy Flask elsewhere

# st.set_page_config(page_title="Mood of the Queue", layout="wide", page_icon="😊")

# # Custom theme with white background and larger button
# st.markdown("""
#     <style>
#     body {
#         background-color: #FFFFFF;
#         color: #343a40;
#         font-family: 'Helvetica', sans-serif;
#     }
#     .stButton > button {
#         width: 100%;
#         padding: 0.75rem 1.5rem;
#         font-size: 1.1rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.title("📝 Mood of the Queue")

# # Mood logging
# st.header("Log your Mood")

# moods = ["😊", "😠", "😕", "🎉"]
# selected_mood = st.selectbox("How are you feeling?", options=moods)
# note = st.text_input("Add a short note (optional):")

# if st.button("Submit Mood"):
#     payload = {
#         "mood": selected_mood,
#         "note": note
#     }
#     response = requests.post(f"{API_URL}/log_mood", json=payload)
#     if response.status_code == 200:
#         st.success("Mood logged successfully!")
#     else:
#         st.error("Failed to log mood.")

# # Auto-refresh every 1 min
# count = st_autorefresh(interval=60 * 1000, key="datarefresh")

# # Mood Visualization
# st.header("Today's Mood Trends")

# # Date filter
# selected_date = st.date_input("Select Date", datetime.now().date())

# response = requests.get(f"{API_URL}/get_moods")
# if response.status_code == 200:
#     data = response.json()
#     df = pd.DataFrame(data)

#     if not df.empty:
#         df['timestamp'] = pd.to_datetime(df['timestamp'])
#         df_filtered = df[df['timestamp'].dt.date == selected_date]

#         if not df_filtered.empty:
#             mood_counts = df_filtered['mood'].value_counts().reset_index()
#             mood_counts.columns = ['Mood', 'Count']

#             fig = px.bar(
#                 mood_counts,
#                 x='Mood',
#                 y='Count',
#                 title=f"Mood Counts for {selected_date.strftime('%Y-%m-%d')}",
#                 text_auto=True,
#                 color='Mood',
#                 color_discrete_sequence=px.colors.qualitative.Pastel
#             )
#             st.plotly_chart(fig, use_container_width=True)
#         else:
#             st.info("No mood entries for the selected date.")
#     else:
#         st.info("No mood data available yet.")
# else:
#     st.error("Failed to fetch mood data.")

import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

API_URL = "http://127.0.0.1:5000"  # Flask API

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
    
    /* Selectbox styling */
    .stSelectbox > div {
        background-color: #1E1E1E;
        border-radius: 8px;
        color: #FFFFFF;
    }
    .stSelectbox > div > div {
        color: #FFFFFF;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background-color: #1E1E1E;
        color: #FFFFFF;
        border-radius: 8px;
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
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📝 Mood of the Queue")

# Log a Mood Section
st.header("Log Your Mood")

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

# Submit Button
if st.button("Submit Mood"):
    payload = {
        "mood": selected_mood_emoji,
        "note": note
    }
    response = requests.post(f"{API_URL}/log_mood", json=payload)
    if response.status_code == 200:
        st.success("Mood logged successfully!")
    else:
        st.error("Failed to log mood. Please try again.")

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
