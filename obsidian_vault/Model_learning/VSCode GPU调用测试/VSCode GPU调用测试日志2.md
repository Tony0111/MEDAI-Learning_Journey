### 检查monai

在vscode中检查，有monai和torch

### 确认python编译器相同

已确认安装这两个包的python就是运行脚本的python

### 运行脚本

结果如下

```
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
tensor([[-0.3953,  0.3486,  5.4120],
        [-3.9918,  0.4930,  2.4628],
        [ 0.3383,  1.6465,  2.2519]], device='cuda:0')
Result moved back to CPU:
tensor([[-0.3953,  0.3486,  5.4120],
        [-3.9918,  0.4930,  2.4628],
        [ 0.3383,  1.6465,  2.2519]])
Tensor to GPU movement successful.

--- Monai GPU Test ---
Monai MetaTensor created on: cpu
Monai MetaTensor moved to: cuda:0
Monai MetaTensor is successfully on GPU.
Transformed data device: cuda:0
Monai transform processed data on GPU successfully.
```

看样子是成功！