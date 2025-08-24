import re

def startWithBoldR(text):
    words=text.split()
    for j in range(len(words)):
        if re.search(r"\bر\w*\b", words[j]):
            words[j] = re.sub(r"ر",r"ڕ", words[j])    
    text=' '.join(words)
    return text
text='''
رامانیت ناڤێت کوردی
روژ و شەڤ
زەرزەوات
رەهەند
رەوشەنبیر
'''
print(startWithBoldR(text))