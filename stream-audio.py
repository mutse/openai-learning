import io
import soundfile as sf
import sounddevice as sd
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()

response = client.audio.speech.create(
    model="tts-1-hd",
    voice="nova",
    input="故人西辞黄鹤楼，烟花三月下扬州。孤帆远影碧空尽，惟见长江天际流。",
)

buffer = io.BytesIO()
for chunk in response.iter_bytes(chunk_size=4096):
  buffer.write(chunk)
buffer.seek(0)

with sf.SoundFile(buffer, 'r') as sound_file:
  data = sound_file.read(dtype='int16')
  sd.play(data, sound_file.samplerate)
  sd.wait()
