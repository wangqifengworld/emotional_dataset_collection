import pandas as pd

path = "./PELD/data/Dyadic_PELD.tsv"
df = pd.read_csv(path, sep='\t')

# Show one PELD sample (first row)
print("--------------------PELD sample--------------------")
print(df.iloc[0])


print("--------------------dialogue data structure--------------------")
speaker1 = df.iloc[0]['Speaker_1']
utterance1 = df.iloc[0]['Utterance_1']
speaker2 = df.iloc[0]['Speaker_2']
utterance2 = df.iloc[0]['Utterance_2']
utterance3 = df.iloc[0]['Utterance_3']

print(f"Speaker_1:{speaker1}    Utterance_1:{utterance1}")
print(f"Speaker_2:{speaker2}    Utterance_2:{utterance2}")
print(f"Speaker_1:{speaker1}    Utterance_3:{utterance3}")

print("every utterance has its emotion&sentiment:positive & negative")

print("detail in ./PELD/data/Dataset_Construction.py")

# Print all unique emotions in column 'Emotion_1'
unique_emotions = df['Emotion_1'].unique()
print("Unique emotions in 'Emotion_1':", unique_emotions)

# Print all unique sentiments in column 'Sentiment_1'
unique_sentiments = df['Sentiment_1'].unique()
print("Unique sentiments in 'Sentiment_1':", unique_sentiments)