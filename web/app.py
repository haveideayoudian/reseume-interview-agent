import streamlit as st
import requests

# API 服务地址（Phase 5 启动的 FastAPI）
API_URL = "http://127.0.0.1:8000/api/analyze"


def read_uploaded_file(uploaded_file):
    """把用户上传的简历文件转成文本
    
    Args:
        uploaded_file: Streamlit 上传的文件对象
    Returns:
        简历文本（字符串）
    """
    # 取文件后缀
    fname = uploaded_file.name.lower()
    
    # 按类型解析
    if fname.endswith(".txt"):
        return uploaded_file.getvalue().decode("utf-8")
    elif fname.endswith(".pdf"):
        from pypdf import PdfReader
        import io
        reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
        return "\n".join(p.extract_text() for p in reader.pages if p.extract_text())
    elif fname.endswith(".docx"):
        from docx import Document
        import io
        doc = Document(io.BytesIO(uploaded_file.getvalue()))
        return "\n".join(p.text for p in doc.paragraphs)
    else:
        return uploaded_file.getvalue().decode("utf-8")


# ===== 页面 UI =====
st.set_page_config(page_title="简历优化 Agent", page_icon="📄", layout="wide")

st.title("📄 简历优化 Agent")
st.caption("粘贴 JD + 导入简历 → 自动评估匹配度并生成优化后的简历")

# 左侧：输入区
with st.container():
    jd_text = st.text_area("📋 粘贴职位描述 (JD)", height=200,
                           placeholder="把岗位 JD 粘贴到这里…")
    resume_file = st.file_uploader("📎 导入你的简历",
                                   type=["txt", "pdf", "docx"])

    analyze_btn = st.button("🚀 开始分析", type="primary", use_container_width=True)

# 右侧：结果区
if analyze_btn:
    # 1. 校验输入
    if not jd_text.strip() or resume_file is None:
        st.warning("请同时提供 JD 和简历文件")
        st.stop()
    
    # 2. 解析简历文件
    with st.spinner("正在解析简历文件…"):
        resume_text = read_uploaded_file(resume_file)
    
    # 3. 调用 API
    with st.spinner("AI 正在分析匹配度并优化简历，请稍候…"):
        try:
            resp = requests.post(API_URL, json={
                "jd_text": jd_text,
                "resume_text": resume_text
            }, timeout=180)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            st.error(f"调用 API 失败：{e}\n\n请确认 FastAPI 服务已启动 (python -m uvicorn api.main:app --reload)")
            st.stop()
    
    # 4. 展示结果（两列）
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 匹配度分析")
        st.markdown(data["analysis"])
    
    with col2:
        st.subheader("✨ 优化后的简历")
        st.markdown(data["optimized_resume"])
