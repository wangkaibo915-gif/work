RED='\033[41m'
BLUE='\033[44m'
WHITE='\033[47m'
END='\033[0m'



line = ' ' * 4
length = 9
height = length


for i in range (height):
    if i < height // 3 :
        print(f'{WHITE}{line * 9}{END}')
    elif i <height // 1.5 :
        print(f'{WHITE}{line * (length // 3)}{END}')
    else :
        print(f'{WHITE}{line * 9}{END}')      
