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
