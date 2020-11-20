# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker


# engine = create_engine('sqlite:///test.db', convert_unicode=True)
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/flask-app',
                       encoding='utf-8',
                       echo=True,
                       convert_unicode=True
                       )
metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    metadata.create_all(bind=engine)