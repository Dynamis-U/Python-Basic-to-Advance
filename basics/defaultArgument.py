# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(400))
# print(net_price(400, 0.1))
# print(net_price(400, 0.1, 0))

import time

# def count(start, end):
def count(end, start = 0): # order doesnt matter
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("Done!")

count(10)
