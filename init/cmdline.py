import optparse
import random

binner2="""
    ██╗    ██╗ █████╗ ████████╗███████╗██████╗ ███████╗██╗  ██╗██████╗ 
    ██║    ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗
    ██║ █╗ ██║███████║   ██║   █████╗  ██████╔╝█████╗   ╚███╔╝ ██████╔╝
    ██║███╗██║██╔══██║   ██║   ██╔══╝  ██╔══██╗██╔══╝   ██╔██╗ ██╔═══╝ 
    ╚███╔███╔╝██║  ██║   ██║   ███████╗██║  ██║███████╗██╔╝ ██╗██║     
     ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝    
                            
              Auth0r:linshao   [网站漏洞模板(42个常见漏洞).docx]辅助挖洞脚本
              这是什么: 一款面向安服仔的漏洞碰瓷工具
              公众号: LinshaoSec  github: https://github.com/linshaoSec
"""
binner="""

                                                  0                                                 
                                                 000                                                
                                                @@@@@                                               
                                               @@@@@@@                                              
                                              @@@@@@@@@                                             
                                            G@@@@@0@@@@0                                            
                                           00@0@000 @@@@@8                                          
                                          @@@@@0008 .@@@@@0                                         
                                         0@@@08888 ...0@@@@@                                        
                                        0000@8888  ....L0@@@@                                       
                                       @@@@@CCC8C   .,,,,@@@@@                                      
                                     ,0@@@@CCCCC     ,,,,,@@@@@                                     
                                    00@@@0GGGCC       ,,:::@@@@@t                                   
                                   0@@@@0GGGGG        ,:::::0@@@@0                                  
                                  00@@@CLGGGG          ::::::@@@@@@                                 
                                 000@@LLLLLG            ;;;;;;0@@@@0                                
                                0@@@0fLLLLL              ;;;;;;;@@@@@                               
                              .@@@@@fffLLL                ;;;iiii@@@@0                              
                             C@@@@0ffffff                  iiiiiii0@@@@.                            
                       @@@00@@@@@0LLLLLL0000@@0@00@0@@@@0@00LLLLLLL00@@@@@@@0                       
                        0@00G....,,,,:::::;@@@@@0LL1111ttttffffLLLLLGGGGG@0@                        
                          @00GG,,,,,::::::;;;8@@0L11111ttt00fffLLLi,:...000                         
                         @0@@0LLL,,,,,,,,,,,,,:0000,,,,f00000L,,::,,,,i00000                        
                        0@@00LLLLL:,,,,,,,,,,,,0000000000LLL8Lf,,:,,,GLL00000                       
                      L0@@@@iLLLffff,,,,,,,,,,000000000LLL;,,,,,,::,LLLLf@0000                      
                     @00@@0iiiLLLffff,,,0,,@0@@@00000@LL,,,,,,,::::LLLLfff00000G                    
                    @@@@@0;;iiiL000ttti,@@@00LLLLL0000LL,,,,,,;;::@0GffffLL000000                   
                   @@@@@f;;;;;; L000ttt1,00LLL1,,,,,0008,,,,:;;;;@@0  LLLLLL00000@                  
                  @0@@0::;;;;:    0001111,,LL,,,,,,,00000C,iiiii000    LLLLGG800000                 
                 @00@@::::::       00011ii,,,,,,,,,,00GLLLLiii8@00      LGGGGGL@0000                
               ,0000@::::::         000iiii,,,,,,,,,,tL:,111i0000         GGGGGG0000@               
              00000@,,,,:            000i;;;,,,,,,,,,,,,11t1@@@,           GGGCCC00000i             
             @0@@@@,,,,,              000i;;;,,,,,,,,,,ttt10@@               CCCCC00@@@@            
            0@@@@8...,                 0000;::,,,,,,,,fttt@@0                 CCC880@@@@0           
           0@@@@.....                   t000:::,,,,,,ffft000                    888800000@          
          0@@@0 ...    GCCCCGGGGGGLLLLLLffLLL:,::,,:LLLfLLLii;;;;;::::::,,,,..    888t00@0@         
         @0@0@ 80088888CCCCCCGGGGGGLLLLLfffLLL,,,::LLLLLLGiii;;;;;;:::::,,,,,......  i@@@@@@        
       G@@@@0GGGGGGGLLLLLLLLLLLffffffffffttfLGL,,,:GGLLLf1111111iiiiiiiii;;;;;;;;;;;;:110@@@0       
      0@@@@@@0@@00000000000000@@@@@@@@@@00@000@@..GG000000@@@@@@0@000@000000000000@000000000000     
     0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G:000000000000000000000000000000000000000000000    
                                               @00000                                               
                                                :000                  Author : Linshao              
                                                  @                   Version: v1.0                 
                                                                                                    
                                                                                                    
"""

usage="""
        python3 %prog -u http://www.target.com
        python3 %prog -f urls.txt
"""
parser=optparse.OptionParser(usage,                         #使用
                             description="",           #描述
                             version="linshao: %prog v1.0", #版本信息
                             epilog="-"*60)                 #演示信息
parser.add_option('-u','--url', dest='url',help='扫描目标网址')    #添加参数
parser.add_option('-f','--urls', dest='urls',help='扫描目标网址文件，一行一个')
# parser.add_option('-l','--showLevel', dest='showLevel',help='显示层级,默认1显示全部,[1全部][2.漏洞检测结果][3.确定存在漏洞]',type=str,default="123")
# parser.add_option('-o','--out', dest='out',default='result.txt',help='导出结果，默认./result.txt')
options,args=parser.parse_args() #解析输入



def parse_args():
    if random.randint(1,2)==1:
        print(binner)
    else:
        print(binner2)
    if options.url==None and options.urls==None:
        parser.print_help()
        exit(0)
    return options
