



from datetime import datetime 




print('----------------------')
print(' โปรเเกรมตรวจสอบอายุ')
print('----------------------')
your_name = input('ป้อนชื่อของคุณ: ')
Your_yearborn = int(input('ป้อนปีเกิดของคุณ (พ.ศ.): '))
print('----------------------')

your_age = (datetime.now().year + 543) - Your_yearborn
if your_age >= 35:
    print(f'สวัสดีคุณ {your_name}')
    print(f'คุณเกิดในปี พ.ศ. {Your_yearborn} ตอนนี้คุณอายุ {your_age}')
    print(f'คุณเเก่เเล้วนะ Too OLD MATE')
else:
    print(f'สวัสดีคุณ {your_name}')
    print(f'คุณเกิดในปี พ.ศ. {Your_yearborn} ตอนนี้คุณอายุ {your_age}')
    print(f'คุณยังไม่เเก่นะ Still Young MATE')

print('----------------------')
print('goback to your home lads ;)')



