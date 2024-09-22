count=0
i=0
while i<=100:
    count+=i
    i+=1
print(count)

i=0
count=0
for j in range(1,101):
    count+=j
print(count)
# print(j)

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")
    print()

