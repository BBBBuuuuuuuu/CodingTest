word = input()

for alphabet in range(97, 123):
    print(word.find(chr(alphabet)), '', end='')
