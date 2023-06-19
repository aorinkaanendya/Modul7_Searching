def linear_search (keyword, data):
    for i in range(len(data)):
        # merubah data dari string ke integer
        # lower = digunakan untuk menamaratakan huruf menjadi 
        # huruf kecil (misal ada yang kapital)
        if str(data[i]).lower() == keyword.lower():
            print(f"Keyword {keyword} has found at index {i}")
            return i
    print(f"Keyword {keyword} not found")
    return -1

data = [23, 3, 4, 78, 9, 10, 32]
keyword = input("Input Keyword :")
linear_search(keyword, data)