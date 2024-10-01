import openai
import streamlit as st
import os

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)
