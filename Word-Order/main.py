# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
 
strings = [input() for _ in range(n)]

dic = {}
for i in strings:
    if i not in dic:
        dic[i] =1
    else:
        dic[i] += 1

count = [dic[i] for i in dic]
print(len(count))

for i in count:
    print(i,end=' ')
