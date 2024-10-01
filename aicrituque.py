import openai
import streamlit as st
import os

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)


image_question = input("Enter your prompt here and clearly describe what you want the model to tell you about the image: ")

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "assistant",
      "content": [
        {"type": "text", "text": image_question},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://shorturl.at/erAGY", #Mona Lisa painting
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])                       
