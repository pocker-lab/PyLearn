# PyLearn

## 参考链接

1. [jobbole/awesome-python-cn | 包资源介绍](https://github.com/jobbole/awesome-python-cn)  
2. [walter201230/Python | python学习](https://github.com/walter201230/Python)
3. [wistbean/learn_python3_spider | python爬虫](https://github.com/wistbean/learn_python3_spider)

## 更改pip代理链接

```shell
pip config set global.index-url http://pypi.douban.com/simple | pip config set global.trusted-host pypi.douban.com | pip config set global.timeout 6000
```

## 更改anaconda清华源

Windows 用户无法直接创建名为 .condarc 的文件，可先执行 conda config --set show_channel_urls yes 生成该文件之后再修改。

1. 创建 .condarc

    ```shell
    conda config --set show_channel_urls yes
    ```

2. 修改 C:\Users\Luck\.condarc

    ```shell
    channels:
      - defaults
    show_channel_urls: true
    default_channels:
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
    custom_channels:
      conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
      simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    ```

## sql 参考链接

1. [Learning/SQL](Learning/SQL.md)  
2. [MySql数据库的列类型（字段类型）](https://blog.csdn.net/xiaotom5/article/details/8140679)
3. [在Docker中安装MySQL](https://ladybug.top/%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85&%E9%85%8D%E7%BD%AE/install-MySQL-and-open-remote-access-in-docker.html#%E5%AE%89%E8%A3%85%E7%8E%AF%E5%A2%83)

## python 参考链接

1. [python函数之传递多个参数](https://blog.csdn.net/u011607898/article/details/107585700)  
2. [在 Python 中合并列表的5种方法](https://cloud.tencent.com/developer/article/1815842)  
3. [Python入门 类class 基础篇](https://zhuanlan.zhihu.com/p/30024792)  
4. [vscode 默认添加python项目的源目录路径到执行环境](https://www.cnblogs.com/qinfangzhe/p/15917263.html)  
5. [python的多个字典dict合并一个字典的九种方法](https://blog.csdn.net/RogerFedereYY/article/details/109544917)  
6. [终止for循环的方式](https://blog.csdn.net/qq_40203552/article/details/107343692)
