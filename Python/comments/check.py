# # # 
# # x = 4
# # print(type(x))
# # name = 'Testing'
# # print(len(name))
# # x = {}
# # x[2]=[10]
# # x[1]=[20, 30, 40]
# # print(x[1][2])
# # # name = input("What is your name? ")
# # # print(name)
# # num = 2
# # del num
# # # print(num)
# # languages = ['Python', 'C', 'C++', 'Java']
# # del languages[0:2]
# # print(languages)


# # d = {'foo': 100, 'bar': 200, 'baz': 300}
# # print(d['bar':'baz'])



# d1 = {'foo':100, 'bar':200, 'baz':300}

# d2 = {}
# d2.update(d1.items())
# print(d2)

for i in range(5):
    if i == 2:
        continue
    print(i)
