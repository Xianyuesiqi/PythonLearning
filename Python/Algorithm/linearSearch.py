answer = 1024

for x in range(0, 10000):
    if x%2 == 0:
        print(x)
        if x == answer:
            print('found it')
            break
