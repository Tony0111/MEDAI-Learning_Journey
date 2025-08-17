import torch
import numpy as np
# 尝试导入 Monai 的核心模块，如果这个导入失败，就认为是Monai未正确安装或配置
try:
    from monai.data import MetaTensor
    from monai.transforms import RandFlipd
    MONAI_AVAILABLE = True
except ImportError as e:
    MONAI_AVAILABLE = False
    MONAI_IMPORT_ERROR = e # 记录导入错误信息

def test_gpu_invocation():
    """
    Comprehensive test to check PyTorch GPU availability and Monai integration.
    """
    print("--- PyTorch GPU Test ---")

    # 1. Check PyTorch version and CUDA availability
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"Number of GPUs available: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i} name: {torch.cuda.get_device_name(i)}")
    else:
        print("CUDA is not available. GPU cannot be used.")
        # If CUDA is not available, we can't test Monai on GPU, so exit early.
        return

    # 2. Create a tensor and move it to the GPU
    print("\n--- Tensor to GPU Test ---")
    try:
        device = torch.device("cuda:0") # Assuming GPU 0 exists
        print(f"Using device: {device}")

        x = torch.randn(3, 3).to(device)
        print(f"Tensor created on device: {x.device}")

        y = x * 2
        print(f"Result of operation x * 2 on GPU:\n{y}")

        y_cpu = y.cpu()
        print(f"Result moved back to CPU:\n{y_cpu}")
        print("Tensor to GPU movement successful.")

    except Exception as e:
        print(f"Error during basic PyTorch tensor GPU test: {e}")

    # 3. Test Monai with a simple operation
    print("\n--- Monai GPU Test ---")
    if MONAI_AVAILABLE:
        try:
            # Create a dummy numpy array
            dummy_data = np.random.rand(1, 1, 16, 16, 16).astype(np.float32)

            # Convert to MetaTensor
            meta_tensor_cpu = MetaTensor(
                dummy_data,
                device="cpu",
                affine=np.eye(4),
            )
            print(f"Monai MetaTensor created on: {meta_tensor_cpu.device}")

            # Move the MetaTensor to the GPU
            # Use device_map='auto' or specify device directly for flexibility with multiple GPUs
            meta_tensor_gpu = meta_tensor_cpu.to("cuda:0")
            print(f"Monai MetaTensor moved to: {meta_tensor_gpu.device}")

            if meta_tensor_gpu.device.type == 'cuda':
                print("Monai MetaTensor is successfully on GPU.")

                # Example of a Monai transform on GPU
                flip_transform = RandFlipd(
                    keys=["image_key"],
                    prob=1.0,
                    spatial_axis=0,
                    # Often, transforms are device-agnostic and use the tensor's device
                    # Or some might have device explicitely. Let's assume it uses tensor's device.
                    # If a transform explicitly requires a device parameter, you'd set it here.
                    # For RandFlipd, it relies on the input tensor's device.
                )

                data_dict = {"image_key": meta_tensor_gpu}
                transformed_data_dict = flip_transform(data_dict)

                print(f"Transformed data device: {transformed_data_dict['image_key'].device}")
                if transformed_data_dict['image_key'].device.type == 'cuda':
                    print("Monai transform processed data on GPU successfully.")
                else:
                    print("Monai transform did NOT process data on GPU.") # This would be an issue

            else:
                print("Monai MetaTensor is NOT on GPU after .to('cuda:0')")
        except Exception as e:
            print(f"Error during Monai GPU test: {e}")
    else:
        print(f"Monai import failed: {MONAI_IMPORT_ERROR}. Please ensure Monai is correctly installed in the selected Python environment.")


if __name__ == "__main__":
    test_gpu_invocation()
