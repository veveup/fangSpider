# Init

## Requirement
Python3.5+ and Scrapy2.0, Mysql 6.0+, requirements.txt extension installed.


## Quick Start
Note：This is requires python3, scrapy, requirements.txt extension in order to work. 

```bash
git glone this
cd this

pip -r install requirements.txt

mysql -u root -p
//connection to mysql, create DATABASE and create TABEL

CREATE DATABASE IF NOT EXISTS `fangSpider` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */

use fangSpider;

source ./sql/loupanindex.sql;
// 使用 ./sql/loupanindex.sql 文件创建 TABEL 
// 退出 mysql 交互页面


scrapy crawl fangIndex
//默认爬取郑州城市在售小区 楼盘信息 
```
## More usage

+ 修改 TABEL 名字，将不同城市的数据放入不同的表内
```sql


# 1、修改 ./sql/loupanindex.sql 文件中 loupanindex 表名 然后重新执行 sql 文件
CREATE TABLE `loupanindex` (

# 2、修改 ./mysqlcfg.py 内关于数据库表名的定义
TABLENAME = 'loupanindex'
```
+ 爬取所有城市数据
```python
./fangSpider/spiders/fangIndex.py

#是否只抓取一个城市 开关设为False
isSoloCityOnly = False
# 从相应网站获得 城市的代码 比如郑州是 zz 仅在isSoloCityOnly 为 True 时有效
citycode = 'zz'
```
>**Note:** 全部城市小区大概有55000+个 单机抓取会需要很长时间 在测试中 1000 个小区大概需要 二十分钟，并且一直访问网站有可能会出现验证码 甚至被封ip 如果必要可以了解一下如何使用 Proxy 和 Redis 分布爬取

+ 配置 mysql 数据库连接信息
```python
./fangSpider/mysqlcfg.py
host = '127.0.0.1'
user = 'root'
passwd = '12345678'
database ='fangSpider'
TABLENAME = 'loupanindex'
```



