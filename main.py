import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast For The Next Days")

place = st.text_input("Place:", placeholder="e.g. London, Tokyo, New York")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select The Number Of Forecasted Days")

option = st.selectbox("Select Data To View", ("Temperature", "Sky"))

st.subheader(f"{option} For The Next {days} Days In {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [round(item["main"]["temp"] - 273.15, 1)
                           for item in filtered_data]
            humidity = [item["main"]["humidity"] for item in filtered_data]
            dates = [item["dt_txt"] for item in filtered_data]

            figure = px.line(x=dates, y=temperature,
                             labels={"x": "Date", "y": "Temperature (°C)"},
                             title=f"Temperature in {place}")
            st.plotly_chart(figure)

            fig2 = px.bar(x=dates, y=humidity,
                          labels={"x": "Date", "y": "Humidity (%)"},
                          title=f"Humidity in {place}")
            st.plotly_chart(fig2)

        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            sky_conditions = [item["weather"][0]["main"]
                              for item in filtered_data]
            image_paths = [images.get(condition, "images/cloud.png")
                           for condition in sky_conditions]

            cols_per_row = 8
            for i in range(0, len(image_paths), cols_per_row):
                chunk_paths = image_paths[i:i + cols_per_row]
                chunk_conditions = sky_conditions[i:i + cols_per_row]
                cols = st.columns(cols_per_row)
                for col, img_path, condition in zip(cols, chunk_paths, chunk_conditions):
                    with col:
                        st.image(img_path, width=60)
                        st.caption(condition)

    except KeyError:
        st.error("❌ Place not found. Please enter a valid city name.")
    except Exception as e:
        st.error(f"❌ Something went wrong: {e}")