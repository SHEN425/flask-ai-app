import openai

# 使用 OpenRouter 免费模型（也可换成你喜欢的）
client = openai.OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

def get_ai_answer(question):
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",  # 免费模型，支持中文
            messages=[
                {"role": "system", "content": "你是一个通信技术讲解员，请用通俗易懂的语言回答问题。"},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI 服务出错：{str(e)}"
