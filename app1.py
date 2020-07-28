from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'index'

#3.在应用对象上注册这个蓝图对象
from admin import index_blue蓝图实例
app.register_blueprint(index_blue蓝图实例)

print(app.url_map)

if __name__=='__main__':
    app.run()
