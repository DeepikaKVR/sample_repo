a = int(input("A:"))
x = int(input("X:"))

n = 2
max_x_times = 1
max_a_iter = a
while True:
    if max_a_iter >= x and max_x_times<=3:
        a += 1
        max_x_times += 1
        x = max_x_times*x
        n = 2
        max_a_iter = a
        print("*"*10)
    elif max_x_times<=3:
        print(max_a_iter)
        max_a_iter = a*n
        n += 1
    else:
        break

    
