from openai import OpenAI
import base64


API_KEY = "your_ak:your_sk"

BASE_URL = "https://ark.cn-beijing.volces.com/api/v1"

MODEL_ID = "deepseek-r1-250120"

encoded_api_key = base64.b64encode(API_KEY.encode("utf-8")).decode("utf-8")


client = OpenAI(
    api_key=encoded_api_key,
    base_url=BASE_URL
)

def chat_with_deepseek(user_query: str) -> str:
    """调用 DeepSeek 模型获取回复"""
    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": "你是一个乐于助人的AI助手，会清晰、准确地回答用户的问题。"},
                {"role": "user", "content": user_query}
            ],
            temperature=0.7,
            max_tokens=2048
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ 调用失败: {str(e)}"

if __name__ == "__main__":
    print("🤖 DeepSeek Chatbot 已启动（输入 'quit' 退出）")
    while True:
        user_input = input("你: ")
        if user_input.lower() in ["quit", "exit"]:
            print("👋 再见！")
            break
        if not user_input.strip():
            print("⚠️  请输入有效问题")
            continue
        reply = chat_with_deepseek(user_input)
        print(f"DeepSeek: {reply}\n")