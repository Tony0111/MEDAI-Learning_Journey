---
created: 2025-08-17
---
### 第一次尝试

运行一下代码时发生问题
```
tonyx@_▒▒__ MINGW64 /d/MEDAI-Learning-Project (main)
$ git add .
```

以下时反馈结果

```
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'medai_project_structure.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/2d_segmentation/unet_evaluation_array.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/2d_segmentation/unet_evaluation_dict.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/2d_segmentation/unet_training_array.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/2d_segmentation/unet_training_dict.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/3d_classification/densenet_training_array.ipynb', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/3d_classification/ignite/densenet_evaluation_array.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/3d_classification/ignite/densenet_evaluation_dict.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/3d_classification/ignite/densenet_training_array.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/3d_classification/ignite/densenet_training_dict.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/3d_classification/torch/densenet_evaluation_array.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/3d_classification/torch/densenet_evaluation_dict.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/3d_classification/torch/densenet_training_array.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/3d_classification/torch/densenet_training_dict.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/DenseNet121/data/MedNIST/README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'models/MONAI/DenseNet121/mednist_tutorial.ipynb', LF will be replaced by CRLF the next time Git touches it
warning: adding embedded git repository: models/MONAI/MONAI
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint:
hint:   git submodule add <url> models/MONAI/MONAI
hint:
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint:
hint:   git rm --cached models/MONAI/MONAI
hint:
hint: See "git help submodule" for more information.
hint: Disable this message with "git config set advice.addEmbeddedRepo false"
warning: in the working copy of 'obsidian_vault/.obsidian/appearance.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/.obsidian/community-plugins.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/.obsidian/core-plugins.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/.obsidian/plugins/calendar/data.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/.obsidian/plugins/calendar/main.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/.obsidian/plugins/calendar/manifest.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/.obsidian/plugins/obsidian-markdown-formatting-assistant-plugin/data.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/.obsidian/plugins/obsidian-markdown-formatting-assistant-plugin/main.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/.obsidian/plugins/quick-latex/main.js', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/.obsidian/templates.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/.obsidian/workspace.json', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/API Keys.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/MONAI/2d_classification/model training优化.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/MONAI/2d_classification/model training认识深化.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/MONAI/2d_classification/model training运行日志1.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/MONAI/2d_classification/model training运行日志1反馈.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/MONAI/2d_classification/model training运行日志2.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/MONAI/2d_segmentation/MONAI 2D分割学习指南.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/MONAI/2d_segmentation/二维分割运行日志1.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/MONAI/MONAI_Dataset.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/VSCode GPU调用测 试/VSCode GPU调用测试.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/VSCode GPU调用测 试/VSCode GPU调用测试2.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/VSCode GPU调用测 试/VSCode GPU调用测试日志.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/VSCode GPU调用测 试/VSCode GPU调用测试日志2.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Model_learning/conda常用指令.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Paper_Reviews/medical_image_analyze/App_of_AI_form2009to2024_阅读分析1_20250816_152208.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Paper_Reviews/medical_image_analyze/App_of_AI_form2009to2024_阅读分析_20250816_153301.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Paper_Reviews/medical_image_analyze/translated_result.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Paper_Reviews/medical_image_analyze/研究日志.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Paper_Reviews/文档结构快速搭建.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Paper_Reviews/社交恐惧/translated_result.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Paper_Reviews/社交恐惧/序号.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/Templates/笔记.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'obsidian_vault/medai_project_structure.md', LF will be replaced by CRLF the next time Git touches it
error: short read while indexing obsidian_vault/医学AI学习项目初始化.md
error: obsidian_vault/医学AI学习项目初始化.md: failed to insert into database
error: unable to index file 'obsidian_vault/医学AI学习项目初始化.md'
fatal: adding files failed

tonyx@_▒▒__ MINGW64 /d/MEDAI-Learning-Project (main)
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        medai_project_structure.md
        models/
        obsidian_vault/
        scripts/

nothing added to commit but untracked files present (use "git add" to track)

```

### 第二次尝试

在处理 `warning: adding embedded git repository` 时出现问题
运行代码为
```
git rm --cached -r models/MONAI/MONAI
```

结果是

```
error: the following file has staged content different from both the
file and the HEAD:
    models/MONAI/MONAI
(use -f to force removal)
```

如果运行
```
git rm --cached -f models/MONAI/MONAI
```

结果为
```
rm 'models/MONAI/MONAI'
```

MONAI原项目地址是
```
https://github.com/Project-MONAI/MONAI.git
```
