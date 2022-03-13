
# 1、构造url于douban平台搜索电影
# https://www.baidu.com/s?ie=UTF-8&wd=%E4%BD%A0%E5%A5%BD
# https://search.douban.com/movie/subject_search?search_text=%E6%B5%81%E6%84%9F%EF%BC%882013%EF%BC%89&cat=1002
# https://search.douban.com/movie/subject_search?search_text=%E4%BC%A0%E6%9F%93%E7%97%85%EF%BC%882011%EF%BC%89&cat=1002

# 设计思路：键入关键词，搜索，提供可爬取选项，选择爬取

film = ['流感（2013）',
'传染病（2011）',
'感染列岛（2009）',
'极度恐慌（1995）',
'末日病毒（2009）',
'盲流感（2008）',
'天外来菌（2008）',
'末日侵袭（2008）',
'末日孤舰（2014-2016）',
'一级恐惧（1999）',
'惊变28天（2002）',
'卡桑德拉大桥（1976）',
'大明劫（2013）',
'十二猴子（1996）',
'终极细胞战（2013）',
'死亡录像（2007）',
'伊波拉病毒（1996）',
'非典人生（2003）',
'流行病毒（2007）',
'神秘感染（2013）',
'灭顶之灾（2008）',
'釜山行（2016）',
'铁线虫入侵（2013）',
'致命拜访（2007）',
'我是传奇（2007）',
'生化危机1',
'生化危机2',
'生化危机3',
'生化危机4',
'生化危机5',
'生化危机6'
]
# print(film[5])
url = []

import urllib.parse

for i in film:
    url.append('https://search.douban.com/movie/subject_search?search_text={}&cat=1002'.format(urllib.parse.quote(i))) # 中文转码

print(url[8])

import urllib.request

for i in url:
   req = urllib.request.Request(i)
   with urllib.request.urlopen(req) as response:
       data = response.read()
       htmlstr = data.decode()
       print(htmlstr)
       # 默认第一个为符合项？




