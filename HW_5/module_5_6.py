def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    for spam in spam_words:
        if not space_around:
            if text.find(spam) > -1:
                return True
        else:
            words = text.split(" ")
            for w in words:
                if w == w.removeprefix(' ') or w == w.removesuffix(' ') or w == w.removesuffix('.'):
                    if w.startswith(spam) or w.endswith(spam):
                        return False
                    else:
                        return True


print(is_spam_words('Молох бог ужасен.', ['лох'], True))

