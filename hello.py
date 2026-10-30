# Số lượng sinh viên 
quantity = input("Vui lòng nhập số lượng sinh viên: ")

while not quantity.isdigit():
    print("Số lượng sinh viên không hợp lệ")
    quantity = input("Vui lòng nhập lại số lượng sinh viên: ")
print (f"SỐ LƯỢNG SINH VIÊN LÀ: {quantity} ")

danh_sach_sv = []
# Thông tin sinh viên
for x in range(1, int(quantity) + 1):
    name = input(f"Nhập tên sinh viên thứ {x}: ")
    while not name.replace(" ","").isalpha():
        print("Tên sinh viên không hợp lệ")
        name = input("Vui lòng nhập lại tên sinh viên: ")
    print (f"TÊN CỦA SINH VIÊN THỨ {x} LÀ: {name} ")

    ID = input(f"Nhập MSSV của sinh viên {name}: ")
    while not ID.isdigit():
        print("MSSV không hợp lệ")
        ID = input("Vui lòng nhập lại MSSV: ")
    print (f"MSSV CỦA SINH VIÊN {name} là: {ID} ")

    Toan = input(f"Nhập điểm Toán của sinh viên {name}: ")
    while not Toan.isdigit() or not (0 <=int(Toan) <=10):
        print("Điểm số không hợp lệ")
        Toan = input("Vui lòng nhập lại điểm Toán: ")
    print (f"ĐIỂM TOÁN CỦA SINH VIÊN {name} LÀ: {Toan} ")

    Ly = input(f"Nhập điểm Lý của sinh viên {name}: ")
    while not Ly.isdigit() or not (0 <=int(Ly) <=10):
            print("Điểm số không hợp lệ")
            Ly = input("Vui lòng nhập lại điểm Lý: ")
    print (f"ĐIỂM LÝ CỦA SINH VIÊN {name} LÀ: {Ly} ")

    Hoa = input(f"Nhập điểm Hóa của sinh viên {name}: ")
    while not Hoa.isdigit() or not (0 <=int(Hoa) <=10):
            print("Điểm số không hợp lệ")
            Hoa = input("Vui lòng nhập lại điểm Hóa: ")
    print (f"ĐIỂM HÓA CỦA SINH VIÊN {name} LÀ: {Hoa} ")

# Xếp loại sinh viên
    y = round ((float(Toan) + float(Ly) + float(Hoa))/3, 2)
    print (f"ĐIỂM TRUNG BÌNH CỦA SINH VIÊN {name} LÀ: {y} ")
    if y < 5:
         print (f"SINH VIÊN {name} XẾP LOẠI: YẾU")
    elif 5 <= y <= 6.5:
         print (f"SINH VIÊN {name} XẾP LOẠI: TRUNG BÌNH")
    elif 6.5 <= y < 8:
         print (f"SINH VIÊN {name} XẾP LOẠI: KHÁ")
    else: 
         print (f"SINH VIÊN {name} XẾP LOẠI: GIỎI")

# Sinh viên có thành tích nổi bật nhất:
    danh_sach_sv.append ({
        "ten": name,
        "dtb": y})

top1 = danh_sach_sv[0]
for x in danh_sach_sv:
     if x["dtb"] > top1["dtb"]:
          top1 = x
print (f"HỌC SINH CÓ THÀNH TÍCH XUẤT SẮC NHẤT LÀ {top1["ten"]} VỚI ĐIỂM TRUNG BÌNH {top1["dtb"]}!")