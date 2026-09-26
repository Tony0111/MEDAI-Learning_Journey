import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 设置阿里云镜像源
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# 检查 GPU 是否可用
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("使用的设备:", device)

try:
    # 加载模型和分词器
    model_name = "microsoft/BioGPT"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

    # 输入提示
    prompt = "The patient was diagnosed with diabetes and"
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

    # 生成文本
    output = model.generate(
        input_ids,
        max_length=100,  # 生成文本的最大长度
        num_return_sequences=1,  # 生成一个序列
        no_repeat_ngram_size=2,  # 避免重复的 n-gram
        top_k=50,  # 使用 top-k 采样
        top_p=0.95,  # 使用 top-p（nucleus）采样
        temperature=0.7,  # 控制生成文本的随机性
        do_sample=True  # 启用采样模式
    )

    # 解码生成的文本
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print("生成的文本:", generated_text)

except Exception as e:
    print("加载模型时出错:", e)