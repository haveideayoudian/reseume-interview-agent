# ResumeMu - 面试简历优化 Agent

一个基于 Deep Agents（LangChain + LangGraph）的面试简历优化 Agent MVP。

## 功能

- **匹配度分析**：粘贴 JD + 上传简历，输出匹配度评分（0-100）、
  核心优势、主要短板、针对性优化建议
- **简历优化**：基于分析结果，按 STAR 原则重写项目描述，
  量化成果、使用专业动词，生成优化后的完整简历
- **多格式支持**：简历支持 .txt / .pdf / .docx

## 技术栈

| 组件 | 选型 |
|------|------|
| Agent 框架 | Deep Agents (LangChain + LangGraph) |
| LLM | qwen-plus（阿里云百炼 OpenAI 兼容接口） |
| 后端 | FastAPI |
| 前端 | Streamlit |
| 文件解析 | pypdf / python-docx |

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API Key

复制 `.env.example` 为 `.env` 并填入你的大模型BaiLian_API_KEY（已创建适配DeepAgents的OpenAI第三方模型，根据需要进行修改）：

```bash
cp .env.example .env
```

编辑 `.env`：

```
BaiLian_API_KEY=sk-xxxxxxxx
BaiLian_API_BASE=https://你的endpoint/compatible-mode/v1
```

（可选）配置 LangSmith 追踪，便于观察 Agent 的调用链路：

```
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_xxxxxxxx
LANGSMITH_PROJECT=resmu-interview
```

### 3. 运行（需要两个终端）

```bash
# 终端 1：启动 API
python -m uvicorn api.main:app --reload --port 8000

# 终端 2：启动前端
python -m streamlit run web/app.py
```

浏览器打开 http://localhost:8501

## 项目结构

```
├── src/
│   ├── agents/          # Agent 定义（base: LLM 配置 / matcher / optimizer）
│   ├── tools/           # 工具函数（file_reader：txt/pdf/docx 解析）
│   ├── core/            # Prompt 模板（prompts.py）
│   └── pipeline.py      # 完整流程：matcher → optimizer
├── api/                 # FastAPI 接口（POST /api/analyze）
├── web/                 # Streamlit 前端
├── tests/               # 测试
├── data/                # 示例 JD / 简历
├── AGENTS.md            # 开发方法论
└── TASKS.md             # 开发进度清单

```
## 架构说明

Streamlit 前端
    │ HTTP POST /api/analyze
    ▼
FastAPI ──► pipeline.run_pipeline()
              ├─► matcher Agent（LLM：匹配度 + 短板 + 建议）
              └─► optimizer Agent（LLM：按建议润色简历）


## License

MIT
