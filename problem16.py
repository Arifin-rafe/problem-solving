# first input total number of shoes
# second input all size of shoes
#total buyers

from collections import Counter

shoes = input("Total number of shoes : ")
size = input("Total size of shoes : ").split()
buyers = input("Total number of buyers : ")
myList = [int(x) for x in size]
my_counter_list = Counter(myList) #if you use counter it behave like a dictionary so you can modify the value
print(my_counter_list)

sell_price = []
total_price = 0

for _ in range(int(buyers)):
    size, price = input("Your size and price : ").split()
    size = int(size)
    price = int(price)

    # Check if the size exists in the Counter
    if my_counter_list[size] > 0:
        print(my_counter_list[size])
        # If it exists, reduce the count
        my_counter_list[size] -= 1
        print(my_counter_list)
        sell_price.append(price)
        print(f"Selling size {size} for price {price}. Remaining count: {my_counter_list[size]}")
    else:
        print(f"Size {size} not available.")

print("Sell Prices:", sell_price)

# Calculate total price
total_price = sum(sell_price)
print("Total Price:", total_price)


# from collections import Counter

# shoes = input("Total number of shoes : ")
# size = input("Total size of shoes : ").split()
# buyers = input("Total number of buyers : ")
# myList = [int(x) for x in size]
# my_counter_list = Counter(myList)
# print(my_counter_list)
# my_counter_list_items = Counter(myList).items()
# print(my_counter_list_items)
# my_counter_list_items_keys = Counter(myList).keys()
# my_counter_list_items_values = Counter(myList).values()
# print(my_counter_list_items_keys)
# print(my_counter_list_items_values)
# sell_price = []
# total_price = 0

# for _ in range(int(buyers)):
#     size,price = input("Your size and price : ").split()
#     size = int(size)
#     price = int(price)
#     for s_size in my_counter_list_items_keys:
#         if s_size == int(size):
#             key_index = list(my_counter_list_items_keys).index(s_size) #here key 6 index is 4
#             print(key_index)
#             value_index= list(my_counter_list_items_values)[key_index] #here 4 is index and value is 1
#             print(value_index)
#             list(my_counter_list_items_values)[key_index] -=1
#             print(list(my_counter_list_items_values))
#             print(f"the key index {key_index} value is {value_index}")           
#             sell_price.append(int(price))
                       
#     print(sell_price)
      
# for price in sell_price:
#     total_price += price
# print(total_price)
    
        


# if len(myList)< shoes:
#     print(f"Total will be {shoes}")
    

# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print (Counter(myList))
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

# print (Counter(myList).items())
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
 
# print (Counter(myList).keys())
# [1, 2, 3, 4, 5]
 
# print (Counter(myList).values())
# [3, 4, 4, 2, 1]