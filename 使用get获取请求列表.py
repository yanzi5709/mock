from flask import Flask, jsonify, request, abort, make_response
#使用get获取请求列表 

app = Flask(__name__)

data = [
    {"name": "test1", "desc": "test1", "id": 1},
    {"name": "test2", "desc": "test2", "id": 2},
    {"name": "test3", "desc": "test3", "id": 3},
]

task_does_not_exist = {"msg": "task does not exist"}
names = ['test1', 'test2', "test3"]
task_exist = {"msg": "name is exist"}


@app.route('/api/tasks/<string:name>')
def get_task(name):
    if len(name) > 0 and name in names:
        for content in data:
            if name == content['name']:
                return make_response(jsonify(content), 200)
    else:
        return make_response(jsonify(task_does_not_exist), 404)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=False)

    #访问时如：http://127.0.0.1:80/api/tasks/test1
    #make_response 内容
