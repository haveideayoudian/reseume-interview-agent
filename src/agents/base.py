import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()

# 统一配置 LLM
raw_key = os.getenv('BaiLian_API_KEY')
base_url = os.getenv('BaiLian_API_BASE')

if raw_key is None or base_url is None:
    raise ValueError("请检查.env文件配置 BaiLian_API_KEY 和 BaiLian_API_BASE")

llm = ChatOpenAI(
    api_key=SecretStr(raw_key),
    base_url=base_url,
    temperature=0.3,
    model="qwen-plus",
    use_responses_api=False
)

__all__ = ['llm']
