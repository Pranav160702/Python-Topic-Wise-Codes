# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)    HUMIDITY(%)            WEATHER

#       >= 30         >= 90                Hot and Humid
#       >= 30          < 90                Hot
#       <30           >= 90                Cool and Humid
#       <30            < 90                Cool



def determine_weather(temperature, humidity):
    if temperature >= 30 and humidity >= 90:
        return "Hot and Humid"
    elif temperature >= 30 and humidity < 90:
        return "Hot"
    elif temperature < 30 and humidity >= 90:
        return "Cool and Humid"
    elif temperature < 30 and humidity < 90:
        return "Cool"

# Taking input for temperature and humidity
temperature = float(input("Enter the temperature (in Celsius): "))
humidity = float(input("Enter the humidity (in percentage): "))

# Determine and print the weather
weather = determine_weather(temperature, humidity)
print(f"The weather is: {weather}")
