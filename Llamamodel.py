from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from itertools import islice
from getComment import YtComments

URL = "https://www.youtube.com/watch?v=oifHmvakt7g&ab_channel=YoutubeItaliaClip"
comm = YtComments()

model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)

lcpp_llm = None
lcpp_llm = Llama(
    model_path=model_path,
    n_threads=2, # CPU cores
    n_batch=512, # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
    n_gpu_layers=32 # Change this value based on your model and your GPU VRAM pool.
    )

comments = comm.GetComments(URL)

for comment in islice(comments, 10):
  user_message=comment["text"]
  system_prompt='''you are a sentiment analist, your job is to classify the prompt of the user between this categories: angry,charmed, sarcastic and amused. you only answer with the sentiment you classified. if you don't know the sentiment answer "i don't know'''
  prompt_template=f'''
  <s>[INST] <<SYS>>
  {system_prompt}
  <</SYS>>

  {user_message} [/INST]
  '''
  
  response=lcpp_llm(prompt=prompt_template, max_tokens=256, temperature=0.6, top_p=0.95,
                    repeat_penalty=1.2, top_k=150,
                    echo=True)
  
  print(response["choices"][0]["text"])