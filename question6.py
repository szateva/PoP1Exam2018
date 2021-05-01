""" You are given the following input:
3
apple orange banana banana orange
banana grapefruit banana apple orange
orange grapefruit banana apple
Where the first line contains the number of lines of input and the successive lines
contain a list of words. Print the word in each line of text that occurs most often. If
there are several such words, print the one that is less in the alphabetical order.
For the sample input the output would be:
banana
banana
apple """

lines = int(input("How many lines of input will there be? "))
d = dict()
key_values = []

for i in range(lines):
    line_in = input("Type in the words: ").split()
    line_in_len = len(line_in)
    for j in range(line_in_len):
        if line_in[j] in d:
            d[line_in[j]] += 1
        else:
            d[line_in[j]] = 1
    sorted(d.items())
    MaxKey = max(d, key=d.get)
    key_values.append(MaxKey)

for items in key_values:
    print(items, sep='\n')




