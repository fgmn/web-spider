

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import collections # 词频统计


# d = path.dirname()
# f = open(path.join(d, '')).read()
#
# default_mode = jieba.cut(f)
# text = " ".join(default_mode)

def GetWordCloud():

    path_text = 'C:/Users/DELL/Desktop/2.txt'
    path_img = 'C:/Users/DELL/Desktop/1.jpg'

    f = open(path_text, 'r', encoding='utf-8').read()

    cut_text = " ".join(jieba.cut(f))

    background_image = np.array(Image.open(path_img))

    wordcloud = WordCloud(
        font_path='C:/Windows/Fonts/HGY4_CNKI.TTF',# 字体设置
        background_color="white",mask=background_image).generate(cut_text)

    image_colors = ImageColorGenerator(background_image)
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.show()

def GetWordCloudd():

    path_text = '生化危机5：罪罚'

    f = open(path_text, 'r', encoding='utf-8').read()# f为字符串类型

    cut_text = jieba.cut(f, cut_all=False) # 精确分词模式
    # print(type(cut_text)) # <class 'collections.Counter'>

    # 自定义滤词库
    remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能',
                    u'都', u'。', u' ', u'、', u'中', u'在', u'了', u'通常', u'如果',
                    u'我们', u'需要', u'“', u'”', u'\n', u'到', u'!', u'我', u'也',
                    u'看', u'就', u'系列', u'最后', u'这', u'…', u'电影', u'?', u'还',
                    u'还是', u'一个', u'！', u'有', u'人', u'但', u'没', u'终于', u'？',
                    u'~', u'啊', u'不']

    scn_text = []
    for word in cut_text:
        if word not in remove_words:
            scn_text.append(word)

    word_counts = collections.Counter(scn_text)
    # print(type(word_counts)) # <class 'collections.Counter'>
    word_counts_top = word_counts.most_common(100)
    print(word_counts_top)

    wordcloud = WordCloud(
        font_path='C:/Windows/Fonts/HGY4_CNKI.TTF',# 字体设置
        background_color="white",height=880,width=1000).generate_from_frequencies(word_counts) # 从字典生成词云

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show(dpi=1080)

GetWordCloud()
