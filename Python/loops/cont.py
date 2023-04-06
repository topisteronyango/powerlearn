colors = ['green', 'white', 'blue', 'grey', 'orange', 'black']
myColor = 'grey'
count = 0
while count < len(colors):
    if colors[count] == myColor:
        print('they have my color')

        continue

    count = count + 1

    print(colors[count])
