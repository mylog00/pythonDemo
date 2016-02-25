file_path = 'task10.txt'
url_path = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open(file_path, 'r') as fr:
    url = fr.readline().strip()

import requests
r = requests.get(url)
while 1:
    if r.text.split()[0] == 'We':
        with open('task10out.txt', 'w') as out:
            out.write(r.text)
        break
    print(r.text)
    r = requests.get(url_path + r.text)
