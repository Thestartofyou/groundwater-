# Import necessary libraries
import requests

# Define function to retrieve groundwater data based on latitude and longitude
def get_groundwater_data(latitude, longitude):
    # Construct the API URL for groundwater data
    url = f"https://api.groundwaterdata.ng/api/groundwater?latitude={latitude}&longitude={longitude}"

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response data
        data = response.json()
        # Extract the groundwater level from the data
        groundwater_level = data["groundwater_level"]
        return groundwater_level
    else:
        # Raise an exception if the request was not successful
        raise Exception("Failed to retrieve groundwater data")

# Call the function to retrieve groundwater data for a specific latitude and longitude
latitude = 37.7749
longitude = -122.4194
groundwater_level = get_groundwater_data(latitude, longitude)

# Print the groundwater level
print(f"The groundwater level at ({latitude}, {longitude}) is {groundwater_level}")
