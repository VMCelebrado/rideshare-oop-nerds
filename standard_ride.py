from ride import Ride

class StandardRide(Ride):
    def __init__(self, distance_km):
        super().__init__(distance_km)
        self.__base_rate = 5.00

    def calculate_fare(self):
        return self.__base_rate + (1.50 * self.distance_km)

    def start_ride(self):
        print("Standard Ride has Started!!!")
        print(f"Distance: {self.distance_km} km")

    def complete_ride(self):
        self.is_completed = True
        print("\n======= STANDARD RIDE RECEIPT =======")
        print(f"Distance: {self.distance_km} km")
        print(f"Base Rate: ₱{self.__base_rate:.2f}")
        print("Rate per km: ₱1.50")
        print(f"Total Fare: ₱{self.calculate_fare():.2F}")
        print("Ride Status: Finished")
        print("=======================================")

