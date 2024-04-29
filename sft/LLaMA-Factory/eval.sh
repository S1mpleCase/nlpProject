#!/bin/bash
export USE_MODELSCOPE_HUB=1 # `set USE_MODELSCOPE_HUB=1` for Windows

CUDA_VISIBLE_DEVICES=0 python src/evaluate.py \
    --model_name_or_path qwen/Qwen1.5-4B  \
    --adapter_name_or_path saves/Qwen4/lora/sft \
    --template fewshot \
    --task mmlu \
    --split test \
    --lang en \
    --n_shot 5 \
    --batch_size 4
