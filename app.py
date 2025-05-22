from flask import Flask, request, jsonify
from flask_cors import CORS
from ai import get_ai_answer

app = Flask(__name__)
CORS(app)  # 允许跨域请求，适配微信小程序

@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "问题不能为空"}), 400

    answer = get_ai_answer(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
