
import requests
import sys

import json



GLOBAL ={
    'unitGroup': 'us',  # Use 'us' for Fahrenheit
    'contentType': 'json'
}
API_KEY ="SNMM734869T3DUPE2G74SACXG"
# PARAMS = {
#         'unitGroup': 'metric',  # Use 'us' for Fahrenheit
#         'key': API_KEY,
#         'contentType': 'json'
#     }

def get_weather_data(API_KEY, location='London'):  

    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    full_url = f"{url}/{location}?unitGroup={GLOBAL['unitGroup']}&include=days%2Chours&key={API_KEY}&contentType={GLOBAL['contentType']}"

    response = requests.request("GET", full_url)
    if response.status_code!=200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()  


    # Parse the results as JSON
    weather_data = response.json()
    return weather_data

    # print(json.dumps(weather_data, indent=4))





# # Print the data

# location = 'Senegal'
# get_weather_data(API_KEY, location)
# print("Successfully retrieved weather data for", location)
# # print(json.dumps(jsonData, indent=2))


# # Save the JSON data to a file
# def save2json(data, filename):
#     with open(filename, 'w') as f:
#         json.dump(data, f, indent=4)  # Pretty print the JSON data


# def main():
#     try:
#         # Fetch data from Visual Crossing
#         weather_data = get_weather_data(API_KEY, location)
        
#         # Save the data to a JSON file
#         save2json(weather_data, 'weather_data.json')
        
#         print(f"Weather data for {location} has been saved to 'weather_data.json'.")
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()





