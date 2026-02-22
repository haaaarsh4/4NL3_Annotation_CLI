import pandas as pd

try:
    df = pd.read_csv('annotated_dialogue.csv')
except FileNotFoundError:
    print("Warning: annotated_dialogue.csv not found!!")

df_subset = df.sample(frac=0.15, random_state=42)
df_subset.to_csv('15_percent_subset.csv', index=False)