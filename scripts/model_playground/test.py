import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def get_generation_params(level):
    if level in ["A1", "A2"]:
        return {
            "max_length": 100,  # 生成较短的文本 
            "temperature": 0.7,  # 控制生成文本的随机性
            "top_p": 0.9,  # 使用 top-p 采样
            "do_sample": True  # 启用采样模式
        }
    elif level in ["B1", "B2"]:
        return {
            "max_length": 150,
            "temperature": 0.8,
            "top_p": 0.95,
            "do_sample": True
        }
    elif level in ["C1", "C2"]:
        return {
            "max_length": 200,
            "temperature": 0.9,
            "top_p": 0.98,
            "do_sample": True
        }
    else:
        raise ValueError("Invalid English level. Please choose from A1, A2, B1, B2, C1, C2.")
    
def generate_sentence(prompt, level, model, tokenizer, device):
    params = get_generation_params(level)
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    outputs = model.generate(input_ids, **params)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
    
def main():
    # 检查 GPU 是否可用
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("使用的设备:", device)

    try:
        # 加载模型和分词器
        model_name = "microsoft/BioGPT"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

        # 输入英语水平和单词
        # level = input("请输入你的英语水平（A1, A2, B1, B2, C1, C2）: ")
        level = "B2"
        word = input("请输入你想学习的单词或短语: ")
        prompt_sentence1 = f"{word} is"
        prompt_sentence2 = f"{word} is not"
        prompt_sentence3 = f"{word} include"

        # 生成句子
        sentence1 = generate_sentence(prompt_sentence1, level, model, tokenizer, device)
        sentence2 = generate_sentence(prompt_sentence2, level, model, tokenizer, device)
        sentence3 = generate_sentence(prompt_sentence3, level, model, tokenizer, device)
        print(f"1.{sentence1}")
        print(f"2.{sentence2}")
        print(f"3.{sentence3}")

            

    except Exception as e:
        print("加载模型时出错:", e)

if __name__ == "__main__":
    main()
    