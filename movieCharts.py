

import requests
import re
import time
import json

def get_one(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.104 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_one(html):
    pattern = re.compile('<dd>.*?<i class="board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?data-val="{.*?}">(.*?)</a></p>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    #print(items)
    #数据规范化
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip(),
            'time':item[4].strip(),
            'score':item[5].strip()+item[6].strip()
        }

def write_to_file(content):
    with open('result.txt', 'at+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one(url)
    #print(html)
    #parse_one(html)
    for item in parse_one(html):
        print(item)
        write_to_file(item)



# 程序入口
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)


















