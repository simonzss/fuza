from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from flask_sqlalchemy import SQLAlchemy

#创建Flask应用程序实例
#需要传入__name__,为了确定资源所在路径

app=Flask(__name__)
app.secret_key='wwwitheima'

#配置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI']='mssql+pyodbc://sa:11111111@11111'
#dialect+driver://username:password@host:port/database   来自Flask-sqlalchemy
#engine = create_engine('mssql+pyodbc://scott:tiger@mydsn')  来自Sqlalchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Role(db.Model):
    #定义表
    __tablename__='roles'
    #定义字段
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

db.create_all()

for foo in Role.query.all():
    print(foo.id,foo.name)

print(Role.query.get(1).name)

class LoginForm(FlaskForm):
    username1=StringField('用户名：')
    password1=PasswordField('密码：')
    submit1=SubmitField('提交')
    selectfield=SelectField(
        label='年份',
        choices=[(1,2015),(2,2016),(3,2017)],
        default=3
    )

#使用装饰器定义路由
#定义视图函数
#路由默认只支持GET，如需其他方式需要自行添加
@app.route('/',methods=['GET','POST'])
def hello_world():
    username = request.form.get('username')
    password = request.form.get('password')
    username1 = request.form.get('username1')
    password1 = request.form.get('password1')
    selectfield=request.form.get('selectfield')
    if request.method=='POST':
        if username1!=password1:
            flash('用户名和密码不相等啊')
            flash(selectfield)
        else:
            flash('成功返回POST页面,成功拿到username1和password1，两者相等')
            flash(selectfield)
    url='www.baidu.com'
    my_dict=[1,3,5,7,9]
    print(selectfield)
    login_form = LoginForm()
    return render_template('index.html',template_zhanwei=url,my_dict=my_dict,login_form=login_form)

@app.route('/form',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username1=request.form.get('username1')
        password1=request.form.get('password1')
        if username1 != password1:
            flash('用户名和密码不相等')
        else:
            flash('成功拿到username1和password1，两者相等')

    login_form=LoginForm()
    return render_template('index1.html',login_form=login_form)

@app.route('/lwzb/<year>',methods=['GET','POST'])
def view_lwzb(year):
    return 'year %s' % year


if __name__ == '__main__':
    app.run()   #执行app.run,就会将Flask应用程序实例运行在一个简易的服务器上（Flask提供，用于测试）
