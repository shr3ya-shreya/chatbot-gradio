"""import gradio as gr

def greet(name):
    return f"Hello, {name}!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch(share=True)
import gradio as gr
import cohere

# Initialize Cohere
co = cohere.Client("YOUR_COHERE_API_KEY")

def chatbot(message, history=[]):
    history_text = "\n".join([f"User: {h[0]}\nBot: {h[1]}" for h in history])
    full_prompt = f"{history_text}\nUser: {message}\nBot:"

    response = co.generate(
        model="command-r",
        prompt=full_prompt,
        max_tokens=100,
        temperature=0.7
    )

    bot_reply = response.generations[0].text.strip()
    return bot_reply

iface = gr.ChatInterface(fn=chatbot)
iface.launch()
"""
import gradio as gr
import cohere

# Initialize Cohere
co = cohere.Client("YOUR_COHERE_API_KEY")

def chatbot(message, history=[]):
    history_text = "\n".join([f"User: {h[0]}\nBot: {h[1]}" for h in history])
    full_prompt = f"{history_text}\nUser: {message}\nBot:"

    response = co.generate(
        model="command-r",
        prompt=full_prompt,
        max_tokens=100,
        temperature=0.7
    )

    bot_reply = response.generations[0].text.strip()
    return bot_reply

iface = gr.ChatInterface(fn=chatbot)
iface.launch()

