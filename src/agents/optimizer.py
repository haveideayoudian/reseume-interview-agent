from deepagents import create_deep_agent
from src.agents.base import llm
from src.agents.matcher import analyze_match
from src.core.prompts import OPTIMIZER_PROMPT

# 创建 optimizer Agent
optimizer_agent = create_deep_agent(
    model=llm,
    system_prompt=OPTIMIZER_PROMPT
)

def optimize_resume(resume_text: str, suggestions: str) -> str:
    """优化简历内容
    
    Args:
        resume_text: 原始简历文本
        suggestions: 优化建议
    
    Returns:
        优化后的简历文本
    """

    if not resume_text or not suggestions:
        return "错误：简历内容或优化建议不能为空"

    
    # 构造用户提示词
    user_prompt = f"""
    ## 原始简历：
    {resume_text}

    ## 优化建议：
    {suggestions}
    """
        
    # 调用 Agent
    try:
        result = optimizer_agent.invoke({
            "messages": [
                {"role": "user", "content": user_prompt}
            ]
        })
    except Exception as e:
        return f"优化失败：{e}"

    # 返回结果
    return result["messages"][-1].content


if __name__ == "__main__":
    # 读取测试数据
    with open("data/sample_jd.txt", "r", encoding="utf-8") as f:
        jd_text = f.read()
    with open("data/sample_resume.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()
    
    # 先分析匹配度
    print("=== 匹配度分析 ===")
    analysis = analyze_match(jd_text, resume_text)
    print(analysis)
    
    # 再优化简历
    print("\n=== 优化简历 ===")
    optimized = optimize_resume(resume_text, analysis)
    print(optimized)
