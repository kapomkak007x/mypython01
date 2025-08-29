print('-------------------------------')
print('โปรเเกรมคำนวณค่าคอมมิชชั่นชองพนักงานขาย')
print('-------------------------------')
user_ID = input('กรุณากรอกไอดีพนักงาน: ')
user_name = input('กรุณากรอกชื่อพนักงาน: ')
user_sales = float(input('กรุณากรอกยอดขาย: '))
if user_sales <= 1000:
    commission = user_sales * 0.00
elif user_sales >= 1001:
    commission = user_sales * 0.01
elif user_sales >= 2001:
    commission = user_sales * 0.03
elif user_sales >= 3001:
    commission = user_sales * 0.05
print('-------------------------------')
print('ไอดีพนักงาน: ', user_ID)
print('ชื่อพนักงาน: ', user_name)
print('ยอดขาย: ', user_sales)
print('ค่าคอมมิชชั่น: ', commission)        
print('--------------------------------')
