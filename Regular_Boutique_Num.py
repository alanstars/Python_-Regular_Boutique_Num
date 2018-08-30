import pymysql, re

# 打开数据库连接
db = pymysql.connect('localhost', 'root', 'root', 'cambie')
# 使用cursor()方法获取操作游标
param = []
j = 0
for i in range(86000000, 87000000):
    j = j + 1
    type = 0
    for i in range(86000000, 87000000):
        # 8位及以上重复带6
        if re.match('^\\d*(66666666)\\d*$', str(i)):
            type = 18
            continue
        # 7位及以上重复带6
        elif re.match('^\\d*(6666666)\\d*$', str(i)):
            type = 17
            continue
        # 6位及以上重复带6
        elif re.match('^\\d*(666666)\\d*$', str(i)):
            type = 16
            continue
        # 5位及以上重复带6
        elif re.match('^\\d*(66666)\\d*$', str(i)):
            type = 15
            continue
        # 4位及以上重复带6
        elif re.match('^\\d*(6666)\\d*$', str(i)):
            type = 14
            continue
        # 8位及以上重复带8
        elif re.match('^\\d*(88888888)\\d*$', str(i)):
            type = 13
            continue
        # 7位及以上重复带8
        elif re.match('^\\d*(8888888)\\d*$', str(i)):
            type = 12
            continue
        # 6位及以上重复带8
        elif re.match('^\\d*(888888)\\d*$', str(i)):
            type = 11
            continue
        # 5位及以上重复带8
        elif re.match('^\\d*(88888)\\d*$', str(i)):
            type = 10
            continue
        # 4位及以上重复带8
        elif re.match('^\\d*(8888)\\d*$', str(i)):
            type = 9
            continue
        # 6位数字重复
        elif re.match('^\\d*(\\d)\\1{5,}\\d*$', str(i)):
            type = 8
            continue
        # ABCDEFG
        elif re.match('^\d(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)|9(?=0)){6,})\\d',str(i)):
            type = 19
            continue
        # ABCDEF
        elif re.match('^\d\d(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)|9(?=0)){5,})\\d',str(i)):
            type = 20
            continue
        # ABCDE
        elif re.match('^\d\d(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)|9(?=0)){4,})\\d',str(i)):
            type = 21
            continue
        # ABCABC
        elif re.match('^\d\d(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)|9(?=0)){2,})(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)|9(?=0)){3,})\\d',str(i)):
            type = 1
            continue
        # AAABBB
        elif re.match('^\\d*(\\d)\\1\\1(\\d)\\2\\2\\d*$', str(i)):
            type = 3
            continue
        # AABBCC
        elif re.match('^(?:(\\d)\\1+)+$', str(i)):
            type = 2
            continue
        # GFEDCBA
        elif re.match('^\d(?:(?:0(?=9)|9(?=8)|8(?=7)|7(?=6)|6(?=5)|5(?=4)|4(?=3)|3(?=2)|2(?=1)|1(?=0)){6,})\\d',str(i)):
            type = 22
            continue
        # FEDCBA
        elif re.match('^\d(?:(?:0(?=9)|9(?=8)|8(?=7)|7(?=6)|6(?=5)|5(?=4)|4(?=3)|3(?=2)|2(?=1)|1(?=0)){5,})\\d',str(i)):
            type = 23
            continue
        # EDCBA
        elif re.match('^\d(?:(?:0(?=9)|9(?=8)|8(?=7)|7(?=6)|6(?=5)|5(?=4)|4(?=3)|3(?=2)|2(?=1)|1(?=0)){4,})\\d',str(i)):
            type = 24
            continue
        else:
            type = 0
    param.append((i, type))
print(j)
# 需要执行的SQL语句
# nums = str(i)
# statusss = str(statu)
sql = "INSERT INTO cambie_store_num (num,type) VALUES (%s,%s)"
cursor = db.cursor()
# 使用事务提交
try:
    # 执行sql语句
    # cursor.execute(sql)
    cursor.executemany(sql, (param))
    # 提交到数据库执行
    db.commit()
    print("插入数据成功")
except:
    # Rollback in case there is any error
    db.rollback()
db.close()
