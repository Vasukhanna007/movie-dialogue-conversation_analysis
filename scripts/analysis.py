"""
basic analysis of pony based on “verbosity”, “mentions”, “follow_on_comments”, “non_dictionary_words”
"""
import argparse
import json
from hw3.verbosity import verbosity
from hw3.follow_on_comments import follow_on_comments
from hw3.non_dictionary_words import non_dictionary_words
from hw3.mentions import mentions
import parser
import os.path as osp
import pandas as pd
from collections import Counter, defaultdict


def parsers():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'src_file', help='the file that has pony dialogues should be a csv')
    parser.add_argument(
        '-o', help='Output file name', default='stdout')
    args = parser.parse_args()

    src_file = args.src_file
    filename = args.o
    return src_file, filename


def read_csv(src_file):
    """
    read csv file
    """
    df = pd.read_csv(src_file, engine='python')
    return df


def final_dict(src_file):
    """
    make final dict and return it 
    """
    final_dict = {}
    final_dict['verbosity'] = verbosity(df=read_csv(src_file))
    final_dict['mentions'] = mentions(df=read_csv(src_file))
    final_dict['follow_on_comments'] = follow_on_comments(
        df=read_csv(src_file))
    final_dict['non_dictionary_words'] = non_dictionary_words(
        df=read_csv(src_file), path_of_dictionary=osp.join("..", 'data', 'words_alpha.txt'))
    # r = json.dumps(final_dict)
    # loaded_r = json.loads(r)
    return final_dict


def write_file(filename, src_file):
    """
    write json into file if optional argument is not given
    """
    if filename == 'stdout':
        r = json.dumps(final_dict(src_file))
        loaded_r = json.loads(r)
        print(loaded_r)
    else:
        with open(filename, 'w') as file:
            file.write(json.dumps(final_dict(src_file)))


def main():
    src_file, filename = parsers()
    read_csv(src_file)
    write_file(filename, src_file)


if __name__ == '__main__':
    main()
