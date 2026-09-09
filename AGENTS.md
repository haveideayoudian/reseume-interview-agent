# 面试简历优化 Agent - 开发计划（学习版）

## 项目定位
- **目标**：构建一个面试简历优化 Agent，帮助用户评估简历与 JD 的匹配度并提供优化建议
- **框架**：Deep Agents (LangChain + LangGraph)
- **LLM**：OpenAI GPT-4o
- **输入**：文件上传 + 粘贴文本
- **输出**：纯对话式
- **后续扩展**：RESTful API + Web 前端

---

## 学习路线总览

| 阶段 | 主题 | 天数 | 核心技能 |
|------|------|------|----------|
| Phase 0 | 环境准备 | 1天 | Python 环境、API Key、Deep Agents 基础 |
| Phase 1 | 第一个 Agent | 2天 | 创建、调用、工具注册 |
| Phase 2 | 文件解析 Agent | 2天 | PDF/Word 解析、文本提取 |
| Phase 3 | JD 解析 Agent | 2天 | LLM 结构化输出、信息抽取 |
| Phase 4 | 简历解析 Agent | 2天 | 简历信息抽取、STAR 识别 |
| Phase 5 | 匹配度评估 Agent | 3天 | 语义匹配、评分逻辑 |
| Phase 6 | 文字质量评估 Agent | 2天 | 语法检查、专业术语评估 |
| Phase 7 | STAR 润色 Agent | 3天 | Prompt 工程、改写能力 |
| Phase 8 | 流水线整合 | 3天 | 并行调度、错误处理 |
| Phase 9 | API + 前端扩展 | 4天 | FastAPI、简单 Web 界面 |

**总计：24天（可灵活调整）**

---

## Phase 0：环境准备（1天）

### 学习目标
- 理解 Deep Agents 的基本概念
- 搭建开发环境
- 跑通第一个 Hello World

### 步骤

#### Step 0.1：创建项目结构
```
resemu_interview/
├── .env                  # API Key 配置
├── requirements.txt      # 依赖列表
├── README.md            # 项目说明
├── src/
│   ├── __init__.py
│   ├── agent/           # Agent 相关代码
│   ├── parsers/         # 解析器
│   ├── evaluators/      # 评估器
│   └── utils/           # 工具函数
├── tests/               # 测试代码
└── data/                # 示例数据
```

**任务**：
1. 创建虚拟环境
2. 安装依赖
3. 配置 .env 文件

#### Step 0.2：理解 Deep Agents 核心概念
- Agent Harness 是什么
- create_deep_agent() 的作用
- 工具（Tool）的概念
- 子智能体（Subagent）的概念

**任务**：
1. 阅读官方文档
2. 写一个最简单的 Agent（ greeting 功能）
3. 理解 agent.invoke() 的执行流程

#### Step 0.3：第一个 Agent
创建一个能回答简单问题的 Agent，测试 LLM 连接是否正常。

---

## Phase 1：第一个 Agent - 简历简介生成器（2天）

### 学习目标
- 掌握 Deep Agents 的基本用法
- 理解工具的注册和使用
- 学会写系统提示词

### 步骤

#### Step 1.1：创建基础 Agent 框架
```python
from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI

agent = create_deep_agent(
    model="openai:gpt-4o",
    system_prompt="你是一个简历优化助手..."
)
```

**任务**：
1. 创建 `src/agent/base.py`
2. 配置 LLM 和系统提示词
3. 测试 agent.invoke() 调用

#### Step 1.2：注册第一个工具
创建一个简单的工具：获取当前时间/天气等，用于熟悉工具注册流程。

**任务**：
1. 用 `@tool` 装饰器定义工具
2. 将工具注册到 Agent
3. 测试工具调用

#### Step 1.3：实现简历简介生成
定义一个工具：将用户提供的简历片段生成简短简介。

**任务**：
1. 设计工具输入/输出
2. 编写工具实现
3. 测试完整流程

---

## Phase 2：文件解析 Agent（2天）

### 学习目标
- 掌握 PDF/Word/TXT 文件解析
- 理解多模态输入处理
- 学会错误处理

### 步骤

#### Step 2.1：实现文本提取工具
```python
from langchain.tools import tool
from langchain_community.document_loaders import PyPDFLoader, DocxLoader

@tool
def read_file(file_path: str) -> str:
    """读取文件内容"""
    ...
```

**任务**：
1. 安装依赖（PyPDF2、python-docx）
2. 实现文件读取工具
3. 处理不同文件格式

#### Step 2.2：文件上传处理
创建接口接受文件上传（先测试，后续接入 Web）。

**任务**：
1. 定义文件读取流程
2. 处理大文件（分块读取）
3. 错误处理（文件不存在、格式不支持）

#### Step 2.3：测试解析 Agent
创建一个专门负责解析文件的 Agent。

**任务**：
1. 将解析工具封装成独立 Agent
2. 测试各种文件格式
3. 优化解析效果

---

## Phase 3：JD 解析 Agent（2天）

### 学习目标
- 掌握 LLM 结构化输出
- 理解信息抽取技巧
- 学会 Prompt 工程

### 步骤

#### Step 3.1：设计 JD 解析 Prompt
定义 JD 需要提取的信息：
- 岗位名称
- 核心技能要求
- 经验要求
- 加分项
- 职责描述

**任务**：
1. 编写 JD 解析系统提示词
2. 定义输出格式（JSON Schema）
3. 测试提取效果

#### Step 3.2：实现 JD 解析工具
```python
@tool
def parse_jd(jd_text: str) -> dict:
    """解析 JD 内容，提取关键信息"""
    ...
```

**任务**：
1. 调用 LLM 进行信息抽取
2. 结构化输出
3. 处理异常情况

#### Step 3.3：创建 JD 解析 Agent
将 JD 解析封装为独立 Agent。

**任务**：
1. 创建 `src/agent/jd_parser.py`
2. 配置专属 Prompt
3. 测试不同岗位类型（技术/职能）

---

## Phase 4：简历解析 Agent（2天）

### 学习目标
- 理解简历信息结构
- 掌握信息抽取方法
- 学会识别 STAR 元素

### 步骤

#### Step 4.1：设计简历解析 Prompt
定义简历需要提取的信息：
- 基本信息
- 工作经历（每段）
- 项目经历（每段）
- 技能清单
- 教育背景

**任务**：
1. 编写简历解析系统提示词
2. 定义输出格式
3. 测试提取效果

#### Step 4.2：实现简历解析工具
```python
@tool
def parse_resume(resume_text: str) -> dict:
    """解析简历内容，提取关键信息"""
    ...
```

**任务**：
1. 调用 LLM 进行信息抽取
2. 结构化输出
3. 识别 STAR 元素

#### Step 4.3：创建简历解析 Agent
将简历解析封装为独立 Agent。

**任务**：
1. 创建 `src/agent/resume_parser.py`
2. 配置专属 Prompt
3. 测试不同类型简历

---

## Phase 5：匹配度评估 Agent（3天）

### 学习目标
- 理解语义匹配原理
- 掌握评估逻辑设计
- 学会量化评分

### 步骤

#### Step 5.1：设计匹配度评估 Prompt
定义评估维度：
- 技能匹配度
- 经验匹配度
- 教育匹配度
- 其他要求匹配度

**任务**：
1. 编写评估系统提示词
2. 定义评分标准
3. 设计输出格式

#### Step 5.2：实现匹配度评估工具
```python
@tool
def evaluate_match(jd_parsed: dict, resume_parsed: dict) -> dict:
    """评估简历与JD的匹配度"""
    ...
```

**任务**：
1. 调用 LLM 进行匹配度评估
2. 输出评分和短板分析
3. 提供优化建议

#### Step 5.3：创建匹配度评估 Agent
将匹配度评估封装为独立 Agent。

**任务**：
1. 创建 `src/agent/matcher.py`
2. 配置专属 Prompt
3. 测试不同匹配场景

---

## Phase 6：文字质量评估 Agent（2天）

### 学习目标
- 理解文字质量评估维度
- 掌握语法检查方法
- 学会专业术语评估

### 步骤

#### Step 6.1：设计文字质量评估 Prompt
评估维度：
- 语法正确性
- 用词专业性
- 表达清晰度
- 逻辑连贯性

**任务**：
1. 编写评估系统提示词
2. 定义评分标准
3. 设计输出格式

#### Step 6.2：实现文字质量评估工具
```python
@tool
def evaluate_writing(resume_text: str) -> dict:
    """评估简历文字质量"""
    ...
```

**任务**：
1. 调用 LLM 进行文字评估
2. 输出问题列表
3. 提供修改建议

#### Step 6.3：创建文字质量评估 Agent
将文字评估封装为独立 Agent。

**任务**：
1. 创建 `src/agent/writing_evaluator.py`
2. 配置专属 Prompt
3. 测试不同类型简历

---

## Phase 7：STAR 润色 Agent（3天）

### 学习目标
- 掌握 STAR 原则
- 理解改写技巧
- 学会优化 Prompt

### 步骤

#### Step 7.1：理解 STAR 原则
- **S**ituation（情境）
- **T**ask（任务）
- **A**ction（行动）
- **R**esult（结果）

**任务**：
1. 学习 STAR 原则
2. 分析优秀简历案例
3. 总结改写规律

#### Step 7.2：设计 STAR 润色 Prompt
```python
@tool
def rewrite_with_star(project_desc: str, jd_requirements: str) -> str:
    """按 STAR 原则润色项目描述"""
    ...
```

**任务**：
1. 编写润色系统提示词
2. 设计改写流程
3. 保持原意同时提升表达

#### Step 7.3：实现 STAR 润色 Agent
将 STAR 润色封装为独立 Agent。

**任务**：
1. 创建 `src/agent/star_optimizer.py`
2. 配置专属 Prompt
3. 测试润色效果

---

## Phase 8：流水线整合（3天）

### 学习目标
- 理解 Agent 编排
- 掌握并行调度
- 学会错误处理

### 步骤

#### Step 8.1：设计流水线架构
```
输入 → [JD 解析] ─┐
                  ├→ [匹配度评估] → [文字评估] → [STAR 润色] → 输出
输入 → [简历解析] ─┘
```

**任务**：
1. 绘制流程图
2. 设计数据流
3. 定义接口规范

#### Step 8.2：实现并行解析
使用 Deep Agents 的子智能体功能，并行执行 JD 和简历解析。

**任务**：
1. 创建并行调度逻辑
2. 等待两个解析完成
3. 合并结果

#### Step 8.3：整合完整流程
串联所有 Agent，形成完整流水线。

**任务**：
1. 创建 `src/pipeline.py`
2. 实现流程控制
3. 添加错误处理
4. 测试完整流程

---

## Phase 9：API + 前端扩展（4天）

### 学习目标
- 理解 RESTful API 设计
- 掌握 FastAPI 基本用法
- 学会前后端交互

### 步骤

#### Step 9.1：设计 API 接口
```
POST /api/analyze - 提交 JD 和简历进行分析
GET  /api/result/{id} - 获取分析结果
```

**任务**：
1. 定义 API 规范
2. 设计请求/响应格式
3. 考虑文件上传

#### Step 9.2：实现 FastAPI 后端
```python
from fastapi import FastAPI, UploadFile
from src.pipeline import run_pipeline

app = FastAPI()

@app.post("/api/analyze")
async def analyze(jd: str, resume: str):
    result = run_pipeline(jd, resume)
    return result
```

**任务**：
1. 创建 `src/api.py`
2. 实现接口
3. 测试 API

#### Step 9.3：创建简单 Web 界面
使用 Streamlit 或 Gradio 快速搭建前端。

**任务**：
1. 选择 UI 框架
2. 实现文件上传
3. 展示分析结果

---

## 文件结构（最终版）

```
resemu_interview/
├── .env                    # API Key 配置
├── requirements.txt        # 依赖列表
├── README.md              # 项目说明
├── src/
│   ├── __init__.py
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── base.py        # 基础 Agent
│   │   ├── jd_parser.py   # JD 解析 Agent
│   │   ├── resume_parser.py # 简历解析 Agent
│   │   ├── matcher.py     # 匹配度评估 Agent
│   │   ├── writing_evaluator.py # 文字评估 Agent
│   │   └── star_optimizer.py # STAR 润色 Agent
│   ├── parsers/
│   │   ├── __init__.py
│   │   └── file_parser.py # 文件解析工具
│   ├── evaluators/
│   │   ├── __init__.py
│   │   └── prompts.py     # 评估 Prompt 模板
│   └── utils/
│       ├── __init__.py
│       └── helpers.py     # 工具函数
├── tests/                  # 测试代码
│   ├── test_jd_parser.py
│   ├── test_resume_parser.py
│   ├── test_matcher.py
│   └── test_pipeline.py
├── api/
│   ├── __init__.py
│   └── main.py            # FastAPI 入口
└── data/                   # 示例数据
    ├── sample_jd.txt
    └── sample_resume.txt
```

---

## 关键 Prompt 模板

### JD 解析 Prompt
```
你是一个专业的 JD 分析助手。请从以下职位描述中提取关键信息：
1. 岗位名称
2. 核心技能要求（列出具体技能）
3. 经验要求（年限）
4. 加分项
5. 主要职责

请以 JSON 格式输出。
```

### 匹配度评估 Prompt
```
请评估以下简历与目标岗位 JD 的匹配度。
评估维度：
1. 技能匹配度（0-100分）
2. 经验匹配度（0-100分）
3. 教育匹配度（0-100分）
4. 整体匹配度（0-100分）

请指出简历的短板，并给出具体的优化建议。
```

### STAR 润色 Prompt
```
请按照 STAR 原则优化以下项目描述：
- Situation（情境）：项目背景
- Task（任务）：你的职责
- Action（行动）：你采取的具体行动
- Result（结果）：可量化的成果

保持原意，提升表达的专业性和影响力。
```

---

## 学习检查点

在每个 Phase 完成后，问自己：
1. 这个 Agent 的核心功能是什么？
2. 它是如何与 LLM 交互的？
3. 工具是如何注册和使用的？
4. 如果有错误，如何调试？
5. 下一步可以如何扩展？

---

## 后续扩展方向

- [ ] 支持更多文件格式（图片、Markdown）
- [ ] 添加历史记录功能
- [ ] 支持批量分析
- [ ] 集成行业知识库
- [ ] 添加 A/B 测试功能
- [ ] 支持多语言简历
- [ ] 移动端适配
