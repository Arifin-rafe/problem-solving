def is_float(value):
    if value == "0":  
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False

n = int(input())  

items = [input().strip() for _ in range(n)] 

for item in items:
    print(is_float(item))
