# mysql-learn

## 其他操作

1. 连接登录mysql  
`mysql -u root -p`

2. 使用数据库  
`use 数据库名;`

## 查询操作

1. 查询正在使用的数据库  
`select database();`

2. 显示数据库列表  
`show databases;`

3. 显示数据库中的数据表  
`show tables;`

4. 显示数据表结构  
`describe [数据库名.]表名;`  
`desc [数据库名.]表名;`

5. 查询指定列有多少数据  
`select count(列名) from 表名`

6. 查询指定列中包含指定内容的数据行  
`select * from 表名 where 列名 like "指定内容";`

7. 查询指定列重复项

    ```sql
    select
        列名, count(列名)
    from
        表名
    group by
        列名
    having
        count(列名) > 1;
    ```

## 新增操作

1. 创建数据库  
`create database 数据库名;`

2. 创建表  

    ```sql
    create table 数据库名.表名 (
        列名1 列类型,
        列名2 列类型,
        ...
    );
    ```

3. 新增数据  

    ```sql
    insert into 数据库名.表名 (列名1, 列名2, ...)
    values(数据1, 数据2, ...);
    ```

## 删除操作

1. 删除列  
`alter table 表名 drop column 列名`

1. 删除表中数据：[MySQL DELETE：删除数据](http://c.biancheng.net/view/2580.html)  
`DELETE FROM <表名> [WHERE 子句] [ORDER BY 子句] [LIMIT 子句]`  
语法说明如下：  
    - `<表名>`：指定要删除数据的表名。
    - `ORDER BY` 子句：可选项。表示删除时，表中各行将按照子句中指定的顺序进行删除。
    - `WHERE` 子句：可选项。表示为删除操作限定删除条件，若省略该子句，则代表删除该表中的所有行。
    - `LIMIT` 子句：可选项。用于告知服务器在控制命令被返回到客户端前被删除行的最大值

## 修改操作

1. 修改列名  
`alter table 表名 rename column 原列名 to 新列名;`

2. 修改列名和列属性  
`alter table 表名 change 原列名 to 新列名 [新列类型];`

3. 设置唯一键  
`alter table 表名 add constraint 列名_unique unique (列名);`  
[MySQL数据库唯一性设置(unique index)](https://www.jianshu.com/p/9d709da221ab)

## 进阶操作

1. 备份及恢复表  
    - 创建一个备份表  
    `create table 备份表名 as select * from 原始表名;`
    - 清空原始表中的数据  
    `truncate table 原始表名;`
    - 从备份表中把数据插入到原始表中  
    `insert into 原始表名 select * from 备份表名;`

2. 查询表索引  
`show index from 表名;`

3. 创建列索引  
`create index 索引名 on 表名(列名);`

4. 分析语句执行时长  
`explain [select，delete，insert或update语句]`

5. 重置自增序号  
`alter table 表名 auto_increment = 0;`
