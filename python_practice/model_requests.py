

import requests
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
#用try和except连进行异常处理 
if __name__=="__main__":
    url="https://item.jd.com/22298647726.html"#注意一定要是http:
    print(getHTMLText(url))
