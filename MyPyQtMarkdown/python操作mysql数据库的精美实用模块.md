```python
import pymysql

########连接数据库###############
def createConnection():
    db = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        db='mydbdemo',
        charset='utf8'
    )
    return db

########执行SELECT语句，返回单条数据###############
def executeSelectONEback(sqlstring):
    try:
        db = createConnection() # 连接数据库
        cursor = db.cursor()
        cursor.execute(sqlstring)
        dataone = cursor.fetchone()
        return dataone
    except:
        return False
    finally:
        db.close()# 关闭数据库连接




########执行SELECT语句，返回多条数据###############
def executeSelectAllback(sqlstring):
    try:
        db = createConnection()  # 连接数据库
        cursor = db.cursor()
        cursor.execute(sqlstring)
        dataall = cursor.fetchall()
        return dataall
    except:
        return False
    finally:
        db.close()# 关闭数据库连接


########执行INSERT语句，返回id主键###############
def executeInsertIDback(sqlstring):
    try:
        db = createConnection()  # 连接数据库
        cursor = db.cursor()
        cursor.execute(sqlstring)
        db.commit()
        the_id = int(cursor.lastrowid)
        return the_id
    except:
        db.rollback()
        return False
    finally:
        db.close()         # 关闭数据库连接


########执行UPDATE 语句，无返回###############
def executeUpdateNOback(sqlstring):
    try:
        db = createConnection() # 连接数据库
        cursor = db.cursor()
        cursor.execute(sqlstring)
        db.commit()
        return True
    except:
        db.rollback()
        return False
    finally:
        db.close()# 关闭数据库连接


########执行DELETE语句，无返回###############
def executeDeleteNOback(sqlstring):
    try:
        db = createConnection() # 连接数据库
        cursor = db.cursor()
        cursor.execute(sqlstring)
        db.commit()
        return True
    except:
        db.rollback()
        return False
    finally:
        db.close()# 关闭数据库连接


########执行CREATE语句，无返回###############
def executeCreateNOback(sqlstring):
    try:
        db = createConnection()  # 连接数据库
        cursor = db.cursor()
        cursor.execute(sqlstring)
        return True
    except:
        db.rollback()
        return False
    finally:
        db.close()# 关闭数据库连接
```