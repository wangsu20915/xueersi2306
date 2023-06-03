# 计算基本平面图形的面积

# 三角形
def square_triangle(a,h):
    """
    a:底
    h:高
    """
    print( a*h/2)

# 矩形（长方形）
def square_rectangle(a,b):
    """
    a:长
    b:宽
    """
    print( a*b)

# 正方形
def square_square(a):
    """
    a:边长
    """
    print( a**2)

# 平行四边形
def square_parallelogram(a,h):
    """
    a:底
    h:高
    """
    print( a*h)

# 梯形
def square_trapezoid(a,b,h):
    """
    a:上底
    b:下底
    h:高    
    """
    print( (a+b)*h/2)

# 圆
def square_circle(r,π=3.14):
    """
    r:半径
    π:圆周率(默认3.14)
    """
    print( r**2*π)

def help():
    print("""# 三角形
def square_triangle(a,h):
    /"/"/"
    a:底
    h:高
    /"/"/"
    return a*h/2

# 矩形（长方形）
def square_rectangle(a,b):
    /"/"/"
    a:长
    b:宽
    /"/"/"
    return a*b

# 正方形
def square_square(a):
    /"/"/"
    a:边长
    /"/"/"
    return a**2

# 平行四边形
def square_parallelogram(a,h):
    /"/"/"
    a:底
    h:高
    /"/"/"
    return a*h

# 梯形
def square_trapezoid(a,b,h):
    /"/"/"
    a:上底
    b:下底
    h:高    
    /"/"/"
    return (a+b)*h/2

# 圆
def square_circle(r,π=3.14):
    /"/"/"
    r:半径
    π:圆周率(默认3.14)
    /"/"/"
    return r**2*π""")

def main():
    help()
    while True:
        i = input("使用函数以进行计算：")
        if i == "exit()":
            break
        else:
            try:
                exec("s = "+i)
            except:
                print("语法错误")

if __name__=="__main__":
    main()