# put your code here.
my_file = open('test.txt')

#Write a program, wordcount.py, that opens a file, and counts how many times each
#space-separated word occurs in that file. Your program should then print those counts to the screen.

word_count = {}

for line in my_file:
    #working on line in file
    words_list = line.rstrip().split(' ')
    #have list of each word in the line
    punctuation = [',','!','.','?']

    for word in words_list:
        word = word.lower()
        if word[len(word)-1] in punctuation:
            word = word[0:-1]
        word_count[word] = word_count.get(word,0)+1

print word, word_count[word]

#print word_count
print word_count.items()
# for pair in word_count.items()