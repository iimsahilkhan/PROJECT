import requests
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from geopy.geocoders import Nominatim
from tkintermapview import TkinterMapView

# Function to get air quality data
def get_air_quality(lat, lon):
    API_KEY = "YOUR_API_KEY"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", "Failed to fetch data. Check API key or location.")
        return None

# Function to interpret AQI value
def interpret_aqi(aqi):
    meanings = {
        1: "Good (Minimal impact)",
        2: "Fair (Acceptable air quality)",
        3: "Moderate (May affect sensitive groups)",
        4: "Poor (Unhealthy for sensitive groups)",
        5: "Very Poor (Health warnings of emergency conditions)"
    }
    return meanings.get(aqi, "Unknown AQI level")

# Function to update air quality data
def update_air_quality():
    lat = lat_var.get()
    lon = lon_var.get()

    if not lat or not lon:
        messagebox.showerror("Error", "Please enter valid coordinates.")
        return

    data = get_air_quality(lat, lon)
    if data:
        aqi = data['list'][0]['main']['aqi']
        components = data['list'][0]['components']
        
        # Update text display
        result_text = f"AQI Level: {aqi} - {interpret_aqi(aqi)}\n\nPollutant Levels (µg/m³):\n"
        for pollutant, value in components.items():
            result_text += f"{pollutant.upper()}: {value:.2f}\n"
        result_label.config(text=result_text)

        # Update graph
        update_graph(components)

    # Auto-refresh data every 10 seconds
    root.after(10000, update_air_quality)

# Function to update pollutant graph
def update_graph(components):
    pollutants = list(components.keys())
    values = list(components.values())

    ax.clear()
    ax.bar(pollutants, values, color='skyblue')
    ax.set_ylabel("µg/m³")
    ax.set_title("Pollutant Levels")
    canvas.draw()

# Function to get coordinates from address
def get_location():
    address = address_entry.get()
    geolocator = Nominatim(user_agent="geoapi")
    
    try:
        location = geolocator.geocode(address)
        if location:
            lat_var.set(location.latitude)
            lon_var.set(location.longitude)
            map_widget.set_position(location.latitude, location.longitude)
        else:
            messagebox.showerror("Error", "Location not found. Try again.")
    except Exception as e:
        messagebox.showerror("Error", f"Geolocation error: {e}")

# GUI setup
root = tk.Tk()
root.title("Air Quality Detector")
root.geometry("600x600")

# Latitude and Longitude input
lat_var = tk.StringVar()
lon_var = tk.StringVar()

tk.Label(root, text="Enter Location:").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()
tk.Button(root, text="Find Location", command=get_location).pack()

tk.Label(root, text="Latitude:").pack()
tk.Entry(root, textvariable=lat_var).pack()
tk.Label(root, text="Longitude:").pack()
tk.Entry(root, textvariable=lon_var).pack()

tk.Button(root, text="Check Air Quality", command=update_air_quality).pack()

# Result label
result_label = tk.Label(root, text="", justify="left", padx=10, pady=10)
result_label.pack()

# Matplotlib figure for pollutant levels
fig, ax = plt.subplots(figsize=(5, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Interactive Map
map_widget = TkinterMapView(root, width=500, height=300)
map_widget.pack()
map_widget.set_position(20, 78)  # Default location (India)

# Start GUI loop
root.mainloop()
