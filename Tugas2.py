def sorting_awal (inputdata,nim):

    for i in range(len(nim)):
        min_index = i
        for j in range(i+1, len(nim)):
            if nim[j] < nim[min_index]:
                min_index = j
        nim[i], nim[min_index] = nim[min_index], nim[i]
    return binary_search(inputdata,nim)

def binary_search(inputdata,nim):
    left = 0
    right = len(nim) - 1
    
    while left <= right : 
        mid = (left+right)//2
        if str(nim[mid]).lower() > inputdata.lower() :
            right = mid - 1
        elif str(nim[mid]).lower() < inputdata.lower() :
            left = mid + 1
        else :
            print(f"\nData Mahasiswa yang hadir: {nim}")
            print(f"Nim : {inputdata} ada dikelas")
            return mid
    
    print(f"\nMahasiswa yang hadir: {nim}")
    print(f"Nim {inputdata} tidak ditemukan")
    return -1


nim = [20103023, 20103002, 20103019, 20103001, 20103017, 
       20103005, 20103011, 20103003, 20103009, 20103021,
       20103006, 20103015, 20103015, 20103007]
inputdata = input("Masukkan Nim : ")
sorting_awal(inputdata,nim)
