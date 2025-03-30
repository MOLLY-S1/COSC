"""Function to calculate speed and distance"""
def main():
    """Speed and distance calculator"""
    
    distance_feet = float(input("Enter the distance traveled in feet: "))
    time_hours = float(input("Enter the time taken in hours: "))
    
    meter_feet = 0.3048
    to_hour = 3600
    ks = 1000
        
    distance_meters = meter_feet * distance_feet 
    time_seconds = time_hours * to_hour
        
    speed_mps = distance_meters/time_seconds
    print(f"Your average speed is: {speed_mps:.4f} m/s")
    speed_kph = to_hour * speed_mps / ks  
    print(f"Which is: {speed_kph:.4f} km/h")
    
# MAIN ROUTINE
main()