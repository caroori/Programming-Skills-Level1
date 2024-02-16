import time
import sys
import os

## dictionary
destinations = {
    "winter": {"Andorra": {"activities": "skiing", "cost:": 100 }, "Switzerland": {"activities": "tour of the Swiss Alps", "cost": 100}},
    "summer": {"Spain": {"activities": "hiking and extreme sports activities", "cost": 400}, "Portugal": {"activities": "on the beaches", "cost": 400}},
    "spring": {"France": {"activities": "extreme sports activities", "cost": 300}, "Italy": {"activities": "cultural and historical tour", "cost": 300}},
    "Autumn": {"Belgium": {"activities": "hiking and extreme sports activities", "cost": 400}, "Austria": {"activities": "cultural and historical activities", "cost": 400}}
}

################## F U N C T I O N S ##################
def preferences():
    print(" - TRAVEL AGENCY - ")
    print("Answer the following questions to get recomemndations")
    season = input("What season do you want to travel? (winter, summer, spring or autumn): ")
    budget = int(input("What is your travel budget?: $"))
    activity = input("What activity do you prefer? (skiing, tour, hiking, beach, extreme sports, cultural, historical): ")
    return season, budget, activity

def recommendation(season, budget, activity):
    for destination, details in destinations[season].items():
        if activity in details['activities'] and details['cost'] <= budget:
            return destination
    return("Match not found")
    
##Console
def clean_console():
    operative_sistems = os.name
    if operative_sistems == 'posix':  # Linux y macOS
        os.system('clear')
    elif operative_sistems == 'nt':   # Windows
        os.system('cls')

################## E N D   F U N C I O N E S ##################
while True: 
    #clean_console()
    season, budget, activity = preferences()
    destination = recommendation(season, budget, activity)
    print(f"Your best destination would be: {destination}")
    print(" ")