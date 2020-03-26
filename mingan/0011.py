import re
def word_check(input_word,filtered_word):
    for word in filtered_word:
        if word in filtered_word:
            return 'Freedom'
        else:
            return 'Human Rright'

file=open('filtered_words.txt')
print(file)
filter_word=[line.replace('\n','') for line in file]
print(filter_word)
print(word_check('程序员',filter_word))

def word_change(input_word,filtered_word):
    result=input_word
    for word in filtered_word:
        if word in result:
            new_str='*'*len(word)
            result=str(result).replace(word,new_str)
    return result

file=open('filtered_words.txt')
#print(file)
filter_word=[line.replace('\n','') for line in file]
#print(filter_word)
print(word_change('程序员在上班',filter_word))