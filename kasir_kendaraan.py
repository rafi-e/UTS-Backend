print("==========")
print("Program Kasir Dealer Kendaraan")
print("Selamat Datang Di Dealer Python")
print("Masukkan identitas anda")
pesan = []
nama = input('Nama Panjenengan :')
hp = int(input('No.HP/WA :'))
while True:
    menu_pilihan = input(' Masukkan Jenis Kendaraan 1-4: \n 1.Mobil\n 2.Sepedah Motor\n 3.Bicycle\n 4.Tank\n ')
    if menu_pilihan == "1":
        print("==========")
        print("Anda memilih kategori nomor 1 : Mobil")
        print("Jenis Mobil")
        car = ["BMW", "Tesla", "Ferari","Kijang"]
        while True:
            for ii in range(0, len(car)):
                print(f'{ii + 1}.{car[ii]}')
            list_car = int(input(f"Masukkan jenis Mobil yang diinginkan? [1-{len(car)}]: "))
            if list_car <= len(car):
                pesan.append(car[list_car-1])
                for iii in range(0,len(pesan)):
                    print(f'{iii+1}.{pesan[iii]} ')
                break
            else:
                print("Silakan Masukkan Jenis Mobil Yang Benar")
                continue
    elif menu_pilihan == "2":
        print("==========")
        print("Anda memilih kategori nomor 2 : Sepedah Motor")
        print("Jenis Sepedah Motor")
        spedah = ["Vario","Nmax","Scoopy","Vespa"]
        while True:
            for ii in range(0, len(spedah)):
                print(f'{ii + 1}.{spedah[ii]}')
            list_spedah = int(input(f"Masukkan jenis Sepedah Motor yang diinginkan? [1-{len(spedah)}]: "))
            if list_spedah <= len(spedah):
                pesan.append(spedah[list_spedah-1])
                for iii in range(0,len(pesan)):
                    print(f'{iii+1}.{pesan[iii]} ')
                break
            else:
                print("Silakan Masukkan Jenis Sepedah Motor Yang Benar")
                continue
    elif menu_pilihan == "3":
        print("==========")
        print("Anda memilih kategori nomor 3 : Bicycle")
        print("Jenis Sepeda")
        pancal = ["Sepeda Gunung","BMX","Sepeda Lipat","Sepeda Ontel"]
        while True:
            for ii in range(0, len(pancal)):
                print(f'{ii + 1}.{pancal[ii]}')
            list_pancal = int(input(f"Masukkan Jenis Sepeda yang diinginkan? [1-{len(pancal)}]: "))
            if list_pancal <= len(pancal):
                pesan.append(pancal[list_pancal-1])
                for iii in range(0,len(pesan)):
                    print(f'{iii+1}.{pesan[iii]} ')
                break
            else:
                print("Silakan Masukkan Jenis Sepeda Yang Benar")
                continue
    elif menu_pilihan == "4":
        print("==========")
        print("Anda memilih kategori nomor 4 : Tank")
        print("Jenis Tank")
        tank = ["Tank Leopard 24AD","Tank F V101 Scorpion","Tank Doosan Tarantula 90","Tank Pindad Harimau 105 MT"]
        while True:
            for ii in range(0, len(tank)):
                print(f'{ii + 1}.{tank[ii]}')
            list_tank = int(input(f"Masukkan Jenis Tank yang diinginkan? [1-{len(tank)}]: "))
            if list_tank <= len(tank):
                pesan.append(tank[list_tank-1])
                for iii in range(0,len(pesan)):
                    print(f'{iii+1}.{pesan[iii]} ')
                break
            else:
                print("Silakan Masukkan Jenis Tank Yang benar")
                continue
    else:
        print(" Kategori Tidak Tersedia")
        continue

    validasi_menu= input('Ada yang ingin ditambahkan[Y/N]? ')
    if validasi_menu == "Y" or validasi_menu == "y":
        continue
    else:
        print(f'Nama Panjang : {nama}')
        print(f'No.HP/WA : {hp}\n')
        print('Kendaraan yang anda Beli:')
        for g in range(0,len(pesan)):
            print(f'{g+1}.{pesan[g]} x1')
        print("\nTerima Kasih Kendaraan Anda Sedang OTW")
        break