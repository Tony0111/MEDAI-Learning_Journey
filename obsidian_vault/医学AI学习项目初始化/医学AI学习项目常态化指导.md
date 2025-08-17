---
title: 医学AI学习项目常态化指导
created: 2025-08-17
source: Cherry Studio
tags: 
---
## 🤖 Assistant

没问题！下面是你作为一名使用 Git 进行版本控制的开发者，常态化的工作流程，用 Markdown 格式清晰地呈现出来：

---
---
---


**建议使用VScode中的插件，更方便，更无脑**

---
---
---


# Git 常态化工作流程指南

## 1. 状态检查 (Status Check)

**目的：** 了解当前代码库的状态，是否有未提交的更改、哪些文件被修改了等。

**命令：**

```bash
git status
```

**说明：**
* 这是你最常用的命令，几乎在每次操作前都应该执行一遍。
* 它会告诉你：
 * 你的分支（例如 `On branch main`）。
 * 哪些文件是 `modified` (已修改但未暂存)。
 * 哪些文件是 `untracked` (新增了但 Git 还没有开始管理)。
 * 哪些文件是 `changes to be committed` (已添加到暂存区，等待提交)。

## 2. 拉取最新更新 (Pull Latest Updates)

**目的：** 从远程仓库（如 GitHub）获取最新的代码和提交，确保你的本地版本是最新的，避免与团队成员的代码发生冲突。

**命令：**

```bash
git pull origin <your-branch-name>
```

**示例（如果你在 `main` 分支）：**

```bash
git pull origin main
```

**说明：**
* `origin` 是你远程仓库的默认名字。
* `<your-branch-name>` 是你当前所在的分支，通常是 `main` 或 `develop`。
* **在开始新工作或提交新代码之前，强烈建议先执行一次 `git pull`**，以合并远程的最新更改。
* **如果 `git pull` 提示有冲突** (`conflicts`)：
 1. Git 会告诉你哪些文件有冲突。
 2. 打开冲突文件，你会看到 `<<<<<<< HEAD`, `========`, `>>>>>>> origin/<your-branch-name>` 这样的标记。
 3. 手动编辑文件，删除这些标记，并根据你的需求保留代码。
 4. 保存文件。
 5. 使用 `git add .` 将解决冲突后的文件添加到暂存区。
 6. **然后执行 `git commit` 来提交合并操作。**

## 3. 添加更改到暂存区 (Add Changes to Staging Area)

**目的：** 选择你想包含在下一次提交中的具体文件。Git 的提交是基于“快照”的，你需要先告诉 Git 你要“拍下”哪些文件的当前状态。

**命令：**

* **添加所有已修改和新增的文件：**
```bash
    git add .
    ```
    （注意：`.` 表示当前目录及其所有子目录）

*   **添加特定文件：**
    ```bash
    git add <file1> <file2> ...
    ```
    例如：
    ```bash
    git add README.md src/main.py
    ```

*   **添加所有修改过的文件（不包括新文件）：**
    ```bash
    git add -u
    ```

**说明：**
*   执行 `git status`，你会看到被 `git add` 的文件会从 `modified` 状态转变为 `changes to be committed`。

## 4. 提交更改 (Commit Changes)

**目的：** 将暂存区的代码更改记录为一个“提交” (commit)，并附带一个清晰的提交信息(commit message)，描述这次更改的内容。

**命令：**

```bash
git commit -m "你的清晰的提交信息"
```

**示例：**

```bash
git commit -m "feat: Add user authentication module"
git commit -m "fix: Resolve bug in login form validation"
git commit -m "docs: Update README with installation instructions"
```

**说明：**
*   **编写有意义的提交信息至关重要！** 好的提交信息应该简明扼要地说明“是什么”和“为什么”。
    *   **风格建议 (Conventional Commits)：**
        *   `feat:`: 新功能。
        *   `fix:`: 修复 bug。
        *   `docs:`: 文档更改。
        *   `style:`: 代码风格（例如，不影响逻辑的格式化）。
        *   `refactor:`: 代码重构（不添加新功能或修复 bug）。
        *   `perf:`: 性能优化。
        *   `test:`: 添加测试。
        *   `chore:`: 其他不修改源代码或测试文件的任务（例如，构建过程的更新）。
        *   `BREAKING CHANGE:`: 如果你的提交引入了不兼容的 API 更改。
    *   **格式：**
        ```
        <type>(<scope>): <subject>

        <body>

        <footer>
        ```
        *   `<type>`: 上述类型之一。
        *   `<scope>`: （可选）影响范围，例如 `auth`, `api`, `ui`。
        *   `<subject>`: 简洁的修改摘要，通常不超过 50 个字符，首字母大写，结尾不加句号。
        *   `<body>`: （可选）详细描述。
        *   `<footer>`: （可选）链接到 issue 编号，例如 `Closes #123`。

*   **如果你想编辑一个很久以前的提交信息**，可以使用 `git commit --amend`，但请谨慎使用，尤其是在已经推送到远程分支后。

## 5. 推送提交到远程仓库 (Push Commits to Remote Repository)

**目的：** 将你本地的提交上传到远程仓库，与团队成员共享你的代码。

**命令：**

```bash
git push origin <your-branch-name>
```

**示例（如果你在 `main` 分支）：**

```bash
git push origin main
```

**说明：**
* 首次为一个新分支推送时，可以使用 `-u` 参数（`--set-upstream`）来关联本地分支和远程分支：
 ```bash
 git push -u origin <your-branch-name>
 ```
 这样以后你就可以直接使用 `git push` 而无需指定 `origin <your-branch-name>` 了。

* **如果你在推送时遇到 `rejected` (non-fast-forward) 错误**，意味着远程分支比你本地的先进。此时，请**优先执行 `git pull`**，解决冲突后再 `git push`。
* **如果你确信要覆盖远程的更改**（例如，你在一个私人分支上做了一些修改，并且不想保留远程的任何内容，或者是在处理 `unrelated histories` 的情况），可以使用：
 ```bash
 git push --force-with-lease origin <your-branch-name>
 ```
 （**强烈建议使用 `--force-with-lease` 而不是 `--force`**，它更安全，不会覆盖掉其他人可能在你拉取后推送的更改。）

## 6. 创建新分支 (Create New Branch)

**目的：** 在不影响主线（如 `main` 或 `develop`）的情况下，开发新功能、尝试新想法或修复 bug。

**命令：**

1. **切换到你想基于其创建新分支的分支（通常是 `main` 或 `develop`）：**
 ```bash
 git checkout main
 ```
 或者
 ```bash
 git checkout develop
 ```

2. **拉取最新更新（确保你的基准分支是最新的）：**
 ```bash
 git pull origin main # 或 git pull origin develop
 ```

3. **创建并切换到新分支：**
 ```bash
 git checkout -b <new-branch-name>
 ```
 **示例：**
 ```bash
 git checkout -b feature/user-profile
 ```
 或者
 ```bash
 git checkout -b bugfix/login-validation
 ```

**说明：**
* **分支命名规范：**
 * `feature/` : 用于开发新功能。
 * `bugfix/` : 用于修复 bug。
 * `hotfix/` : 用于紧急修复生产环境问题（通常直接从 production tag 创建）。
 * `docs/` : 用于文档相关的更改。
 * “/” 可以用于分类。

## 7. 合并分支 (Merge Branches)

**目的：** 将一个分支的更改合并到另一个分支。

**命令：**

1. **先切换到你想要合并到的目标分支**（例如，你想把 `feature/user-profile` 合并到 `main`）：
 ```bash
 git checkout main
 ```

2. **执行合并：**
 ```bash
 git merge <branch-to-merge-from>
 ```
 **示例：**
 ```bash
 git merge feature/user-profile
 ```

**说明：**
* **如果合并过程中有冲突**，按照“2. 拉取最新更新”中提到的冲突解决步骤进行处理：
 1. 编辑冲突文件。
 2. `git add .`
 3. `git commit` (Git 会为合并创建一个新的 commit)。

## 8. 撤销操作 (Undoing Actions)

**目的：** 撤销某些不希望提交的更改。

* **撤销暂存区（`git add` 后的更改，但未提交）：**
 ```bash
 git reset HEAD <file>
 ```
 * `git reset HEAD .` 撤销所有已暂存的更改。

* **撤销工作区（`modified` 状态）的更改（谨慎！这个会丢失你的本地修改**）：
 ```bash
 git checkout -- <file>
 ```
 * `git checkout -- .` 撤销所有未暂存的更改。

* **撤销上一次的提交（保留工作区更改，但会从历史中移除提交）：**
 ```bash
 git reset HEAD~1
 ```
 （如果在推送到远程之前使用，可以在本地安全地修改提交并将内容重新 `git add` 后 `git commit`）。

* **撤销上一次的提交（并且不保留工作区更改）：**
 ```bash
 git reset --hard HEAD~1
 ```
 （**谨慎使用！这会丢失你本地的最近一次 commit 和其工作区的所有更改！**）

* **写好提交信息后，但发现有错误，想修改提交信息和/或本次提交的文件：**
 ```bash
 git commit --amend
 ```
 （这会让你重新编辑提交信息，或者添加新的文件/修改已有文件到本次提交。**如果这个提交已经推送到远程，慎用！**）

## 9. 查看历史和其他信息

* **查看提交历史：**
 ```bash
 git log
 ```
 * `git log --oneline`: 以简洁的单行格式显示。
 * `git log --graph --decorate --oneline --all`: 以图示方式显示所有分支和提交。

* **查看文件修改详情：**
 ```bash
 git diff
 ```
 * `git diff <file>`: 查看特定文件的修改（工作区 vs. 暂存区）。
 * `git diff --staged`: 查看暂存区 vs. 上一次提交。
 * `git diff HEAD~1`: 查看上一次提交 vs. 工作区。

* **查看远程仓库列表：**
 ```bash
 git remote -v
 ```

---

### 总结一下你日常会做的主要事项：

1. **写代码。 (Work on your code)**
2. **提交前，检查状态：** `git status`
3. **提交前，拉取最新：** `git pull origin <your-branch-name>` (必要时处理冲突)
4. **添加要提交的文件：** `git add .` (或 `git add <file>`)
5. **提交更改：** `git commit -m "feat: ..."`
6. **将本地提交推送到远程：** `git push origin <your-branch-name>`

**当你想开启一个新任务时：**

1. **在 `main` 或者 `develop` 分支上：**
 * `git checkout main`
 * `git pull origin main`
2. **创建新分支：**
 * `git checkout -b <new-feature-or-bugfix-branch>`
3. **然后按照上面的 1-6 步骤进行开发和提交。**
