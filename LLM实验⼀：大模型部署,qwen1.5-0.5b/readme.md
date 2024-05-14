# LLM实验一：大模型部署，qwen1.5-0.5b

------



### 一、Qwen1.5-0.5B-Chat-GGUF 模型部署

##### 1.使用download_model.py文件下载代码

```python
from modelscope.hub.file_download import model_file_download

model_dir = model_file_download(model_id='qwen/Qwen1.5-0.5B-ChatGGUF',file_path='qwen1_5-0_5b-chat
q5_k_m.gguf',revision='master',cache_dir='path/to/local/dir')
```

![](Qwen1.5-0.5B-Chat-GGUF/实验记录图/download_py.png)

##### 2.下载llama.cpp

```
git clone https://github.com/ggerganov/llama.cpp
```

![](Qwen1.5-0.5B-Chat-GGUF/实验记录图/git_clone_llama.png)

编译llama.cpp项⽬

![](Qwen1.5-0.5B-Chat-GGUF/实验记录图/编译llama.png)

```
cd llama.cpp
make -j
```

##### 3.加载模型并执行

![](Qwen1.5-0.5B-Chat-GGUF/实验记录图/大模型部署.png)

```
./main -m /mnt/workspace/home/llm/qwen/Qwen1.5-0.5B-Chat-GGUF/qwen1_5-0_5b-chatq5_k_m.gguf -n 512 --color -i -cml
```

------

### 二、Qwen2.openvino 模型部署

##### 1.创建⽬录qwen-ov&&创建Python虚拟环境&&安装依赖的包

![](Qwen2.openvino/实验记录图/requirement文件.png)

```
python -m venv qwenVenv
source qwenVenv/bin/activate

pip install wheel setuptools
pip install -r requirements.txt
```

![](Qwen2.openvino/实验记录图/安装依赖包.png)

##### 2.下载模型

```
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download --resume-download --local-dir-use-symlinks False Qwen/Qwen1.5-0.5B-Chat --
local-dir /mnt/workspace/home/llm/qwen-ov/Qwen1.5-0.5B-Chat
```

![](Qwen2.openvino/实验记录图/下载模型.png)

##### 3.转换模型

```
python3 convert.py --model_id /mnt/workspace/home/llm/qwen-ov/Qwen/Qwen1.5-0.5B-Chat --precision int4 --output /mnt/workspace/home/llm/qwen-ov/Qwen1.5-0.5B-Chat-ov
```

![](Qwen2.openvino/实验记录图/转换模型.png)

##### 4.加载模型并执行

```
python3 chat.py --model_path /mnt/workspace/home/llm/qwen-ov/Qwen1.5-0.5B-Chat-ov --max_sequence_length 4096 --device CPU
```

![](Qwen2.openvino/实验记录图/加载模型并执行.png)

##### 5.模型对话测试

![](Qwen2.openvino/实验记录图/模型对话测试.png)