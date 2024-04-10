from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from peft import PeftModel

def merge_lora(lora_path, model_path, output_dir)
    # 加载模型配置
    config = AutoConfig.from_pretrained(model_path)
    # 加载模型
    model = AutoModelForCausalLM.from_pretrained(model_path, config=config, low_cpu_mem_usage=True)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    # 加载lora配适器
    p_model = PeftModel.from_pretrained(model, model_id=lora_path)
    # 合并并保存
    merge_model = p_model.merge_and_unload()
    merge_model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    config.save_pretrained(output_dir)

if __name__ == "__main__":
    lora_path = "lemonilia/LimaRP-perscengen-v5"
    model_path = "Yarn-Llama-2-7b-64k"
    output_dir - "merge_model/"
    merge_lora(lora_path, model_path, output_dir)