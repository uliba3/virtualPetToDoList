import os
import random
from datetime import datetime
import sys
import cv2
from pet.pet import Pet

class InteractivePet:
    def __init__(self):
        try:
            self.pet = Pet()
            self.current_activity = None
            self.mood = "happy"
            self.last_interaction = datetime.now()
        except Exception as e:
            print(f"Error initializing pet: {str(e)}")
            raise
    
    def greet_user(self):
        try:
            current_time = datetime.now()
            if current_time.hour < 12:
                greeting = f"Good morning! {self.pet.get_name()} is ready to help you with your tasks!"
            elif current_time.hour < 17:
                greeting = f"Good afternoon! {self.pet.get_name()} wants to see what's on the agenda!"
            else:
                greeting = f"Good evening! {self.pet.get_name()} is here to help you wrap up your day!"
                
            return greeting + "\n" + self.pet.get_smiling_image()
        except Exception as e:
            print(f"Error in greeting: {str(e)}")
            return "Hello! Let's get started!"
    
    def run_random_activity(self):
        try:
            activities = [self.pet.get_walking_image(), self.pet.get_barking_image(), self.pet.get_smiling_image()]
            return random.choice(activities)
        except Exception as e:
            print(f"Error getting random activity: {str(e)}")
            return self.pet.get_smiling_image()

def main():
    try:
        # Print current working directory and Python path for debugging
        print("Current working directory:", os.getcwd())
        print("Python path:", sys.path)
        
        interactive_pet = InteractivePet()
        print(interactive_pet.greet_user())
        
        while True:
            print("\nWhat would you like to do?")
            print("1. View tasks")
            print("2. Add task")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ")
            print(f"Your choice: {choice}")
            
            if choice == "1":
                print("Here are your tasks:")
                tasks = interactive_pet.pet.get_all_event()
                if not tasks:
                    print("No tasks yet!")
                else:
                    for i, task in enumerate(tasks):
                        print(f"{i}. {task['Event']} (Date: {task['date']}, Time: {task['time']})")
                
            elif choice == "2":
                try:
                    date = input("Enter date (YYYYMMDD): ")
                    event = input("Enter event description: ")
                    time = input("Enter time (HHMM): ")
                    
                    event_details = {
                        "date": int(date),
                        "Event": event,
                        "time": int(time)
                    }
                    
                    interactive_pet.pet.add_event(event_details)
                    print("Task added successfully!")
                except ValueError as e:
                    print(f"Error adding task: {str(e)}")
                
            elif choice == "3":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
            
            interactive_pet.get_random_activity()
            

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Current working directory:", os.getcwd())
        print("Python path:", sys.path)

if __name__ == "__main__":
    main()
    