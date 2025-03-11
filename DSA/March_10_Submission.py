class Vehicle:
    def __init__(self, license_plate:str):
        self.license_plate = license_plate
    
    def __str__(self):
        return f"Vehicle {self.license_plate}"

class ParkingGarage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parked_vehicles = []
    
    def park_vehicle(self, vehicle):
        if len(self.parked_vehicles) >= self.capacity:
            raise ValueError("Parking garage is full!")
        self.parked_vehicles.append(vehicle)
        print(f"Parked {vehicle}")
    
    def remove_vehicle(self, license_plate):
        for vehicle in self.parked_vehicles:
            if vehicle.license_plate == license_plate:
                self.parked_vehicles.remove(vehicle)
                print(f"Removed {vehicle}")
                return
        raise ValueError(f"Vehicle with license plate {license_plate} not found in garage.")
    
    def __str__(self):
        return f"Parking Garage: {len(self.parked_vehicles)}/{self.capacity} vehicles parked."


garage = ParkingGarage(2)

# Create some vehicles
vehicle1 = Vehicle("ABC123")
vehicle2 = Vehicle("XYZ789")
vehicle3 = Vehicle("DEF456")

# Park vehicles
garage.park_vehicle(vehicle1)  # Parks Vehicle ABC123
garage.park_vehicle(vehicle2)  # Parks Vehicle XYZ789

# Try to park a third vehicle (should raise an error)
try:
    garage.park_vehicle(vehicle3)
except ValueError as e:
    print(e)  # Output: Parking garage is full!

# Print the current state of the garage
print(garage)  # Output: Parking Garage: 2/2 vehicles parked.

# Remove a vehicle
garage.remove_vehicle("ABC123")  # Removes Vehicle ABC123

# Print the updated state of the garage
print(garage)  # Output: Parking Garage: 1/2 vehicles parked.
        
