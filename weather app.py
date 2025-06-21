import streamlit as st
import requests

# Replace with your own OpenWeatherMap API key
API_KEY = "763b0c8bcc3830f7a8432740c0475d8c"

st.set_page_config(page_title="Weather App", page_icon="🌦️")
st.title("🌤️ Weather App")
st.subheader("Check the weather of any city")

city = st.text_input("Enter city name")

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["main"]
        icon = data["weather"][0]["icon"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        st.markdown(f"## {weather}")
        st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
        st.metric("Temperature", f"{temp} °C")
        st.metric("Humidity", f"{humidity} %")
        st.metric("Wind Speed", f"{wind} m/s")

    else:
        st.error("City not found. Please check the name.")

st.caption("Powered by OpenWeatherMap")

