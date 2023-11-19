from dotenv import load_dotenv
from openai import OpenAI
import requests
from io import BytesIO

load_dotenv()
client = OpenAI()

prompt = "best quality,young Chinese girl with long black hair, wearing a white shirt, a white dress"

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  n=1,
  size="1024x1024",
  response_format="url",
  quality="hd"
)
image_url = response.data[0].url
response = requests.get(image_url)

with open('girl.png', 'wb') as f:
    f.write(response.content)
