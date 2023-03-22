byt_word = b'r\xc3\xa9sum\xc3\xa9'

word = byt_word.decode()

word_latin1 = word.encode('latin1')

word_encode = word_latin1.decode('Latin1')

print(byt_word)
print(word)
print(word_latin1)
print(word_encode)