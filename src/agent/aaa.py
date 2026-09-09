import os
from dotenv import load_dotenv
from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

# 1. 加载环境变量（读取 .env 文件）
load_dotenv()


# 2. 创建 Agent
# model 参数指定使用哪个模型
# system_prompt 是 Agent 的系统提示词


raw_key=os.getenv('BaiLian_API_KEY')
# 获取模型回复
llm = ChatOpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key=SecretStr(raw_key),
    base_url=os.getenv('BaiLian_API_BASE'),
    temperature=0.3,
    model="qwen3.5-ocr",
    # 国内兼容接口一定要关闭 responses_api，否则会报错
    use_responses_api=False
)



agent = create_deep_agent(
    model=llm,
    system_prompt="你是一个友好的简历优化助手。请用简洁的方式回答用户的问题。"
)

# 3. 调用 Agent
if __name__ == "__main__":
    result = agent.invoke({
        "messages": [
            {"role": "user", "content": "你好，请用一句话介绍你自己"}
        ]
    })
    
    # 4. 打印结果
    print(result["messages"][-1].content)

