from sys import stdin

count = int(input())

sentences = [stdin.readline().strip() for i in range(count)]
for i in range(count):
    words = sentences[i].split(' ')

    for j in range(len(words)):
        word = list(words[j])
        word.reverse()
        words[j] = ''.join(word)

    print(' '.join(words))

