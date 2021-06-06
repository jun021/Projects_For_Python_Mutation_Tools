def triangle_type(a,b,c):
    print("Enter lenghts of triangle sides:")
    if a<0 or b<0 or c<0:
        return "4=error"
    else:
        if a+b>c and a+c>b and b+c>a:
            if a==b==c:
                return "3=equilateral"
            elif a==b or a==c or b==c:
                return "2=isosceles"
            else:
                return "1=scalene"
        else:
            return "4=error"