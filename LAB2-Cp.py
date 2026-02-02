def calculate_height(h0,t):
    g=9.8 # acceleration due to gravity in m/s^2
    height=h0 - 0.5 * g * t**2
    return round(height)

def calculate_car_distance(time):
    speed=20 # speed in m/s
    distance = speed * time
    return round (distance)

if __name__ == "__main__":
    h0 = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter the time (in seconds): "))
    print("The height of the ball at time", t, "seconds is", calculate_height(h0,t), "meters")
    time=float(input("Enter the time here(in seconds): "))
    print("The car will travel", calculate_car_distance(time), "meters in", time, "seconds")