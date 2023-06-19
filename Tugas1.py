def plat_nomor(InputNo,Plat):
    print (f"Database Nomor Kendaraan : {Plat}")

    for i in range(len(Plat)):
        if str(Plat[i]).lower() == InputNo.lower():
            print(f"{InputNo} ada di dalam database")
            return 

    print(f"Nomor Kendaraan {InputNo} Tidak ada di database")
    return -1

data = ['R 2477 SR', 'R 1234 DJ', 'R 7015 LP', 'R 0201 RR', 'R 3304 DA', 
        'R 2401 SK', 'R 2103 RT', 'R 1708 RI', 'R 1111 SR', 'R 4987 LH']
keyword = input("Masukkan Plat Nomor: ")
plat_nomor(keyword, data)