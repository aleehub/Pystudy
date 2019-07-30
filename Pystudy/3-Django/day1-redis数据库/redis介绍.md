# nosql定义
# Redis特点



## 1. nosql介绍

**NoSQL:一类新出现的数据库（not only sql)**
* 泛指非关系的数据库
* 不支持SQL语法
* 存储结构跟传统关系型数据库中的那种关系表完全不同，nosql中存储的数据都是KV形式（key-value 键值对）
* Nosql中的产品种类相当多
    * MongoDB
    * Redis
    * Hbase Hadoop
    * Cassandra hadoop
    
**Nosql 和SQL 数据库的比较：**

## 2. Redis简介
* Redis是一个开源的使用ANSI C语言编写，支持网络、科技与内存亦可持续化的日志型。key-value数据库，并提供多种开发语言的API。从2010年3月15日起，Redis的开发工作有VMware主持。从2013年5月开始，Redis的开发有Pivotal赞助。
* Redis是Nosql技术阵营的中一员，他通过多种键值数据类型来适应不同场景下的存储需求，借助一些高层级的接口使用其可以胜任，如缓存。队列系统的不同角色


**Redis特性**
* Redis与其他key-value 缓存产品有以下三个特点：
* Redis支持数据的可持续化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
* Redis不仅仅支持简单的key-value类型的数据，同时还提供list ,set ，zset,hash等数据结构的存储。
* Redis支持数据的备份，即master-slave模式的数据备份


**Redis优势**
* 性能极高——Redis能读的速度是110000次/s，写的速度是81000次/s。
* 丰富的数据类型——Redis支持二进制案例的String，Lists,Hashes,Sets及Ordered Sets数据类型操作。
* 原子-Redis的所有操作都是原子性的 ，同时Redis还支持对几个操作全并后的 原子性操作。
* 丰富的特性——Redis还支持publish/SUBSCRIBE,通知，Key等等特性

**Redis应用场景**
* 用来做缓存（ehcache/memcahed)——redis的所有数据是放在内存中的（内存数据库）
* 可以在某些特定应用场景下替代传统数据库——比如社交类的应用
* 在一些大型系统中，巧妙的实现了一些特定定的功能，session共享、购物车
* 只要你有丰富的想象力，redis可以用在可以给你无限的惊喜....



 