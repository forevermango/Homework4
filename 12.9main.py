#Raahima Ahmed
#1892523

parts = input().split()
name = parts[0]

while name != '-1':
    try:
        age = int(parts[1]) + 1
        print("{} {}".format(name, age))
    except:
        print("{} 0".format(name))
    parts = input().split()
    name = parts[0]
