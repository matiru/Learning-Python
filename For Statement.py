word_list = ['Python','Chair','Shaa']

for word in word_list:
    if len(word) < 3:
        print('I do not like the word: '+ word)
    else:
        print('I like the word:' + word)
        
        
        
words = ('red', 'purple', 'blue', 'green', 'yellow', 'orange')
target_letter = input('Enter a letter to count >')
count = 0
for word in words:
  for letter in word:
    if letter == target_letter:
      count = count + 1
print(count)


#Question 1
#Write a program that prompts the user to enter some words as shown in the sample run. Then output a list that contains these words. Then output the input version and uppercase version of each word on the same line, separated by a space, as shown in the sample run:

my_string= input("Enter some words >")
my_list = my_string.split()
print(my_list)

for word in my_list:
    print(word +' '+ word.upper())
