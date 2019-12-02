f = open("input2")

my_str = f.read()
data = [int(x) for x in my_str.split(',')]
index = 0
code = data[index]
print(data[data[index+3]])
while 1 == 1:
    if code == 1:
        data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
    elif code == 2:
        data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
    elif code == 99:
        break
    else:
        print("Error")
    
    index = index + 4
    code = data[index]

print(data[0])