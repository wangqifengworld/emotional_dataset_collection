import pandas as pd

path="./CPED/data/CPED/test_split.csv"
# Load the CSV file
df = pd.read_csv(path)


columns = df.columns
# Get all column names
print("columns")
print(columns.tolist())


# Print every column of the first row
first_row = df.iloc[0]
print("--------------------CPED sample--------------------")

print(first_row)

# --------------------CPED emotion--------------------
# ['neutral', 'worried', 'astonished', 'disgust', 'happy', 'relaxed', 'positive-other', 'negative-other', 'depress', 'anger', 'fear', 'sadness', 'grateful']
# --------------------CPED sentiment--------------------
# ['neutral', 'negative', 'positive']
# --------------------CPED DA--------------------
# 19types:['statement-non-opinion', 'thanking', 'interjection', 'question', 'apology', 'statement-opinion', 'answer', 'greeting', 'other', 'irony', 'disagreement', 'acknowledge', 'command', 'agreement', 'quotation', 'reject', 'conventional-closing', 'appreciation', 'comfort']
print("--------------------CPED emotion--------------------")
emotion_col = 'Emotion'
unique_emotions = df[emotion_col].unique().tolist()
print(unique_emotions)
print("Emotion count:", len(unique_emotions))
with open('cped_emotions.txt', 'w') as f:
    for emo in unique_emotions:
        f.write(f"{emo}\n")

print("--------------------CPED sentiment--------------------")
sentiment_col = 'Sentiment'
unique_sentiments = df[sentiment_col].unique().tolist()
print(unique_sentiments)
print("Sentiment count:", len(unique_sentiments))
with open('cped_sentiments.txt', 'w') as f:
    for sent in unique_sentiments:
        f.write(f"{sent}\n")

print("--------------------CPED DA--------------------")
da_col = 'DA'
unique_das = df[da_col].unique().tolist()
print(unique_das)
print("DA count:", len(unique_das))
with open('cped_das.txt', 'w') as f:
    for da in unique_das:
        f.write(f"{da}\n")