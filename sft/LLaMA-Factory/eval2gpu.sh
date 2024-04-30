#!/bin/bash
export USE_MODELSCOPE_HUB=1 # `set USE_MODELSCOPE_HUB=1` for Windows

CUDA_VISIBLE_DEVICES=0,1,2,3 accelerate launch \
    --config_file single_config.yaml \
    src/evaluate.py \
    --model_name_or_path qwen/Qwen1.5-7B  \
    --template fewshot \
    --task mmlu \
    --split test \
    --lang en \
    --n_shot 5 \
    --batch_size 1
