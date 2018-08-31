
import requests

r = requests.get('http://localhost:5000/rescan?/etc/')
for k, v in r.json().items():
    print(k)
    for one_value in sorted(v):
        print(f'\t{one_value}')

