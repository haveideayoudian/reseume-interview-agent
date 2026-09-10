# ResumeMu - 面试简历优化 Agent

一个基于 Deep Agents（LangChain + LangGraph）的面试简历优化 Agent MVP。

## 功能

- **JD 解析**：自动提取职位描述的关键要求
- **简历解析**：提取简历的核心信息
- **匹配度评估**：语义匹配 + 量化评分，指出短板
- **文字质量评估**：语法、专业性、清晰度三维度检查
- **STAR 润色**：按 STAR 原则重写项目描述

## 技术栈

| 组件 | 选型 |
|------|------|
| Agent 框架 | Deep Agents (LangChain + LangGraph) |
| LLM | 免费LLM，AgensAI |
| 文件解析 | PyPDF2, python-docx |
| 开发语言 | Python 3.11+ |

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API Key

复制 `.env.example` 为 `.env` 并填入你的 OpenAI API Key：

```bash
cp .env.example .env
```

编辑 `.env`：

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. 运行

```bash
python src/agent/hello.py
```

## 项目结构

```
resemu_interview/
├── src/
│   ├── agent/        # Agent 相关代码
│   ├── parsers/      # 文件解析器
│   ├── evaluators/   # 评估器
│   └── utils/        # 工具函数
├── tests/            # 测试代码
├── api/              # API 接口（后续阶段）
└── data/             # 示例数据
```

## License

MIT
