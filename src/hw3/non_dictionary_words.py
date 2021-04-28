from collections import Counter, defaultdict
import re
import pandas as pd
import os.path as osp


def non_dictionary_words(df, path_of_dictionary=osp.join("..", "..", 'data', 'words_alpha.txt')):
    """
     5 most non english words spoken by a poony
    """
    no_word_dict = {}
    english_words = set(pd.read_csv(
        path_of_dictionary, sep=" ", header=None)[0])

    ponies = ['Twilight Sparkle', 'Rainbow Dash',
              'Pinkie Pie', 'Applejack', 'Rarity', 'Fluttershy']
    cnt = defaultdict(Counter)
    df_onlyponies = df[df.pony.isin(ponies)]
    for index, row in df_onlyponies.iterrows():
        for i in re.split("[^a-zA-Z]", row['dialog']):
            if i.lower() not in english_words and i != "":
                cnt[row['pony']][i.lower()] += 1
    list_twilight = []
    list_rainbow = []
    list_pinky = []
    list_apple = []
    list_rarity = []
    list_fluttershy = []

    for j in range(5):
        list_twilight.append((cnt['Twilight Sparkle']).most_common(5)[j][0])
        list_rainbow.append((cnt['Rainbow Dash']).most_common(5)[j][0])
        list_pinky.append((cnt['Pinkie Pie']).most_common(5)[j][0])
        list_apple.append((cnt['Applejack']).most_common(5)[j][0])
        list_rarity.append((cnt['Rarity']).most_common(5)[j][0])
        list_fluttershy.append((cnt['Fluttershy']).most_common(5)[j][0])
    no_word_dict["twilight"] = list_twilight
    no_word_dict["rainbow"] = list_rainbow
    no_word_dict["pinky"] = list_pinky
    no_word_dict["applejack"] = list_apple
    no_word_dict["rarity"] = list_rarity
    no_word_dict['fluttershy'] = list_fluttershy
    return no_word_dict
