import json
import os

def readSat(sat, pathToJSONDataFiles):
    """
    Reads satellite data from a JSON file.
    """
    file_name = sat + "-satellite.json"
    file_path = os.path.join(pathToJSONDataFiles, file_name)

    try:
        with open(file_path) as file_handle:
            data = json.load(file_handle)
            return data
    except IOError:
        print("ERROR: Unable to open the file " + file_path)
        raise IOError

def gpsValue(x, y, sat):
    """
    Returns the GPS value for the given coordinates and satellite.
    """
    path_to_json_data_files = "C:/Users/rayna/OneDrive/Documents/Github/Glady-West-App-Assignment"

    # Read satellite data
    data = readSat(sat, path_to_json_data_files)

    # Search for matching coordinates (x, y) in the data
    for entry in data:
        if entry.get('x') == x and entry.get('y') == y:
            return entry.get('value')

    # If no matching coordinates are found, return None
    print(f"No GPS value found for coordinates ({x}, {y}) and satellite {sat}")
    return None

# Example usage
if __name__ == "__main__":
    # Sample coordinates and satellite name
    x = 10
    y = 20
    satellite_name = "example_satellite"

    # Calculate GPS value
    gps = gpsValue(x, y, satellite_name)
    if gps is not None:
        print("GPS Value:", gps)
