# Chatbot-Gradio

This project is a simple chatbot interface built using **Gradio** and powered by **Cohere's Command-R model** for generating conversational responses. 
It also includes basic **Natural Language Processing (NLP)** operations using the `nltk` library, such as tokenization and stopword removal.

---

## 🚀 Features

### 🤖 Chatbot with Gradio + Cohere
- Interactive chatbot interface using `gr.ChatInterface`
- Context-aware responses using chat history
- Utilizes Cohere's `command-r` model for text generation

### 📊 NLP Text Processing (NLTK)
- Sentence and word tokenization
- Stopword removal
- Text preprocessing using regex

---

## 🧪 Requirements

Install the necessary libraries:

```bash
pip install gradio cohere nltk
```

## 🛠️ How to Run
Clone the repo
```bash
git clone https://github.com/shr3ya-shreya/chatbot-gradio.git
cd chatbot-gradio
Run the chatbot script

python chatbot.py
```
This will launch a Gradio web UI locally (with a sharable link if share=True is used).

(Optional) Run the NLP processing section separately for basic text cleaning and tokenization.

## 📚 NLTK Notes
To use nltk features, make sure to download the required resources:

python
import nltk
nltk.download('punkt')
nltk.download('stopwords')

## 🤝 Contributions
Pull requests are welcome! If you find bugs or have suggestions, feel free to open an issue or submit a PR.
