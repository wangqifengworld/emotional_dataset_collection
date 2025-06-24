import pandas as pd
import re

csv_path = "./personality-detection/CSV/friends-personality.csv"
df = pd.read_csv(csv_path, index_col=0)
print("--------------------persona sample--------------------")
print(df.iloc[0])

def extract_utterances(row):
    # Remove the first <b>...</b> if it matches the scene/character header
    text = re.sub(r"^<b>.*?</b><br><br>", "", row['text'], count=1, flags=re.DOTALL)
    # Find all utterances in the text
    utterances = re.findall(r"<b>(.*?)</b>:\s*(.*?)(?=<b>|$)", text, re.DOTALL)
    results = []
    for speaker, utterance in utterances:
        speaker = speaker.strip()
        utterance = utterance.strip().replace('<br>', '').replace('\n', ' ')
        # Only assign personality if speaker matches the target character
        if speaker == row['character']:
            results.append({
                'scene_id': row['scene_id'],
                'character': speaker,
                'utterance': utterance,
                'cAGR': row['cAGR'],
                'cCON': row['cCON'],
                'cEXT': row['cEXT'],
                'cOPN': row['cOPN'],
                'cNEU': row['cNEU'],
            })
        else:
            results.append({
                'scene_id': row['scene_id'],
                'character': speaker,
                'utterance': utterance,
                'cAGR': None,
                'cCON': None,
                'cEXT': None,
                'cOPN': None,
                'cNEU': None,
            })
    return results
print("in \"text\",many characters speak,but only one speaker have OCEAN,the processed dialogue is below:")
# Flatten all utterances into a new DataFrame
all_utterances = []
for _, row in df.iterrows():
    all_utterances.extend(extract_utterances(row))

utterance_df = pd.DataFrame(all_utterances)

# Show a sample
print(utterance_df.head(10))