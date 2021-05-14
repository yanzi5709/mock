# 不同api接口 返回 不同的 mock信息
from flask import Flask
app=Flask(__name__)
#studentinfo支持 GET和POST两种 请求方式
@app.route('/studentinfo/',methods=["GET","POST"])
def student_info():
    return '{"name":"lilei","age":18,"sex":"男","isStudent":true}'
#不同的接口地址，定义不同的Router即可，收到 请求直接返回mock数据
@app.route('/schoolinfo/',methods=["POST"])
#只有一个post请求浏览器直接 访问报405方法不被允许
def school_info():
    return '{"school":"sichuang  daxue","grade":2}'

if  __name__=="__main__":
    app.run(debug=False, port=8080)
#浏览器访问http://127.0.0.1:8080/studentinfo 或者schoolinfo即可返回相应的内容
