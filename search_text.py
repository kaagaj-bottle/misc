from typing import List, Dict, Tuple

corpusWordMap = {}
isMapCreated = False


def create_word_map(sentences: List[str]) -> Tuple[Dict, bool]:
    lenSentences = len(sentences)
    map = {}
    for i in range(lenSentences):

        wordList = sentences[i].strip().split(" ")
        lenWords = len(wordList)

        for j in range(lenWords):

            if wordList[j] == "":
                continue
            if wordList[j] in map:
                map[wordList[j]].append(i)
            else:
                map[wordList[j]] = [i]

    return map, True


def search(word: str) -> List[str]:
    global corpusWordMap, isMapCreated, sentences
    if not isMapCreated:

        corpusWordMap, isMapCreated = create_word_map(sentences)

    idxs = corpusWordMap.get(word, [])
    result = [sentences[i] for i in idxs]

    return result


sentences = [
    "The sun set behind the mountains, painting the sky in shades of orange and pink.",
    "She opened the book and was instantly transported to a magical world.",
    "The smell of freshly baked bread filled the kitchen.",
    "He watched the rain fall, lost in his own thoughts.",
    "The cat curled up on the windowsill, basking in the afternoon sun.",
    "The sound of the waves crashing against the shore was soothing.",
    "She wore a dress that sparkled like the night sky.",
    "He couldn't help but laugh at the silly joke.",
    "The flowers in the garden were in full bloom.",
    "The city lights twinkled like stars in the distance.",
    "She danced as if no one was watching.",
    "The dog wagged its tail happily when it saw its owner.",
    "The snow covered everything in a blanket of white.",
    "He played the piano with a passion that was contagious.",
    "The wind whispered through the trees.",
    "She sang a lullaby to her baby, hoping to soothe him to sleep.",
    "The coffee shop was buzzing with activity.",
    "He climbed to the top of the hill and looked out over the valley.",
    "The children ran through the park, laughing and playing.",
    "She wrote a letter to her friend, telling her all about her adventures.",
    "The fire crackled in the fireplace, casting a warm glow in the room.",
    "He built a sandcastle on the beach, complete with turrets and a moat.",
    "The autumn leaves crunched underfoot as she walked through the forest.",
    "The airplane soared above the clouds, heading to a distant land.",
    "She planted a tree in memory of her grandmother.",
    "The street was filled with the sound of music and laughter.",
    "He sat by the river, watching the water flow by.",
    "The stars shone brightly in the night sky.",
    "She cooked a delicious meal for her family.",
    "The butterfly landed on a flower, its wings shimmering in the sunlight.",
    "He read a poem aloud, his voice filled with emotion.",
    "The library was a quiet haven, filled with the scent of old books.",
    "She painted a picture of a serene landscape.",
    "The train chugged along the tracks, taking them to a new destination.",
    "The birds sang a beautiful melody at dawn.",
    "He fixed the broken chair with care.",
    "The balloon floated up into the sky, disappearing from view.",
    "She organized a surprise party for her best friend.",
    "The horse galloped across the field, its mane flying in the wind.",
    "He discovered an old photograph in the attic.",
    "The market was filled with the colors and smells of fresh produce.",
    "She knitted a scarf for her sister.",
    "The clock struck midnight, signaling the start of a new day.",
    "He sailed his boat on the calm lake.",
    "The cake was decorated with bright icing and sprinkles.",
    "She told a ghost story around the campfire.",
    "The street was lined with cherry blossom trees in full bloom.",
    "He played a game of chess with his grandfather.",
    "The sun rose, casting a golden light over the landscape.",
    "She watched a shooting star and made a wish.",
]
