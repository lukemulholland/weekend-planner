import activities

def load_activities():
    # Load or define activity data
    return activities.activity_list

def get_user_preferences():
    # Collect user input (activity type, time, weather)
    activity_type = ""
    time = 0
    weather = ""

    while activity_type == "":
        activity_input = input("\nWhat would you like to do this weekend? Restaurant or Activity?\n")
        # Take the first letter of user input to determine activity type, handle exceptions
        if activity_input[0].lower() == "r":
            activity_type = "restaurant"
        elif activity_input[0].lower() == "a":
            activity_type = "activity"
        else: 
            activity_type = ""
            print("\nPlease select either restaurant or activity\n")
    
    while time == 0:
        time_input = input("\nHow long do you have (in minutes)?\n")
        try:
            time = int(time_input)
        except ValueError:
            print("\nPlease enter a valid number for time.")
    
    while weather == "":
        weather = input("\nWhat's the weather forecast?")
    
    return activity_type, time, weather

def filter_activities(activities, preferences, weather):
    # Filter activities based on user input
    pass

def display_recommendations(filtered_activities):
    # Display matching activities
    pass

def main():
    print("\nWelcome to your weekend planner\n")
    activities = load_activities()
    preferences = get_user_preferences()
    filtered = filter_activities(activities, preferences)
    display_recommendations(filtered)

if __name__ == "__main__":
    main()
