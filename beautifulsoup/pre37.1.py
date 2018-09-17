import requests
from bs4 import BeautifulSoup

url = 'assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
r = requests.get('https://' + url)
soup = BeautifulSoup(r.content, 'html.parser')
my_string = soup.get_text().lower()


def remove_punc(my_s):
    punc = '?!,";:'
    no_punc = ''
    for char in my_s:
        if char not in punc:
            no_punc += char
    return no_punc


clean_list = remove_punc(my_string).split()
average = sum(len(word) for word in clean_list) / len(clean_list)

# for my_word in clean_list:
#    if my_word not in words:
#        print('  -->', my_word)
#        new_lst.append(my_word)

with open('/usr/share/dict/words', 'r') as fd:
    os_dict = fd.read()

new_lst2 = [my_word for my_word in clean_list if my_word not in os_dict]

print("\nRepeated and unique words not in MAC dictionary:")
for dup_word in new_lst2:
    print('  -->', dup_word)
print('\nTotal words {}'.format(len(clean_list)))
print('Average word length: {0}'.format(int(average)))
print('Total unique words not in dictionary: {}\n'.format(len(set(new_lst2))))
