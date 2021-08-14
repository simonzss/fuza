from datetime import date, timedelta

import pandas as pd

pd.options.display.max_columns=777  #不管DataFrame有多少columns通通显示出来

# read_excel默认只读取Sheet1，如果需要读多个Sheet，需要传进Sheet列表，传进列表得到结果不是DataFrame，而是字典{'Sheet1':DataFrame1,'Sheet2':DataFrame2...}
data = pd.read_excel(r'C:\Users\89638\Desktop\123.xlsx', 'Sheet1', header=0) #重要参数 index_col='期别'，可以在读取时直接指定某列为index
data.columns = ['期别', '存量', '新增', '退出']  # 此处10行4列         实际上是把原有的第一行又设置了一遍
data.set_index('期别', inplace=True)  # 将其中一行设为index
print(data,"这是文件123.xlsx的内容")
print(data.shape)  # 此处10行3列，index不算columns
print(data.columns)
print(data.head(1))
print(data.tail(1))

# data['存量'].at['2020_3']=99999
# data=data[data.存量>100]
# print(data)

df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tom', 'Victor', 'Nick'], 'color': ['red', 'orange', 'black']})
df = df.set_index('ID')
df.to_excel(r'C:\Users\89638\Desktop\output.xlsx')
# df.to_excel(r'C:\Users\89638\Desktop\123.xlsx', sheet_name='Sheet1')

"""
pandas的序列，对应python的字典。因此序列的生成方式一：将字典d直接转成序列s1  s1=pd.Series(d)
"""
d={'x':100,'y':200,'z':300}
print(d.keys())
print(d.values())
s1=pd.Series(d)
print(s1)
print(s1.index,'这是s1的index')
print(s1.keys())
#print(s1.columns)  #  提示'Series' object has no attribute 'columns'
"""
序列的生成方式二，使用一个列表定义序列值，使用另一个列表定义序列的index index=['x','y','z']
"""
s2=pd.Series([100,200,300],index=['x','y','z'])
#  s2['y']=999   这是访问series的值的方法
print("这是s2的index：",s2.index)
print(s2)
"""
由Series扩展为DataFrame
"""
s1=pd.Series([1,2,3],index=[1,2,3],name='A')
s2=pd.Series([10,20,30],index=[1,2,3],name='B')
s3=pd.Series([100,200,300],index=[1,2,3],name='C')
s4=pd.Series([1000,2000,3000],index=[4,2,3],name='D')

df=pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3,s4.name:s4})#字典的形式决定了s1、s2、s3成为了列
print(df,"************")
print(df.index,'这是Dataframe的index，请注意它和Series的index之间的关系')
print(df.columns,'这是Dataframe的columns')

df2=pd.DataFrame([s1,s2,s3,s4]) # 列表的形式决定了s1、s2、s3成为了行
df3=pd.DataFrame([]) # 列表的形式决定了s1、s2、s3成为了行
print(df3,'##################')
df3=df3.append([s1,s2],ignore_index=True)# append一般都会选择ignore_index=True
df3=df3.append(s3)     #注意这里没有ignore_index=True
df3=df3.append(s4)
print(df2,'这是df2，应该与df3相等')
print(df3,'这是df3，应该与df2相等，注意有没有ignore_index=True而造成index的不同')

"""
从excel中读取特定区域的数据
pandas读取excel的空白单元格时，会自动将空白单元格读取内容NaN设置为float类型，需要在read_excel里通过dtype={字典}对columns进行格式设定
"""
def add_month(startdate,deltamonth):
    year_delta=deltamonth//12
    month=startdate.month+deltamonth%12
    if month !=12:
        year_delta=year_delta+month//12
        month=month%12
    return date(startdate.year+year_delta,month,startdate.day)

print(add_month(date(2018,11,1),2))

data = pd.read_excel(r'C:\Users\89638\Desktop\1234.xlsx', skiprows=14,usecols="H:N",dtype={'ID':str,'InStore':str,'Date':str,})
for i in data.index:
    data['ID'].at[i]=i+1    #这是用DataFrame先取到特定的Series,再修改Series的值
    data.at[i,'InStore']='Yeaa!' if i%2==0 else 'No'  #这是直接定位修改DataFrame的值
    startdate=date(2018,1,1)
    # data['Date'].at[i]=startdate+timedelta(weeks=i)                         # 周数加1，用到了牛逼的函数timedelta，但最多只能加到weeks，不能加month
    # data['Date'].at[i]=date(startdate.year+i,startdate.month,startdate.day) # 年份加1
    data['Date'].at[i]=add_month(startdate,i)                                 # 月份加1，用到了自写函数add_month

"""
单元格的计算
其中apply函数的用法相当重要！！！
"""
def add_2(x):
    return x+2

#算出Price，然后用apply函数+2，再用lambda函数+2
data['Price']=data['ListPrice']*data['Discount']
data['Price']=data['Price'].apply(add_2)   #我们是要函数的名字，不是要调用函数，所以add_2不要加括号
data['Price']=data['Price'].apply(lambda x:x+2)   #lambda的用法！

print(data,"data全部输出完毕")
print(data['ID']) #输出结果 Name: ID, dtype: float64
"""
将自己修改好的DataFrame，写入到另一个excel文件
"""
data.to_excel(r'C:\Users\89638\Desktop\1234_副本.xlsx')
print("Done!")


"""
DataFrame有两个轴，一个是0，一个是1
在DataFrame的处理中经常会遇到轴的概念，这里先给大家一个直观的印象
我们所说的axis=0即表示沿着每一列或行索引值，从上向下执行方法
axis=1即表示沿着每一行或者列标签，从左到右横向执行对应的方法

DataFrame选定1列的方法，是DataFrame['column_name']
DataFrame选定多列的方法，是DataFrame[['column_name1','column_name2',...]]
DataFrame增加行的方法，是DataFrame.append(Series_name,ignore_index=True),注意append会返回一个新的DataFrame，注意用变量去接收
DataFrame增加列的方法，是DataFrame['New_column_name']=Series_name
s2['y']=999   这是访问或设定Series的值的方法，s2是Series，'y'是s2的index的一个值，同理可访问s2['y']，s2['z']
data['ID'].at[i]=i+1    #访问或设定DataFrame某个值的方法，这是用DataFrame先取到特定的Series列,再修改Series列的值
data.at[i,'ID']='Yeaa!' #访问或设定DataFrame某个值的方法，这是直接定位修改DataFrame的值，注意at里是列表，索引在前列名在后
"""
