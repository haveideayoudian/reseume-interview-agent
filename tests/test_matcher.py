import sys
sys.path.insert(0, '..')

from src.agents.matcher import analyze_match

# 读取测试数据
with open("../data/sample_jd.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()
with open("../data/sample_resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

# 测试分析
result = analyze_match(jd_text, resume_text)
print(result)
