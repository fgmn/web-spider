

from pyquery import PyQuery as pq
# 库名和文件名重名，默认为文件名
# 引入pyquery对象，取别名为pq

html = '''
    <body>
    <p class='fake'>腼腆</p>
    <a id='list-121'>崩坏了的我啊</a>
    <a></a>
    <a><div>你无法想象</div></a>
    <i>
        <li class='item-0>无边的孤独连接起来</li>
    </i>
    </body>
'''

# 将长字符串html作为参数传给pyquery类
# 初始化
doc = pq(html)
print(doc('a'))

# 还可直传URL
# https://mp.weixin.qq.com/s/-dIVgVw6OYToBunm6UzVtg

# doc = pq(url='https://mp.weixin.qq.com/s/-dIVgVw6OYToBunm6UzVtg')
# print(doc('title'))

# 返回pyquery类型

# 遍历
# 调用items()得到一个生成器
a = doc('a').items()

print(str(a))
print('---------')
print(type(a))

for item in a:
    print(item, type(item))

























