# กรณี 1 print(1) มีข้อมูลหลายประเภททำไง ดีนะะะะะะะะ มี 4วิธี
print('hello',5555,'wow','jesus',True,'sunshine',20+50-24,4465.1048)

# วิธีที่ 2 ใช้ + (ข้อมูลไม่ใช้ sting ต้องทำให้เป็น sting ใช้ฟังก์ชัน str())
print('hello'+str(555)+'wow'+str(999)+str(True)+'HI'+str(10+20-5)+str(152.875))
print('hello'+str(555)+'wow'+str(999)+'True'+'HI'+"25"+(152.875))

# วิธีที่ 3 ใช้ format() โดยข้อมูลที่แสดงอยู่ในของ string
print('hello{}wow {} {} HI {} {}'.format(555,999,True,'HI',25,152.875))

#index nimber
print('{4} {2}'.format('a','b','c','d'))

#วิธีที่  4 ใช้ f-string
print(f'hello {555} wow {999} {True} HI {10+20-5} {152.875}')