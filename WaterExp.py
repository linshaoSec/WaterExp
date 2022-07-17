

from init.HeaderVlun import HeaderVlun
from init.cmdline import parse_args
from init.PrintEntity import PrintEntity
from init.ExportEntity import ExportEntity
import console


allVuln= {}

def scanSingle(url):

    ExportEntity()

    printEntity.showgreen("=>扫描Headers相关漏洞",printEntity.seatNum)
    headers=headerVlun.getHeaders(url)
    if not headers:return
    for key,value in headers.items():
        printEntity.showUnvipInfo2("\t   "+key+" : "+value)
    printEntity.printDefault(""+'- '*20)
    vulnresult1=headerVlun.getHeadersVuln(headers)

    printEntity.showgreen("=>扫描HTTP请求相关漏洞",printEntity.seatNum)
    vulnresult2=headerVlun.getOptionsVlun(url)

    printEntity.showgreen("=>扫描报错信息相关漏洞",printEntity.seatNum)
    vulnresult3=headerVlun.getErrorInfoVuln(url)

    allVuln.setdefault(url,vulnresult1+vulnresult2+vulnresult3)
    printEntity.printDefault(""+'_'*60)
    # printEntity.showgreen("=>页面爬行",printEntity.seatNum)


if __name__ == '__main__':
    options=parse_args()
    print("█  WaterExp: 打工人新时代的摸鱼解决方案，安抚仔挖不到洞的最后一丝欢颜！")#旨在使我们有更多的时间来提升自身能力，而非重复于无意义的操作")

    printEntity=PrintEntity(1)#设置一级显示块
    headerVlun=HeaderVlun()
    from init.Inittools import Inittools
    urls=[]
    okurls=[]
    errUrls=[]

    if options.url:
        print("[+] 开始扫描单个目标 "+options.url)
        urls.append(options.url)
        okurls,errUrls=Inittools.getokurls(None,urls)
        scanSingle(okurls[0])
    if options.urls:
        # globals(urls)
        # globals(okurls)
        # globals(errUrls)
        import os
        if not(os.path.exists(options.urls)):exit("[!] File ["+options.urls+"] not exist!!")
        print("[+] 开始扫描多个目标 "+options.urls)
        f=open(options.urls,'r')
        urls=f.readlines()

        if len(tuple(set(urls)))!=len(urls):
            print("[*] 原%d个,去重后%d个"%(len(urls),len(tuple(set(urls)))))
            urls=tuple(set(urls)) #去重

        okurls,errUrls=Inittools.getokurls(None,urls)
        # print("\n==>",okurls)
        for i in okurls:
            i=i.strip()
            if not i[0:4] == "http": i = "http://" + i
            print("\n"+"█ 开始扫描--> "+i)
            scanSingle(i)
    print()
    # print("█"*80+"\n")
    # printEntity.showred("扫描完毕,请求成功/错误/所有:"+str(len(okurls))+"/"+str(len(errUrls))+"/"+str(len(urls)),1)
    printEntity.showred("扫描完毕,请求成功/错误/所有:"+str(len(okurls))+"/"+str(len(errUrls))+"/"+str(len(urls)),1)
    print()

    for i in allVuln.keys():
        printEntity.showgreen("\tTarget"+"\t"+i,0)
        if len(allVuln[i])<=0:
            printEntity.showUnvipInfo2("-没有找到漏洞,碰瓷失败",2)
        else:
            showonce=True
            for i in allVuln[i]:
                printEntity.seatNum=2
                printEntity.showVulnInfo("-"+i,2)
        printEntity.showUnvipInfo2("_"*60+"\n",2)

    if len(errUrls)>0:
        printEntity.showred("\t请求失败的url: "+str(len(errUrls)),0)
        for i in errUrls:
            printEntity.showUnvipInfo2("-"+i,2)
        printEntity.showUnvipInfo2("_"*60+"\n",2)