import re

sarr = input().split()

regp = re.compile(r'[^a-zA-Z]')
reg1 = re.compile(r'[^aeiou][aeiou][^aeiou]e')
reg2 = re.compile(r'e[^aeiou][aeiou][^aeiou]')
count=0
for word in sarr:

    if regp.search(word):
        reg = reg1
    else:
        reg = reg2

    for i in range(len(word)-3):
        if reg.match(word[i:i+4]) is not None:
            count +=1

print(count)

