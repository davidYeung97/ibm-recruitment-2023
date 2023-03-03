stock_count = input()
tshirt_stock = input().split(' ')

request_count = input()
req_details = input().split(' ')

tshirt_stock_list = [str(x) for x in tshirt_stock]
req_details_list = [str(x) for x in req_details]

#Sort the list in decending order

# XS < S < M < L < XL < XXL < XXXL
def get_key(item):
    num_x = item.count("X")
    if("S" in item):
        return -num_x
    elif("M" in item):
        return 1
    elif("L" in item):
        return 2 + num_x 

tshirt_stock_list = sorted(tshirt_stock_list, key=get_key, reverse=True)
req_details_list = sorted(req_details_list, key=get_key, reverse=True)

print(tshirt_stock_list)
print(req_details_list)


num_sum = 0
canFufill = True
for i in range(int(request_count)):
    request_item = req_details_list[i]
    stock_item = tshirt_stock_list[i]

    if(get_key(stock_item) < get_key(request_item)):
        canFufill = False
        break

print(canFufill)
