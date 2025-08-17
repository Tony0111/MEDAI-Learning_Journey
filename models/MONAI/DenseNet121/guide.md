好的，各位医学的准栋梁们，你们好！很高兴能和大家一起探索 MONAI 这个强大的医学影像处理工具。今天我们要学习的项目是 **MedNIST 数据集的医学影像分类教程**。

### 1. 项目是什么？（用大一新生能听懂的话说）

想象一下，医院里每天都有大量的医学影像，比如 CT、X 光片、MRI 等等。这些影像里藏着很多重要的信息，可以帮助医生判断病情。但是，人工一张张地看，非常耗费时间和精力，而且人难免会出错。

**MedNIST 模型分类教程** 就像是教你如何建立一个“数字医生助手”，这个助手能自动“看懂”医学影像，并且知道这些影像属于哪一类别，比如判断一张 X 光片是正常的还是肺炎。

#### 从特殊性中提炼普遍性

MedNIST 数据集里面包含了六种不同的医学影像类别（HeadCT, BreastMRI, CXR, ChestCT, Hand, AbdomenCT）。这个教程的特别之处在于，它用这些具体的医学影像来演示一个通用的方法：

1.  **收集和整理图片**：就像你要把各种解剖学的手绘图整理好一样，教程里把不同类别的医学影像分门别类地“收集”起来。
2.  **“训练”你的助手**：我们把这些整理好的影像“喂”给一个叫做 **DenseNet121** 的AI模型。这个模型就像一个非常聪明、善于学习的学生，通过大量练习（也就是看大量的影像），它会学会区分不同类别影像的特征。
3.  **“考试”和“评估”**：学完了，我们就要让这个助手“考试”（在测试数据集上评估），看看它学得怎么样，它能准确地识别出新影像的类别吗？
4.  **MONAI 是什么？**：MONAI 就像是给这个“数字医生助手”的“工具箱”。它里面有很多预先做好的零件和方法，比如：
    *   **数据增强**：就像你学习生理学时，会看不同角度、不同光照条件下的图像一样，MONAI 可以在现有影像基础上，稍微旋转、缩放、翻转一下，生成新的影像，这样你的助手就能学到更全面的知识，不容易被细微变化“欺骗”。
    *   **模型搭建**：MONAI 提供了很多可以直接使用的AI模型（比如我们用的 DenseNet121），就像你不用自己从头造一个听诊器，可以直接拿MONAI提供的模块来搭建你的“数字助手”的“大脑”。

#### 以后有什么样的用？

学会了这个教程，你不仅学会了如何用 MONAI 做医学影像分类，更重要的是，你掌握了一种处理和分析医学影像的通用思路和方法。未来，你就可以把这个思路应用到更多更复杂的医学影像任务上：

*   **疾病诊断**：比如更精确地检测早期癌症、识别眼底病变。
*   **药物研发**：通过分析影像来评估新药的效果。
*   **个性化医疗**：根据患者的影像特征，制定更适合的治疗方案。
*   **医学研究**：分析大量影像数据，发现新的医学规律。

甚至，你还可以把这种思路推广到其他领域，比如工业上的缺陷检测、生物学上的细胞识别等等。

### 2. 运行代码的指导文稿 (mednist_tutorial.ipynb)

下面，我将结合你提供的 Jupyter Notebook 内容，为你编写一份详细的 Markdown 指导文稿。这份文稿会按照 Notebook 的逻辑，并用大一新生易于理解的语言来解释每一步。

---

# MedNIST 数据集上的二分类医学影像教程

欢迎来到 MONAI 的世界！在这个教程中，我们将一步一步地学习如何使用 MONAI 库来完成一个典型的医学影像分类任务。我们将完整地走过从数据准备、模型训练到模型评估的整个流程，以 MedNimpib 数据集为例。

**本教程将涵盖以下内容：**

*   **环境配置**：确保你拥有所有必需的软件库。
*   **数据准备**：下载并组织 MedNIST 数据集，理解数据结构。
*   **数据预处理**：使用 MONAI 的强大转换（Transforms）技术来处理医学影像。
*   **模型构建**：选择并配置一个适合图像分类的深度学习模型（DenseNet121）。
*   **模型训练**：使用 PyTorch 框架训练我们的模型。
*   **模型评估**：在独立的测试数据集上评估模型的性能，生成分类报告。

---

### 1. 环境设置 (Setup environment)

首先，我们需要安装 MONAI 库以及一些辅助的 Python 库，例如用于绘图的 Matplotlib。`pip install -q "monai-weekly[pillow, tqdm]"` 这行命令会帮你安装 MONAI 的最新开发版本（以及 Pillow 和 tqdm，一个是图片处理库，一个是进度条库），`-q` 表示安静模式，尽量不打扰你。`%matplotlib inline` 是 Jupyter Notebook 的一个魔法命令，让图表可以直接显示在 Notebook 里。

```python
!python -c "import monai" || pip install -q "monai-weekly[pillow, tqdm]"
!python -c "import matplotlib" || pip install -q matplotlib
%matplotlib inline
```

---

### 2. 导入必要的库 (Setup imports)

接下来，我们导入在整个教程中会用到的所有 Python 库和 MONAI 的模块。这里面有 PyTorch（深度学习的核心框架）、NumPy（科学计算）、Matplotlib（绘图），以及 MONAI 提供的各种工具，比如数据加载 (`DataLoader`)、模型 (`DenseNet121`)、转换 (`Compose`, `LoadImage`, `RandFlip` 等) 和评估指标 (`ROCAUCMetric`)。`print_config()` 会显示 MONAI 的版本信息，这在你遇到问题时很有帮助。

```python
import os
import shutil
import tempfile
import matplotlib.pyplot as plt
import PIL
import torch
from torch.utils.tensorboard import SummaryWriter
import numpy as np
from sklearn.metrics import classification_report

from monai.apps import download_and_extract
from monai.config import print_config
from monai.data import decollate_batch, DataLoader
from monai.metrics import ROCAUCMetric
from monai.networks.nets import DenseNet121
from monai.transforms import (
    Activations,
    AsDiscrete,
    Compose,
    LoadImage,
    RandFlip,
    RandRotate,
    RandZoom,
    ScaleIntensity,
)
from monai.utils import set_determinism

# 打印 MONAI 的配置信息
print_config()
```

---

### 3. 设置数据目录 (Setup data directory)

你可以通过设置 `MONAI_DATA_DIRECTORY` 环境变量来指定数据存储的位置。如果没设置，MONAI 会使用一个临时目录。这里我们打印出实际使用的数据目录。

```python
directory = os.environ.get("MONAI_DATA_DIRECTORY")
if directory is not None:
    os.makedirs(directory, exist_ok=True)
root_dir = tempfile.mkdtemp() if directory is None else directory
print(root_dir)
```

---

### 4. 下载数据集 (Download dataset)

MedNIST 数据集包含了多种医学影像。本教程将使用这个数据集来演示如何在 64x64 像素的医学影像上进行分类。

```python
resource = "https://github.com/Project-MONAI/MONAI-extra-test-data/releases/download/0.8.1/MedNIST.tar.gz"
md5 = "0bc7306e7427e00ad1c5526a6677552d"

compressed_file = os.path.join(root_dir, "MedNIST.tar.gz")
data_dir = os.path.join(root_dir, "MedNIST")
if not os.path.exists(data_dir):
    download_and_extract(resource, compressed_file, root_dir, md5)
```

---

### 5. 设置可复现的随机种子 (Set deterministic training for reproducibility)

为了让每次运行代码都能得到相同的结果，我们设置一个随机种子。这对于调试和复现实验非常重要。

```python
set_determinism(seed=0)
```

---

### 6. 读取影像文件名和统计信息 (Read image filenames from the dataset folders)

 数据集被分成了 6 个子文件夹，每个文件夹代表一个影像类别。我们将列出所有的影像文件路径，并统计出每类影像的数量，这有助于我们了解数据的分布。

```python
class_names = sorted(x for x in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, x)))
num_class = len(class_names)
image_files = [
    [os.path.join(data_dir, class_names[i], x) for x in os.listdir(os.path.join(data_dir, class_names[i]))]
    for i in range(num_class)
]
num_each = [len(image_files[i]) for i in range(num_class)]
image_files_list = []
image_class = []
for i in range(num_class):
    image_files_list.extend(image_files[i])
    image_class.extend([i] * num_each[i])
num_total = len(image_class)
image_width, image_height = PIL.Image.open(image_files_list[0]).size

print(f"Total image count: {num_total}")
print(f"Image dimensions: {image_width} x {image_height}")
print(f"Label names: {class_names}")
print(f"Label counts: {num_each}")
```

---

### 7. 可视化部分影像 (Randomly pick images from the dataset to visualize and check)

这一步，我们随机抽取一些影像，将它们显示出来。这可以帮助我们直观地了解数据的样子，以及它们是否被正确地加载和分类。

```python
plt.subplots(3, 3, figsize=(8, 8))
for i, k in enumerate(np.random.randint(num_total, size=9)):
    im = PIL.Image.open(image_files_list[k])
    arr = np.array(im)
    plt.subplot(3, 3, i + 1)
    plt.xlabel(class_names[image_class[k]])
    plt.imshow(arr, cmap="gray", vmin=0, vmax=255)
plt.tight_layout()
plt.show()
```

---

### 8. 划分训练、验证和测试数据集 (Prepare training, validation and test data lists)

将数据集按照 70% 训练、15% 验证、15% 测试的比例进行划分。数据划分是机器学习流程中的一个关键步骤，以确保我们能够以无偏见的方式评估模型的泛化能力。

```python
val_frac = 0.1
test_frac = 0.1
length = len(image_files_list)
indices = np.arange(length)
np.random.shuffle(indices)

test_split = int(test_frac * length)
val_split = int(val_frac * length) + test_split
test_indices = indices[:test_split]
val_indices = indices[test_split:val_split]
train_indices = indices[val_split:]

train_x = [image_files_list[i] for i in train_indices]
train_y = [image_class[i] for i in train_indices]
val_x = [image_files_list[i] for i in val_indices]
val_y = [image_class[i] for i in val_indices]
test_x = [image_files_list[i] for i in test_indices]
test_y = [image_class[i] for i in test_indices]

print(f"Training count: {len(train_x)}, Validation count: {len(val_x)}, Test count: {len(test_x)}")
```

---

### 9. 定义 MONAI 转换、数据集和数据加载器 (Define MONAI transforms, Dataset and Dataloader to pre-process data)

这一部分是 MONAI 的核心魅力所在。

*   **`Compose`**：它是一个转换的“容器”，可以把多个转换按照顺序堆叠起来。
*   **`LoadImage`**：负责加载图像文件。`image_only=True` 表示我们只需要图像本身，不需要元数据。
*   **`EnsureChannelFirst`**：医学影像的通道顺序可能不同，这个转换确保我们的图像数据通道都在第一个维度（例如，对于 2D RGB 图像，它会是 `[channels, height, width]`）。
*   **`ScaleIntensity`**：将图像像素值缩放到一个标准的范围（通常是 0 到 1），这有助于模型更好地学习。
*   **`RandRotate`, `RandFlip`, `RandZoom`**：这些是**数据增强 (Data Augmentation)** 的转换。通过随机地旋转、翻转或缩放图像，我们可以生成更多样化的训练数据，提高模型的鲁棒性，使其在面对各种情况的真实影像时表现更好。
*   **`Activations(softmax=True)`**：在输出层应用 Softmax 激活函数，将模型的输出转化为概率分布。
*   **`AsDiscrete(to_onehot=num_class)`**：将标签转换为独热编码 (one-hot encoding) 格式，这通常是分类任务的标签形式。

最后，我们创建 `MedNISTDataset` 类来包装我们的影像文件和标签，并使用 `DataLoader` 来高效地加载和批处理数据。`num_workers` 参数可以设置使用多少个子进程来加载数据，以加快速度。

```python
train_transforms = Compose(
    [
        LoadImage(image_only=True),
        EnsureChannelFirst(),
        ScaleIntensity(),
        RandRotate(range_x=np.pi / 12, prob=0.5, keep_size=True),
        RandFlip(spatial_axis=0, prob=0.5),
        RandZoom(min_zoom=0.9, max_zoom=1.1, prob=0.5),
    ]
)

val_transforms = Compose([LoadImage(image_only=True), EnsureChannelFirst(), ScaleIntensity()])

y_pred_trans = Compose([Activations(softmax=True)])
y_trans = Compose([AsDiscrete(to_onehot=num_class)])

class MedNISTDataset(torch.utils.data.Dataset):
    def __init__(self, image_files, labels, transforms):
        self.image_files = image_files
        self.labels = labels
        self.transforms = transforms

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, index):
        return self.transforms(self)

Define network and optimizer 部分代码解析
python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = DenseNet121(spatial_dims=2, in_channels=1, out_channels=num_class).to(device)
loss_function = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), 1e-5)
max_epochs = 50
val_interval = 1
1. 设备选择 (device)
torch.device("cuda" if torch.cuda.is_available() else "cpu")：这行代码检查系统是否有可用的CUDA（GPU），如果有则使用GPU加速计算，否则使用CPU。

深度学习模型在GPU上训练速度会快很多，因为GPU擅长并行计算。

2. 模型定义 (model)
DenseNet121(spatial_dims=2, in_channels=1, out_channels=num_class)：创建了一个DenseNet121模型。

spatial_dims=2：表示这是处理2D图像数据的模型

in_channels=1：输入图像的通道数，这里是1（灰度图）

out_channels=num_class：输出类别数，对应MedNIST数据集的6个类别

.to(device)：将模型移动到之前定义的设备（GPU或CPU）上

3. 损失函数 (loss_function)
torch.nn.CrossEntropyLoss()：使用交叉熵损失函数，这是分类任务常用的损失函数。

交叉熵损失衡量模型预测的概率分布与实际标签分布的差异。

4. 优化器 (optimizer)
torch.optim.Adam(model.parameters(), 1e-5)：使用Adam优化器来更新模型参数。

model.parameters()：获取模型的所有可训练参数

1e-5：学习率，控制参数更新的步长

5. 训练参数
max_epochs = 50：最大训练轮数为50

val_interval = 1：每1个epoch验证一次模型性能

训练和验证循环部分代码解析
python
best_metric = -1
best_metric_epoch = -1
epoch_loss_values = []
metric_values = []

for epoch in range(max_epochs):
    print("-" * 10)
    print(f"epoch {epoch + 1}/{max_epochs}")
    model.train()
    epoch_loss = 0
    step = 0
    
    for batch_data in train_loader:
        step += 1
        inputs, labels = batch_data[0].to(device), batch_data[1].to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_function(outputs, labels)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
        print(f"{step}/{len(train_loader.dataset) // train_loader.batch_size}, " f"train_loss: {loss.item():.4f}")
    
    epoch_loss /= step
    epoch_loss_values.append(epoch_loss)
    print(f"epoch {epoch + 1} average loss: {epoch_loss:.4f}")

    if (epoch + 1) % val_interval == 0:
        model.eval()
        with torch.no_grad():
            y_pred = torch.tensor([], dtype=torch.float32, device=device)
            y = torch.tensor([], dtype=torch.long, device=device)
            
            for val_data in val_loader:
                val_images, val_labels = val_data[0].to(device), val_data[1].to(device)
                y_pred = torch.cat([y_pred, model(val_images)], dim=0)
                y = torch.cat([y, val_labels], dim=0)
            
            y_onehot = [y_onehot(i, num_class) for i in decollate_batch(y, detach=False)]
            y_pred_act = [Activations(softmax=True)(i) for i in decollate_batch(y_pred)]
            y_pred_act = torch.cat(y_pred_act, dim=0)
            y_onehot = torch.cat(y_onehot, dim=0)
            
            acc_value = torch.eq(y_pred_act.argmax(dim=1), y)
            acc_metric = acc_value.sum().item() / acc_value.shape[0]
            
            auc_metric = ROCAUCMetric()
            auc_metric(y_pred_act, y_onehot)
            auc_result = auc_metric.aggregate()
            auc_metric.reset()
            del y_pred_act, y_onehot
            
            metric_values.append(auc_result)
            if auc_result > best_metric:
                best_metric = auc_result
                best_metric_epoch = epoch + 1
                torch.save(model.state_dict(), os.path.join(root_dir, "best_metric_model.pth"))
                print("saved new best metric model")
            
            print(f"current epoch: {epoch + 1} current AUC: {auc_result:.4f} " f"current accuracy: {acc_metric:.4f} best AUC: {best_metric:.4f} " f"at epoch: {best_metric_epoch}")
训练循环 (for epoch in range(max_epochs))
初始化：

设置最佳指标初始值

准备记录训练损失和验证指标的列表

每个epoch的训练：

model.train()：将模型设置为训练模式（启用dropout等）

遍历训练数据加载器：

将数据移动到指定设备

optimizer.zero_grad()：清空梯度（防止梯度累积）

outputs = model(inputs)：前向传播，得到预测结果

loss = loss_function(outputs, labels)：计算损失

loss.backward()：反向传播，计算梯度

optimizer.step()：更新模型参数

累计并打印损失

验证阶段：

model.eval()：将模型设置为评估模式（禁用dropout等）

with torch.no_grad()：禁用梯度计算（节省内存）

收集验证集的所有预测和真实标签

计算准确率和AUC（Area Under Curve）指标：

acc_value：计算预测正确的样本数

auc_metric：计算AUC值，衡量模型区分不同类别的能力

保存性能最好的模型

关键概念解释
Epoch：完整遍历一次训练数据集称为一个epoch

Batch：由于内存限制，数据被分成小批量(batch)处理

前向传播：数据通过网络计算输出的过程

反向传播：根据损失计算梯度并反向传播的过程

AUC：评估分类模型性能的指标，值在0.5-1之间，越大越好

测试模型部分代码解析
python
model.load_state_dict(torch.load(os.path.join(root_dir, "best_metric_model.pth")))
model.eval()
y_true = []
y_pred = []
with torch.no_grad():
    for test_data in test_loader:
        test_images, test_labels = test_data[0].to(device), test_data[1].to(device)
        pred = model(test_images).argmax(dim=1)
        for i in range(len(pred)):
            y_true.append(test_labels[i].item())
            y_pred.append(pred[i].item())

print(classification_report(y_true, y_pred, target_names=class_names))
加载最佳模型：

model.load_state_dict()：加载之前保存的最佳模型参数

测试模型：

model.eval()：设置为评估模式

遍历测试集，收集预测结果和真实标签

argmax(dim=1)：获取预测概率最大的类别作为最终预测

生成分类报告：

classification_report()：生成详细的分类报告，包括每个类别的精确度、召回率、F1分数等

可视化部分代码解析
python
plt.figure("train", (12, 6))
plt.subplot(1, 2, 1)
plt.title("Epoch Average Loss")
x = [i + 1 for i in range(len(epoch_loss_values))]
plt.xlabel("epoch")
plt.plot(x, epoch_loss_values)
plt.subplot(1, 2, 2)
plt.title("Val AUC")
plt.xlabel("epoch")
plt.plot(x, metric_values)
plt.show()
创建一个大图（12x6英寸）

左侧子图绘制训练损失随epoch的变化

右侧子图绘制验证集AUC值随epoch的变化

可视化训练过程有助于理解模型是否收敛或过拟合

总结
这部分代码完成了以下关键步骤：

定义模型架构（DenseNet121）并设置训练设备

配置损失函数和优化器

实现训练循环，包括前向传播、反向传播和参数更新

定期验证模型性能并保存最佳模型

最终在测试集上评估模型性能

可视化训练过程

理解这些代码的关键是掌握PyTorch训练模型的基本流程：准备模型、数据→训练循环（前向、损失计算、反向传播、参数更新）→评估模型→保存和使用模型。