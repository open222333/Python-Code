from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import DBNAME

Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    test_data = Column(String(100))


def set_sqlalchemy_engine(db):
# 建立連接引擎
    engine = create_engine(
        # 'mysql://user:pass@host/dbname'
        f'mysql+pymysql://root:root@192.168.31.56:32001/{db}',
        # 將所有SQL記錄到Python記錄器，此記錄器會寫入標準輸出
        # 基於python logging模組完成
        echo=True,
        # 啟用2.0樣式 https://docs.sqlalchemy.org/en/14/glossary.html#term-2.0-style
        future=True
    )
    return engine

# 創建實例
engine = set_sqlalchemy_engine(DBNAME)
ed_test = Test(test_data='test')

# 創建會話
Session = sessionmaker(bind=engine, future=True)
session = Session()

# 添加資料
session.add(ed_test)
session.commit()
