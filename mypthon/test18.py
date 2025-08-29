print('---------------------------')
print(     'โปรเเกรมเเสดงข้อความต้อนรับนักศึกษา' )
print('---------------------------')
id_student = input('ป้อนรหัสนักศึกษา: ')
name_student = input('ป้อนชื่อนักศึกษา: ')
year_student = int(input('ป้อนปีการศึกษาที่เข้า: '))
print('---------------------------')
if year_student == 1:
    print(f'สวัสดีคุณ {name_student}')
    print(f'นักศึกษารหัส {id_student} ชื่อ {name_student} เข้าศึกษาปี {year_student}')
    print('welcome freshman')
elif year_student == 2:
    print(f'สวัสดีคุณ {name_student}')
    print(f'นักศึกษารหัส {id_student} ชื่อ {name_student} เข้าศึกษาปี {year_student}')
    print('welcome sophomore')
elif year_student == 3:
    print(f'สวัสดีคุณ {name_student}')
    print(f'นักศึกษารหัส {id_student} ชื่อ {name_student} เข้าศึกษาปี {year_student}')
    print('welcome junior')
elif year_student == 4:
    print(f'สวัสดีคุณ {name_student}')
    print(f'นักศึกษารหัส {id_student} ชื่อ {name_student} เข้าศึกษาปี {year_student}')
    print('welcome senior')
else:
    print('คุณป้อนปีการศึกษาผิด ที่หลังก็หัดดูดีๆหน่อยนะน้อง..........ป้อนให้มันถูกสิหรือจะมาเเฝงตัว')