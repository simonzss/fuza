from sqlalchemy import create_engine,text
from sqlalchemy import MetaData
#engine = create_engine("mssql+pyodbc://sa:11111111@11111", echo=True)
engine = create_engine("mssql+pyodbc://sa:zss11111111@localhost:58651/退出单位数据库?driver=ODBC+Driver+13+for+SQL+Server", echo=True)
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result)
# with engine.begin() as conn:
#      result =conn.execute(text("CREATE TABLE some_table5 (x int, y int)"))
#      conn.execute(
#          text("INSERT INTO some_table5 (x, y) VALUES (:x, :y)"),
#          [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
#      )
#      print(result,"***")
aa=0
with engine.connect() as conn:
     #result = conn.execute(text("SELECT 单位类型,审核类型,详细名称 FROM month_1to7 where 行业代码_17 = :pr"),{"pr":8415})
     #参数用 :pr 表示，注意这里的参数是字典形式，如果有多个参数，则传递字典列表
     result = conn.execute(text("SELECT 单位类型,审核类型,详细名称 FROM month_1to7 where 行业代码_17 = :pr").bindparams(pr=8415))
     #result的结构是[(x,y,z),(x1,y1,z1)...(xn,yn,zn)]
     for x,y,z in result:
         #aa=row[2]
         print(f"单位类型: {x}  审核类型: {y}    详细名称：{z}")


print(aa)

metadata = MetaData()
from sqlalchemy import Table, Column, Integer, String
user_table = Table(
     "user_account",
     metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String(30)),
     Column('fullname', String)
 )
from sqlalchemy import ForeignKey
address_table = Table(
     "address",
     metadata,
     Column('id', Integer, primary_key=True),
     Column('user_id', ForeignKey('user_account.id'), nullable=False),
     Column('email_address', String, nullable=False)
 )
metadata.create_all(engine)
print(user_table.c.name,"****")
print(user_table.c.keys())
print(user_table.c.values())
print(type(user_table.c))
print(type(user_table))