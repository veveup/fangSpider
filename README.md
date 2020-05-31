# Init

# Requirement
Python3.5+ and Scrapy2.0, Mysql 6.0+, requirements.txt extension installed.


# Quick Start
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
// use ./sql/x.sql file to create TABEL
//exit mysql and make sure 
scrapy crawl fangIndex
//默认爬取郑州城市在售小区 楼盘信息 


```




