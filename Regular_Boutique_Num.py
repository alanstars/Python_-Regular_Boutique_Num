import pymysql, re
# 打开数据库连接
db = pymysql.connect('localhost', 'root', '123456', 'cambie')
# 使用cursor()方法获取操作游标
param = []
j = 0
for i in range(86000000, 87000000):
    # 8位及以上重复带6
    if re.match('^\\d*(66666666)\\d*$', str(i)):
        typea = 18
        param.append((i, typea))
        # continue
    # 7位及以上重复带6
    elif re.match('^\\d*(6666666)\\d*$', str(i)):
        typea = 17
        param.append((i, typea))
        # continue
    # 6位及以上重复带6
    elif re.match('^\\d*(666666)\\d*$', str(i)):
        typea = 16
        param.append((i, typea))
        # continue
    # 5位及以上重复带6
    elif re.match('^\\d*(66666)\\d*$', str(i)):
        typea = 15
        param.append((i, typea))
        # continue
    # 4位及以上重复带6
    elif re.match('^\\d*(6666)\\d*$', str(i)):
        typea = 14
        param.append((i, typea))
        # continue
    # 8位及以上重复带8
    elif re.match('^\\d*(88888888)\\d*$', str(i)):
        typea = 13
        param.append((i, typea))
        # continue
    # 7位及以上重复带8
    elif re.match('^\\d*(8888888)\\d*$', str(i)):
        typea = 12
        param.append((i, typea))
        # continue
    # 6位及以上重复带8
    elif re.match('^\\d*(888888)\\d*$', str(i)):
        typea = 11
        param.append((i, typea))
        # continue
    # 5位及以上重复带8
    elif re.match('^\\d*(88888)\\d*$', str(i)):
        typea = 10
        param.append((i, typea))
        # continue
    # 4位及以上重复带8
    elif re.match('^\\d*(8888)\\d*$', str(i)):
        typea = 9
        param.append((i, typea))
        # continue
    # 8位数字重复
    elif re.match('^\\d*(\\d)\\1{7,}\\d*$', str(i)):
        typea = 8
        param.append((i, typea))
    # 7位数字重复
    elif re.match('^\\d*(\\d)\\1{6,}\\d*$', str(i)):
        typea = 7
        param.append((i, typea))
    # 6位数字重复
    elif re.match('^\\d*(\\d)\\1{5,}\\d*$', str(i)):
        typea = 6
        param.append((i, typea))
        # continue
    # ABCDEFG
    elif re.match('^\d(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)|9(?=0)){6,})\\d', str(i)):
        typea = 19
        param.append((i, typea))
        # continue
    # ABCDEF
    elif re.match('^\d\d(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)|9(?=0)){5,})\\d', str(i)):
        typea = 20
        param.append((i, typea))
        # continue
    # ABCABC
    elif re.match('^\d(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)|9(?=0)){2,})(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)|9(?=0)){3,})\\d',str(i)):
        typea = 1
        param.append((i, typea))
        # continue
    # ABCDE
    elif re.match('^\d\d(?:(?:0(?=1)|1(?=2)|2(?=3)|3(?=4)|4(?=5)|5(?=6)|6(?=7)|7(?=8)|8(?=9)|9(?=0)){4,})\\d', str(i)):
        typea = 21
        param.append((i, typea))
        # continue
    # AAABBB
    elif re.match('^\\d*(\\d)\\1\\1(\\d)\\2\\2\\d*$', str(i)):
        typea = 3
        param.append((i, typea))
        # continue
    # AABBCC
    elif re.match('^\\d*(\\d)\\1(\\d)\\2(\\d)\\3\\d*$', str(i)):
        typea = 2
        param.append((i, typea))
        # continue
    # GFEDCBA
    elif re.match('^\d(?:(?:0(?=9)|9(?=8)|8(?=7)|7(?=6)|6(?=5)|5(?=4)|4(?=3)|3(?=2)|2(?=1)|1(?=0)){6,})\\d', str(i)):
        typea = 22
        param.append((i, typea))
        # continue
    # FEDCBA
    elif re.match('^\d(?:(?:0(?=9)|9(?=8)|8(?=7)|7(?=6)|6(?=5)|5(?=4)|4(?=3)|3(?=2)|2(?=1)|1(?=0)){5,})\\d', str(i)):
        typea = 23
        param.append((i, typea))
        # continue
    # EDCBA
    elif re.match('^\d(?:(?:0(?=9)|9(?=8)|8(?=7)|7(?=6)|6(?=5)|5(?=4)|4(?=3)|3(?=2)|2(?=1)|1(?=0)){4,})\\d', str(i)):
        typea = 24
        param.append((i, typea))
        # continue
    else:
        j = j + 1
        num = i
        typea = 0
        param.append((num, typea))

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