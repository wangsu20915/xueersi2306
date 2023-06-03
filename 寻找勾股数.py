# 寻找勾股数
def find_Pythagorean_number(max_num=10):
    list_Pythagorean_number = list()
    for a in range(1,max_num+1):
        for b in range(1,max_num+1):
            for c in range(1,max_num+1):
                if a**2+b**2==c**2 and not (b,a,c) in list_Pythagorean_number:
                    list_Pythagorean_number.append((a,b,c))
    
    return list_Pythagorean_number,len(list_Pythagorean_number)

find_Pythagorean_number(10000)
        