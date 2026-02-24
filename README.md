# The Office Dialogue Annotator

--------------------------------------------------

This tool lets our team label dialogue lines from *The Office* and keeps track of progress for each annotator.

It is simple to run and automatically saves your work.

--------------------------------------------------

## What You Need

• Python 3 installed  
• A file named **dialogue.csv** in the same folder  
• The project files in one directory  

--------------------------------------------------

## Setup (First Time Only)

### 1. Install Python
Check if Python is installed:

python --version

If not installed, download from:
https://www.python.org/downloads/

---

### 2. Install required library

Open terminal / command prompt in the project folder and run:

pip install -r requirements.txt

This installs everything needed.

--------------------------------------------------

## dialogue.csv Format

The CSV file must have **two columns**:  

1. `name` → the original speaker (e.g., Michael, Jim, Pam)  
2. `dialogue` → the line they say  

Example:

name,dialogue  
Michael,"That's what she said."  
Jim,"Hey Pam."  
Dwight,"Identity theft is not a joke."  

--------------------------------------------------

## How to Run the Annotator

In the project folder run:

python annotator.py

--------------------------------------------------

## How It Works

1. Select your user:
   1 = Vedant  
   2 = Kyen  
   3 = Harsh  

2. A random dialogue appears (from the `dialogue` column).

3. Enter the number for the character label (see mapping below).

4. The annotation saves automatically.

5. Press **q** anytime to quit safely.

--------------------------------------------------

## Label Mapping

Use the following numbers to label each dialogue line with the correct character:

1 = Michael  
2 = Dwight  
3 = Jim  
4 = Pam  
5 = Ryan  
6 = Andy  
7 = Angela  
8 = Kevin  
9 = Oscar  
10 = Stanley  
11 = Phyllis  
12 = Meredith  
13 = Creed  
14 = Kelly  
15 = Toby  
16 = Darryl  
17 = Erin  

**Example:**  
If the dialogue is `"That's what she said."`, type `1` for Michael and press Enter.  
If the dialogue is `"I love this project."`, type `4` for Pam and press Enter.  

--------------------------------------------------

## Files Created Automatically

annotated_dialogue.csv  
→ stores labeled dialogue  

progress.json  
→ tracks time spent and completed lines  

--------------------------------------------------

## Important Notes

• You can stop anytime. Progress is saved.  
• Keep all files in the same folder.  
• Do not rename the files.  
• If dialogue.csv is missing, the program will warn you.  

--------------------------------------------------

## Quick Start (TLDR)

pip install -r requirements.txt  
python annotator.py  

Pick your user → label dialogue using the number mapping → press q to exit.

## Credit and License
--------------------------------------------------

The data we used for annotated is derived from [https://github.com/maxwiseman/officequotes](https://github.com/maxwiseman/officequotes), which is licensed under the GNU Affero General Public License v3.0. 
This repository is therefore also licensed under AGPL-3.0.
