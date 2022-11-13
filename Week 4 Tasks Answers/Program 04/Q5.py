def C_into_F(Centigrade):
    return (Centigrade*1.8)+32

def F_into_C(Fahrenheit):
    return (Fahrenheit-32)/1.8

cels = 100
fah= 100
print(cels,"degree Centigrade into Fahrenheit:",C_into_F(cels),"F")
print(fah,"degree Fahrenheit into Centigrade:",F_into_C(fah),"C")