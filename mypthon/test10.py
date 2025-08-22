#=====================
# PROGRAM AVERAGE5
#=====================
#
#=====================
numbers = []
print('ป้อนตัวเลขทั้งหมด 5 ตัว')
for i in range(5):
    number = int(input('ป้อนตัวเลขที่ ' + str(i+1) + ' : '))
    numbers.append(number)


sum_of_numbers = sum(numbers)
average_of_numbers = sum_of_numbers/5



print('=====================================')
print(f"ผลรวมของตัวเลขทั้งหมด 5 ตัว {sum_of_numbers}") 
print(f"ค่าเฉลี่ยของตัวเลขทั้งหมดคือ {average_of_numbers/5}")
print('=====================================')

#=====================
# PROGRAM AVERAGE5
#=====================
