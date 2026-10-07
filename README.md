# DCode

> A lightweight AI Coding Agent built from scratch with Python.

DCode 是一个基于 Python 实现的轻量级 AI Coding Agent Demo，项目灵感来自 OpenCode 等 AI Coding 工具。

目前项目主要聚焦于 **AI Coding Agent 的终端交互界面与基础架构设计**，后续会持续完善 Agent、Model、Tool、Session 等核心能力。

本项目目前处于 **Early Development / Demo** 阶段。

## ✨ Features

目前已经实现：

* 🖥️ Terminal TUI interface
* 💬 Chat-style interaction
* 🤖 Model Provider abstraction
* 🧠 Basic Agent architecture

其他 Coding Agent 能力将在后续版本中逐步实现。

## 🏗️ Project Structure

```text
DCode_project/
│
├── README.md
├── LICENSE
├── pyproject.toml
│
├── src/
│   └── DCode/
│       │
│       ├── main.py
│       │
│       ├── ui/
│       │   ├── app.py
│       │   ├── chat_view.py
│       │   ├── input_box.py
│       │   ├── message.py
│       │   └── status_bar.py
│       │
│       ├── agent/
│       │   └── agent.py
│       │
│       ├── model/
│       │   ├── base.py
│       │   ├── factory.py
│       │   ├── deepseek.py
│       │   └── mock.py
│       │
│       ├── tools/
│       │   ├── edit_file.py
│       │   ├── shell.py
│       │   ├── search.py
│       │   └── read_file.py
│       │
│       ├── session/
│       │   └── session.py
│       │
│       └── config/
│           └── config.py
│
└── tests/
```

## 🏛️ Architecture

目前 DCode 采用简单的模块化设计：

```text
                    ┌─────────────┐
                    │     UI      │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    Agent    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    Model    │
                    └─────────────┘
```

目前各模块的主要职责：

| Module    | Responsibility           |
| --------- | ------------------------ |
| `ui`      | Terminal UI 和用户交互        |
| `agent`   | Agent 核心逻辑               |
| `model`   | Model Provider 抽象及具体模型实现 |
| `tools`   | 后续用于扩展 Agent 工具能力        |
| `session` | 后续用于管理对话和上下文状态           |
| `config`  | 项目配置                     |
| `tests`   | 测试代码                     |

## 🚀 Getting Started

### Requirements

* Python 3.11+
* uv

### Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd DCode_project
```

安装项目依赖：

```bash
uv sync
```

### Configuration

在运行 DCode 之前，需要配置模型相关的环境变量。

目前默认使用 DeepSeek Provider，需要配置：

```bash
export DEEPSEEK_API_KEY="你的模型密钥"
export DCODE_MODEL_PROVIDER="deepseek"
```

其中：

| Environment Variable   | Description                 |
| ---------------------- | --------------------------- |
| `DEEPSEEK_API_KEY`     | DeepSeek API Key            |
| `DCODE_MODEL_PROVIDER` | 模型 Provider，目前使用 `deepseek` |

例如：

```bash
export DEEPSEEK_API_KEY="sk-xxxxxxxxxxxxxxxx"
export DCODE_MODEL_PROVIDER="deepseek"
```

> ⚠️ **Security Notice**
>
> 请不要将真实的 API Key 直接写入代码、`README.md` 或提交到 Git 仓库。
>
> 推荐通过环境变量进行配置，并确保包含密钥的配置文件不会被提交到 Git。

### Run

完成环境变量配置后：

```bash
uv run DCode
```

## ⚙️ Model

DCode 对模型进行了基础的 Provider 抽象，目前模型相关代码位于：

```text
src/DCode/model/
```

结构：

```text
model/
├── base.py
├── factory.py
├── deepseek.py
└── mock.py
```

其中 `mock.py` 用于本地开发和 UI 调试，避免开发过程中必须依赖真实模型。

## 🧪 Testing

运行测试：

```bash
uv run pytest
```

## 🗺️ Roadmap

DCode 会按照以下方向持续开发：

### Phase 1 — UI & Basic Architecture

* [x] Terminal TUI
* [x] Chat interface
* [x] Model Provider abstraction
* [x] Basic Agent architecture

### Phase 2 — Agent Loop

* [ ] Streaming model output
* [ ] Tool calling
* [ ] Agent execution loop
* [ ] Context management

### Phase 3 — Coding Capabilities

* [ ] File reading
* [ ] File search
* [ ] File editing
* [ ] Shell command execution
* [ ] Tool execution confirmation

### Phase 4 — Advanced Features

* [ ] Multi-model / multi-provider support
* [ ] Better context management
* [ ] MCP support
* [ ] Plugin / tool system

## 📌 Project Status

DCode is currently an experimental project under active development.

The architecture and APIs may change frequently during development.

The goal of this project is to **understand and implement the core engineering ideas behind AI Coding Agents step by step**, rather than simply reproducing an existing AI Coding tool.

## 📄 License

This project is licensed under the MIT License.
