# Init

#Requirement
Python3.5+ and Scrapy2.0, Mysql 6.0+, requirement.txt extension installed.


#Quick Start
Note：This is requires python3, scrapy, requirement.txt extension in order to work. 

```bash
git glone this
cd this

pip -r install requirement.txt

mysql -u root -p
//connection to mysql, create DATABASE and create TABEL

CREATE DATABASE IF NOT EXISTS `fangSpider` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */

use fangSpider;

source ./sql/loupanindex.sql;
// use ./sql/x.sql file to create TABEL
//exit mysql and make sure 
scrapy crawl fangIndex
//爬取所有城市在售小区 楼盘信息

scrapy crawl fangIndexSolo
//爬取单独城市在售小区 
```

#爬取单独城市在售小区
./spiders/fangIndexSolo.py


# 数据库 Mysql 
>版本要求: >= 5.7 (理论上高于该版本，只要支持JSON类型就可以 实际使用8.x)
>创建数据库语句
```sql
CREATE DATABASE IF NOT EXISTS `fangSpider` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */
```

>创建所有表 tabels 的sql文件在 ./sql/ 文件下


