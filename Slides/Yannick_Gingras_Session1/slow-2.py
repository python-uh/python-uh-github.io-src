#! /usr/bin/env python3

import os
import sys
import json
import requests
import postgres

PG_AUTH = os.environ['PG_AUTH']


def word_intersects(word, db, en, fr):
    """ Find if a word is present in three collection of words. """
    is_en = word in en
    is_fr = word in fr
    in_db = db.one("SELECT id FROM words WHERE word = %(w)s", w=word)
    return is_en and is_fr and is_db

def main():
    conn = postgres.Postgres(f'postgresql://ygingras:{PG_AUTH}@localhost/advpy')
    en = json.load(open("words-en.json", "r"))
    fr_data = requests.get("http://files.ygingras.net/words-fr.json")
    fr = json.loads(fr_data.text)
    
    nb_inter = 0
    for word in list(open('words-de.txt', 'r')):
        if word_intersects(word, conn, en, fr):
            nb_inter += 1
    print(f"{nb_inter} word(s) intersects")


if __name__ == "__main__":
    main()
    

