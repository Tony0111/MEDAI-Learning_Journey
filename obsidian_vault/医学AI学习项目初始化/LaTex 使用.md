---
title: LaTex 使用
created: 2025-08-24
source: 自制
---
## 把notebook转化为lex

```bash
jupyter nbconvert --to latex your_notebook_file.ipynb
```

## 解决中文问题

```latex
\usepackage{ctex}

    % 如果上面那行加了还不行，考虑加上显式字体设置（不带sffamily和ttfamily，只设置mainfont）

    \ctexset{

        % 主字体，用于正文

        mainfont = 'Source Han Serif SC', % 例如：思源宋体

        % 无衬线字体，用于标题、粗体等

        sansfont = 'Source Han Sans SC', % 例如：思源黑体

        % 等宽字体，用于代码

        monofont = 'Consolas' % 或 'Consolas', 'Courier New' 等

    }
```

## 模板

https://www.overleaf.com/latex/templates

