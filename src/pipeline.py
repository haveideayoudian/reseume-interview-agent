from src.agents.matcher import analyze_match
from src.agents.optimizer import optimize_resume


def run_pipeline(jd_text: str, resume_text: str) -> dict:
    """完整流程：JD+简历 → 匹配度分析 → 优化简历
    
    Args:
        jd_text: JD 文本
        resume_text: 简历文本
    
    Returns:
        包含分析和优化结果的字典
    """
    # Step 1: 分析匹配度
    analysis = analyze_match(jd_text, resume_text)

    # 判断第一步是否执行失败，如果失败直接返回，不再执行优化
    if analysis.startswith("错误：") or analysis.startswith("匹配度分析失败："):
        return {
            "analysis": analysis,
            "optimized_resume": "终止，无法执行简历优化"
        }
    
    # Step 2: 根据分析结果优化简历
    optimized_resume = optimize_resume(resume_text, analysis)
    
    # 返回结构化结果
    return {
        "analysis": analysis,
        "optimized_resume": optimized_resume
    }


if __name__ == "__main__":
    with open("data/sample_jd.txt", "r", encoding="utf-8") as f:
        jd_text = f.read()
    with open("data/sample_resume.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()
    
    result = run_pipeline(jd_text, resume_text)
    print("=== 分析结果 ===")
    print(result["analysis"])
    print("\n=== 优化简历 ===")
    print(result["optimized_resume"])
