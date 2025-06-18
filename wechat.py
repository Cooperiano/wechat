from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        # 微信服务器验证接口用
        return request.args.get('echostr', '')
    if request.method == 'POST':
        # 微信推送消息
        xml_data = request.data
        # ... 这里处理微信消息
        return 'success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
