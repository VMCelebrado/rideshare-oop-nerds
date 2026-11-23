from abc import ABC, abstractmethod

class Ride(ABC):

    def __init__(self, distance_km):
        self.distance_km = distance_km
        self.is_completed = False

    @abstractmethod
    def calculate_fare(self):
        pass
    
    def start_ride(self):
        pass

    def complete_ride():
        pass

        
