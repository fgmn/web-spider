


def HTTD(headers):

    # 格式化headers
    st1 = headers.split('\n')   # 以该符号分隔文本
    headers_dict = {}
    for text1 in st1:
        s1 = text1.replace(': ', '#$', 1)
        st2 = s1.split('#$')
        headers_dict[st2[0]] = st2[1]
        # print(st2)
    # 返回字典格式的headers
    return headers_dict


headers ='''Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Cookie: ll="118220"; bid=uo6qbpntGdE; douban-fav-remind=1; _vwo_uuid_v2=D843314CE04CCBB03109064B0FCEE72BB|3541694b8165faa953fc78d1e228aad9; dbcl2="222546299:WVqp0AeMZi4"; __gads=ID=669c5b056fcd0086-2254ffb9e5c400ad:T=1606387728:S=ALNI_MY-rt4SYXx7RqeHEwpIiQ4g7hbmig; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22254; ct=y; ck=nhuh; ap_v=0,6.0; __utmc=30149280; __utma=30149280.1926299260.1604057374.1628153545.1628155644.14; __utmb=30149280.0.10.1628155644; __utmz=30149280.1628155644.14.5.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/
Host: erebor.douban.com
Referer: https://movie.douban.com/subject/26985127/comments?status=P
sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: script
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'''

print(HTTD(headers))