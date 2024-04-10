# Merge-lora-to-base
以一个hf的lora适配器为例子，将其合并到base模型
## 依赖
**peft, transformers**
## Lora适配器
lemonilia/LimaRP-perscengen-v5

hf地址：https://huggingface.co/lemonilia/LimaRP-perscengen-v5
## Base模型
Yarn-Llama-2-7b-64k

hf地址：https://huggingface.co/NousResearch/Yarn-Llama-2-7b-64k
## 模型下载
**设置镜像**

    export HF_ENDPOINT=https://hf-mirror.com

**下载模型**

    huggingface-cli download --resume-download --local-dir-use-symlinks False lemonilia/LimaRP-perscengen-v5 --local-dir lemonilia/LimaRP-perscengen-v5

    huggingface-cli download --resume-download --local-dir-use-symlinks False Yarn-Llama-2-7b-64k --local-dir Yarn-Llama-2-7b-64k
## Merge ！
    python merge.py