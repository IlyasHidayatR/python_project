# In[]:
# read data from full-list-of-bad-words_text-file_2022_05_05.txt
open_file = open('full-list-of-bad-words_text-file_2022_05_05.txt', 'r')
# read the file
read_file = open_file.read()
# split the file
split_file = read_file.split('\n')
# show the split file
split_file

# In[]:
# put in a list
bad_words = []
for i in split_file:
    bad_words.append(i)
# show the list
bad_words

# In[]:
# input the text
input_text = str(input('Enter the text: '))
# show the input text
word = input_text.split()
# filter the text if text contains bad words or not
for i in word:
    if i in bad_words:
        print('Sorry the word is not allowed')
        break
    else:
        print('The text does not contain bad words')
        break

# %%
