```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#######################################################################################################
##############初始化数据库连接，返回session
#######################################################################################################
def get_session():
    # 初始化数据库连接 # '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    engine = create_engine('mysql+pymysql://root:root@10.10.10.11:9000/mysqldb?charset=utf8')
    DBSession = sessionmaker(bind=engine)  # 创建DBSession类型
    session = DBSession()
    return session



#######################################################################################################
##############表格对象创建
#######################################################################################################
###创建对象的基类:
Base = declarative_base()

###定义Asset表对象
class Asset(Base):
    # 表的名字:
    __tablename__ = 'hr_asset'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    assetnum = Column(String(50))
    assetname = Column(String(50))
    assetmodel = Column(String(50))
    assettype = Column(Integer)
    assetstate =  Column(Integer)
    usepersonid = Column(Integer, ForeignKey("hr_user.id"))
    userperson = relationship("User",backref="asset", uselist=False)


####定义User表对象
class User(Base):
    # 表的名字:
    __tablename__ = 'hr_user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    age =  Column(Integer)
    degree = Column(String(50))



#######################################################################################################
##############数据操作模板
########################################################################################################
####INSERT插入数据  模板
if __name__ == "__main__":
    try:
      # 创建session对象
      session1 = get_session()
      # 创建新表格对象
      new_user = User(username='龙九', age=33, degree="本科")
      # 添加到session
      session1 .add(new_user)
      # 提交即保存到数据库
      session1 .commit()
      # 得到新数据id  
      the_id=new_user.id    
      # 关闭session
      session1 .close()
    except:
        pass



####DELETE删除数据  模板
if __name__ == "__main__":
    try:
        session2 = get_session()
        session2.query(User).filter(User.id == '3').delete()
        session2.commit()
        session2.close()
    except:
        pass

####UPDATE更新数据  模板
if __name__ == "__main__":    #模板1
    try:
        session3 = get_session()
        session3.query(User).filter(User.id == '2').update({User.degree: '高中'}, synchronize_session=False)
        session3.commit()
        session3.close()
    except:
        pass




if __name__ == "__main__":   #模板2   
    try:
        session3 = get_session()
        the_user = session3.query(User).get(2)  #参数为主键id
        the_user.username ="小王"
        the_user.age= 40
        the_user.degree ="博士"
        session3.commit()
        session3.close()
    except:
        pass


####SELECT查询数据之单条数据 模板
if __name__ == "__main__":
    try:
        session4 = get_session()
        user = session4.query(User).filter(User.id == 3).one()    #注：这里用one()
        print('type:', type(user))
        print('name:', user.username)
        session4.close()
    except:
        pass



####SELECT查询数据之多条数据 模板
if __name__ == "__main__":
    try:
        session5 = get_session()
        users = session5.query(User).filter(User.id > 0).all()    #注：这里用all()
        for i in range(len(users)):
            print(users[i].id)
            print(users[i].username)
        session5.close()
    except:
        pass

####SELECT查询数据之连表查询 模板
if __name__ == "__main__":
    try:
        session6 = get_session()
        assets = session6.query(Asset).join(User).filter(User.id > 0).all()
        for i in range(len(assets)):
            pass
        session6.close()
    except:
        pass
```