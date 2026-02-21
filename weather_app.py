import streamlit as st
import requests

# Page ki configuration (Title aur Icon browser tab ke liye)
st.set_page_config(page_title="Mausam App", page_icon="🌤️")

st.title("Mera Mausam App 🌤️")

api_key = "a3fc380c67a5d951ca10a07fb8115450"

sheher = st.text_input("Apne sheher ka naam likhen:", placeholder="Maslan: Karachi")

if sheher:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sheher}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["main"]["temp"] # Hawa ki raftar
        
        # Mausam ke hisab se icon chun-na
        icon = "☁️" # Default
        if "clear" in weather_desc.lower(): icon = "☀️"
        elif "rain" in weather_desc.lower(): icon = "🌧️"
        elif "haze" in weather_desc.lower() or "mist" in weather_desc.lower(): icon = "🌫️"

        st.markdown(f"### 📍 {sheher.capitalize()}")
        
        # Columns mein data dikhana
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Temperature", f"{temp}°C", delta=icon)
        with col2:
            st.metric("Humidity (Nami)", f"{humidity}%")

        st.info(f"**Surat-e-haal:** {weather_desc}")
    else:
        st.error("Sheher ka naam sahi nahi hai!")