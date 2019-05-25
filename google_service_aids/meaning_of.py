#!/usr/bin/python3.7

from bs4 import BeautifulSoup
import requests
import sys

url = 'https://www.google.com/search?q={}'
query = 'meaning of {} in english'

def find_meaning_of(word):
    final_url = url.format(query.format(word))
    source_code = requests.get(final_url)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    plain_text = soup.find("div", {'class': 'BNeawe s3v9rd AP7Wnd'})
    ret_value = ''
    for val in plain_text.findAll('div', {'class': 'BNeawe s3v9rd AP7Wnd'}):
        ret_value += val.text + '\n'
    return ret_value[:-1]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        word = sys.argv[1]

        result = find_meaning_of(word)
        print(result)
    else:
        print('No input word found')
