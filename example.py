import requests

API_KEY = 'trnsl.1.1.20190710T094556Z.6c30d1c7df878f86.fa25a144af7a9ee2609235c6ae47b53f877c4768'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, from_lang, to_lang='ru'):

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return '\n'.join(json_['text'])


with open('News/FR.txt', encoding="utf-8") as text:
    text = [line.rstrip('\n') for line in text.readlines()]
    output = open('News/translated_FR.txt', 'w')
    output.write(translate_it(text, 'fr'))

with open('News/ES.txt', encoding="utf-8") as text:
    text = [line.rstrip('\n') for line in text.readlines()]
    output = open('News/translated_ES.txt', 'w')
    output.write(translate_it(text, 'es'))

with open('News/DE.txt', encoding="utf-8") as text:
    text = [line.rstrip('\n') for line in text.readlines()]
    output = open('News/translated_DE.txt', 'w')
    output.write(translate_it(text, 'de'))
