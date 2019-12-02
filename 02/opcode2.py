f = open("input2")
my_str = f.read()

for i in range(100):
    for j in range(100):
        data = [int(x) for x in my_str.split(',')]
        data[1] = i
        data[2] = j
        index = 0
        code = data[index]
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

        if data[0] == 19690720:
            print(100 * i + j)