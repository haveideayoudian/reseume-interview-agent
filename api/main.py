from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.pipeline import run_pipeline


# 定义请求体结构
class AnalyzeRequest(BaseModel):
    jd_text: str
    resume_text: str


# 创建 FastAPI 应用
app = FastAPI(title="简历优化 Agent API")

@app.get("/")
def root():
    return {"status": "ok", "message": "简历优化 API 正在运行，请访问 /docs 查看接口文档"}


@app.post("/api/analyze")
def analyze(req: AnalyzeRequest):
    """分析 JD 和简历的匹配度，并生成优化后的简历"""
    
    # 校验输入不为空
    if not req.jd_text.strip() or not req.resume_text.strip():
        raise HTTPException(status_code=400, detail="JD 和简历内容不能为空")
    
    # 调用 pipeline
    result = run_pipeline(req.jd_text, req.resume_text)
    
    return result
