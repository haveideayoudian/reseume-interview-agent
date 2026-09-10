from deepagents import create_deep_agent
from src.agents.base import llm
from src.core.prompts import MATCHER_PROMPT


# 创建 matcher Agent
matcher_agent = create_deep_agent(
    model=llm,
    system_prompt=MATCHER_PROMPT
)

def analyze_match(jd_text: str, resume_text: str) -> str:
    """分析 JD 和简历的匹配度
    
    Args:
        jd_text: JD 文本
        resume_text: 简历文本
    
    Returns:
        匹配度分析结果（字符串）
    """

    if not jd_text or not resume_text:
        return "错误：JD内容或简历内容不能为空"
    
    # 构造用户提示词
    user_prompt = f"""
    ## JD 内容：
    {jd_text}

    ## 简历内容：
    {resume_text}
    """
    
    # 调用 Agent
    try:
        result = matcher_agent.invoke({
            "messages": [
                {"role": "user", "content": user_prompt}
            ]
        })
    except Exception as e:
        return f"匹配度分析失败：{e}"

    # 返回结果
    return result["messages"][-1].content


if __name__ == "__main__":
    # 读取测试数据
    with open("data/sample_jd.txt", "r", encoding="utf-8") as f:
        jd_text = f.read()
    with open("data/sample_resume.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()
    
    # 测试分析
    result = analyze_match(jd_text, resume_text)
    print(result)



