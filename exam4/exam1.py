#汽车数量为100辆
cars = 100
#每辆车载客4人
space_in_a_car = 4.0
#司机有30人
drivers = 30
#乘客有90人
passengers = 90
#不需要用到的车的数量
cars_not_driven = cars - drivers
#用到的车的数量
cars_drivern = drivers
#载客量
carpool_capacity = cars_drivern * space_in_a_car
#平均每辆车的载客量
average_passengers_per_car = passengers / cars_drivern


print('There are ' , cars , 'cars avaliable.')
print('There are only ' , drivers , 'drivers avaliable.')
print('There will be ' , cars_not_driven , 'empty cars today.')
print('We can transport ' , carpool_capacity , 'people today.')
print('We have ' , passengers , ' to carpool today.')
print('We need to put about ' , average_passengers_per_car , 'in each car.')