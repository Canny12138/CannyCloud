from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import openai
import threading

app = Flask(__name__)
CORS(app, supports_credentials=True)

openai.api_key = ""  # 替换为您的 OpenAI API 密钥

def generate_chat_response(messages):
    response = openai.Completion.create(
        engine="text-davinci-003",  # 替换为您想要使用的 GPT-3 引擎
        prompt=messages,
        max_tokens=2000,  # 设置生成文本的最大长度
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

@app.route('/api/chat', methods=['POST'])
@cross_origin(supports_credentials=True)
def chat():
    data = request.get_json()
    messages = [msg["content"] for msg in data.get('messages', [])]

    try:
        response_data = generate_chat_response(messages)

        # 处理 ChatGPT API 响应并返回给前端
        return jsonify({"response": response_data})

    except Exception as e:
        # 处理请求错误
        error_message = "请求错误: {}".format(str(e))
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)