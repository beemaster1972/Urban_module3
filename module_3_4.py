def single_root_words(root_word,*args):
    return [word for word in args if word.upper().find(root_word.upper())+1 or root_word.upper().find(word.upper())+1]


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)