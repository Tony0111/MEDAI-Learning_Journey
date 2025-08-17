---
title: conda常用指令
created: 2025-08-15
source: Cherry Studio
tags: 
---
## 🤖 Assistant

好的，这是一份简洁明了的 Conda 指令说明文档，适用于 Windows 系统：

---

## Conda 指令说明文档 (Windows)

Conda 是一个强大的包管理器和环境管理器，尤其适用于数据科学和机器学习项目。

### 在什么环境下使用？

**推荐使用 `Anaconda Prompt` 或 `Miniconda Prompt`**。

* **Anaconda Prompt/Miniconda Prompt:**
 * 这些是预设了 Conda 环境变量的终端。
 * 您看到提示符的开头会有 `(base)` 字样，表示当前在 base 环境中。
 * 直接在这里输入 Conda 指令即可。

* **PowerShell / CMD:**
 * 如果要在普通 PowerShell 或 CMD 中使用 Conda，您需要确保 Conda 的环境变量已正确添加到系统的 PATH 中，或者使用 `conda init powershell`/`conda init cmd.exe` 进行初始化。
 * **但最简单的方式还是直接打开 `Anaconda Prompt`。**

---

### 常用指令

#### 1. 创建虚拟环境 (指定 Python 版本)

* **指令:** `conda create --name <环境名称> python=<Python版本>`
* **示例:** 创建一个名为 `myenv` 的虚拟环境，并指定 Python 版本为 3.9：
 ```bash
 conda create --name myenv python=3.9
 ```
* **解释:**
 * `--name <环境名称>`：为您的新环境指定一个独特的名称。
 * `python=<Python版本>`：指定您想要在该环境中安装的 Python 版本。您可以指定精确的版本号（如 `3.9.12`）或主要版本（如 `3.9`）。

#### 2. 显示有哪些虚拟环境

* **指令:** `conda env list` 或 `conda info --envs`
* **示例:**
 ```bash
 conda env list
 ```
* **输出解读:**
 * 会列出所有 Conda 环境的名称及其对应的路径。
 * 当前激活的环境会有一个星号 `*` 标记。

#### 3. 激活虚拟环境

* **指令:** `conda activate <环境名称>`
* **示例:** 激活名为 `myenv` 的环境：
 ```bash
 conda activate myenv
 ```
* **激活后:** 命令行提示符的开头会显示 `(myenv)`，表示您已成功进入该环境。

#### 4. 关闭虚拟环境

* **指令:** `conda deactivate`
* **示例:**
 ```bash
 conda deactivate
 ```
* **效果:** 将您从当前激活的环境（如 `(myenv)`）切换回 `(base)` 环境或之前的环境。
* **注意:** 如果您在 `Anaconda Prompt` 中，它会自然地从 `(myenv)` 变回 `(base)`。

#### 5. 删除虚拟环境

* **指令:** `conda remove --name <环境名称> --all`
* **示例:** 删除名为 `myenv` 的环境：
 ```bash
 conda remove --name myenv --all
 ```
* **解释:**
 * `--name <环境名称>`：指定要删除的虚拟环境的名称。
 * `--all`：表示删除该环境及其包含的所有包。
* **确认:** Conda 会询问您是否确认删除，输入 `y` 并回车即可。

---

**小贴士:**

* 在激活某个环境后，您就可以在该环境下使用 `pip install <包名>` 来安装 PyTorch、Monai 等库了。
* 通常，您的项目应该在一个独立的虚拟环境中进行，以避免不同项目之间的库版本冲突。

希望这份文档对您有帮助！
