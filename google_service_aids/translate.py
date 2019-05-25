#!/usr/bin/python3.7

from bs4 import BeautifulSoup
import requests
import sys

url = 'https://www.google.com/search?q={}'
query = 'meaning of {} in {}'

def translate_to(word, language='English'):
    final_url = url.format(query.format(word, language))
    source_code = requests.get(final_url)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    plain_text = soup.find("div", {'class': 'AP7Wnd'}).text
    return plain_text


if __name__ == '__main__':
    if len(sys.argv) >= 1 and len(sys.argv) <= 3:
        f = 0
        word = sys.argv[1]

        try:
            language = sys.argv[2]
        except IndexError:
            result = translate_to(word)
            print(result)
            f = 1

        if f == 0:
            result = translate_to(word, language=language)
            print(result)
    else:
        print('No input word found')
