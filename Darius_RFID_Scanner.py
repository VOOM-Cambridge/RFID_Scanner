import json
from datetime import datetime
import os

# Predefined lab location
tag = "3D printing lab"

def create_json(unique_str, tag):
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a dictionary with the unique string, timestamp, and tag
    data = {
        "ID": unique_str,
        "timestamp": timestamp,
        "tag": tag
    }

    # Generate a unique filename using the timestamp
    filename = f"output_{timestamp.replace(' ', '_').replace(':', '-')}.json"

    # Convert the dictionary to a JSON object and write it to a file
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)



# Loop to keep asking for unique strings and creating new JSON files
while True:
    # Ask for a unique string as input
    unique_str = input("Please enter a unique string (or 'exit' to quit): ")

    # Check if the user wants to exit
    if unique_str.lower() == 'exit':
        break

    # Call the function
    create_json(unique_str, tag)
