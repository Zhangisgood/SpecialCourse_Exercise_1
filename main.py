with open('file_to_read.txt', 'r') as file:
    text = file.read()

terribleNum = text.count('terrible')

words = text.split()

count = 0

for i in range(len(words)):
    if 'terrible' in words[i]:
        count += 1
        if count % 2 == 0:
            words[i] = 'pathetic'
        else:
            words[i] = 'marvellous'

newText = ' '.join(words)

if terribleNum % 2 == 0:
    newText = newText.replace('terrible', 'pathetic', terribleNum - 1)
else:
    newText = newText.replace('terrible', 'marvellous', terribleNum - 1)

with open('result.txt', 'w') as resultFile:
    resultFile.write(newText)

print(f'The total times "terrible" appears: {terribleNum}')