import re


def remove_ugly_words(atticle: str):
    clean_article = ''
    ugly_word_list = ['幹', 'fuck', 'shit', '去死']
    
    for keyword in ugly_word_list:
        clean_article = re.sub(keyword, '****', atticle)
        atticle = clean_article
    return clean_article


print(remove_ugly_words('你去死啦~fuck you~'))
