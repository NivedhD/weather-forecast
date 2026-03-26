# Weather Forecast App

A Streamlit web app that shows weather forecasts for any
city using the OpenWeatherMap API.

## Features
- 5-day weather forecast for any city worldwide
- Temperature trend chart using Plotly
- Humidity chart
- Sky condition view with weather icons
- Supports Clear, Clouds, Rain and Snow conditions
- Clean error handling for invalid city names

## Setup
1. Clone the repo
2. pip install streamlit plotly requests python-dotenv
3. Create a `.env` file based on `.env.example`
4. Get a free API key at openweathermap.org
5. Add your API key to `.env`

## Usage
streamlit run main.py
