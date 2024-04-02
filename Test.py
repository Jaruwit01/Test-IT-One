Grades = [int(x) for x in input("Enter the grades: ").split()]

def Average (Grades):  # function หาค่าเฉลี่ยเกรด โดยใข้ sum ของ list และหารด้วย len ของ list
    return round(sum(Grades) / len(Grades), 2)

def Highest (Grades): # finctoin หาค่าสูงสุดของเกรด โดยใช้ฟังก์ชัน max
    return max(Grades)

def Lowest(Grades):# finctoin หาค่าต่ำสุดของเกรด โดยใช้ฟังก์ชัน min
    return min(Grades)

dict_grades = {} # สร้าง dictionary  เปล่าๆเพื่อเก็บค่าเกรดและเกรดที่ได้

for i in Grades:  # loop check และแยกเกรดจากนั้นเก็บใน dictionary
    if i >= 95:
        dict_grades[i] = "A"
    elif i <= 94 and i >= 85:
        dict_grades[i] = "B"
    elif i <= 84 and i >= 75:
        dict_grades[i] = "C"
    elif i <= 74 and i >= 65:
        dict_grades[i] = "D"
    else:
        dict_grades[i] = "F"
        
def Grade_count(dict_grades): # Function นับจำนวนของเกรดที่แบ่งได้ ใน dictionary
    count = {}
    for i in dict_grades.values():
        count[i] = count.get(i, 0) + 1
    return count
        
print("Average grade : ", Average(Grades))
print("Highest grade : ", Highest(Grades))
print("Lowest grade : ", Lowest(Grades))
print("Grade count : ")
for j in sorted(Grade_count(dict_grades).items()):
    print(j[0] ,": ", j[1])


# testCases1 = [100 90 80 70 60 50]
# testCases2 = [55 90 69 84 60 99]
# testCases3 = [45 78 55 70 96 50]
# testCases4 = [100 72 66 87 64 50]