# MVP 开发任务清单

> 每完成一步就打个勾 ✅

## Phase 0：环境准备
- [x] 创建项目目录结构
- [x] 安装依赖（deepagents、langchain、PyPDF2、python-docx）
- [x] 配置 .env 文件（API Key）
- [x] 测试 LLM 连接

## Phase 1：基础框架
- [x] 创建 `src/agents/base.py`（统一配置 LLM）
- [x] 创建 `src/tools/file_reader.py`（文件读取工具）
- [x] 创建 `src/core/prompts.py`（Prompt 模板）
- [x] 测试文件读取功能

## Phase 2：matcher Agent（核心）
- [x] 创建 `src/agents/matcher.py`（匹配度评估）
- [x] 测试 matcher Agent
- [x] 验证输出格式正确

## Phase 3：optimizer Agent
- [x] 创建 `src/agents/optimizer.py`（优化润色）
- [x] 测试 optimizer Agent
- [x] 验证输出格式正确

## Phase 4：整合测试
- [x] 创建 `src/pipeline.py`（串联 matcher → optimizer）
- [x] 测试完整流程（JD + 简历 → 分析 → 优化）
- [x] 验证优化效果

## Phase 5：API 接口
- [x] 创建 `api/main.py`（FastAPI）
- [x] 实现 `/api/analyze` 接口
- [x] 测试 API（访问 /docs 通过验证）

## Phase 6：前端界面
- [x] 创建 `web/app.py`（Streamlit）
- [x] 实现 JD 粘贴 + 简历文件上传
- [x] 展示匹配度分析结果
- [x] 展示优化后的简历

## Phase 7：工程化收尾
- [ ] 补全 `requirements.txt`（缺 fastapi / uvicorn / streamlit / requests / pypdf）
- [ ] 更新 `README.md`（安装、配置、运行、目录结构、架构说明）
- [ ] 创建一键启动脚本（同时起 API + 前端）
- [ ] 端到端验收测试（用真实简历 + 真实 JD 跑一遍）
- [ ] 提交 Git 并推送到 GitHub

## 待办技术债（MVP 之后再处理）
- [ ] `web/app.py` 里的 `read_uploaded_file` 与 `src/tools/file_reader.py` 逻辑重复，应统一
- [ ] `analyze_match` / `optimize_resume` 缺少重试与超时控制
- [ ] 匹配度评分为纯文本，未来可结构化为 JSON 便于前端展示
- [ ] 无缓存机制，同一份 JD+简历重复分析会重复消耗 token
