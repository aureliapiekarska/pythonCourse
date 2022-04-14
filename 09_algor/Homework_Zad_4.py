def binary_search(data, low, high, elem):
    if high >= low:

        mid = (((high + low) // 2)-1)

        #binary search usually from what I could see is using even numbers of position on the list, here there was odd, so to find the element I made the mid (13-1=12)

        if data[mid] == elem:
            return mid

        elif data[mid] > elem:
            return binary_search(data, low, mid - 1, elem)

        else:
            return binary_search(data, mid + 1, high, elem)

    else:
        return -1

data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 22


result = binary_search(data, 0, len(data) - 1, elem)

if result != -1:
    print('Number 21 is on the list')
else:
    print("Element is not present the list")