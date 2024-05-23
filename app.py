# Import dependencies
import gradio as gd
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load the dotenv (.env)
load_dotenv()
genai.configure(api_key=os.getenv("api_key"))
model = genai.GenerativeModel(model_name='gemini-pro')
chat = model.start_chat(history=[])

# Get the model response
def get_model_response(query):
    response = chat.send_message(query,stream=True)
    return response

# Create gradio interface
def interface(message,history):
    response = get_model_response(message)
    r = []
    for chunk in response:
        r.append(chunk.text)
    return "".join(r) # this will return combined response. 

# Create Chat GUI
demo = gd.ChatInterface(fn=interface,title="Gemini Chatbot by Sindhura Nadendla")

# Run the chatbot
if __name__ == '__main__':
    demo.queue().launch()

