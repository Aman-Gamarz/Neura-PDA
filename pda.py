
import tkinter as tk
from tkinter import scrolledtext
import webbrowser
import pywhatkit as kit
import requests
import wikipedia

# Function to get IP location
def get_ip_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        location = f"{data['city']}, {data['region']}, {data['country']}"
        output_text.insert(tk.END, f"Your IP location is: {location}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error fetching IP location: {e}\n")

# Function to open YouTube video
def open_youtube_video():
    query = youtube_entry.get()
    try:
        kit.playonyt(query)
        output_text.insert(tk.END, f"Opening YouTube video for: {query}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error opening YouTube video: {e}\n")

# Function to send WhatsApp message
def send_whatsapp_message():
    phone_number = whatsapp_phone_entry.get()
    message = whatsapp_message_entry.get()
    try:
        kit.sendwhatmsg_instantly(phone_number, message)
        output_text.insert(tk.END, f"Message sent to {phone_number}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error sending WhatsApp message: {e}\n")

# Function to get daily news
def get_daily_news():
    try:
        api_key = "YOUR_NEWS_API_KEY"  # Replace with your NewsAPI key
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        news_data = response.json()
        articles = news_data['articles']
        output_text.insert(tk.END, "Top 5 News Headlines:\n")
        for i, article in enumerate(articles[:5], 1):
            output_text.insert(tk.END, f"{i}. {article['title']} - {article['url']}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error fetching news: {e}\n")

# Function to get weather updates
def get_weather_updates():
    city = weather_entry.get() or "New York"
    try:
        api_key = "YOUR_WEATHER_API_KEY"  # Replace with your OpenWeatherMap key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        weather_data = response.json()
        weather = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        output_text.insert(tk.END, f"Weather in {city}: {weather}, Temperature: {temperature}°C\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error fetching weather: {e}\n")

# Function to get animal information from Wikipedia
def get_animal_info():
    animal = animal_entry.get()
    try:
        summary = wikipedia.summary(animal, sentences=2)
        output_text.insert(tk.END, f"Information about {animal}: {summary}\n")
    except wikipedia.exceptions.DisambiguationError:
        output_text.insert(tk.END, "Multiple results found. Please be more specific.\n")
    except wikipedia.exceptions.PageError:
        output_text.insert(tk.END, "No information found for that animal.\n")

# Create the main window
root = tk.Tk()
root.title("Personal Digital Assistant (PDA)")
root.geometry("600x500")

# Create and place widgets
tk.Label(root, text="YouTube Video:").grid(row=0, column=0, padx=10, pady=5)
youtube_entry = tk.Entry(root, width=40)
youtube_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Open YouTube", command=open_youtube_video).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="WhatsApp Phone:").grid(row=1, column=0, padx=10, pady=5)
whatsapp_phone_entry = tk.Entry(root, width=20)
whatsapp_phone_entry.grid(row= 1, column=1, padx=10, pady=5)
tk.Label(root, text="WhatsApp Message:").grid(row=2, column=0, padx=10, pady=5)
whatsapp_message_entry = tk.Entry(root, width=40)
whatsapp_message_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Send WhatsApp", command=send_whatsapp_message).grid(row=2, column=2, padx=10, pady=5)

tk.Label(root, text="City for Weather:").grid(row=3, column=0, padx=10, pady=5)
weather_entry = tk.Entry(root, width=20)
weather_entry.grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Get Weather", command=get_weather_updates).grid(row=3, column=2, padx=10, pady=5)

tk.Label(root, text="Animal for Info:").grid(row=4, column=0, padx=10, pady=5)
animal_entry = tk.Entry(root, width=20)
animal_entry.grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Get Animal Info", command=get_animal_info).grid(row=4, column=2, padx=10, pady=5)

tk.Button(root, text="Get IP Location", command=get_ip_location).grid(row=5, column=0, padx=10, pady=5)
tk.Button(root, text="Get Daily News", command=get_daily_news).grid(row=5, column=1, padx=10, pady=5)

output_text = scrolledtext.ScrolledText(root, width=70, height=20)
output_text.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Start the main loop
root.mainloop()