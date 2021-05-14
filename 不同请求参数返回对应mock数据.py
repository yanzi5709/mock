#不同的请求参数，返回对应 的mock数据
from flask import Flask
from flask import request
from flask import jsonify

app=Flask(__name__)
@app.route('/studentInfo',methods=['GET','POST'])

def  student_info():
    if request.method=='GET':
        user_id=request.args.get("uid")
        name=request.args.get("name")
        #print("Request Param [uid]:%s  [name]:%s" %(user_id,name))
        return jsonify({"uid":user_id,"name":name,"age":18})
    if request.method=='POST':
         user_id=request.form.get("uid")
         name=request.form.get("name")
         return jsonify({"uid":user_id,"name":name})
    else:
         return '{"name":"kite","age":18,"isStudent":true}'


if __name__=="__main__":
    app.run(debug=False,port=8082)

'''
request.method 判断请求方法
request.form.get 获取网络请求数据----用于POST请求
request.args.get 获取网络请求参数---用于GET请求
jsonify 将传入的 Json形式的数据序列化，转为json字符串做返回
'''
