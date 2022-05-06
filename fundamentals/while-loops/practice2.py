# Write a program that continually asks the user to enter
# a word until they enter the word "q" or "quit", at 
# which point the program should print the average length
# of all of the entered words, excluding the "q" or "quit".
# if the user doesn't enter any words, (i.e. immediately
# enters "q" or "quit"), your program shouldn't print 
# anything

word_length_sum = 0
word_count = 0

while True:
    word = input("Enter a word: ")

    if word == "q" or word == "quit":
        break

    word_length_sum += len(word)
    word_count += 1

if word_count > 0:
    average_word_length = word_length_sum / word_count
    print(f"The average word length is: {average_word_length}.")
