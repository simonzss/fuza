#1创建一个蓝图对象
from flask import Blueprint
index_blue蓝图实例 = Blueprint("admin蓝图名称",__name__)


#2注册路由
#@app.route('/edit')改为
@index_blue蓝图实例.route('/edit2')
def edit视图函数():
    return 'edit视图函数的返回结果'
