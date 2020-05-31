import logging
import time

"""
一级页面：全国城市 
二级页面：城市首页 Yello
三级页面：城市新房、二手房、租房首页 Green 
四级页面：楼盘首页、二手房房源信息，租房房源信息首页 Blue + hight
五级页面：楼盘详情页面及以下页面、二手房源详情页面及以下页面、租房房源信息及以下页面 Blue
"""
defaultc = '\033[0m'
l1c = ''
l2c = '\033[33m'
l3c = '\033[32m'
l4c = '\033[1;34m'
l5c = '\033[34m'
debugc = '\033[35m'
errorc = '\033[1;31m'

isLimitOutMsg = 100
# 是否限制输出内容 避免一条信息就刷屏的问题 数字为只输出前多少个字符



logFileName = 'logScrapy.log'
logFIleMode = 'a'

def limitedOut(msg):
    l = len(msg)
    if isLimitOutMsg and l>isLimitOutMsg:
        return msg[:isLimitOutMsg-1]+'      more %d char'%l
    return msg

def singleton(cls):
    instances = {}
    def _singleton(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return _singleton


@singleton
class myLogger:
    def __init__(self,logName=None,model=logging.DEBUG):
        if logName == None:
            logName = 'scrapyLog'+str(time.ctime())+'.log'

        self.logger = logging.getLogger()
        self.initLogger(model=model)
        
    def initLogger(self,model=logging.DEBUG):
        #1、获取一个logger并设置级别
        self.logger.setLevel(model)
        #2、获取一个文件流
        fh = logging.FileHandler('./'+logFileName,mode=logFIleMode)
        fh.setLevel(model)
        #3、获取一个终端输出流
        ch = logging.StreamHandler()
        ch.setLevel(model)
        #4、给文件流和终端流设置输出格式
        fformater = logging.Formatter('%(asctime)s %(levelname)s:%(message)s',datefmt='%m%d %H:%M:%S')
        cformater = logging.Formatter('%(asctime)s:%(message)s',datefmt='%H:%M:%S')
        
        fh.setFormatter(fformater)
        ch.setFormatter(cformater)
        #5、将文件流和终端流添加到logger中  直接使用logger输出log
        self.logger.addHandler(fh)
        
        # windows 或无法输出log的情况下打开下面这行代码  Mac下打开会重复输出 Log 还没找到原因
        #self.logger.addHandler(ch)
        self.logger.propagate = False
    
    def getLogger(self):
        return self.logger
        
    def l1(self,msg):
        msg = limitedOut(msg)
        self.logger.info(l1c+msg+defaultc)
    def l2(self,msg):
        """二级页面：城市首页 Yello
        """
        msg = limitedOut(msg)
        self.logger.info(l2c+msg+defaultc)
    def l3(self,msg):
        """三级页面：城市新房、二手房、租房首页 Green 
        """
        msg = limitedOut(msg)
        self.logger.info(l3c+msg+defaultc)
    def l4(self,msg):
        """四级页面：楼盘首页、二手房房源信息，租房房源信息首页 Blue + hight
        """
        msg = limitedOut(msg)
        self.logger.info(l4c+msg+defaultc)
    def l5(self,msg):
        """五级页面：楼盘详情页面及以下页面、二手房源详情页面及以下页面、租房房源信息及以下页面 Blue
        """
        msg = limitedOut(msg)
        self.logger.info(l5c+msg+defaultc)
    def debug(self,msg):
        #msg = limitedOut(msg)
        self.logger.debug(debugc+msg+defaultc)
    def error(self,msg):
        #msg = limitedOut(msg)
        self.logger.error(errorc+msg+defaultc)

    



def testLogger():
    ml = myLogger()
    logger = ml.getLogger()
    ml.l1('一级页面：全国城市 ')
    ml.l2('二级页面：城市首页 Yello')
    ml.l3('三级页面：城市新房、二手房、租房首页 Green ')
    ml.l4('四级页面：楼盘首页、二手房房源信息，租房房源信息首页 Blue + hight')
    ml.l5('五级页面：楼盘详情页面及以下页面、二手房源详情页面及以下页面、租房房源信息及以下页面 Blue')
    ml.debug('This is Debug msg')
    ml.error('This is error msg')

if __name__ == "__main__":
    testLogger()

#mylogger = myLogger().getLogger()

