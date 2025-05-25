import activities

def load_activities():
    # Load or define activity data
    return activities.activity_list

def get_user_preferences():
    # Collect user input (activity, time, weather)
    activity = ""
    time = 0
    weather = ""

    while activity == "":
        activity_input = input("\nWhat would you like to do this weekend? Restaurant or Activity?\n")
        # Take the first letter of user input to determine activity type, handle exceptions
        if activity_input[0].lower() == "r":
            activity = "restaurant"
        elif activity_input[0].lower() == "a":
            activity = "activity"
        else: 
            activity = ""
            print("\nPlease select either restaurant or activity\n")
    
    while time == 0:
        time_input = input("\nHow long do you have (in minutes)?\n")
        try:
            time = int(time_input)
        except ValueError:
            print("\nPlease enter a valid number for time.\n")
    
    while weather == "":
        weather_input = input("\nWhat's the weather forecast (Sunny, Overcast or Raining)?\n")
        if weather_input[0].lower() == "s":
            weather = "sunny"
        elif weather_input[0].lower() == "o":
            weather = "overcast"
        elif weather_input[0].lower() == "r":
            weather = "raining"
        else: 
            weather = ""
            print("\nPlease select either sunny, overcast or raining\n")
    
    print(activity, time, weather)
    return activity, time, weather

def filter_activities(activities, preferences):
    # Filter activities based on user input
    activity, time, weather = preferences
    filtered_activities = []
    for option in activities:
        if option["type"] == activity:
            if option["time"] <= time:
                if weather in option["weather"]:
                    filtered_activities.append(option)
    return filtered_activities


def display_recommendations(filtered_activities):
    # Display matching activities
    print("\nDisplaying your weekend recommendations:\n")
    for option in filtered_activities:
        print(f"Activity: {option["name"]}")
        print(f"Type: {option["type"]}")
        print(f"Time: {option["time"]}\n")

def main():
    print("\nWelcome to your weekend planner\n")
    activities = load_activities()
    preferences = get_user_preferences()
    filtered = filter_activities(activities, preferences)
    display_recommendations(filtered)

if __name__ == "__main__":
    main()
