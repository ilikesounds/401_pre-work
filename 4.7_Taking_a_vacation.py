def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city.lower() == 'charlotte':
        return 183
    elif city.lower() == 'tampa':
        return 220
    elif city.lower() == 'pittsburgh':
        return 222
    elif city.lower() == 'los angeles':
        return 475

def rental_car_cost(days):
    if days < 3:
        return days * 40
    elif days >= 3 and days < 7:
        return (days * 40) - 20
    elif days > 6:
        return (days * 40) - 50

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print trip_cost('los Angeles', 5, 600)
