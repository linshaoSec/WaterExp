import threading
import time
import requests
import console
import sys

th=40
my_urlOks=[]
my_urlErrs=[]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
           # 'Connection':'keep-alive',
           'Cookie': 'baidu=79212t0db8t7tkdiiaggr8f2tl',
           'Cache-Control': 'max-age=0',
           'connection': 'close'}
def doscan(url):
    if not url[0:4] == "http": url = "http://" + url
    url=str.strip(url)
    try:
        res = requests.get(url, verify=False, timeout=3, stream=True, headers=headers,)#proxies=proxy)
        status = res.status_code
        if status==400:
            print("\033[1;0;90m[*]"+url+"--400,开始使用https协议\033[0m")
            if (url[:7] == "http://"):
                url = "https://" + url[7:]
                res2 = requests.head(url, verify=False, timeout=3, stream=True, headers=headers,)#proxies=proxy)
                if(res2.status_code==400):
                    print("\033[1;0;90m[*]" + url + "--400,http和https都返回400,已移到my_urlErrs[]\033[0m")
                    # print(url+" ")
                    my_urlOks.append(url)
                elif(res2.status_code==200):
                    print("\033[1;0;1m%s%d\033[0m"%(url,200))
                    my_urlOks.append(url)
                else:
                    print("注意:未知响应码__110行")
        elif status==200:
            print("\033[1;0;1;92m%s\t%d\033[0m"%(url,200))
            my_urlOks.append(url)
        else:
            print(url,status)
            my_urlOks.append(url)
    except Exception as e:
        # print(url+" 报错",e.__class__.__name__)
        my_urlErrs.append(url+" 错误类型:"+e.__class__.__name__)
class Inittools:
    def getokurls(self,urls):

        s=[]
        for i in urls:
            t1 = threading.Thread(target=doscan, args=[i], kwargs={})
            s.append(t1)
        print("添加任务完成，共%d个"%(len(s)))

        #过滤可访问url
        while len(s):
            if threading.activeCount() < th:
                # print("当前存活线程数%d,当前线程最大值%d,剩余任务%d"%(threading.activeCount(),th,len(s)))
                s[0].start()
                s.remove(s[0])
            else:
                time.sleep(1)
                # print("休眠")
        while threading.activeCount()!=1:
            # print(threading.activeCount())
            time.sleep(1)
        return my_urlOks,my_urlErrs
    pass
#

#

#
#

# print("-----------------------------------------")
# for i in my_urlOks:
#     print(i)