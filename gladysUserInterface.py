import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

def printMenu():
    """
    Prints the menu options for the Gladys West Map App.
    """
    print("-- Welcome to the Gladys West Map App --")
    print("[c] to set current position")
    print("[d] to set destination position")
    print("[m] which tells the distance")
    print("[t] to run module tests")
    print("[q] to quit")

def runTests():
    """
    Tests some module functions.
    """
    print("Running a few tests")

    # Test login function
    userLogin.login()

    # Test readSat function
    satellite_data = satellite.readSat("example_satellite", "path_to_data")
    print("Satellite Data:", satellite_data)

    # Test gpsValue function
    result = compute.gpsValue(10, 20, "satellite_name")
    print("GPS Value:", result)

    print("Tests completed.")

def setCurrentPosition():
    """
    Sets the current position.
    """
    current_pos = input("Enter current position (x y): ").split()
    if len(current_pos) != 2 or not all(coord.isdigit() and 0 <= int(coord) <= 99 for coord in current_pos):
        print("Invalid input. Position must be in the format 'x y' and both x and y must be integers between 0 and 99.")
    else:
        print("Current position set to:", tuple(map(int, current_pos)))

def setDestinationPosition():
    """
    Sets the destination position.
    """
    dest_pos = input("Enter destination position (x y): ").split()
    if len(dest_pos) != 2 or not all(coord.isdigit() and 0 <= int(coord) <= 99 for coord in dest_pos):
        print("Invalid input. Position must be in the format 'x y' and both x and y must be integers between 0 and 99.")
    else:
        print("Destination position set to:", tuple(map(int, dest_pos)))

def mapDistance():
    """
    Maps the distance.
    """
    pass  # Placeholder for actual functionality

def start():
    """
    Logs the user in, and runs the app
    """
    userName = userLogin.login()
    runApp(userName)

def runApp(userName):
    """
    Runs the app.
    """
    print("Hello,", userName)
    
    menu_options = {
        'c': setCurrentPosition,
        'd': setDestinationPosition,
        'm': mapDistance,
        't': runTests,
        'q': lambda: print("Exiting...")
    }

    user_quit = False
    while not user_quit:
        printMenu()
        userInput = input("Enter a command: ").lower()

        if userInput in menu_options:
            menu_options[userInput]()
            if userInput == 'q':
                user_quit = True
        else:
            print("Invalid command. Please try again.")

    print("\nThank you for using the Gladys West Map App!\n")

# Example usage
if __name__ == "__main__":
    start()
