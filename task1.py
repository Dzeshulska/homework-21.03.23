import random
auto_park = [
    {   "lable" : "Seat",
        "price" : "15000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
    {   "lable" : "Seat",
        "price" : "16000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
    {   "lable" : "Seat",
        "price" : "20000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
    {   "lable" : "Seat",
        "price" : "25000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
    {   "lable" : "Seat",
        "price" : "75000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
    {   "lable" : "Seat",
        "price" : "95000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
    {   "lable" : "Seat",
        "price" : "100000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
    {   "lable" : "Seat",
        "price" : "120000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
    {   "lable" : "Seat",
        "price" : "150000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
    {   "lable" : "Seat",
        "price" : "170000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
    {   "lable" : "Seat",
        "price" : "200000",
        "wheels" : "4",
        "color" : "Black",
        "number" : random.randint(0,1000000000000),
    },
]
sorted_auto_park = sorted(auto_park, key=int("price"))
if key < 20000:
    print("!")
