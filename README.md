# Nekopara Desktop Pet

基于 Python (PyQt6) 和 FreeMote 技术构建的桌面桌宠程序。
这是一个专为Nekopara角色打造的桌面桌宠程序，并支持鼠标交互、眼部全屏追踪、多角色切换以及鼠标穿透模式。

## ✨ 功能特性 (Features)

* **透明背景渲染**：使用 `QtWebEngine` 实现无边框、透明背景的角色渲染，完美融入桌面。
* **鼠标穿透模式**：开启后，鼠标点击操作会直接穿透角色，作用于后方的窗口（适合工作/游戏时挂机）。
* **交互反馈**：支持点击身体不同部位触发不同的动作和语音反馈（仅在非穿透模式下有效）。
* **眼部追踪**：角色的视线和头部会全屏跟随鼠标光标移动。
* **多角色/服装切换**：内置Nekopara角色库（Azuki, Chocola, Vanilla, Coconut 等）及多种服装配置。
* **系统托盘支持**：
    * 右键菜单：隐藏/显示、锁定位置、开关鼠标穿透、退出程序。
    * 双击托盘：快速切换显示/隐藏状态。
* **完全可配置**：支持调整缩放比例 (Scale)、窗口大小，并自动保存配置。
* **位置锁定**：防止误触导致桌宠被拖动（穿透模式下强制开启）。

## 🥰 功能展示
<video src="https://raw.githubusercontent.com/kylin930/NekoparaDesktopPet/refs/heads/main/2026-01-31%2021-04-30.mp4" controls="controls" width="500" height="300"></video>

## 🛠️ 技术致谢 (Credits)

本项目基于以下优秀的开源项目和代码实现：

* **FreeMote-SDK**: 本项目的核心模型驱动与渲染技术使用了 [FreeMote-SDK](https://github.com/Project-AZUSA/FreeMote-SDK)。
* **NekoWebShow**: 本项目中关于角色的动作定义、交互逻辑部分代码参考并修改自 **Chocola-X** 的 [NekoWebShow](https://github.com/Chocola-X/NekoWebShow) 项目。

## 📂 目录结构 (Directory Structure)

```text
FreeMote-Desktop-Pet/
├── app.py                 # [主程序] PyQt6 窗口逻辑、交互事件处理、托盘管理
├── server.py              # [后端] HTTP 静态文件服务器 (默认端口 53421)
├── config.json            # [配置] 保存用户设置（位置、缩放、锁定、穿透状态）
├── icon.png               # [资源] 系统托盘图标
├── fflate.js              # [库] 用于解压压缩后的模型文件
├── emoteplayer.js         # [驱动] FreeMote SDK 核心
├── FreeMoteDriver.js      # [驱动] FreeMote SDK 驱动
├── config/                # [配置] 存放每个角色的动作定义 (.js 文件)
├── model/                 # [资源] 存放模型文件 (.psb 或 .zip)
└── sounds/                # [资源] 存放语音文件 (.mp3/.wav)

```

## 🚀 快速开始 (Getting Started)

### 1. 环境要求

确保已安装 Python 3.8 或更高版本。

### 2. 安装依赖

本项目主要依赖 PyQt6 和 WebEngine。

```bash
pip install PyQt6 PyQt6-WebEngine

```

### 3. 运行程序

由于 WebEngine 的安全策略，无法直接通过 `file://` 协议加载复杂的本地资源，因此需要先启动本地服务器。

**步骤 1：启动本地静态文件服务器**

```bash
python server.py
```
保持该窗口运行，或使其在后台运行。默认监听 [http://127.0.0.1:53421](http://127.0.0.1:53421)

**步骤 2：启动主程序**

```bash
python app.py

```

## 🎮 使用指南 (Usage)

### 基础操作

* **拖动**：按住鼠标左键可拖动桌宠位置（需在 **未锁定** 且 **未开启穿透** 状态下）。
* **交互**：点击角色不同部位（身体、眼睛等）触发反应。

### 鼠标穿透模式 (Click Through)

* **开启方法**：
1. 右键点击角色 -> 勾选 **"鼠标穿透"**。
2. 或右键点击系统托盘图标 -> 勾选 **"鼠标穿透"**。


* **功能效果**：开启后，鼠标点击将无视角色窗口，直接点击到后面的网页或程序。窗口将**强制置顶**并**锁定位置**。
* **如何关闭**：**注意！** 开启穿透后无法通过点击角色唤出菜单。**必须右键点击系统托盘图标**，取消勾选 "鼠标穿透" 才能恢复交互。

### 菜单功能

* **右键角色**：
* **切换角色**：选择不同的角色和服装。
* **锁定位置**：固定窗口，防止误拖动。
* **布局设置**：手动调整模型缩放大小和渲染偏移。


* **系统托盘**：
* **双击**：快速隐藏/显示桌宠。
* **右键**：全局控制（包含在无法点击角色时的紧急控制）。



## 🐛 已知问题 (Known Issues)

* **头部交互无反馈**：目前点击角色的头部区域（Head）时，可能无法正常触发预设的动作或语音反馈，计划在下一个版本中修复。

## 📜 开源许可 (License)

本项目遵循 **AGPL v3** 开源协议。

> **根据 AGPL v3 许可，修改后的版本请一并开源并使用相同许可证。**
> (According to the AGPL v3 license, modified versions must be open-sourced and use the same license.)

## ⚠️ 免责声明 (Disclaimer)

本项目仅供编程学习与技术研究使用。
项目中涉及的角色模型、语音及相关美术资源（如《Nekopara》系列）版权归原作者 **NEKO WORKs** 所有。请勿将本项目用于商业用途。

---

### 📝 开发日志

* **v1.0.0**:
* 初始版本发布。支持基础交互、眼动追踪、托盘管理及配置持久化。
* 整合 FreeMote-SDK 与 NekoWebShow 核心逻辑。
