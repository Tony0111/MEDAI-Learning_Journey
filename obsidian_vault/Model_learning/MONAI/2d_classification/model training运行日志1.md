### 本日志主要研究参数
optimizer 1e-5
num_workers = 0

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

### 运行后总结

- `optimizer = 1e-5` 比 `optimizer = 1e-3` 整体运行速度更快，但是不知道原因
- `num_workers = 0` 单线程工作，可以正常工作；`num_workers = 2` 多线程工作，就无法工作了。

### 问题

- 运行时发现 `cpu` 运行正常，大约在 `10% - 20%`，但是 `gpu` 运行不正常，仅仅 `< 5%` 

### 希望指导

- 首先解决 `gpu` 问题，然后评价我的运行后总结，并解决其中我的问题
