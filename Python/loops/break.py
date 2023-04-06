colors = ['green', 'white', 'blue', 'grey', 'orange', 'black']
myColor = 'grey'

for color in colors:
    if color == myColor:
        print('They have my color')
        # print(color)
        break

    print(color)

colors = ['green', 'white', 'blue', 'grey', 'orange', 'black']
myColor = 'grey'
count = 0
while count < len(colors):
    if colors[count] == myColor:
        print('they have my color')
        break

    print(colors[count])
    count = count + 1
