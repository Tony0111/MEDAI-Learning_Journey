### 更新驱动

在英伟达的app上更新了gpu驱动

### 运行测试脚本

```
PS D:\AI> & D:\Apps\Python\python.exe d:/AI/MONAI/DenseNet121/gpu-test.py
D:\Apps\Python\Lib\site-packages\ignite\handlers\checkpoint.py:17: DeprecationWarning: `TorchScript` support for functional optimizers is deprecated and will be removed in a future PyTorch release. Consider using the `torch.compile` optimizer instead.
  from torch.distributed.optim import ZeroRedundancyOptimizer
--- PyTorch GPU Test ---
PyTorch version: 2.5.1+cu118
CUDA available: True
CUDA version: 11.8
Number of GPUs available: 1
GPU 0 name: NVIDIA GeForce RTX 4060 Laptop GPU

--- Tensor to GPU Test ---
Using device: cuda:0
Tensor created on device: cuda:0
Result of operation x * 2 on GPU:
tensor([[-1.1246, -2.7586,  1.1204],
        [-1.5425,  0.2329, -0.2236],
        [-0.9992, -0.3285, -4.7301]], device='cuda:0')
Result moved back to CPU:
tensor([[-1.1246, -2.7586,  1.1204],
        [-1.5425,  0.2329, -0.2236],
        [-0.9992, -0.3285, -4.7301]])
Tensor to GPU movement successful.

--- Monai GPU Test ---

Monai is not installed. Please install Monai (`pip install monai`) to run this part.
```

### pip install monai

根据建议重新安装 monai

```
pip install monai
```

运行结果如下

```
PS D:\AI\MONAI\DenseNet121> pip install monai
Collecting monai
  Downloading monai-1.5.0-py3-none-any.whl.metadata (13 kB)
Requirement already satisfied: numpy<3.0,>=1.24 in d:\apps\python\lib\site-packages (from monai) (2.0.2)
Requirement already satisfied: torch<2.7.0,>=2.4.1 in d:\apps\python\lib\site-packages (from monai) (2.5.1+cu118)
Requirement already satisfied: filelock in d:\apps\python\lib\site-packages (from torch<2.7.0,>=2.4.1->monai) (3.11.0)
Requirement already satisfied: typing-extensions>=4.8.0 in d:\apps\python\lib\site-packages (from torch<2.7.0,>=2.4.1->monai) (4.12.2)
Requirement already satisfied: networkx in d:\apps\python\lib\site-packages (from torch<2.7.0,>=2.4.1->monai) (3.4.2)
Requirement already satisfied: jinja2 in d:\apps\python\lib\site-packages (from torch<2.7.0,>=2.4.1->monai) (3.1.4)
Requirement already satisfied: fsspec in d:\apps\python\lib\site-packages (from torch<2.7.0,>=2.4.1->monai) (2024.12.0)
Requirement already satisfied: setuptools in d:\apps\python\lib\site-packages (from torch<2.7.0,>=2.4.1->monai) (75.6.0)
Requirement already satisfied: sympy==1.13.1 in d:\apps\python\lib\site-packages (from torch<2.7.0,>=2.4.1->monai) (1.13.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in d:\apps\python\lib\site-packages (from sympy==1.13.1->torch<2.7.0,>=2.4.1->monai) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in d:\apps\python\lib\site-packages (from jinja2->torch<2.7.0,>=2.4.1->monai) (2.1.5)
Downloading monai-1.5.0-py3-none-any.whl (2.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 5.1 MB/s  0:00:00
Installing collected packages: monai
Successfully installed monai-1.5.0
```

### 再次运行测试脚本

```
PS D:\AI\MONAI\DenseNet121> & D:\Apps\Python\python.exe d:/AI/MONAI/DenseNet121/gpu-test.py
D:\Apps\Python\Lib\site-packages\ignite\handlers\checkpoint.py:17: DeprecationWarning: `TorchScript` support for functional optimizers is deprecated and will be removed in a future PyTorch release. Consider using the `torch.compile` optimizer instead.
  from torch.distributed.optim import ZeroRedundancyOptimizer
--- PyTorch GPU Test ---
PyTorch version: 2.5.1+cu118
CUDA available: True
CUDA version: 11.8
Number of GPUs available: 1
GPU 0 name: NVIDIA GeForce RTX 4060 Laptop GPU

--- Tensor to GPU Test ---
Using device: cuda:0
Tensor created on device: cuda:0
Result of operation x * 2 on GPU:
tensor([[-0.5390,  0.6643,  2.0060],
        [-0.1554,  1.1972,  0.7340],
        [ 0.0358, -0.1353, -3.4202]], device='cuda:0')
Result moved back to CPU:
tensor([[-0.5390,  0.6643,  2.0060],
        [-0.1554,  1.1972,  0.7340],
        [ 0.0358, -0.1353, -3.4202]])
Tensor to GPU movement successful.

--- Monai GPU Test ---

Monai is not installed. Please install Monai (`pip install monai`) to run this part.
```

输出结果仍然如下，不知道原因何在，请指教