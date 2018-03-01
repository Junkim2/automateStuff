import regex, logging, pyperclip

textRegex = regex.compile(r'''
\S:                #group2 Q:
\s*                #group3 space
(\w*\.\s\D*\?)        #group4 question sentence
\s*                #group5 space
''', regex.VERBOSE)
text = pyperclip.paste()
text = textRegex.findall(text)
text = '\n'.join(text)
pyperclip.copy(text)
print(pyperclip.paste())