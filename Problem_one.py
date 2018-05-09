'''
problem 1: lengaburu traffic
King Shan wants to visit the suburb of Hallitharam, and has 2 possible orbits and 3 possible vehicles to chose from.
Your coding challenge is to determine which orbit and vehicle King Shan should take to reach Hallitharam the fastest
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

    return [vehicles[0][orbit_1_vehicles_time.index(min(orbit_1_vehicles_time))],min(orbit_1_vehicles_time)]
def getMinPath(climate,traffic_speed_orbit1,traffic_speed_orbit2):
    '''
      :param climate: User input  CLimate
      :param traffic_speed_orbit1: Orbit 1 Traffic Speed
      :param traffic_speed_orbit2: Orbit 2 Traffic Speed
      :return: Shortest time and Vehicle details
      '''
    print("Weather is  ", climate)
    print("Orbit1 traffic speed is {0} megamiles/hour".format(traffic_speed_orbit1))
    print("Orbit1 traffic speed is {0} megamiles/hour".format(traffic_speed_orbit2))
    vehicles=getvehicles(climate)
    orbit1 = get_orbit_Time(vehicles=vehicles, taffic_speed=traffic_speed_orbit1, orbit_distance=18, craters_count=20)
    orbit2 = get_orbit_Time(vehicles=vehicles, taffic_speed=traffic_speed_orbit2, orbit_distance=20, craters_count=10)
    if orbit1[1] < orbit2[1]:
        print("Vehicle {0} on Orbit1".format(orbit1[0]['name']))
    else:
        print("Vehicle {0} on Orbit2".format(orbit2[0]['name']))


getMinPath(climate="Sunny",traffic_speed_orbit1=12,traffic_speed_orbit2=10)









