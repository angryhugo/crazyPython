string="Hello Python!"

print('length:'+str(len(string)))#不能直接连接非字符串值与字符串
print('length:%d' % len(string))
print(string.upper())

#pig latin game
pyg_suffix = 'ay'

original = raw_input('Enter a word:').lower()
first_letter = original[0]
new_word = (original + first_letter + pyg_suffix)
new_word = new_word[1:len(new_word)]

if len(original) > 0 and original.isalpha():
    print new_word
else:
    print 'Input invalid!'

