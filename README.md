# Simple Weather CLI

A beginner-friendly Command Line Interface (CLI) application that uses Python to fetch and display the current weather for any city.

## API Used
OpenWeatherMap API

## How to Get API Key
1. Go to the OpenWeatherMap website and sign up for a free account.
2. Navigate to the "API keys" tab in your account dashboard.
3. Generate a new API key and copy it.

## How to Install Dependencies
1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Project
1. Open `config.py` and replace `YOUR_API_KEY_HERE` with your actual API key.
2. Run the application using the command:
   ```bash
   python main.py
   ```
3. Enter a city name when prompted.

## Sample Output
```text
Welcome to the Simple Weather App!
Enter city name: London

==============================
Weather in London:
Temperature: 15.32°C
Humidity: 72%
Description: Scattered clouds
==============================
```

## MLH Global Week
This project was built for MLH Global Week to demonstrate API usage in Python!
