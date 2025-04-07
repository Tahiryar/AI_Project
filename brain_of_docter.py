import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

//convert img to binary

import base64

img_path='img.png'

img_file=open(img_path,'rb')

encoded_img=base64.b64encode(img_file.read()).decode('utf-8')

//setup multimodal LLM

from groq import Groq

client=Groq()
model="llama-3.2-90b-vision-preview"

