---
title: model training优化
created: 2025-08-15
source: Cherry Studio
tags: 
---
## 🤖 Assistant

CPU 占用率不到 5%，GPU 占用率也不到 5%？这确实非常低，表明您的训练过程几乎处于停滞状态。这已经远超了“缓慢”的范畴，更像是卡住或根本没有有效运行。

这种情况通常指向几个更深层的问题。让我们来系统地排查：

---

### 1. 核心问题：数据加载并行化与主循环的死锁/停滞

CPU 和 GPU 都低占用率，最常见的解释是：
* **DataLoader 的 `.__getitem__()` 方法存在问题，导致死锁或无限等待**：当 `num_workers > 0` 时，主进程在 `for batch_data in train_loader:` 循环中会等待 DataLoader 准备好数据。如果 DataLoader 的某个部分（例如，`__getitem__` 中的某个操作）卡住了，整个训练就会停滞。
* **主训练循环的启动问题**：虽然不太可能，但也有可能是 PyTorch 的训练循环本身在代码的某个地方卡住。
* **VS Code 的环境隔离问题**：某些 VS Code 的扩展或设置可能干扰到 Python 进程的正常执行。

---

### 2. 详细排查与解决方案

#### 2.1. **彻底检查 DataLoader 和 Transforms**

**这是目前最可疑的环节。**

* **解决方案 - 隔离测试 `DataLoader`**：
 1. **尝试 `num_workers=0`**：
 这是最安全、最直接的诊断步骤。将 `num_workers` 设置为 0，表示数据加载将在主进程中同步进行。这会牺牲一部分数据加载效率，但能非常有效地判断 DataLoader 是否是问题的根源。
 ```python
 # 尝试 num_workers=0
 train_loader = DataLoader(train_ds, batch_size=300, shuffle=True, num_workers=0)
 val_loader = DataLoader(val_ds, batch_size=300, num_workers=0)
 test_loader = DataLoader(test_ds, batch_size=300, num_workers=0)
 ```
 * **观察**：如果设置 `num_workers=0` 后，CPU 和 GPU 占用率能正常（CPU 变高，GPU 变高），并且训练速度恢复，那么问题就出在 `num_workers > 0` 时的多进程数据加载环节。
 * **如果 `num_workers=0` 后仍然卡住**：说明瓶颈不在多进程，而是 `__getitem__` 的内容本身，或者主循环。

运行结果
```
12m 1.1s
---------- epoch 1/4 1/157, train_loss: 1.8068 2/157, train_loss: 0.8542 3/157, train_loss: 0.4919 4/157, train_loss: 0.2516 5/157, train_loss: 0.1245 6/157, train_loss: 0.1059 7/157, train_loss: 0.1750 8/157, train_loss: 0.1102 9/157, train_loss: 0.1167 10/157, train_loss: 0.0549 11/157, train_loss: 0.0626 12/157, train_loss: 0.0640 13/157, train_loss: 0.0344 14/157, train_loss: 0.0606 15/157, train_loss: 0.0948 16/157, train_loss: 0.0326 17/157, train_loss: 0.0113 18/157, train_loss: 0.0252 19/157, train_loss: 0.0910 20/157, train_loss: 0.1226 21/157, train_loss: 0.0572 22/157, train_loss: 0.0186 23/157, train_loss: 0.0446

...

158/157, train_loss: 0.0258 epoch 4 average loss: 0.0050 current epoch: 4 current AUC: 1.0000 current accuracy: 0.9841 best AUC: 1.0000 at epoch: 3 train completed, best_metric: 1.0000 at epoch: 3
```

optimizer 1e-5
num_workers = 0
```
9m 57.5s
---------- epoch 1/4 1/157, train_loss: 1.8068 2/157, train_loss: 1.7499 3/157, train_loss: 1.7304 4/157, train_loss: 1.7317 5/157, train_loss: 1.6639 6/157, train_loss: 1.6366 7/157, train_loss: 1.6334 8/157, train_loss: 1.5917 9/157, train_loss: 1.5928 10/157, train_loss: 1.5605 11/157, train_loss: 1.5266 12/157, train_loss: 1.5147 13/157, train_loss: 1.4861 14/157, train_loss: 1.4724 15/157, train_loss: 1.4434 16/157, train_loss: 1.4170 17/157, train_loss: 1.3985 18/157, train_loss: 1.3872 19/157, train_loss: 1.3451 20/157, train_loss: 1.3483 21/157, train_loss: 1.3232 22/157, train_loss: 1.2767 23/157, train_loss: 1.2681

...

epoch 4 average loss: 0.0390 saved new best metric model current epoch: 4 current AUC: 1.0000 current accuracy: 0.9951 best AUC: 1.0000 at epoch: 4 train completed, best_metric: 1.0000 at epoch: 4
```
![[Pasted image 20250815104413.png]]

第二次尝试：
optimizer 1e-5
num_workers = 0
```
10m 38.8s
---------- epoch 1/4 1/157, train_loss: 1.8068 2/157, train_loss: 1.7499 3/157, train_loss: 1.7304 4/157, train_loss: 1.7317 5/157, train_loss: 1.6639 6/157, train_loss: 1.6366 7/157, train_loss: 1.6334 8/157, train_loss: 1.5917 9/157, train_loss: 1.5928 10/157, train_loss: 1.5605 11/157, train_loss: 1.5266 12/157, train_loss: 1.5147 13/157, train_loss: 1.4861 14/157, train_loss: 1.4724 15/157, train_loss: 1.4434 16/157, train_loss: 1.4170 17/157, train_loss: 1.3985 18/157, train_loss: 1.3872 19/157, train_loss: 1.3451 20/157, train_loss: 1.3483 21/157, train_loss: 1.3232 22/157, train_loss: 1.2767 23/157, train_loss: 1.2681

...

epoch 4 average loss: 0.0390 saved new best metric model current epoch: 4 current AUC: 1.0000 current accuracy: 0.9951 best AUC: 1.0000 at epoch: 4 train completed, best_metric: 1.0000 at epoch: 4
```

![[Pasted image 20250815105843.png]]


optimizer 1e-3
num_workers = 0
```
24m 15.5
---------- epoch 1/4 1/157, train_loss: 1.8068 2/157, train_loss: 0.8542 3/157, train_loss: 0.4919 4/157, train_loss: 0.2516 5/157, train_loss: 0.1245 6/157, train_loss: 0.1059 7/157, train_loss: 0.1750 8/157, train_loss: 0.1102 9/157, train_loss: 0.1167 10/157, train_loss: 0.0549 11/157, train_loss: 0.0626 12/157, train_loss: 0.0640 13/157, train_loss: 0.0344 14/157, train_loss: 0.0606 15/157, train_loss: 0.0948 16/157, train_loss: 0.0326 17/157, train_loss: 0.0113 18/157, train_loss: 0.0252 19/157, train_loss: 0.0910 20/157, train_loss: 0.1226 21/157, train_loss: 0.0572 22/157, train_loss: 0.0186 23/157, train_loss: 0.0446

...

158/157, train_loss: 0.0258 epoch 4 average loss: 0.0050 current epoch: 4 current AUC: 1.0000 current accuracy: 0.9841 best AUC: 1.0000 at epoch: 3 train completed, best_metric: 1.0000 at epoch: 3
```
![[Pasted image 20250815112713.png]]

optimizer 1e-5
num_workers = 2
即使时间过去13min，仍毫无输出
```
---------- epoch 1/4
```


 2. **逐步检查 Transforms**：
 * **删除所有 Transforms**：
 ```python
 # 仅加载图像
 train_transforms_minimal = Compose([LoadImage(image_only=True), EnsureChannelFirst()])
 val_transforms_minimal = Compose([LoadImage(image_only=True), EnsureChannelFirst()])
 test_transforms_minimal = Compose([LoadImage(image_only=True), EnsureChannelFirst()])

 train_ds_minimal = MedNISTDataset(train_x, train_y, train_transforms_minimal)
 train_loader_minimal = DataLoader(train_ds_minimal, batch_size=300, shuffle=True, num_workers=0) # 使用 num_workers=0 诊断

 # 运行一小段，看是否能前进
 print("Testing minimal transforms...")
 for batch_data in train_loader_minimal:
 print("Batch loaded successfully. Exiting test.")
 break # 只加载一个 batch
 ```
 如果这都能卡住，问题非常严重，可能是文件读取本身有问题，或者 VS Code 环境。
 * **逐个添加 Transforms**：如果 `Minimal` 版本工作正常，则逐个添加 `ScaleIntensity`, `RandRotate`, `RandFlip`, `RandZoom`，观察哪一步会引入停滞。

 3. **检查 `MedNISTDataset.__getitem__`**：
 确保 `__getitem__` 内部没有意外的 `.item() Called outside of a Python GIL` 错误，或者其他状态修改导致的问题。这里的实现 (`return self.transforms(self.image_files[index]), self.labels[index]`) 是标准的，应该没问题。

#### 2.2. **检查 PyTorch 模型本身**

* **前向传播问题**：
 * **解决方案**：在 `for batch_data in train_loader:` 循环内部，只执行数据加载，**暂时跳过模型前向传播和反向传播**，看程序是否能顺利迭代完一个 DataLoader 的所有 batch。
 ```python
 # 仅用于诊断
 # 假设 'inputs' 和 'labels' 已经从 batch_data 中获取
 # inputs, labels = batch_data[^0].to(device), batch_data[^1].to(device)
 # 暂时跳过模型相关操作
 # outputs = model(inputs)
 # loss = loss_function(outputs, labels)
 # ...
 ```
 如果跳过模型操作后，DataLoader 可以迭代，说明问题出在 `model(inputs)` 或其后的反向传播/优化步骤。
 * **CPU/GPU 之间的 tensor 移动**：
 确保 `inputs` 和 `labels` 移动到 device 的操作 (`.to(device)`) 是正确的。

#### 2.3. **VS Code 和环境隔离**

* **问题原因**：VS Code 的了一些扩展（例如，Python 扩展的问题，Jupyter 扩展如果 Notebook 运行在这种模式下）可能会干扰进程的通信，尤其是在涉及多进程 (`num_workers`) 的时候。
* **解决方案**：
 * **尝试在纯 Python 终端运行**：脱离 VS Code 的 Notebook 或 Debugger 环境，直接在 VS Code 集成的 Python 终端中运行 `.py` 文件。
 ```bash
 # 假设你的训练代码保存为 train.py
 python train.py
 ```
 如果纯 Python 脚本能正常运行，说明 VS Code Notebook 或其它的集成环境是问题所在。
 * **禁用 VS Code 扩展**：尝试禁用一些可能与 Python 进程管理或远程开发相关的 VS Code 扩展，然后重新尝试。
 * **清理 VS Code 缓存**：有时 VS Code 的缓存问题也可能导致奇怪的行为。
 * **检查 Python 解释器设置**：确保 VS Code 使用的是您期望的、包含 GPU PyTorch 的 Conda 或虚拟环境。

#### 2.4. **内存泄露或死锁诊断**

* **问题原因**：如果训练过程中在某个点卡住，并且资源占用率都很低，可能是内存泄露导致系统最终无响应，或者某种逻辑死锁。
* **解决方案**：
 * **逐步打印信息**：在训练循环的每个小步骤 `step` 处，打印一些信息，看它能进展到哪一步。
 * **使用 PyTorch Profiler (更高级)**：如果上述诊断方法都无法定位，可以考虑使用 `torch.profiler` 来详细分析代码的执行时间和瓶颈。

---

### 针对您情况的建议（优先级排序）：

1. **`num_workers=0` 诊断**：这是最重要的一步。
 * **如果 `num_workers=0` 后速度正常**：问题在多进程 DataLoader。您需要仔细审查 `DataLoader` 的设置，或者尝试调整 `num_workers` 的值（比如 2、4），或者检查 MONAI Transforms 的 CPU/GPU 依赖。
 * **如果 `num_workers=0` 后仍然卡住**：问题在 `__getitem__` (transforms) 或主循环。
2. **逐步移除 Transforms**：使用 `num_workers=0` 后，再尝试移除所有随机 transforms，看是否能执行。
3. **隔离主循环**：在 `train_loader` 循环中，仅执行数据加载，跳过模型计算，看是否能前进。
4. **在纯 Python 终端运行**：排除 VS Code 集成环境的影响。

**请务必先设置 `num_workers=0` 进行测试。** 如果这解决了问题，我们再进一步分析是为何多进程会产生问题；如果没解决，我们再继续深入检查 Transforms 和主循环。
