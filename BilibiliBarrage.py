from bilibili_api import video
import re
import pandas as pd

# BVid、fileName
BVid = "BV1oW41157Na"
file_name = '刺客伍六七第一集.csv'

# 获取弹幕
my_video = video.get_video_info(bvid=BVid)
# print(my_video)
danmu = video.get_danmaku(page_id="47506569", bvid=BVid)

# 数据处理
data = [data.text for data in danmu]
for i in data:
    i = re.sub('\s+', '', i)

# 查看数量
print("弹幕数量为：{}".format(len(data)))

# 输出到文件
df = pd.DataFrame(data)
df.to_csv(file_name, index=False, header=None, encoding="utf_8_sig")
print("写入文件成功")