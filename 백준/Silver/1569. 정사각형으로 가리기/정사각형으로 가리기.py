import sys
import math
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    i = list(map(int,input().split()))
    l.append(i)
   

def base():

    min_x = l[0][0]
    min_y = l[0][1]
    max_x = l[0][0]
    max_y = l[0][1]
    k = 0
    index = 0
    
    for i in l[1:]:
        if min_x > i[0]:
            min_x = i[0]
        else:
            if max_x < i[0]:
                max_x = i[0]
        if min_y > i[1]:
            min_y = i[1]
        else:
            if max_y < i[1]:
                max_y = i[1]

    if max_x - min_x < max_y - min_y:
        k = max_y - min_y
        index = 1
        
    elif max_x - min_x > max_y - min_y:
        k = max_x - min_x
        index = 0

    else:
        k = max_x - min_x
        index = 2
        
    bound = [[min_x,max_x],[min_y,max_y],k,index]

    return bound


def makesquare(bound):

    k = bound[2]
    sqr_range = [[],[],k]

    if bound[3] == 0:
        y_case1 = range(bound[1][0], bound[1][0]+k)
        y_case2 = range(bound[1][1]-k, bound[1][1])
        x_case = range(bound[0][0],bound[0][1])
        sqr_range[0].append(x_case)
        sqr_range[1].append(y_case1)
        sqr_range[1].append(y_case2)
    
    elif bound[3] == 1:
        x_case1 = range(bound[0][0], bound[0][0]+k)
        x_case2 = range(bound[0][1]-k, bound[0][1])
        y_case = range(bound[1][0],bound[1][1])
        sqr_range[0].append(x_case1)
        sqr_range[0].append(x_case2)
        sqr_range[1].append(y_case)

    else:
        x_case = range(bound[0][0],bound[0][1])
        y_case = range(bound[1][0],bound[1][1])
        sqr_range[0].append(x_case)
        sqr_range[1].append(y_case)

    return sqr_range


def onsquare(sqr_range):

    on = 0
    
    for j in sqr_range[0]:
        for k in sqr_range[1]:
            for i in l:
        
                if i[0] in j and i[1] in [k[0],k[-1]+1]:
                    on += 1
                    
                elif i[1] in k and i[0] in [j[0],j[-1]+1]:
                    on += 1
        
                elif i[0] == j[-1]+1 and i[1] == k[-1]+1:
                    on += 1

            if on == n:
                return sqr_range[2]
        
            else:
                on = 0
                
    return -1


print(onsquare(makesquare(base())))