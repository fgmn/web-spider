


import requests
from pyquery import PyQuery as pq



url = "https://www.zhihu.com/explore"

headers = {
            "user-agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
html = requests.get(url=url, headers=headers).text

doc = pq(html)
# print(doc)
items = doc('.ExploreHomePage-ContentSection-body .ExploreCollectionCard-contentItem').items()
# print(items)
# 返回一个生成器

for item in items:
    # 问题和回答为一组信息，先获得一个上级标签，在一起提取问答
    q = item.find('.ExploreCollectionCard-contentTitle').text()
    # print(q + '\n')
    # author = item.find('.author-link-line').text()
    answer = item.find('.ExploreCollectionCard-contentExcerpt').text()
    # print(answer + '\n')

    # 写入文件

    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([q, answer]))
    # 分隔
    file.write('\n' + '=' * 50 + '\n')
    file.close()


# find('.ExploreCollectionCard-contentTitle').

# 问题class：ExploreCollectionCard-contentTitle

# 回答class：ExploreCollectionCard-contentExcerpt











