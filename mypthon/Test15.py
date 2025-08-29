print('-----------------------------')
print('       ตรวจสอบสภาพรถ')
print('-----------------------------')
car_owner= input('ป้อนชื่อเจ้าของรถ: ')
car_number = input('ป้อนทะเบียนรถ: ')
car_carbon = float( input('ป้อนปริมาณก๊าซคาร์บอนไดซ์ออกไซด์: '))
print('-----------------------------')

if car_carbon > 678.55:
    print(f'สวัสดีคุณ {car_owner}')
    print(f'เจ้าของรถ {car_owner} ทะเบียน {car_number} มีสภาพรถผ่าน')
else:
    print(f'สวัสดีคุณ {car_owner}')
    print(f'เจ้าของรถ {car_owner} ทะเบียน {car_number} มีสภาพรถไม่ผ่าน')

print('-----------------------------')
print('goback to your home lads ;)')




