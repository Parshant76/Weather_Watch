import requests
from config import API_KEY

# Constants
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Fetches weather data for a specific city.
    Returns the JSON data if successful, or None if there was an error.
    """
    # Setup our request parameters
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # We want Celsius
    }
    
    try:
        # distinct timeout to prevent hanging if the network is bad
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status() # Check for HTTP errors (like 404 or 401)
        
        return response.json()
        
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f"❌ Error: We couldn't find a city named '{city_name}'. Check your spelling!")
        elif response.status_code == 401:
             print("❌ Error: Authorization failed. Please check your API key in config.py.")
        else:
            print(f"❌ HTTP Error: {err}")
    except requests.exceptions.ConnectionError:
        print("❌ Error: No internet connection. Please check your network.")
    except Exception as err:
        print(f"❌ An unexpected error occurred: {err}")
    
    return None

def display_weather(data):
    """
    Neatly prints the weather data to the console.
    """
    if not data:
        return

    # Extracting the bits we care about
    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]

    # ASCII art or just a clean border makes it look polished
    print(f"\n🌍 Weather Report for {city}")
    print("=" * 30)
    print(f"🌡️  Temperature: {temp}°C")
    print(f"💧 Humidity:    {humidity}%")
    print(f"☁️  Condition:   {desc.capitalize()}")
    print("=" * 30 + "\n")

def main():
    print("🌤️  Welcome to Weather Watch!")
    print("Type the city name to get the weather.")
    print("Type 'q' or 'quit' to exit.")

    while True:
        try:
            city = input("\n> Enter city name: ").strip()
            
            # Check for exit command
            if city.lower() in ['q', 'quit', 'exit']:
                print("Goodbye! Thanks for using Weather Watch. 👋")
                break
            
            if not city:
                print("⚠️  Please enter a valid city name.")
                continue

            weather_data = get_weather(city)
            if weather_data:
                display_weather(weather_data)
                
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nGoodbye! 👋")
            break

if __name__ == "__main__":
    main()
