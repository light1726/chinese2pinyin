# -*- coding=utf-8 -*-
import config as conf
import os
import pickle

if __name__ == "__main__":
    word_dict = {}
    # read the word dictionary
    # create a dict to map Chinese word to pinyin
    with open(conf.dict_file, 'r') as f:
        for line in f:
            s = line.split(',')
            # the 1st is character, the 2nd is pinyin,
            # the 3rd is part of speech
            word_dict[s[0]+'/'+s[2]] = s[1]

    # read the corpus file
    with open(conf.corpus_file, 'r') as f:
        write_file = open('word_to_add.txt', 'a+')
        for line in f:
            # print(line)
            s = line.split()
            for string in s:
                if not(string in word_dict.keys()):
                    if not(string in write_file.read()):
                        write_file.write(string+'\n')
        write_file.close()


