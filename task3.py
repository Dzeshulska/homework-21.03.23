def sort_car_by_auto_park(i) :
    return i[1]
sorted(auto_park, key = price)

def auto_park_price(i) :
   return i.get("price")
sorted(auto_park, key=auto_park_price )

i = 0
for i in range(len(auto_park)) :
    print(auto_park[i])
