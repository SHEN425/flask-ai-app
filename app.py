from flask import Flask, request, jsonify
from flask_cors import CORS
from ai import get_ai_answer
import os

app = Flask(__name__)
CORS(app)  # 允许跨域请求，适配微信小程序

# 健康检查路由，用于Render检测服务状态
@app.route('/')
def health_check():
    return jsonify({"status": "OK"}), 200

@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "问题不能为空"}), 400

    try:
        answer = get_ai_answer(question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": f"AI处理失败: {str(e)}"}), 500

if __name__ == '__main__':
    # 获取Render提供的端口，默认为5000
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
