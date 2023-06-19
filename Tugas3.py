def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

def binary_search(data, keyword):
    sorted_data = insertion_sort(data)
    print(f"Data Sorted: {sorted_data}")
    low = 0
    high = len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_data[mid] == keyword:
            print(f"{keyword} is found at index {mid}")
            return mid
        elif sorted_data[mid] < keyword:
            low = mid + 1
        else:
            high = mid - 1

    print(f"{keyword} is not found")
    return -1

data = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]
keyword = 72
binary_search(data, keyword)
