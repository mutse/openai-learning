from dotenv import load_dotenv
from openai import OpenAI

import gradio as gr

load_dotenv()
client = OpenAI()


def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages= history_openai_format,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message

gr.ChatInterface(predict).queue().launch(share=True)
