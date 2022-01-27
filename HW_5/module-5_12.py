import re


def replace_spam_words(text, spam_words):
    for words in spam_words:
      num = len(words)
      text = re.sub(words,num *"*", text, flags=re.IGNORECASE)
    print(text)
    return text
