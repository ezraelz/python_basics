import json
import os


if os.path.exists('exercise_data.json'):
    with open('exercise_data.json', 'r') as f:
        data = json.load(f)
else:
    data = []


def add_exercise():
    name = input("enter new exercise name: ")
    description = input("enter new exercise description: ")

    exercise = {
        "name": name,
        "description": description
    }

    data.append(exercise)
    with open('exercise_data.json', 'w') as f:
        json.dump(data, f, indent=4)

def view_exercises():
    for exercise in enumerate(data, start=1):
        print(f"{exercise}")

    if not data:
        print("No exercises found. Please add some exercises first.")


def update_exercise():
    excercise_name = input("enter exercise name to update: ")
    for exercise in data:
        if exercise['name'] == excercise_name:
            excercise_name = input("enter new exercise name: ")
            excercise_description = input("enter new exercise description: ")
            exercise['name'] = excercise_name
            exercise['description'] = excercise_description
            with open('exercise_data.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("exercise updated successfully!")

def delete_exercise():
    excercise_name = input("enter exercise name to delete: ")
    for exercise in data:
        if exercise['name'] == excercise_name:
            data.remove(exercise)
            
            with open('exercise_data.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("exercise deleted successfully!")


while True:
    print("""
        1. Add Exercise
        2. View Exercises
        3. Update Exercise
        4. Delete Exercise
        5. Exit
        """
    )
    options = int(input("Select your option: "))
    if options == 1:
        add_exercise()
    if options == 2:
        view_exercises()
    if options == 3:
        update_exercise()
    if options == 4:
        delete_exercise()
    if options == 5:
        break
        print('Goodbye!')


