import random
def auto_park(lable, price, wheels, color, number):
    return [
    {    "lable" : lable,
         "price" : price,
         "wheels" : wheels,
         "color" : color,
         "number" : random.randint(0,1000000000000),
    } 
    ]
    for i, el in enumerate(auto_park) :
        print(i,el)
