n = int(input())

for _ in range(n):
    m = input().split()
    # a= int(m[0])
    if m[0].isdigit():
        a= int(m[0])
    else:
        a= m[0]
    # b= (m[1])
    if m[1].isdigit():
        b= int(m[1])
    else:
        b= m[1]
    try:
        print (a/b)
    except ZeroDivisionError as e:
        print ("Error Code:",e)
        # ll.append("Error Code:",e)
    except TypeError as t:
        print("Error Code:",t)
        # ll.append("Error Code:",t)
