import pandas as pd
from sklearn.model_selection import train_test_split

# Load labeled data
df = pd.read_csv("train1.csv")

# Basic check
df = df.dropna(subset=['complaint_what_happened', 'label'])
df['label'] = df['label'].astype(int)

# Train-test split (80-20)
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df['complaint_what_happened'].tolist(),
    df['label'].tolist(),
    test_size=0.2,
    stratify=df['label'],
    random_state=42
)
