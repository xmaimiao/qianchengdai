for i in range(5):
    print(" "*(4-i)+" *"*(i+1))

for i in range(5):
    for y in range(4-i):
        print(" ",end='')
    print(" *"*(i+1))
