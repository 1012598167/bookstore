from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, PrimaryKeyConstraint, Text, DateTime, Boolean, LargeBinary
from sqlalchemy.orm import sessionmaker

import psycopg2
from datetime import datetime,time
# �������ݿ�legend �ǵ��޸����������
# engine = create_engine('postgresql://postgres:amyamy@localhost:5433/bookstore')
engine = create_engine('postgresql://postgres:990814@[2001:da8:8005:4056:81e9:7f6c:6d05:fe47]:5432/Bookstore')
Base = declarative_base()

# # String���ȿ�����Ҫ���޸�
# # �û���
# class User(Base):
#     __tablename__ = 'usr'
#     user_id = Column(String(128), primary_key=True)
#     password = Column(String(128), nullable=False)
#     balance = Column(Integer, nullable=False)
#     token = Column(String(400))
#     terminal = Column(String(64))
#
#
# # �̵�����鱾��Ϣ��
# class Store(Base):
#     __tablename__ = 'store'
#     store_id = Column(String(128), nullable=False)
#     book_id = Column(Integer, nullable=False)
#     stock_level = Column(Integer, nullable=False)
#     price = Column(Integer, nullable=False) # �ۼ�
#     __table_args__ = (
#         PrimaryKeyConstraint('store_id', 'book_id'),
#         {},
#     )

class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    author = Column(Text)
    publisher = Column(Text)
    original_title = Column(Text)
    translator = Column(Text)
    pub_year = Column(Text)
    pages = Column(Integer)
    original_price = Column(Integer) # ԭ��
    currency_unit = Column(String(16))
    binding = Column(Text)
    isbn = Column(Text)
    author_intro = Column(Text)
    book_intro = Column(Text)
    content = Column(Text)
    tags = Column(Text)
    picture = Column(LargeBinary)

#
# # �û��̵��ϵ��
# class User_store(Base):
#     __tablename__ = 'user_store'
#     user_id = Column(String(128), ForeignKey('usr.user_id'), nullable=False)
#     store_id = Column(String(128), nullable=False)
#     __table_args__ = (
#         PrimaryKeyConstraint('user_id', 'store_id'),
#         {},
#     )
#
#
# # δ�����
# class New_order_pend(Base):
#     __tablename__ = 'new_order_pend'
#     order_id = Column(String(128), primary_key=True)
#     buyer_id = Column(String(128), ForeignKey('usr.user_id'), nullable=False)
#     seller_id = Column(String(128), ForeignKey('usr.user_id'), nullable=False)
#     price = Column(Integer, nullable=False)
#     pt = Column(DateTime, nullable=False)
#
#
# # ��ȡ������
# class New_order_cancel(Base):
#     __tablename__ = 'new_order_cancel'
#     order_id = Column(String(128), primary_key=True)
#     buyer_id = Column(String(128), ForeignKey('usr.user_id'), nullable=False)
#     seller_id = Column(String(128), ForeignKey('usr.user_id'), nullable=False)
#     price = Column(Integer, nullable=False)
#     pt = Column(DateTime, nullable=False)
#
# # �Ѹ����
# class New_order_paid(Base):
#     __tablename__ = 'new_order_paid'
#     order_id = Column(String(128), primary_key=True)
#     buyer_id = Column(String(128), ForeignKey('usr.user_id'), nullable=False)
#     seller_id = Column(String(128), ForeignKey('usr.user_id'), nullable=False)
#     price = Column(Integer, nullable=False)
#     status = Column(Integer, nullable=False) # 0Ϊ�Ѹ��1Ϊ�ѷ�����2Ϊ���ջ�
#
#
# # �����е��鱾��Ϣ
# class New_order_detail(Base):
#     __tablename__ = 'new_order_detail'
#     order_id = Column(String(128), nullable=False)
#     book_id = Column(Integer, nullable=False)
#     count = Column(Integer, nullable=False)
#     price = Column(Integer, nullable=False)
#     __table_args__ = (
#         PrimaryKeyConstraint('order_id', 'book_id'),
#         {},
#     )

def init():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    Base.metadata.create_all(engine)
    # �ύ�����浽���ݿ�
    session.commit()
    # �ر�session
    session.close()

def add_info():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    # �ύ�����浽���ݿ�A
    A = User(user_id = '���ƹ�',
            password = '123456',
            balance = 100,
            token = '***',
            terminal = 'Edge')
    B = User(user_id = 'С��',
            password = '123456',
            balance = 500,
            token = '***',
            terminal='Chrome')
    Book1 = Book(book_id = 0,
                title='���ݽṹ')
    Book2 = Book(book_id=1,
                title='PRML')
    session.add_all([A, B, Book1, Book2])
    session.commit()
    StoreA = Store(store_id = '���ƹ�����',
                    book_id = 0,
                    stock_level=10,
                    price=1000) # �۸�λ�Ƿ�
    StoreB = Store(store_id = '���ƹ�Ľ������',
                    book_id = 1,
                    stock_level=10,
                    price=10000)
    session.add_all([StoreA, StoreB])
    session.commit()
    A_Store1 = User_store(user_id = '���ƹ�',
                        store_id = '���ƹ�����')
    A_Store2 = User_store(user_id = '���ƹ�',
                        store_id = '���ƹ�Ľ������')
    OrderA = New_order_paid(order_id = 'order1',
                            buyer_id = 'С��',
                            seller_id = '���ƹ�',
                            price=2000,
                            status = 0)  # 0Ϊ�ѷ�����1Ϊ���ջ�
    Order_detailA = New_order_detail(order_id = 'order1',
                                    book_id = 0,
                                    count = 2,
                                    price = 2000)
    OrderB = New_order_pend(order_id = 'order2',
                            buyer_id = 'С��',
                            seller_id = '���ƹ�',
                            price = 10000,
                            pt = datetime.now())
    Order_detailB = New_order_detail(order_id = 'order2',
                                    book_id = 1,
                                    count = 1,
                                    price = 10000)
    session.add_all([
        A_Store1, A_Store2, OrderA, Order_detailA, OrderB, Order_detailB
    ])
    session.commit()
    # �ر�session
    session.close()

if __name__ == "__main__":
    # �������ݿ�
    init()
    # ������Ϣ
    add_info()
