#百度的关键词接口http://www.baidu.com/s?wd=keyword
#要点params来增加url的条件
import requests
url="http://www.baidu.com/s"
keyword="Python"
kv={'wd':keyword}
try:
    r=requests.get(url,params=kv)
    #params是参数的意思
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")





