def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) -i -1):
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j+1], data[j]
    return data

def binary_search(keywords, data):
    sorted_data = bubble_sort(data)
    print(f"Data (Sorted) = {sorted_data}")
    left = 0
    right = len(sorted_data) - 1

    while left <= right:
        mid = (left + right)//2
        str_data = str(sorted_data[mid]).lower()
        if str_data > keywords.lower():
            right = mid - 1
        elif str_data < keywords.lower():
            left = mid + 1
        else:
            print(f"Keyword {keywords} has found at index {mid}")
            return mid
    print(f"Keyword {keywords} not found")
    return -1

data = [23, 3, 4, 78, 9, 10, 32]
keywords = input("Input Keyword : ")
binary_search(keywords, data)