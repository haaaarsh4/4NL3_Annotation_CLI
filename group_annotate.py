import pandas as pd
import csv
import time
import sys
import json

users ={ 
    "1": "Vedant", 
    "2": "Kyen",  
    "3": "Harsh"
        }

ANNOTATED_FILE = "annotated_dialogue.csv"
PROGRESS_FILE = "progress.json"

try:
    df = pd.read_csv('dialogue.csv')
except FileNotFoundError:
    print("Warning: dialogue.csv not found!!")

try:
    with open(PROGRESS_FILE, "r") as f:
        progress = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    progress = {uid: {"time": 0, "completed": 0} for uid in users}

try:
    open(ANNOTATED_FILE, "r").close()
except FileNotFoundError:
    with open(ANNOTATED_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["dialogue", "label", "user"])

labels = {
    "1": "Michael",
    "2": "Dwight",
    "3": "Jim",
    "4": "Pam",
    "5": "Ryan",
    "6": "Andy",
    "7": "Angela",
    "8": "Kevin",
    "9": "Oscar",
    "10": "Stanley",
    "11": "Phyllis",
    "12": "Meredith",
    "13": "Creed",
    "14": "Kelly",
    "15": "Toby",
    "16": "Darryl",
    "17": "Erin"
        }

def select_user():
    print("╔════════════════════════════════════╗")
    print("║  THE OFFICE  ·  Annotator Login    ║")
    print("╚════════════════════════════════════╝")

    current_user = ""

    while True:
        current_user = input("Select User (1- Vedant, 2- Kyen, 3- Harsh): ")

        if current_user == "q":
            print("Exiting...")
            sys.exit(0)

        if current_user in users:
            return current_user
        else:
            print("Invalid selection.\n")

def format_time(seconds):
    seconds = int(seconds)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    if h > 0:
        return f"{h}h {m}m {s}s"
    elif m > 0:
        return f"{m}m {s}s"
    else:
        return f"{s}s"

def stats(user, elapsed, completed):
    elapsed_text = format_time(elapsed)

    lines = [
        f"User: {users[user]}",
        f"Time: {elapsed_text}",
        f"Completed: {completed}"
    ]

    width = max(len("Your Stats"), *(len(line) for line in lines)) + 4

    def line(text):
        return f"║ {text:<{width-2}} ║"

    print("╔" + "═" * (width-0) + "╗")
    print(f"║ {'Your Stats':^{width-2}} ║")
    print("╠" + "═" * (width-0) + "╣")
    for l in lines:
        print(line(l))
    print("╚" + "═" * (width-0) + "╝")

def random_row():
    row = df.sample(n=1)
    return row.values.tolist()[0]

def save_annotation(dialogue, label, user):
    with open(ANNOTATED_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            dialogue,
            label,
            users[user]
        ])

def save_stats(user, session_time, completed):
    progress[user] = {
        "time": round(session_time, 2),
        "completed": completed
    }

    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=4)

def annotate(user, total_time, total_completed):
    session_start = time.time()
    completed = 0
    
    while True:
        print("Total time spent:", round(total_time + (time.time() - session_start), 1), "seconds")
        row = random_row()
        dialogue_text = row[1]
        
        print("\nDialogue:")
        print(dialogue_text)

        choice = input("Enter label number or q to quit: ")

        if choice == "q":
            session_time = time.time() - session_start
            save_stats(user, round(total_time + session_time, 1), total_completed + completed)
            print("Session saved.\n")

            stats(user, round(total_time + session_time, 1), total_completed + completed)
            return

        if choice in labels:
            label = labels[choice]
            save_annotation(dialogue_text, label, user)
            completed += 1
            print("Saved.\n")
        else:
            print("Invalid choice.\n")

def main():
    user = select_user()
    stats(
        user,
        progress[user]["time"],
        progress[user]["completed"]
    )
    annotate(user, progress[user]["time"], progress[user]["completed"])

if __name__ == "__main__":
    main()
