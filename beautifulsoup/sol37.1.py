import requests
from bs4 import BeautifulSoup
from pprint import pprint

report = {}

urls = ['https://lerner.co.il/',
        # 'https://nytimes.com/',
        # 'https://washingtonpost.com/'
        ]

dict_filename = '/usr/share/dict/words'

dict_words = {one_word.strip() for one_word in open(dict_filename)}

average_length = {}
not_in_dict = {}

for one_url in urls:
    print(f"Retrieving '{one_url}'...")
    body = requests.get(one_url).content

    soup = BeautifulSoup(body, 'lxml')
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    print(text[:1000])
    words = text.split()

    not_in_dict[one_url] = len(set(words) - dict_words)
    average_length[one_url] = sum([len(one_word)
                                   for one_word in words]) / len(words)
print()
for one_url in urls:
    print(f"{one_url:20}: {average_length[one_url]} {not_in_dict[one_url]}")
