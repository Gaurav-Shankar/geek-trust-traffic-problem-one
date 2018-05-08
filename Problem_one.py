def getvehicles(climate):
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
    orbit_1_vehicles_time=[]
    for i in vehicles[0]:
        if taffic_speed <= i['speed_in_Km']:
            temp_speed=taffic_speed
        else:
            temp_speed=i['speed_in_Km']
        temp= (orbit_distance+(vehicles[1]*craters_count))*i['crater_speed_in_Min']+(60/temp_speed)*orbit_distance
        orbit_1_vehicles_time.append(temp)

    return [vehicles[0][orbit_1_vehicles_time.index(min(orbit_1_vehicles_time))],min(orbit_1_vehicles_time)]
def getMinPath(climate,taffic_speed_obit1,taffic_speed_obit2):
    print("Weather is  ", climate)
    print("Orbit1 traffic speed is {0} megamiles/hour".format(taffic_speed_obit1))
    print("Orbit1 traffic speed is {0} megamiles/hour".format(taffic_speed_obit2))
    vehicles=getvehicles(climate)
    orbit1=get_orbit_Time(vehicles,taffic_speed_obit1,18,20)
    orbit2 = get_orbit_Time(vehicles, taffic_speed_obit2, 20, 10)
    if orbit1[1] < orbit2[1]:
        print("Vehicle {0} on Orbit1".format(orbit1[0]['name']))
    else:
        print("Vehicle {0} on Orbit2".format(orbit2[0]['name']))


getMinPath(climate="Sunny",taffic_speed_obit1=12,taffic_speed_obit2=10)









