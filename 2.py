import requests
import tkinter as tk
from tkinter import messagebox

# Function to get air quality data
def get_air_quality():
    city = input("Enter yur city: \n")
    API_KEY = f"http://api.weatherapi.com/v1/current.json?key=9fa6955d9c7e433bb7a81707251103&q={city}"  # Replace with your OpenWeatherMap API key
    lat = lat_entry.get()
    #lon = lon_entry.get()

    if not lat:
        messagebox.showerror("Error", "Please enter both latitude and longitude.")
        return

    url = f"{API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        display_air_quality(data)
    else:
        messagebox.showerror("Error", "Failed to retrieve data. Check API key and location.")

# Function to interpret AQI value
def interpret_aqi(aqi):
    aqi_meaning = {
        1: "Good (Minimal impact)",
        2: "Fair (Acceptable air quality)",
        3: "Moderate (May affect sensitive groups)",
        4: "Poor (Unhealthy for sensitive groups)",
        5: "Very Poor (Health warnings of emergency conditions)"
    }
    return aqi_meaning.get(aqi, "Unknown AQI level")

# Function to display air quality information
def display_air_quality(data):
    aqi = data['list'][0]['main']['aqi']
    components = data['list'][0]['components']

    result_text = f"AQI Level: {aqi} - {interpret_aqi(aqi)}\n\nPollutant Levels (µg/m³):\n"
    for pollutant, value in components.items():
        result_text += f"{pollutant.upper()}: {value:.2f}\n"

    result_label.config(text=result_text)

# GUI setup
root = tk.Tk()
root.title("Air Quality Detector")
root.geometry("400x400")

tk.Label(root, text="Enter City:").pack()
lat_entry = tk.Entry(root)
lat_entry.pack()

#tk.Label(root, text="Enter Longitude:").pack()
#lon_entry = tk.Entry(root)
#lon_entry.pack()

tk.Button(root, text="Check Air Quality", command=get_air_quality).pack()

result_label = tk.Label(root, text="", justify="left", padx=10, pady=10)
result_label.pack()

root.mainloop()
