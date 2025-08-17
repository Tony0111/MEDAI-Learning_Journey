---
created: 2025-08-17
---

---
## 🤖 Assistant

太棒了！学习 Git 是版本控制和项目管理的重要一步。下面我将一步一步地指导你如何使用 Git 管理你的项目。

**在你开始之前，请确保你已经在大约 200 字左右的描述中，提到了你的项目是关于“医学生学习与医学相关的AI内容，或学习科研方法”的。**

---

### 步骤 1：安装 Git

如果你还没有安装 Git，你需要先安装它。

1. **访问 Git 官网**：前往 [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. **下载适合你操作系统的版本**：
 * Windows 用户：下载 `.exe` 安装程序。
 * macOS 用户：通常已经预装，如果没有，可以访问官网下载，或者通过 Homebrew (`brew install git`) 安装。
 * Linux 用户：大多数发行版可以通过包管理器安装，例如 Debian/Ubuntu (`sudo apt update && sudo apt install git`)，Fedora (`sudo dnf install git`)。
3. **安装过程**：
 * **Windows**：一路点击“Next”，使用默认选项安装即可。在安装过程中，关于“Adjusting your PATH environment”的选项，选择“Git from the command line and also from 3rd-party software”是最灵活的，这样你就可以在任何命令行中使用 Git。
 * **macOS/Linux**：通常通过终端命令安装。
4. **验证安装**：打开你的终端（Windows 上是 Git Bash、CMD 或 PowerShell；macOS/Linux 上是 Terminal），输入以下命令：
 ```bash
 git --version
 ```
 如果安装成功，它会显示你安装的 Git 版本号，例如 `git version 2.39.1`。

---

### 步骤 2：配置 Git 用户信息

Git 需要知道你是谁，以便在提交记录中标记你的名字和邮箱。

1. **打开终端**。
2. **设置你的用户名**（替换 `"你的名字"` 为你的实际名字），使用 `-global` 表示这个配置对你系统上的所有 Git 项目都生效：
 ```bash
 git config --global user.name "Tony0111"
 ```
3. **设置你的邮箱**（替换 `"你的邮箱@example.com"` 为你常用的邮箱）：
 ```bash
 git config --global user.email "tonyxu0111@gamil.com"
 ```
4. **验证配置**：
 ```bash
 git config --global user.name
 git config --global user.email
 ```
 这两条命令应该会输出你刚刚设置的值。

---

### 步骤 3：创建或初始化一个 Git 仓库

你的项目需要被 Git “跟踪”起来，这叫做创建一个 Git 仓库（repository）。

**场景 A：你已经有了一个项目文件夹，想开始用 Git 管理**

1. **打开终端**。
2. **进入你的项目文件夹**。假设你的项目文件夹叫做 `medai_project`，并且它在 `D:\Projects\` 目录下（Windows）或者 `~/Projects/` (macOS/Linux)。你需要 `cd`（change directory）到这个文件夹：
 * **Windows 示例**：
 ```bash
 cd D:\MEDAI-Learning-Project
 ```
  
1. **初始化 Git 仓库**：在你进入项目文件夹后，运行以下命令：
 ```bash
 git init
 ```
 这会在你的项目文件夹根目录下创建一个名为 `.git` 的隐藏文件夹。这个文件夹包含了 Git 仓库的所有信息。
 你会看到类似 `Initialized empty Git repository in /path/to/your/project/.git/` 的输出。


2. **创建你的 `.gitignore` 文件**：
 在你刚刚初始化 Git 的项目根目录下，创建一个名为 `.gitignore` 的文件，并将你之前提供的（或 GitHub 标准的）内容粘贴进去。
 * **Windows 示例 (使用 `notepad` 编辑)**：
 ```bash
 notepad .gitignore
 ```
 粘贴内容后保存并关闭。

---

### 步骤 4：添加文件到暂存区（Staging Area）

在 Git 中，你不能直接提交所有修改。你需要先将你想提交的文件“暂存”起来。

1. **查看 Git 状态**：在项目根目录下的终端，输入：
 ```bash
 git status
 ```
 你会看到所有尚未被 Git 跟踪的文件，它们会以红色显示。

2. **添加所有文件到暂存区**：
 ```bash
 git add .
 ```
 这里的 `.` 表示当前目录下所有文件（包括子目录下）都被添加到暂存区。
 再次运行 `git status`，你会看到之前红色的文件现在变成了绿色的，表示它们已经被 Git 暂存，准备提交。

 * **如果你只想添加特定文件**：
 ```bash
 git add your_file1.py your_folder/your_file2.ipynb
 ```

3. **检查 `.gitignore` 的作用**：如果你正确配置了 `.gitignore` 文件，那么在运行 `git add .` 后，那些被 `.gitignore` 规则匹配到的文件（如 `.pyc` 文件、`venv/` 目录下的内容等）是不会被添加到暂存区的。

---

### 步骤 5：提交更改（Commit）

暂存区就绪后，你可以将这些文件“提交”到你的本地 Git 仓库。每一次提交都代表你的项目的一个快照。

1. **执行提交**：
 ```bash
 git commit -m "你的提交信息"
 ```
 * `-m` 后面是你的提交信息（commit message）。写一个清晰、概括性的信息非常重要，能帮助你和他人理解这次提交做了什么。
 * **对于第一次提交，一个好的信息可以是**："Initial commit. Set up project structure and added essential files for AI and research methodology learning." (例如：初次提交。设置项目结构并添加了AI和科研方法学习所需的核心文件。)

2. **查看提交历史**：
 ```bash
 git log
 ```
 这条命令会显示你所有的提交记录，包括提交者、提交日期和提交信息。

---

### 步骤 6：创建远程仓库（例如 GitHub, GitLab, Gitee）

到目前为止，你的 Git 仓库只在你本地。为了备份、协作和分享，你需要将你的项目推送到一个远程仓库。

1. **选择一个平台**：最常用的是 GitHub ([github.com](https://github.com/))。你也可以选择 GitLab ([gitlab.com](https://gitlab.com/)) 或 Gitee ([gitee.com](https://gitee.com/))。
2. **注册/登录账号**。
3. **创建一个新的远程仓库**：
 * 在 GitHub 页面，点击右上角的 "+" 号，选择 "New repository"。
 * 给你的仓库起一个名字（例如 `medai-learning-project`）。
 * 可以选择添加一个 `README.md` 文件（如果你刚初始化项目，可以不添加，因为你已经有文件了）。
 * **重要**：**不要**勾选“Initialize this repository with a README”或“Add .gitignore”。因为你本地已经有项目和 `.gitignore` 了。
 * 点击“Create repository”。

4. **复制远程仓库的 URL**：创建成功后，你会看到页面的右侧有一个 URL，通常是 `https://github.com/你的用户名/你的仓库名.git`。复制这个 URL。

---

### 步骤 7：连接本地仓库到远程仓库

现在，你需要告诉你的本地 Git 仓库，它应该和哪个远程仓库进行交互。

1. **回到你的终端（必须在项目根目录下）**。
2. **添加远程仓库**：将你刚刚复制的 URL 替换到下面的命令中：
 ```bash
 git remote add origin https://github.com/你的用户名/你的仓库名.git
 ```
 * `origin` 是远程仓库默认的别名，你可以用其他名字，但 `origin` 最常用。

3. **验证**：
 ```bash
 git remote -v
 ```
 这条命令会显示你所有的远程仓库连接，你应该能看到 `origin` 对应的 fetch (获取) 和 push (推送) 地址。

---

### 步骤 8：将本地的提交推送到远程仓库

这是将你的本地工作上传到远程服务器的关键一步。

1. **推送**：
 ```bash
 git push -u origin main
 ```
 * `push`：命令本身，用于发送本地提交。
 * `-u` (或 `--set-upstream`)：这是一个一次性的参数。它会将你的本地 `main` 分支与远程的 `origin/main` 分支进行关联。之后，你就可以直接使用 `git push` 了。
 * `origin`：你之前添加的远程仓库别名。
 * `main`：这是 Git 的主分支名称（有时也可能是 `master`，如果你创建仓库时不是 `main`，就用对应的名字）。

2. **认证**：如果这是你第一次推送，或者 Git 提示你需要身份验证，它会要求你输入 GitHub 用户名和密码，或者使用 SSH 密钥（更推荐，但设置稍复杂）。如果你使用 HTTPS，输入你的 GitHub 密码即可。
3. **检查**：推送完成后，刷新你的 GitHub（或其他平台）上的仓库页面。你应该能看到你刚刚提交的所有文件和提交记录。

---

### 步骤 9：日常工作流程（添加、提交、推送）

一旦以上步骤完成，你今后的工作流程就会变得非常简单：

1. **写代码，做修改，创建新文件，或删除不需要的文件。**
2. **查看状态**：
 ```bash
 git status
 ```
 了解哪些文件被修改了。
3. **暂存你想要提交的更改**：
 ```bash
 git add .
 # 或者 git add specific_file.py
 ```
4. **提交这些更改**：
 ```bash
 git commit -m "描述你这次提交做了什么"
 ```
 例如："Update README with project goals", "Add initial data preprocessing script", "Refactor model training function".
5. **将你的本地提交推送到远程仓库**：
 ```bash
 git push
 ```
 （由于你之前用了 `-u`，现在可以直接 `git push`）

---

### 常用 Git 命令概览

* `git status`：查看当前工作目录的状态（哪些文件被修改，哪些被暂存）。
* `git add <file>`：将文件添加到暂存区。`git add .` 添加所有。
* `git commit -m "message"`：将暂存区的文件提交到本地仓库，并附带提交信息。
* `git log`：查看提交历史。
* `git push`：将本地的提交推送到远程仓库。
* `git pull`：从远程仓库获取最新的更改，并合并到你的本地分支。
* `git clone <url>`：克隆一个远程仓库到本地。
* `git branch`：列出所有本地分支。
* `git checkout <branch_name>`：切换到另一个分支。
* `git diff`：查看工作目录中未暂存的修改。
* `git diff --staged`：查看已暂存但未提交的修改。

---

**重要提示：**

* **谨慎使用 `git rm -r --cached .`**：这个命令会从 Git 追踪中移除所有文件，但保留你在文件系统中的文件。通常用于清理 Git 仓库，**不是你日常工作需要的**。
* **`.gitignore` 是第一次初始化 Git 时最重要的文件之一**：确保它在你第一次 `git add .` 和 `git commit` 之前就已创建并配置好，这样可以避免很多不必要的添加到仓库的文件。

现在，你就可以开始用 Git 管理你的医学AI学习项目了！祝你学习顺利！
