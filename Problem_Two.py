'''
problem 2: Mission Impossible
King Shan now would like to visit Hallitharam and RK Puram on the same day. Write code to determine which orbits
& vehicle he should take to visit both destinations in the quickest possible time.
'''

def getvehicles(climate):
    '''
    :param climate: type of climate
    :return: Based on climete, return available vehicles
    '''

    Bike = {'name':'Bike','speed_in_Km': 10, 'crater_speed_in_Min': 2}
    Tuktuk = {'name':'Tuktuk','speed_in_Km': 12, 'crater_speed_in_Min': 1}
    Car = {'name':'Car','speed_in_Km': 20, 'crater_speed_in_Min': 3}
    if climate == "Sunny":
        return [[Bike,Tuktuk,Car],-0.1]
    elif climate == "Rainy":
        return [[Car, Tuktuk],0.2]
    else:
        return [[Car,Bike],0.0]

def get_orbit_Time(vehicles,taffic_speed,orbit_distance,craters_count):
    '''

    :param vehicles: Based on Climate, gets the available vehicles
    :param taffic_speed: orbit traffic speed
    :param orbit_distance: orbit distance
    :param craters_count: Number of craters in particular orbit
    :return: [Vehicle Details,minimum Time takes to travel in Minutes, Craters change ]
    '''
    orbit_1_vehicles_time=[]
    for i in vehicles[0]:
        if taffic_speed <= i['speed_in_Km']:
            temp_speed=taffic_speed
        else:
            temp_speed=i['speed_in_Km']
        temp= (orbit_distance+(vehicles[1]*craters_count))*i['crater_speed_in_Min']+(60/temp_speed)*orbit_distance
        orbit_1_vehicles_time.append(temp)

    return [vehicles[0][orbit_1_vehicles_time.index(min(orbit_1_vehicles_time))],min(orbit_1_vehicles_time),vehicles[1]]
def getMinPath(climate,traffic_speed_orbit1,traffic_speed_orbit2,traffic_speed_orbit3,traffic_speed_orbit4):
    '''

    :param climate: User input  CLimate
    :param traffic_speed_orbit1: Orbit 1 Traffic Speed
    :param traffic_speed_orbit2: Orbit 2 Traffic Speed
    :param traffic_speed_orbit3: Orbit 3 Traffic Speed
    :param traffic_speed_orbit4: Orbit 4 Traffic Speed
    :return: Shortest time and Vehicle details
    '''
    print("Weather is  ", climate)
    print("Orbit1 traffic speed is {0} megamiles/hour".format(traffic_speed_orbit1))
    print("Orbit2 traffic speed is {0} megamiles/hour".format(traffic_speed_orbit2))
    print("Orbit3 traffic speed is {0} megamiles/hour".format(traffic_speed_orbit3))
    print("Orbit4 traffic speed is {0} megamiles/hour".format(traffic_speed_orbit4))
    vehicles=getvehicles(climate)
    orbit1=get_orbit_Time(vehicles=vehicles,taffic_speed=traffic_speed_orbit1,orbit_distance=18,craters_count=20)
    orbit2 = get_orbit_Time(vehicles=vehicles,taffic_speed= traffic_speed_orbit2, orbit_distance=20, craters_count=10)
    orbit3=get_orbit_Time(vehicles=vehicles,taffic_speed=traffic_speed_orbit3,orbit_distance=30,craters_count=15)
    orbit14=get_orbit_Time(vehicles=[[orbit1[0]],orbit1[2]],taffic_speed=traffic_speed_orbit4,orbit_distance=15,craters_count=18)
    orbit24=get_orbit_Time(vehicles=[[orbit2[0]],orbit2[2]],taffic_speed=traffic_speed_orbit4,orbit_distance=15,craters_count=18)
    orbit34=get_orbit_Time(vehicles=[[orbit3[0]],orbit3[2]],taffic_speed=traffic_speed_orbit4,orbit_distance=15,craters_count=18)
    if (orbit14[1]+orbit1[1] < orbit24[1]+orbit2[1]) and (orbit14[1]+orbit1[1] < orbit34[1]+orbit3[1]):
        print("Vehicle {0} to Hallitharam Via Orbit1 and RK Puram via Orbit4".format(orbit14[0]['name']))
    elif (orbit24[1]+orbit2[1] < orbit14[1]+orbit1[1]) and (orbit24[1]+orbit2[1] < orbit34[1]+orbit3[1]) :
        print("Vehicle {0} to Hallitharam Via Orbit2 and RK Puram via Orbit4".format(orbit24[0]['name']))
    else:
        print("Vehicle {0} to Kr Puram Via Orbit3 and Hallitharam via Orbit4".format(orbit34[0]['name']))

getMinPath(climate="Windy",traffic_speed_orbit1=5,traffic_speed_orbit2=10,traffic_speed_orbit3=20,traffic_speed_orbit4=20)

print(get_orbit_Time.__doc__)







