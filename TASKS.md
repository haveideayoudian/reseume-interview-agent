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
- [x] 创建 pipeline.py（串联 matcher → optimizer）
- [x] 测试完整流程（JD + 简历 → 分析 → 优化）
- [x] 验证优化效果

## Phase 5：API 接口
- [ ] 创建 `src/api/main.py`（FastAPI）
- [ ] 实现 `/analyze` 接口
- [ ] 测试 API

## Phase 6：前端界面
- [ ] 创建 `src/web/app.py`（Streamlit）
- [ ] 实现文件上传
- [ ] 展示分析结果
- [ ] 展示优化后的简历

## Phase 7：文档与部署
- [ ] 更新 README.md
- [ ] 编写使用说明
- [ ] 测试完整流程
