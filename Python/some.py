names = ['Topi', 'Nandera', 'Betty', 'Onyango']
count = 0
# for loop with indexes

while count < len(names):
    print(count, names[count])
    count = count + 1

# for loop without indexes

while count < len(names):
    print(names[count])
    count = count + 1
# for loop with indexes

for idx, i in enumerate(names):
    print(idx, i)

# for loop without indexes
for i in (names):
    print(i)