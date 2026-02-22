import pandas as pd
import csv
import sys
import json

users ={ 
    "1": "Vedant", 
    "2": "Kyen",  
    "3": "Harsh"
        }

ANNOTATED_FILE = "15_perct_annotated_dialogue.csv"
PROGRESS_FILE = "progress.json"
INPUT_FILE = "15_percent_subset.csv"

try:
    df = pd.read_csv(INPUT_FILE, encoding='latin-1')
    df = df.reset_index(drop=True)
except FileNotFoundError:
    print("Warning: Input file not found!!")
    sys.exit(1)

try:
    with open(PROGRESS_FILE, "r") as f:
        progress = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    progress = {uid: {"index": 0, "completed": 0} for uid in users}

# Make sure all users exist in progress (in case progress.json is from old version)
for uid in users:
    if uid not in progress:
        progress[uid] = {"index": 0, "completed": 0}

try:
    open(ANNOTATED_FILE, "r").close()
except FileNotFoundError:
    with open(ANNOTATED_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["dialogue", "label", "other_label", "user"])

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

    while True:
        current_user = input("Select User (1- Vedant, 2- Kyen, 3- Harsh): ")
        if current_user == "q":
            print("Exiting...")
            sys.exit(0)
        if current_user in users:
            return current_user
        else:
            print("Invalid selection.\n")

def stats(user, completed, total):
    remaining = max(0, total - completed)
    lines = [
        f"User      : {users[user]}",
        f"Completed : {completed} / {total}",
        f"Remaining : {remaining}",
    ]
    width = max(len("Your Stats"), *(len(line) for line in lines)) + 4

    def row(text):
        return f"║ {text:<{width-2}} ║"

    print("╔" + "═" * width + "╗")
    print(f"║ {'Your Stats':^{width-2}} ║")
    print("╠" + "═" * width + "╣")
    for l in lines:
        print(row(l))
    print("╚" + "═" * width + "╝")

def save_annotation(dialogue, label, other_label, user):
    with open(ANNOTATED_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([dialogue, label, other_label, users[user]])

def save_progress(user, index, completed):
    progress[user] = {"index": index, "completed": completed}
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=4)

def annotate(user):
    total = len(df)
    current_index = progress[user].get("index", 0)
    completed = progress[user].get("completed", 0)

    # Clamp index in case of stale progress
    if current_index >= total:
        print("You have already annotated all rows!")
        return

    print(f"\nStarting from row {current_index + 1} of {total}\n")

    for i in range(current_index, total):
        row = df.iloc[i]
        dialogue_text = row.iloc[0]
        other_label = row.iloc[1]

        print(f"\n{'─'*50}")
        print(f"[{i+1} / {total}]  ({total - i - 1} remaining after this)")
        print(f"{'─'*50}")
        print(f"Dialogue:\n  {dialogue_text}\n")

        while True:
            choice = input("\nEnter label number (or q to quit): ").strip()

            if choice == "q":
                save_progress(user, i, completed)
                print("\nProgress saved.\n")
                stats(user, completed, total)
                return

            if choice in labels:
                label = labels[choice]
                save_annotation(dialogue_text, label, other_label, user)
                completed += 1
                print(f"✓ Saved as '{label}'\n")
                break
            else:
                print("Invalid choice, try again.")

    save_progress(user, total, completed)
    print("\n All rows annotated!")
    stats(user, completed, total)

def main():
    user = select_user()
    total = len(df)
    stats(user, progress[user].get("completed", 0), total)
    annotate(user)

if __name__ == "__main__":
    main()