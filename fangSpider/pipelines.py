# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
from fangSpider.items import NewhouseIndexItem
from fangSpider.items import NewhouseDetailItem
import json
from fangSpider.items import NewhouseKaipanDetail
from fangSpider.items import NewhouseKaipanPostDetail
from fangSpider.items import NewhouseDeliveryTimeDetailIndex

from fangSpider import mysqlcfg
from fangSpider import mylogger

TABLENAME = mysqlcfg.TABLENAME

# 获得logger
ml = mylogger.myLogger()
logger = ml.getLogger()


class MysqlUtil:
    
    
    def __init__(self):
        
        self.mydb = mysql.connector.connect(
            host = mysqlcfg.host,
            user = mysqlcfg.user,
            passwd = mysqlcfg.passwd,
            database =mysqlcfg.database,
        )
        self.cursor = self.mydb.cursor()
    def getDBcur(self):
        return (self.mydb,self.cursor)
    def close(self):
        if self.mydb is None:
            pass
        else:
            self.mydb.close()
            self.mydb = None

sqlutil = MysqlUtil()

# pylint: disable=no-member
class FangspiderPipeline(object):
    def process_item(self, item, spider):
        return item


# class FangspiderCityloupan(object):
#     def __init__(self):

#         self.mydb = mysql.connector.connect(
#             host = '127.0.0.1',
#             user = 'root',
#             passwd = '12345678',
#             database ='fangSpider',
#         )
#         self.cursor = self.mydb.cursor()
        
#         #连接数据库
    
#     def process_item(self,item,spider):
#         print('*'*20+str(type(item)))
#         sql = "INSERT INTO cityloupan_copy1(name,url,huxin,area,address,tag,phone_plat,unit_price,city) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         val = (item['name'],item['url'],item['huxin'],item['area'],item['address'],str(item['tag']),item['phone_plat'],item['unit_price'],item['city'])
#         self.cursor.execute(sql,val)
#         self.mydb.commit()

#     def close_spider(self,spider):
#         self.mydb.close()


class FangspiderCityloupanIndex(object):
    def __init__(self):
        self.mydb,self.cur = sqlutil.getDBcur()
        

    def process_item(self,item,spider):
        if not type(item) == type(NewhouseIndexItem()):
            ml.debug('不是Index对象 返回'+str(type(item)))
            return item
        if 'newhouse.fang.com' in item['url']:
            ml.debug('不是index页面 返回'+item['url'])
            return item
        #print('*'*20+str(type(item)))
        sql = 'INSERT INTO '+TABLENAME+'(url, name, unit_price, tag, louaddress, sale_time, delivery_time, huxin_main,other_name,part,compart,city) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)'
        val = (item['url'],item['name'],item['unit_price'],str(item['tag']),item['louaddress'],
        item['sale_time'],item['delivery_time'],item['huxin_main'],item['other_name'],item['part'],
        item['compart'],item['city'])
        self.cur.execute(sql,val)
        self.mydb.commit()

    def close_spider(self,spider):
        self.mydb.close()


class fangSpiderCityloupanDetail(object):
    def __init__(self):
        self.mydb,self.cur = sqlutil.getDBcur()
    def process_item(self,item,spider):
        if not type(item) == type(NewhouseDetailItem()):
            ml.debug('不是Detail对象 返回'+str(type(item)))
            return item
        #print('#'*20+str(type(item)))
        sql = 'UPDATE '+TABLENAME+' SET profile=%s,presale=%s,history_price=%s,poi=%s,buiding_type=%s,alright=%s,location=%s,property=%s,status=%s,marker_address=%s,phone_plat = %s,floor_area=%s,gross_area=%s,gross_area_ratio=%s,greening_ratio=%s,parking=%s,counter_buidings=%s,counter_households=%s,wuye_corp=%s,wuye_cost=%s,wuye_note=%s,status_buidings=%s WHERE url=%s'

        val = (item['profile'],json.dumps(item['presale']),json.dumps(item['price_history']),
        item['poi'],item['buiding_type'],item['alright'],item['location'],
        item['property_'],item['status'],item['marker_address'],item['phone_plat'],
        item['floor_area'],item['gross_area'],item['gross_area_ratio'],item['greening_ratio'],
        item['parking'],item['counter_buidings'],
        item['counter_households'],item['wuye_corp'],item['wuye_cost'],
        item['wuye_note'],item['status_buidings'],item['url'])
        self.cur.execute(sql,val)
        self.mydb.commit()

    def close_spider(self,spider):
        self.mydb.close()

class fangSpiderCityloupanKaipanDetail(object):
    def __init__(self):
        self.mydb,self.cur = sqlutil.getDBcur()
    
    def process_item(self,item,spider):
        if not type(item) == type(NewhouseKaipanDetail()):
            ml.debug('不是KaipanDetail对象 返回'+str(type(item)))
            return item
        sql = 'UPDATE '+TABLENAME+' SET history_kaipan = %s WHERE url = %s'
        val = (json.dumps(item['kaipan']),item['url'],)
        self.cur.execute(sql,val)
        self.mydb.commit()

    def close_spider(self,spider):
        self.mydb.close()


class fangSpiderCityloupanPosthistory(object):
    def __init__(self):
        self.mydb,self.cur = sqlutil.getDBcur()
    
    def process_item(self,item,spider):
        if not type(item) == type(NewhouseKaipanPostDetail()):
            ml.debug('不是Posthistory对象 返回'+str(type(item)))
            return item
        sql = 'UPDATE '+TABLENAME+' SET history_post = %s WHERE url = %s'
        val = (json.dumps(item['post_list']),item['url'],)
        self.cur.execute(sql,val)
        self.mydb.commit()

    def close_spider(self,spider):
        self.mydb.close()

class fangSpiderCityloupanDeliveryTimeIndex(object):
    def __init__(self):
        self.mydb,self.cur = sqlutil.getDBcur()
    
    def process_item(self,item,spider):
        if not type(item) == type(NewhouseDeliveryTimeDetailIndex()):
            ml.debug('不是DeliveryTimeList对象 返回'+str(type(item)))
            return item
        sql = 'UPDATE '+TABLENAME+' SET delivery_time = %s WHERE url = %s'
        val = (str(item['delivery_time']),item['url'],)
        self.cur.execute(sql,val)
        self.mydb.commit()

    def close_spider(self,spider):
        self.mydb.close()

