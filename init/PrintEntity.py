class PrintEntity:
    seat="\t|"
    seatNum=0
    def __init__(self,num):
        self.seatNum=num
        pass
    def printDefault(self,info):
        print(self.seat*self.seatNum+"%s"%info)
    def showVulnInfo(self,info,numb=-1):#鲜红文字
        if numb!=-1:
            print("\t"*numb+"|\033[1;0;31m%s  \033[0m"%info)
        else:
            print(self.seat*self.seatNum+"\033[1;0;31m%s  \033[0m"%info)
    def showInfo(self,info):#绿色文字
        print(self.seat*self.seatNum+"\033[1;0;32m%s  \033[0m"%info)
    def showInfo2(self,info):#暗蓝文字
        print(self.seat*self.seatNum+"\033[1;0;34m%s  \033[0m"%info)

    def showUnvipInfo(self,info):#暗红文字
        print(self.seat*self.seatNum+"\033[1;0;35m%s  \033[0m"%info)
    def showUnvipInfo2(self,info,numb=-1):#灰色文字
        if numb!=-1:
            print("\t"*numb+"|\033[0;1;30m%s  \033[0m"%info)
        else:
            print(self.seat*self.seatNum+"\033[0;1;30m%s  \033[0m"%info)
    def showgreen(self,info,seat):#绿色背景文字
        print(self.seat*seat+"\033[0;1;42m%s  \033[0m"%info)
    def showred(self,info,seat,numb=-1):#红色背景文字

        if numb!=-1:
            print("\t"*numb+"|\033[0;1;41m%s  \033[0m"%info)
        else:
            print(self.seat*seat+"\033[0;1;41m%s  \033[0m"%info)
