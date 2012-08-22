#coding=utf8
#接收用户信息，复制特定次数，并保存到剪贴板。
#TaoKY made this program.

import sys
import os

reload(sys)
sys.setdefaultencoding('utf8') 

def copy(infor,time,join=''):
    try:
        re=(infor+join)*(time-1)+infor
        print re
        #sc(re)
        scxe(re)
    except OverflowError:
        print '数值过大！任务中止！'

def copysc(infor,time,join=''):
    try:
        re=(infor+join)*(time-1)+infor
        print re
        sc(re)
        scxe(re)
    except OverflowError:
        print '数值过大！任务中止！'
def sc(text):
    #鼠标中键粘贴支持
    os.popen('xsel', 'wb').write(text)
    
def scxe(text):
    try:
        import xerox
        xerox.copy(u'%s'%text)
    except ImportError:
        print '请使用easy_install安装xerox以支持剪贴板。Windows用户需要额外安装pywin32'

if len(sys.argv)<2:
    print '不执行任何操作，输入--help参数以获得帮助。'
    sys.exit()
if sys.argv[1].startswith('--version') or sys.argv[1].startswith('--help'):
    op=sys.argv[1][2:]
    if op=='version':
        print 'Version 0.04 Alpha，可能有未知错误。'
        sys.exit()
    elif op=='help':
        print "程序帮助：\
                \n此程序可以接收用户发出的信息，按用户的要求复制特定次数，并保存到剪切板（需要xerox模块）。使用Python2。\
                \n程序参数：\
                \n--version：显示版本号\
                \n--help：显示帮助\
                \n--space：在复制得出信息中加入空格以更容易识别（必须放在末尾）\
                \n--middle：启用鼠标中键粘贴功能（仅限于支持Xorg且安装xsel的系统）\
                \n使用程序的方法：\
                \n如果你需要复制“a”5次，输入以下命令：\
                \n程序名 a 5\
                \n将会返回aaaaa\
                \n如果你需要复制“a”5次，且在“a”之间需要加入空格，输入：\
                \n程序名 a 5 ' ' 或者 程序名 a 5 --space\
                \n需要加入其他符号时可以这样：\
                \n程序名 a 5 符号\
                \n复制特殊字符（如空格，参数名）时在外面包上单引号。"
        sys.exit()
    else:
        print '未知参数，输入--help参数以获得帮助。'
if len(sys.argv)==3:
    try:
        infor=sys.argv[1]
        time=int(sys.argv[2])
        copy(infor,time)
    except ValueError:
        print '输入有误，输入--help参数以获得帮助。'
if len(sys.argv)==4:
    if '--space' in sys.argv[2:]:
        try:
            infor=sys.argv[1]
            time=int(sys.argv[2])
            join=' '
            copy(infor,time,join)
        except ValueError:
            print '输入有误，输入--help参数以获得帮助。' 
    elif '--middle' in sys.argv:
        try:
            infor=sys.argv[1]
            time=int(sys.argv[2])
            join=' '
            copysc(infor,time,join)
        except ValueError:
            print '输入有误，输入--help参数以获得帮助。' 
    else:
       try:
            infor=sys.argv[1]
            time=int(sys.argv[2])
            join=sys.argv[3]
            copy(infor,time,join)
       except ValueError:
            print '输入有误，输入--help参数以获得帮助。'
