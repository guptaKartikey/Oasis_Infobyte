import streamlit as st
import requests

# --- App Config ---
st.set_page_config(page_title="🌤️ Weather App", page_icon="☁️", layout="centered")
st.title("🌤️ Real-Time Weather App")

# --- Sidebar for Input ---
st.sidebar.header("🔍 Search City")
city = st.sidebar.text_input("Enter city name", "Delhi")

# --- API Setup ---
API_KEY = "YOUR_API_KEY"  # 🔑 Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city, api_key):
    url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# --- Fetch Weather ---
if st.sidebar.button("Get Weather"):
    weather_data = get_weather(city, API_KEY)

    if weather_data:
        st.subheader(f"📍 Weather in {weather_data['name']}, {weather_data['sys']['country']}")
        
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        condition = weather_data['weather'][0]['description'].capitalize()
        
        st.metric("🌡️ Temperature (°C)", f"{temp}°C", f"Feels like {feels_like}°C")
        st.metric("💧 Humidity", f"{humidity}%")
        st.info(f"🌥️ Condition: {condition}")
    else:
        st.error("❌ City not found. Please enter a valid city name.")
