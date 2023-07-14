from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/api/chat', methods=['POST'])
@cross_origin(supports_credentials=True)
def chat():
    data = request.get_json()
    endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": ""  # 替换为您自己的 ChatGPT API 密钥
    }
    body = {
        "model": "gpt-3.5-turbo",
        "messages": data.get('messages', [])
        # 根据您的需求自定义请求体的内容
    }

    try:
        response = requests.post(endpoint, json=body, headers=headers)
        response.raise_for_status()  # 检查是否出现请求错误
        response_data = response.json()

        # 处理 ChatGPT API 响应并返回给前端
        return jsonify(response_data)

    except requests.exceptions.RequestException as e:
        # 处理请求错误
        error_message = "请求错误: {}".format(str(e))
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
