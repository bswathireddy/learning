#str="1,3,4,5"
#arr =[178,89,90,898]
#output=str.split(',')
#sum=0
#output=int(str)
#for i in output:
  #  sum=sum+int(i)
#print(sum)

#reverse an array of string


T=int(input())
for i in range(T):
    n=int(input())
    s=input().split()
    if len(s)==n:
        print(*s[::-1])

#print second largest num in an array
T = int(input())
for i in range(T):
    n = int(input())
    s = input().split()
    if int(s[0]) > int(s[1]):
        m1 = int(s[0])  # 42
        m2 = int(s[1])  # 56
    else:
        m2 = int(s[0])
        m1 = int(s[1])
    # print(m1)
    # print(m2)
    for num in s[2:]:
        num = int(num)
        # print(num)
        if num > m2:
            # print("a")
            # print(num)
            m2 = num
        if m2 > m1:
            m2 = m1
            m1 = num

    print(m2)


# print largest name in a list
T = int(input())
for i in range(T):
    n = int(input())
    output = ""
    for j in range(n):
        x = input()
        if len(x) > len(output):
            output = x
    print(output)


#wave array example
T = int(input())
for i in range(T):
    n = int(input())
    s = input().split()
    for i in range(0, len(s), 2):
        if (i + 1 < n):
            temp = s[i]
            s[i] = s[i + 1]
            s[i + 1] = temp

    print(" ".join(s))     #input=12345 output=21435


#Leaders in an array
    T = int(input())
    for n in range(T):
        N = int(input())
        arrS = input().split()
        output = ''
        for i in range(len(arrS)):
            outputi = True
            for j in range(i + 1, len(arrS)):
                if int(arrS[i]) < int(arrS[j]):
                    outputi = False
                    break
            if (outputi == True):
                if (output == ''):
                    output = arrS[i]
                else:
                    output = output + ' ' + arrS[i]
        print(output)

#leaders in an array 2nd type
T=int(input())
for n in range(T):
    N=int(input())
    arr=input().split()
    output=''
    iarr=[]
    for i in range(len(arr)-1,0):
        maxelement=len(arr[i]-1)
        if int(maxelement)<=int(arr[i]):
            iarr.append(int(arr[i]))
            maxelement=int(arr[i])
        if arr[i]>maxelement:
            output+=arr[i]
        print(output)



        #greater on right side

        T = int(input())
        for n in range(T):
            N = int(input())
            arr = list(map(int, input().split()))
            output = []
            for i in range(0, len(arr) - 1):
                t = max(arr[i + 1:])
                output.append(t)
            output.append(-1)
            print(' '.join(map(str, output)))

# friendly array

T = int(input())
for n in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    output = 0
    for i in range(len(arr)):
        mina = 100000
        minb = 100000
        if (i - 1 >= 0):
            mina = arr[i] - arr[i - 1]
        if (i + 1 < len(arr)):
            minb = arr[i + 1] - arr[i]
        if mina < minb:
            output += mina
        else:
            output += minb
    print(output)

# count pair sum
T = int(input())
for s in range(T):
    N = list(map(int, input().split()))
    m = N[0]
    n = N[1]
    marr = list(map(int, input().split()))
    narr = list(map(int, input().split()))
    x = int(input())
    output = 0
    for i in range(len(marr)):
        for j in range(len(narr)):
            if (marr[i] + narr[j] == x):
                output += 1
    print(output)
#majority element (i,e majority element is > than N/2)
T=int(input())
for n in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    countDict={}
    output=-1
    for i in arr:
        if i in countDict:
            countDict.update({i:countDict.get(i)+1})
            if countDict.get(i)>N/2:
                output=i
                break
        else:
            countDict.update({i:1})
    print(output)

# unique number
T=int(input())
for i in range(T):
    N=input().split()
    n=N[0]
    k=N[1]
    arr=list(map(int,input().split()))
    countDict={}
    output=0
    for i in arr:
        if i in countDict:
            countDict.update({i:countDict.get(i)+1})
        else:
            countDict.update({i:1})
    for j in countDict:
        val = countDict.get(j)
        if val ==1:
            print(j)
            break

            # print given lowercase alphabets in alphabetical order
            T = int(input())
            for n in range(T):
                text = sorted(input())
                print("".join(text))

                # print first repeated character in string
                T = int(input())
                for n in range(T):
                    s = input()
                    output = -1
                    for i in range(len(s)):
                        for j in s[i + 1:]:
                            if s[i] == j:
                                output = s[i]
                                break
                        if output != -1:
                            break
                    print(output)

    #adding ones to N by K pointing element of k in N
    T = int(input())
    for n in range(T):
        L1 = list(map(int, input().split()))
        N = L1[0]
        K = L1[1]
        Karr = list(map(int, input().split()))
        Narr = [0] * N
        for i in Karr:
            for j in range(i - 1, len(Narr)):
                Narr[j] = Narr[j] + 1
        Narr = map(str, Narr)
        print(' '.join(Narr))





