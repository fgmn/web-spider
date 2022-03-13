


from bs4 import BeautifulSoup

html ='''
    <title id='list-2'>hello</title>
    <p>
        <a name='sqq' class='爱永恒'>
            <span>'ABC'</span>
            <sqq>'forever fake love
            <a>你知不知</a>
            <a>我不知</a>
            <a>除非你知</a>
            <a>否则我不知</a></sqq>
        </a>
    </p>
        
'''


soup = BeautifulSoup(html, 'lxml')


'''
# 标准化缩进格式
print(soup.prettify())
# 输出title节点的文本内容
print(soup.title.string)

# 打印整个标签
print(soup.title)
print(type(soup.title))

# 获取名称
print(soup.title.name)
# 获取属性
print(soup.title.attrs)     # 返回字典形式

# 关联选择

# 选取直接子节点
print(soup.p.contents)

print(soup.p.children)  # 返回生成器类型
for i, child in enumerate(soup.p.children):
    print(i, child)
print('------')
# 得到所有子孙节点
print(soup.p.descendants)
print('------')
for i, child in enumerate(soup.p.descendants):
    print(i, child)

# 获得父亲节点
print(soup.span.parent)

# 获得所有祖先节点
print(soup.span.parents)
print(type(soup.span.parents))
print('------')
print(list(enumerate(soup.a.parents)))  # 返回列表形式



# 查询所有符合条件的节点
# find_all(name, attrs, recursive, text, **kwargs)

# 节点名查询
print(type(soup.find_all(name='sqq')[0]))



for a in soup.find_all(name='sqq'):
    print(a.find_all(name='a'))
    for per in a.find_all(name='a'):
        print(per.string)


# 属性查询

print(soup.find_all(attrs={'name': 'sqq'}))
print('------')
print(soup.find_all(name='sqq'))
'''


# CSS选择器

# print(soup.select('#123'))
print(soup.select('.爱永恒'))


















