# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 16:15:20
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 16:47:29
import multiprocessing
import string

from multiprocessing_mapreduce import SimpleMapReduce

def file_to_words(filename):
    STOP_WORDS = set([
        'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'if',
        'in', 'is', 'it', 'of', 'or', 'py', 'rst', 'that', 'the',
        'to', 'with',
        ])
    TR = str.maketrans({
        p: ' '
        for p in string.punctuation
        })
    print(f'{multiprocessing.current_process().name} reading {filename}')
    output = []

    with open(filename, 'rt') as f:
        for line in f:
            if line.lstrip().startswith('..'):
                continue
            line = line.translate(TR)
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append((word, 1))
    return output

def count_words(item):
    word, occurences = item
    return (word, sum(occurences))

if __name__ == '__main__':
    import operator
    import glob

    input_files = glob.glob('*.rst')

    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()

    print(f'\nTOP 20 WORDS BY FREQUENCY\n')
    top20 = word_counts[:20]
    longest = max(len(word) for word, count in top20)
    for word, count in top20:
        print(f'{word:<{longest+1}}: {count:5}')

