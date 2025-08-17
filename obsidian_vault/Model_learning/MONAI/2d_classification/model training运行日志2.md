
### py文件运行

按照指示，把notebook中的代码复制到py文件中，重新运行
以下为运行结果
```
d:\AI\MONAI\DenseNet121\model-traning.py:41: SyntaxWarning: invalid escape sequence '\A'
  os.environ["MONAI_DATA_DIRECTORY"] = "D:\AI\MONAI\DenseNet121\data"
D:\Apps\Python\Lib\site-packages\ignite\handlers\checkpoint.py:17: DeprecationWarning: `TorchScript` support for functional optimizers is deprecated and will be removed in a future PyTorch release. Consider using the `torch.compile` optimizer instead.
  from torch.distributed.optim import ZeroRedundancyOptimizer
MONAI version: 1.6.dev2532
Numpy version: 2.0.2
Pytorch version: 2.5.1+cu118
MONAI flags: HAS_EXT = False, USE_COMPILED = False, USE_META_DICT = False
MONAI rev id: d14a44f388c5e9ace8496387cca7cd93cfc4d60d
MONAI __file__: D:\Apps\Python\Lib\site-packages\monai\__init__.py

Optional dependencies:
Pytorch Ignite version: 0.4.11
ITK version: 5.4.4
Nibabel version: 5.3.2
scikit-image version: 0.25.2
scipy version: 1.14.1
Pillow version: 11.0.0
Tensorboard version: 2.20.0
gdown version: 5.2.0
TorchVision version: 0.20.1+cu118
tqdm version: 4.67.1
lmdb version: 1.7.3
psutil version: 6.1.0
pandas version: 2.2.3
einops version: 0.8.0
transformers version: 4.47.1
mlflow version: 3.2.0
pynrrd version: 1.1.3
clearml version: 2.0.3rc0

For details about installing the optional dependencies, please visit:
    https://docs.monai.io/en/latest/installation.html#installing-the-recommended-dependencies

PyTorch version: 2.5.1+cu118
CUDA available: True
CUDA version: 11.8
Number of GPUs available: 1
GPU 0 name: NVIDIA GeForce RTX 4060 Laptop GPU
D:\AI\MONAI\DenseNet121\data
Total image count: 58954
Image dimensions: 64 x 64
Label names: ['AbdomenCT', 'BreastMRI', 'CXR', 'ChestCT', 'Hand', 'HeadCT']
Label counts: [10000, 8954, 10000, 10000, 10000, 10000]
Training count: 47164, Validation count: 5895, Test count: 5895
----------
epoch 1/4
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "D:\Apps\Python\Lib\multiprocessing\spawn.py", line 122, in spawn_main
    exitcode = _main(fd, parent_sentinel)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Apps\Python\Lib\multiprocessing\spawn.py", line 131, in _main
    prepare(preparation_data)
  File "D:\Apps\Python\Lib\multiprocessing\spawn.py", line 246, in prepare
    _fixup_main_from_path(data['init_main_from_path'])
  File "D:\Apps\Python\Lib\multiprocessing\spawn.py", line 297, in _fixup_main_from_path
    main_content = runpy.run_path(main_path,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen runpy>", line 286, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "d:\AI\MONAI\DenseNet121\model-traning.py", line 159, in <module>
    for batch_data in train_loader:
  File "D:\Apps\Python\Lib\site-packages\torch\utils\data\dataloader.py", line 484, in __iter__
    return self._get_iterator()
           ^^^^^^^^^^^^^^^^^^^^
  File "D:\Apps\Python\Lib\site-packages\torch\utils\data\dataloader.py", line 415, in _get_iterator
    return _MultiProcessingDataLoaderIter(self)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Apps\Python\Lib\site-packages\torch\utils\data\dataloader.py", line 1138, in __init__
    w.start()
  File "D:\Apps\Python\Lib\multiprocessing\process.py", line 121, in start
    self._popen = self._Popen(self)
                  ^^^^^^^^^^^^^^^^^
  File "D:\Apps\Python\Lib\multiprocessing\context.py", line 224, in _Popen
    return _default_context.get_context().Process._Popen(process_obj)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Apps\Python\Lib\multiprocessing\context.py", line 337, in _Popen
    return Popen(process_obj)
           ^^^^^^^^^^^^^^^^^^
  File "D:\Apps\Python\Lib\multiprocessing\popen_spawn_win32.py", line 46, in __init__
    prep_data = spawn.get_preparation_data(process_obj._name)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Apps\Python\Lib\multiprocessing\spawn.py", line 164, in get_preparation_data
    _check_not_importing_main()
  File "D:\Apps\Python\Lib\multiprocessing\spawn.py", line 140, in _check_not_importing_main
    raise RuntimeError('''
RuntimeError:
        An attempt has been made to start a new process before the
RuntimeError:
RuntimeError:
RuntimeError:
RuntimeError:
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.

        This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:

            if __name__ == '__main__':
                freeze_support()
                ...

        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable.

        To fix this issue, refer to the "Safe importing of main module"
        section in https://docs.python.org/3/library/multiprocessing.html
```
![[Figure_1.png]]

### MONAI conda虚拟环境运行（cpu）

num_workers = 0
optimizer = 1e-5
batch_size = 300
```
32m 22.7s

---------- epoch 1/4 1/157, train_loss: 1.8068 2/157, train_loss: 1.7499 3/157, train_loss: 1.7305 4/157, train_loss: 1.7318 5/157, train_loss: 1.6639 6/157, train_loss: 1.6368 7/157, train_loss: 1.6335 8/157, train_loss: 1.5917 9/157, train_loss: 1.5928 10/157, train_loss: 1.5607 11/157, train_loss: 1.5266 12/157, train_loss: 1.5149 13/157, train_loss: 1.4860 14/157, train_loss: 1.4724 15/157, train_loss: 1.4435 16/157, train_loss: 1.4168 17/157, train_loss: 1.3987 18/157, train_loss: 1.3875 19/157, train_loss: 1.3451 20/157, train_loss: 1.3483 21/157, train_loss: 1.3232 22/157, train_loss: 1.2767 23/157, train_loss: 1.2684

...

epoch 4 average loss: 0.0390 saved new best metric model current epoch: 4 current AUC: 1.0000 current accuracy: 0.9951 best AUC: 1.0000 at epoch: 4 train completed, best_metric: 1.0000 at epoch: 4
```

![[Pasted image 20250815232449.png]]

### MONAI conda虚拟环境运行（gpu）

num_workers = 0
optimizer = 1e-5
batch_size = 300
```
---------- epoch 1/4 1/157, train_loss: 1.7928 2/157, train_loss: 1.7632 3/157, train_loss: 1.7364 4/157, train_loss: 1.7093 5/157, train_loss: 1.6653 6/157, train_loss: 1.6517 7/157, train_loss: 1.6178 8/157, train_loss: 1.6064 9/157, train_loss: 1.5730 10/157, train_loss: 1.5393 11/157, train_loss: 1.5407 12/157, train_loss: 1.5082 13/157, train_loss: 1.4869 14/157, train_loss: 1.4563 15/157, train_loss: 1.4401 16/157, train_loss: 1.4183 17/157, train_loss: 1.3893 18/157, train_loss: 1.3901 19/157, train_loss: 1.3482 20/157, train_loss: 1.3761 21/157, train_loss: 1.2911 22/157, train_loss: 1.2909 23/157, train_loss: 1.2856

...

epoch 4 average loss: 0.0389 saved new best metric model current epoch: 4 current AUC: 1.0000 current accuracy: 0.9956 best AUC: 1.0000 at epoch: 4 train completed, best_metric: 1.0000 at epoch: 4
```
![[Pasted image 20250816010303.png]]

```
				precision    recall  f1-score   support

   AbdomenCT     0.9891    0.9990    0.9940       995
   BreastMRI     0.9943    0.9886    0.9915       880
         CXR     0.9990    0.9969    0.9980       982
     ChestCT     0.9971    1.0000    0.9985      1014
        Hand     0.9981    0.9933    0.9957      1048
      HeadCT     0.9990    0.9980    0.9985       976

    accuracy                         0.9961      5895
   macro avg     0.9961    0.9960    0.9960      5895
weighted avg     0.9961    0.9961    0.9961      5895
```

### **`batch_size`** 参数分析

#### 第一次尝试
num_workers = 0
optimizer = 1e-5
batch_size = 128
```
9m 54s
---------- epoch 1/4 1/368, train_loss: 1.7984 2/368, train_loss: 1.7807 3/368, train_loss: 1.7514 4/368, train_loss: 1.6958 5/368, train_loss: 1.7192 6/368, train_loss: 1.6636 7/368, train_loss: 1.6495 8/368, train_loss: 1.6311 9/368, train_loss: 1.6158 10/368, train_loss: 1.6003 11/368, train_loss: 1.5574 12/368, train_loss: 1.5091 13/368, train_loss: 1.5470 14/368, train_loss: 1.4920 15/368, train_loss: 1.4943 16/368, train_loss: 1.4662 17/368, train_loss: 1.4429 18/368, train_loss: 1.4252 19/368, train_loss: 1.4229 20/368, train_loss: 1.4213 21/368, train_loss: 1.3609 22/368, train_loss: 1.3548 23/368, train_loss: 1.3125

...

epoch 4 average loss: 0.0171 saved new best metric model current epoch: 4 current AUC: 1.0000 current accuracy: 0.9988 best AUC: 1.0000 at epoch: 4 train completed, best_metric: 1.0000 at epoch: 4
```

![[Pasted image 20250816011842.png]]

```
				precision    recall  f1-score   support

   AbdomenCT     1.0000    1.0000    1.0000       995
   BreastMRI     0.9955    1.0000    0.9977       880
         CXR     1.0000    0.9980    0.9990       982
     ChestCT     1.0000    1.0000    1.0000      1014
        Hand     0.9990    0.9962    0.9976      1048
      HeadCT     0.9990    1.0000    0.9995       976

    accuracy                         0.9990      5895
   macro avg     0.9989    0.9990    0.9990      5895
weighted avg     0.9990    0.9990    0.9990      5895
```

#### 第二次尝试

num_workers = 0
optimizer = 1e-5
batch_size = 64
```
12m 41.7s
---------- epoch 1/4 1/736, train_loss: 1.8155 2/736, train_loss: 1.7690 3/736, train_loss: 1.7509 4/736, train_loss: 1.7548 5/736, train_loss: 1.7077 6/736, train_loss: 1.7258 7/736, train_loss: 1.6348 8/736, train_loss: 1.6458 9/736, train_loss: 1.6720 10/736, train_loss: 1.6354 11/736, train_loss: 1.6046 12/736, train_loss: 1.5826 13/736, train_loss: 1.5715 14/736, train_loss: 1.5303 15/736, train_loss: 1.5243 16/736, train_loss: 1.5176 17/736, train_loss: 1.5295 18/736, train_loss: 1.4779 19/736, train_loss: 1.4843 20/736, train_loss: 1.4463 21/736, train_loss: 1.4463 22/736, train_loss: 1.3989 23/736, train_loss: 1.3552

...

epoch 4 average loss: 0.0114 saved new best metric model current epoch: 4 current AUC: 1.0000 current accuracy: 0.9993 best AUC: 1.0000 at epoch: 4 train completed, best_metric: 1.0000 at epoch: 4
```

![[Pasted image 20250816013411.png]]

```
				precision    recall  f1-score   support

   AbdomenCT     1.0000    1.0000    1.0000       995
   BreastMRI     0.9977    1.0000    0.9989       880
         CXR     1.0000    0.9990    0.9995       982
     ChestCT     1.0000    1.0000    1.0000      1014
        Hand     0.9990    0.9981    0.9986      1048
      HeadCT     1.0000    1.0000    1.0000       976

    accuracy                         0.9995      5895
   macro avg     0.9995    0.9995    0.9995      5895
weighted avg     0.9995    0.9995    0.9995      5895
```

#### 第三次尝试

num_workers = 0
optimizer = 1e-5
batch_size = 512

```
---------- epoch 1/4 1/92, train_loss: 1.7888 2/92, train_loss: 1.7636 3/92, train_loss: 1.7243 4/92, train_loss: 1.6981 5/92, train_loss: 1.6691 6/92, train_loss: 1.6320 7/92, train_loss: 1.6276 8/92, train_loss: 1.5919 9/92, train_loss: 1.5623 10/92, train_loss: 1.5367 11/92, train_loss: 1.5142 12/92, train_loss: 1.4999 13/92, train_loss: 1.4598 14/92, train_loss: 1.4505 15/92, train_loss: 1.4148 16/92, train_loss: 1.3910 17/92, train_loss: 1.3586 18/92, train_loss: 1.3494 19/92, train_loss: 1.3347 20/92, train_loss: 1.3079 21/92, train_loss: 1.2690 22/92, train_loss: 1.2695 23/92, train_loss: 1.2531

...

epoch 4 average loss: 0.0712 saved new best metric model current epoch: 4 current AUC: 0.9999 current accuracy: 0.9932 best AUC: 0.9999 at epoch: 4 train completed, best_metric: 0.9999 at epoch: 4
```
![[Pasted image 20250816093113.png]]

```
				precision    recall  f1-score   support

   AbdomenCT     0.9840    0.9920    0.9880       995
   BreastMRI     0.9920    0.9875    0.9897       880
         CXR     0.9990    0.9939    0.9964       982
     ChestCT     0.9941    1.0000    0.9971      1014
        Hand     0.9952    0.9914    0.9933      1048
      HeadCT     0.9949    0.9939    0.9944       976

    accuracy                         0.9932      5895
   macro avg     0.9932    0.9931    0.9931      5895
weighted avg     0.9932    0.9932    0.9932      5895
```

