import re

def clear_text(text):
    text = str(text).lower()
    text = re.sub(r'https?://\S+ |www\. \S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    return text.strip()