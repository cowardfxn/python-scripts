#!/usr/bin/env/python3


import random, re

class Markov(object):
    def __init__(self, open_file):
        self.cache = {}
        self.open_file = open_file
        self.words = self.file_to_pure_chswords()
        self.word_size = len(self.words)
        self.database()

    def file_to_words(self):
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words

    def file_to_pure_chswords(self):
        self.open_file.seek(0)
        data = self.open_file.read()
        ptr = re.compile("[^\s]")
        words = ptr.findall(data)
        return words

    def triples(self):
        if len(self.words) < 3:
            return

        for i in range(self.word_size - 2):
            yield(self.words[i], self.words[i+1], self.words[i+2])

    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate_markov_text(self, size=25):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in range(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return ''.join(gen_words)

if __name__ == '__main__':
    with open("/Users/fanxn/Desktop/4234/2.txt") as ifs:
        markov = Markov(ifs)
        print(markov.generate_markov_text(200))