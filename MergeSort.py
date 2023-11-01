
def sort_order(P):

    leng = len(P)

    if leng == 1:
        return P
    elif leng == 2:
        Q = []
        if(P[0] < P[1]):
            Q.append(P[0])
            Q.append(P[1])
        else:
            Q.append(P[1])
            Q.append(P[0])
        return Q
    else:
        subleng = 0
        if(leng%2 == 0):
            subleng = leng//2
        else:
            subleng = (leng+1)//2

        P1 = P[0:subleng]
        P2 = P[subleng:leng]


        P1 = sort_order(P1)
        P2 = sort_order(P2) 

        k = len(P1) + len(P2)
        P3 = []
        i = 0
        j = 0

        for n in range(0,k):          
            if(i < len(P1) and j < len(P2) and P1[i] < P2[j]):
                P3.append(P1[i])
                i += 1
            elif(i < len(P1) and j < len(P2) and P2[j] <= P1[i]):
                P3.append(P2[j])
                j += 1
            else:                

                if(i == len(P1) - 1):
                    P3.append(P1[i])
                elif(j == len(P2)-1):
                    P3.append(P2[j])
                elif(j >= len(P2)):
                    for p in range(i,len(P1)):
                        P3.append(P1[p])
                    break
                elif(i >= len(P1)):
                    for p in range(j,len(P2)):
                        P3.append(P2[p])                        
                    break
        return P3


final = sort_order([0,8,9,9,0,1,2,3,4,4,9,9,9,4,4,7,7,2,2,3,3])

print(final)
