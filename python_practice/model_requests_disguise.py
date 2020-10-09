import requests
def Disguise(url):
    kv={"user-agent":"Mozilla/5.0"}
    #把自己伪装成浏览器
    try:
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬虫失败"

if  __name__=="__main__":
    url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
    print(Disguise(url))