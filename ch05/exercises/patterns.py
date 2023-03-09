def star_pyramid(rows):
    for i in range(0,rows):
        print('*'*i)

def rstar_pyramid(rows):
    for i in range(rows,0, -1):
        print('*'*i)


rows = int(input("How many rows are in your pyramid?:"))

star_pyramid(rows)
rstar_pyramid(rows)