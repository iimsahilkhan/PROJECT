import requests
import json
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    api_key = "9fa6955d9c7e433bb7a81707251103"  # Replace with your actual API key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    
    try:
        response = requests.get(url)
        data = response.json()
        if "error" in data:
            messagebox.showerror("Error", data["error"]["message"])
        else:
            temp_c = data["current"]["temp_c"]
            weather_label.config(text=f"Temperature: {temp_c}°C", fg="blue")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Failed to fetch weather data.")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

tk.Label(root, text="Enter City:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

weather_label = tk.Label(root, text="", font=("Arial", 12))
weather_label.pack(pady=10)

root.mainloop()
