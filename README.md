# Emotional Dataset Collection

![Dataset Comparison](CPED/images/dataset_comparison.png)

---

## CPED

- [CPED GitHub](https://github.com/scutcyr/CPED)

### Sample

```
TV_ID: 27
Dialogue_ID: 27_000
Utterance_ID: 27_000_000
Speaker: 林宛瑜
Gender: female
Age: young
Neuroticism: low
Extraversion: high
Openness: high
Agreeableness: high
Conscientiousness: high
Scene: car
FacePosition_LU: 488_14
FacePosition_RD: 654_204
Sentiment: neutral
Emotion: neutral
DA: statement-non-opinion
Utterance: 好了没事了
```

### Emotion Labels (13)
```
['neutral', 'worried', 'astonished', 'disgust', 'happy', 'relaxed', 'positive-other', 'negative-other', 'depress', 'anger', 'fear', 'sadness', 'grateful']
```

### Sentiment Labels (3)
```
['neutral', 'negative', 'positive']
```

### DA Labels (19)
```
['statement-non-opinion', 'thanking', 'interjection', 'question', 'apology', 'statement-opinion', 'answer', 'greeting', 'other', 'irony', 'disagreement', 'acknowledge', 'command', 'agreement', 'quotation', 'reject', 'conventional-closing', 'appreciation', 'comfort']
```

- **OCEAN**: high & low

---

## PELD

- [PELD GitHub](https://github.com/preke/PELD)

### Sample

```
Speaker_1: Chandler
Speaker_2: The Interviewer
Personality: [0.648, 0.375, 0.386, 0.58, 0.477]
Utterance_1: also I was the point person on my company s transition from the KL-5 to GR-6 system.
Utterance_2: You must ve had your hands full.
Utterance_3: That I did. That I did.
Emotion_1: neutral
Emotion_2: neutral
Emotion_3: neutral
Sentiment_1: neutral
Sentiment_2: neutral
Sentiment_3: neutral
```

#### Dialogue Data Structure

```
Speaker_1: Chandler    Utterance_1: also I was the point person on my company s transition from the KL-5 to GR-6 system.
Speaker_2: The Interviewer    Utterance_2: You must ve had your hands full.
Speaker_1: Chandler    Utterance_3: That I did. That I did.
```

#### Emotion & Sentiment Mapping

- **MELD Sentiments** are mapped as:
    ```python
    Emotion_Senti = {
        'anger': 'negative',
        'sadness': 'negative',
        'neutral': 'neutral',
        'joy': 'positive',
        'surprise': 'positive',
        'fear': 'negative',
        'disgust': 'negative'
    }
    ```
- **EmoryNLP Emotions** are mapped as:
    ```python
    Emo_rename_dict = {
        'Joyful': 'joy',
        'Mad': 'anger',
        'Neutral': 'neutral',
        'Sad': 'sadness',
        'Scared': 'fear'
    }
    ```
- **EmoryNLP Sentiments** are mapped as:
    ```python
    Senti_dict = {
        'Joyful': 'positive',
        'Mad': 'negative',
        'Neutral': 'neutral',
        'Sad': 'negative',
        'Scared': 'negative'
    }
    ```

- **Unique emotions in 'Emotion_1'**: `['neutral', 'surprise', 'fear', 'sadness', 'joy', 'disgust', 'anger']`
- **Unique sentiments in 'Sentiment_1'**: `['neutral', 'positive', 'negative']`

> PELD is merged from MELD & EmoryNLP. Details in `./PELD/data/Dataset_Construction.py`.

---

## FriendsPersona (personality-detection)

- [FriendsPersona GitHub](https://github.com/emorynlp/personality-detection)

### Sample

```
scene_id: 01_e01_c01
text: <b>s01_e01_c01(1) for Joey Tribbiani</b><br>...
character: Joey Tribbiani
cAGR: 1
cCON: 1
cEXT: 0
cOPN: 0
cNEU: 1
```

#### In "text", many characters speak, but only one speaker has OCEAN. The processed dialogue is below:

| scene_id   | character       | utterance                                               | cAGR | cCON | cEXT | cOPN | cNEU |
|------------|-----------------|---------------------------------------------------------|------|------|------|------|------|
| 01_e01_c01 | Ross Geller     | No!! Okay?! Why does everyone keep fixating on...       | NaN  | NaN  | NaN  | NaN  | NaN  |
| 01_e01_c01 | Chandler Bing   | Sometimes I wish I was a lesbian... (They all stare...) | NaN  | NaN  | NaN  | NaN  | NaN  |
| 01_e01_c01 | Ross Geller     | I told mom and dad last night, they seemed to take...   | NaN  | NaN  | NaN  | NaN  | NaN  |
| 01_e01_c01 | Monica Geller   | Oh really, so that hysterical phone call I got...       | NaN  | NaN  | NaN  | NaN  | NaN  |
| 01_e01_c01 | Ross Geller     | Sorry.                                                  | NaN  | NaN  | NaN  | NaN  | NaN  |
| 01_e01_c01 | Joey Tribbiani  | Alright Ross, look. You're feeling a lot of pain...     | 1.0  | 1.0  | 0.0  | 0.0  | 1.0  |
| 01_e01_c01 | Joey Tribbiani  | Strip joint! C'mon, you're single! Have some hormones!  | 1.0  | 1.0  | 0.0  | 0.0  | 1.0  |
| 01_e01_c01 | Ross Geller     | I don't want to be single, okay? I just... I just...    | NaN  | NaN  | NaN  | NaN  | NaN  |
| 01_e01_c02 | Monica Geller   | Now I'm guessing that he bought her the big pipe organ  | NaN  | NaN  | NaN  | NaN  | NaN  |
| 01_e01_c02 | Chandler Bing   | (imitating the characters) Tuna or egg salad? Decide!   | 1.0  | 0.0  | 1.0  | 1.0  | 1.0  |

---

## MEmoR

- [MEmoR GitHub](https://github.com/sunlightsgy/MEmoR)