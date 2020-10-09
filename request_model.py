import requests
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status() #如果状态不是异常，引发HTTPError异常
        r.encoding=r.apparent_encoidng
        return r.text
    except:
        return "产生异常"

if __name__=="__main__":
    url="http://www.baidu.com"
    print(getHTMLText(url))
