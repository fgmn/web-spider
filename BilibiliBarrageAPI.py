
from bilibili_api.video import get_comments_g
from bilibili_api import video
# import bilibili_api as bili
import pandas as pd
import re


# BV1WX4y1g7Pf 哪吒重生
# BV1uv411q7Mv
bvid = "BV1WX4y1g7Pf"
# file_name = "哪吒重生(弹幕"
file_name = "哪吒重生（评论"

v = video.get_video_info(bvid=bvid)

# 先用items()处理
for i, j in v.items():
    if(i == "cid"):
        cid = j
# print(cid)
# print(v)

# 获得弹幕信息
'''
dat = []

c = video.get_danmaku(bvid=bvid, page_id=cid)
# c = video.get_danmaku(bvid=bvid)
# 返回danmuku类生成器
# print(c)
for i in c:
    # print(i)
    dat.append(str(i)[37:])

# print(dat)
''' 

# 评论部分

# module 'bilibili_api' has no attribute 'get_comments_g'
long_c = get_comments_g(bvid=bvid)
# print(long_c)
comments = []
for comment in long_c:
    # 将评论项目加入列表，也就是普通的所有评论爬虫
    comments.append(comment)

# print(comments)
# 返回字典形式，其中content存储message即评论信息

data = []

for i in comments:
    # print(i)
    # 搜索content
    for dict_key, dict_value in i.items():
        if(dict_key == "content"):
            # print(dict_value)
            # 开始套娃
            for dict_key1, dict_value1 in dict_value.items():
                if(dict_key1 == "message"):
                    # print(dict_value1)
                    data.append(dict_value1)

# 输出到文件
df = pd.DataFrame(data)
df.to_csv(file_name, index=True, header=None, encoding="utf_8_sig")
print("写入文件成功")

