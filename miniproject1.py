# Dictionary containing information about One Piece characters
onepiece_chars = {
    "Luffy": {
        "real name": "Monkey D. Luffy",
        "powers": "Gomu Gomu no Mi (Rubber Fruit)",
        "archenemy": "Akainu"
    },
    "Zoro": {
        "real name": "Roronoa Zoro",
        "powers": "Three-Sword Style",
        "archenemy": "Hawkeye Mihawk"
    },
    "Nami": {
        "real name": "Nami",
        "powers": "Cartography and weather manipulation (Clime-Tact)",
        "archenemy": "Arlong"
    }
}

# Main program loop
while True:
    # Input from user for character name and statistic
    char_name = input("Which One Piece character do you want to know about? (Luffy, Zoro, Nami) (Type 'quit' to exit): ")
    
    # Check if user wants to quit
    if char_name.lower() == 'quit':
        print("Exiting program. Goodbye!")
        break  # Exit the loop if the user chooses to quit
    
    # Check if the character exists in the dictionary
    if char_name in onepiece_chars:
        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ")
        # Check the statistic requested
        if char_stat in onepiece_chars[char_name]:
            value = onepiece_chars[char_name][char_stat]
            # Print the output
            print(f"{char_name}'s {char_stat} is: {value}")
        else:
            print("Invalid statistic entered.")
    else:
        print("Invalid character entered.")

