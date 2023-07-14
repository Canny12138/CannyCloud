from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)
CORS(app, supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins="*")

def send_openapi_request(message):
    endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": ""
    }
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": message}]
    }

    response = requests.post(endpoint, json=body, headers=headers)
    response_data = response.json()
    return response_data["choices"][0]["message"]["content"]

@socketio.on('chat')
def handle_chat(message):
    # 发送消息到 OpenAPI 并获取响应
    response = send_openapi_request(message)

    # 将响应发送给客户端
    emit('chat_response', response)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
