from modelscope.hub.file_download import model_file_download

model_dir = model_file_download(model_id='qwen/Qwen1.5-0.5B-Chat-GGUF',file_path='qwen1_5-0_5b-chat-q5_k_m.gguf',revision='master',cache_dir='path/to/local/dir')