print('******************************')
print('*********6719410014***********')
print('******************************')
print('1.พื้นที่สี่เหลี่ยม')
print('2.พื้นที่วงกลม')
print('3.พื้นที่สามเหลี่ยม')
print('4.ปริมาตรทรงกลม')
print('0.ออกจากการทำงาน')
menu = int(input('เลือกเมนูที่ต้องการ : '))
import math
while menu != 0:
    if menu == 1:
        print('คำนวณพื้นที่สี่เหลี่ยม')
        width = float(input('ป้อนความกว้าง : '))
        height = float(input('ป้อนความสูง : '))
        area = width * height
        print(f'พื้นที่สี่เหลี่ยม เท่ากับ : {area:.2f}')
        print('******************************')
    elif menu == 2:
        print('คำนวณพื้นที่วงกลม')
        radius = float(input('ป้อนรัศมี : '))
        area = math.pi * radius ** 2
        print(f'พื้นที่วงกลม เท่ากับ : {area:.2f}')
        print('******************************') 
    elif menu == 3:
        print('คำนวณพื้นที่สามเหลี่ยม')
        base = float(input('ป้อนฐาน : '))
        height = float(input('ป้อนความสูง : '))
        area = 0.5 * base * height
        print(f'พื้นที่สามเหลี่ยม เท่ากับ : {area:.2f}')
        print('******************************')
    elif menu == 4:
        print('คำนวณปริมาตรทรงกลม')
        radius = float(input('ป้อนรัศมี : '))
        volume = (4/3) * math.pi * radius ** 3
        print(f'ปริมาตรทรงกลม เท่ากับ : {volume:.2f}') 
        print('******************************')
    else:
        print('เมนูที่เลือกไม่ถูกต้อง')
        print('กรุณาเลือกเมนู 1,2,3,4 หรือ 0 เท่านั้น')

    
    print('******************************')
    menu = int(input('เลือกเมนูที่ต้องการ : '))
