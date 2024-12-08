car_speed = int(input('Car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed > speed_limit_max or car_speed < speed_limit_min:
    print('Warning! Invalid speed')