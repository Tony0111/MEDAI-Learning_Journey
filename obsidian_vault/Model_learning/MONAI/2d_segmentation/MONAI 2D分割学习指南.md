---
title: MONAI 2D分割学习指南
created: 2025-08-16
source: Cherry Studio
tags: 
---
## 🤖 Assistant

非常抱歉，我之前的回答可能造成了误解！你说得对，你提供的 GitHub 链接是 MONAI 2D 分割的教程，但里面的文件数量和我之前理解的不太一样。

你提供的四个 Python 文件分别是：

1. `unet_evaluation_array.py`
2. `unet_evaluation_dict.py`
3. `unet_training_array.py`
4. `unet_training_dict.py`

这些文件实际上已经**包含了训练和评估的完整逻辑**，只是它们被分成了两个主要的任务：**训练**和**评估**，并且针对两种不同的数据处理方式：**Array-based** 和 **Dict-based**。

**核心解释：**

* **`unet_training_array.py` 和 `unet_training_dict.py`:** 这两个文件负责**训练**一个 UNet 模型。
 * `_array` 版本使用了 MONAI 的 Map-style `ArrayDataset`，直接传递 NumPy 数组或 PIL Image 对象。
 * `_dict` 版本使用了 MONAI 的 Map-style `Dataset`，配合 `LoadImaged` 等 Dict-based transforms，处理的是字典形式的数据，键值对会明确定义。
* **`unet_evaluation_array.py` 和 `unet_evaluation_dict.py`:** 这两个文件负责**评估**一个*.pth*文件中保存的、**已经训练好的 UNet 模型**。它们使用与训练文件相对应的加载方式（`_array` 或 `_dict`）来加载模型进行推理，并计算 Dice 指标。

**如何运行这个项目：**

这个项目的代码已经被组织得相当完善，可以直接运行。核心流程是：

1. **生成合成数据**: 代码首先会创建一个临时目录，并生成一些合成的 2D 医学图像和对应的分割掩码。
2. **定义数据加载和预处理**: 根据是 `_array` 还是 `_dict` 版本，会定义相应的 `transforms` 来加载和预处理这些数据。
3. **构建模型**: 定义一个 UNet 模型。
4. **训练模型 (当运行 `_training.py` 文件时)**:
 * 将数据加载到 `DataLoader`。
 * 定义损失函数 (Dice Loss) 和优化器 (Adam)。
 * 执行训练循环：前向传播、计算损失、反向传播、更新参数。
 * 在每个验证间隔，进行模型评估，并保存表现最好的模型（`best_metric_model_segmentation2d_array.pth` 或 `best_metric_model_segmentation2d_dict.pth`）。
 * 可以使用 TensorBoard 进行可视化。
5. **评估模型 (当运行 `_evaluation.py` 文件时)**:
 * 加载预先训练好的模型权重。
 * 将模型设置为评估模式 (`model.eval()`)。
 * 使用 `sliding_window_inference` 进行高效的推理，尤其适用于输入图像比模型接受的 ROI 大很多的情况。
 * 计算 Dice 指标，并保存推理结果。

**重写一份更详细的指导文件，聚焦于如何理解和运行这些文件：**

---

## MONAI 2D 分割教程学习指南 (进阶版)

**项目地址:** [https://github.com/Project-MONAI/tutorials/tree/master/2d_segmentation/torch](https://github.com/Project-MONAI/tutorials/tree/master/2d_segmentation/torch)

**核心目标:** 理解并成功运行 MONAI 提供的 2D 医学图像分割训练和评估流程，掌握 Array-based 和 Dict-based 数据处理两种方式的区别，并学习 UNet 模型在 MONAI 中的应用。

---

### 第一部分：项目概览与运行前准备

1. **理解项目文件:**
 * **`unet_training_array.py`**: 使用 **Array-based** 数据加载方式进行 UNet 模型**训练**。
 * **`unet_training_dict.py`**: 使用 **Dict-based** 数据加载方式进行 UNet 模型**训练**。
 * **`unet_evaluation_array.py`**: 使用 **Array-based** 数据加载方式**评估**已训练好的 UNet 模型。
 * **`unet_evaluation_dict.py`**: 使用 **Dict-based** 数据加载方式**评估**已训练好的 UNet 模型。

2. **环境安装:**
 * 确保你已安装 Python、PyTorch 和 MONAI。
 * 推荐拥有 NVIDIA GPU 以加速训练和推理。
 * **查看 `requirements.txt` (如果存在)** 或根据 MONAI 官方文档安装所需的其他库。
 * **代码中已包含 `monai.config.print_config()`**，运行代码时会打印出 MONAI 的配置信息，可以用来检查环境是否正确。

3. **理解数据生成:**
 * 所有脚本的开头都会使用 `create_test_image_2d(128, 128, num_seg_classes=1)` 生成合成的 128x128 大小的图像和掩码。
 * 这些图像是 PNG 格式，保存在一个临时的目录中。
 * **注意**: `create_test_image_2d` 生成的分割掩码的值可能是 0 或 1（如果是 `num_seg_classes=2`），代码中 `ScaleIntensity()` 会将其缩放到 0-1 范围，并与图像一起保存为 0-255 的 uint8 图像。

### 第二部分：学习与运行 `unet_training_array.py` 和 `unet_training_dict.py` (训练脚本)

**目标:** 理解如何使用 MONAI 训练一个 UNet 模型进行 2D 分割。

#### 1. 数据加载与处理 (核心区别点)

* **`unet_training_array.py` (Array-based):**
 * **数据组织:** 使用 Python 的 `glob` 查找图片文件列表 (`images`, `segs`)。
 * **`ArrayDataset`:** 直接将图片文件路径列表和对应的 transforms 传递给 `ArrayDataset`。
 * **Transfoms:**
 * `LoadImage(image_only=True, ensure_channel_first=True)`: 加载 PNG 图片，并确保通道数在第一维（例如 `[C, H, W]`）。
 * `ScaleIntensity()`: 将图像像素值缩放到 [0, 1] 范围。
 * `RandSpatialCrop((96, 96), ...)`: 随机裁剪出 96x96 的区域。
 * `RandRotate90(...)`: 随机进行 90 度旋转。
 * **`DataLoader`:** 使用 `DataLoader(..., pin_memory=torch.cuda.is_available())` 来加速数据加载。

* **`unet_training_dict.py` (Dict-based):**
 * **数据组织:** 创建一个包含字典的列表 (`train_files`, `val_files`)，每个字典包含 "img" 和 "seg" 键，值为对应的文件路径。
 * **`Dataset`:** 使用 `monai.data.Dataset`，并将 transforms 作为一个整体应用。
 * **Transfoms (with `d` suffix for Dict-based):**
 * `LoadImaged(keys=["img", "seg"])`: 加载 "img" 和 "seg" 对应的文件，并将结果存回字典。
 * `EnsureChannelFirstd(keys=["img", "seg"])`: ENSURE通道在第0维度。
 * `ScaleIntensityd(keys=["img", "seg"])`: 对 "img" 和 "seg" 进行缩放。
 * `RandCropByPosNegLabeld(...)`: **一个更高级的裁剪方式**。它会根据标签中前景（`pos=1`）和背景（`neg=1`）的位置来采样。`num_samples=4` 表示每个字典会生成 4 个样本。**这是 Dict-based 方式的一个关键优势**。
 * `RandRotate90d(keys=["img", "seg"], ...)`: 对字典中的 "img" 和 "seg" 进行旋转。
 * **`list_data_collate`:** Dict-based 的 `DataLoader` 通常需要 `collate_fn=list_data_collate` 来正确处理字典列表。

#### 2. 模型、损失与优化器

* **模型:** 两个脚本都使用 `monai.networks.nets.UNet`。
 * `spatial_dims=2`: 定义为 2D 模型。
 * `in_channels=1`, `out_channels=1`: 输入和输出通道为 1 (灰度图，单类分割)。
 * `channels=(16, 32, 64, 128, 256)`: UNet 编码器和解码器各层的卷积通道数。
 * `strides=(2, 2, 2, 2)`: 定义了下采样/上采样的步长。
 * `num_res_units=2`: 每个 Encoder/Decoder block 中的残差单元数量。
* **损失函数:** `monai.losses.DiceLoss(sigmoid=True)`。`sigmoid=True` 意味着模型输出是 logits，DiceLoss 会在内部应用 Sigmoid 将其转换为概率。
* **优化器:** `torch.optim.Adam(model.parameters(), 1e-3)`。

#### 3. 训练流程

* **Epoch 循环:** 迭代 10 个 epoch。
* **训练步:**
 * `model.train()`: 设置模型为训练模式。
 * `optimizer.zero_grad()`: 清零前一步的梯度。
 * `outputs = model(inputs)`: 前向传播。
 * `loss = loss_function(outputs, labels)`: 计算损失。
 * `loss.backward()`: 反向传播。
 * `optimizer.step()`: 更新模型权重。
* **验证步 (`val_interval = 2`):**
 * `model.eval()`: 设置模型为评估模式（禁用 dropout 等）。
 * `torch.no_grad()`: 禁用梯度计算，节省内存和计算。
 * `sliding_window_inference`: 当输入图像大于模型期望的 ROI 时，使用此函数进行滑动窗口预测，以避免显存溢出并能处理大图像。`roi_size=(96, 96)` 是 UNet 实际处理的尺寸，`sw_batch_size=4` 是处理滑动窗口时的 Mini-batch size。
 * `post_trans = Compose([Activations(sigmoid=True), AsDiscrete(threshold=0.5)])`: 后处理。先用 Sigmoid 激活将模型输出（logits）转为概率，然后用 `AsDiscrete` 将概率图转为 0/1 的分割掩码。
 * `decollate_batch`: 将批次形式的输出转换为列表，以便逐个处理。
 * `dice_metric(y_pred=val_outputs, y=val_labels)`: 计算 Dice 指标，并累加。
 * **保存最佳模型:** 如果当前 epoch 的 Dice 分数高于之前的最佳分数，则保存模型权重到 `best_metric_model_segmentation2d_array.pth` 或 `best_metric_model_segmentation2d_dict.pth`。
 * **TensorBoard 可视化:** 使用 `SummaryWriter` 记录训练损失、验证 Dice 分数，并可视化输入、标签和预测结果。

#### 4. 如何运行训练脚本:

1. **选择版本:** 决定是要用 `_array` 还是 `_dict` 版本。`_dict` 版本提供了更灵活的数据处理方式（如 `RandCropByPosNegLabeld`）。
2. **安装依赖:** 确保你的环境已准备好。
3. **运行命令:**
 * 训练 Array-based: `python unet_training_array.py`
 * 训练 Dict-based: `python unet_training_dict.py`
4. **观察输出:**
 * 脚本会打印生成数据的路径、每个 epoch 的训练损失。
 * 每隔 `val_interval` 个 epoch，会打印验证的 Dice 分数。
 * 如果你的环境中安装了 TensorBoard (`pip install tensorboard`)，你可以在终端运行 `tensorboard --logdir runs` (假设 `runs` 是 `SummaryWriter` 默认的日志目录)，然后在浏览器中访问 `http://localhost:6006` 查看可视化图表。
 * 训练完成后，会在当前目录下生成 `best_metric_model_segmentation2d_array.pth` 或 `best_metric_model_segmentation2d_dict.pth` 文件。

---

### 第三部分：学习与运行 `unet_evaluation_array.py` 和 `unet_evaluation_dict.py` (评估脚本)

**目标:** 理解如何加载一个预训练好的 UNet 模型，并使用它进行推理和评估。

#### 1. 数据加载与处理

* 与训练脚本类似，这两个脚本也区分了 `_array` 和 `_dict` 两种加载方式。
* **关键区别:**
 * **不包含训练的随机增强:** 评估时只需要 `LoadImage`/`LoadImaged` 和 `ScaleIntensity`/`ScaleIntensityd` 这样的预处理步骤。
 * **`DataLoader` batch_size=1:** 通常评估时，为了方便处理每个样本和 `sliding_window_inference`，`batch_size` 设置为 1。
 * **`num_workers`:** `_array` 版本使用 `num_workers=1`，`_dict` 版本使用 `num_workers=4`，这与它们各自的 `DataLoader` 配置有关。

#### 2. 加载预训练模型

* **`model = UNet(...)`**: 重新实例化一个 UNet 模型，结构要与训练时一致。
* **`model.load_state_dict(torch.load("best_metric_model_segmentation2d_....pth", weights_only=True))`**: 加加载之前训练过程中保存的模型权重。`weights_only=True` 是 PyTorch 1.6+ 的推荐做法。
* **`model.eval()`**: 将模型设置为评估模式。

#### 3. 推理与评估流程

* **`sliding_window_inference`**: 同训练脚本一样，用于高效处理输入图像。
* **`post_trans`**: 同样的后处理步骤，将 logits 转换为二值分割掩码。
* **`dice_metric`**: 实例化 `DiceMetric` 来计算评价指标。
* **`saver = SaveImage(...)`**: 实例化一个 `SaveImage` transform，用于将推理结果的分割掩码保存到 `./output` 目录下，并设置了输出文件扩展名和后缀。
* **保存输出:** 在循环中，`saver(val_output)` 会将每个输入图像的分割结果保存为 PNG 文件。
* **打印最终指标:** `dice_metric.aggregate().item()` 会计算所有样本的平均 Dice 指标，并将其打印到控制台。
* **重置指标:** `dice_metric.reset()` 清除累积的指标值，为下一次运行做准备。

#### 4. 如何运行评估脚本:

1. **首先，确保你已经成功运行了训练脚本** (`unet_training_array.py` 或 `unet_training_dict.py`)，并且在当前目录下生成了对应的 `best_metric_model_segmentation2d_....pth` 模型文件。
2. **选择版本:** 选择与你训练时相同方式的评估脚本（如果你训练时用的是 `_array`，就运行 `unet_evaluation_array.py`）。
3. **运行命令:**
 * 评估 Array-based: `python unet_evaluation_array.py`
 * 评估 Dict-based: `python unet_evaluation_dict.py`
4. **观察输出:**
 * 脚本会打印生成数据的路径。
 * 加载模型，并输出评估阶段的 Dice 分数。
 * 在当前目录下的 `./output` 文件夹中，你会看到保存的分割结果图像。

---

### 第三部分：学习MONAI的要点总结

通过运行和理解这四个脚本，你应该能掌握以下 MONAI 的关键特性：

1. **`transforms` 系统:**
 * `Compose`: 组合多个 transform。
 * `LoadImage`/`LoadImaged`: 加载医学图像。
 * `ScaleIntensity`/`ScaleIntensityd`: 图像强度归一化。
 * `EnsureChannelFirst`/`EnsureChannelFirstd`: 统一数据通道维度。
 * **数据增强:** `RandSpatialCrop`, `RandRotate90`, `RandCropByPosNegLabeld` 等，是训练的关键。
 * **后处理:** `Activations`, `AsDiscrete` 用于将模型输出转换为监督信号。
 * **数据保存:** `SaveImage`。
2. **`Dataset` 和 `DataLoader`:**
 * `ArrayDataset`: 适用于直接处理数组或文件路径的 Map-style dataset。
 * `Dataset` (配合 Dict-based transforms): 适用于处理字典形式数据的 Map-style dataset。
 * `DataLoader`: 管理数据批次加载，并支持多进程数据预取 (`num_workers`)。
 * `list_data_collate`: Dict-based DataLoader 需要的 collate_fn。
3. **模型与训练:**
 * `monai.networks.nets.UNet`: MONAI 提供的 UNet 实现。
 * `monai.losses.DiceLoss`: 常见的分割损失函数。
 * `monai.metrics.DiceMetric`: 用于评估分割任务的指标。
4. **推理与评估:**
 * `model.load_state_dict()`: 加载预训练模型。
 * `sliding_window_inference`: 处理大尺寸图像的高效推理方法。

**进一步学习建议:**

* **修改参数:** 尝试修改 `batch_size`, `learning_rate`, `epochs`, `roi_size` 等参数，观察训练和评估结果。
* **尝试不同的增强:** 探索 MONAI 提供的其他 `transforms`，并将它们添加到训练 pipeline 中。
* **自定义数据集:** 尝试将你自己的医学图像数据集替换掉生成的合成数据。你需要调整文件路径的组织方式和 `transforms`。
* **理解 `RandCropByPosNegLabeld`:** 这是一个非常实用的 transform，理解它的工作原理可以帮助你更好地处理分割任务中的样本不平衡问题。

希望这份更详细的指南能帮助你更好地理解和运行 MONAI 的 2D 分割教程！
