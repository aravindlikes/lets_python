## Reference used: https://github.com/pankaj9310/parking-lot-design

import time

from enum import Enum
from datetime import datetime


class VehicleType(Enum):
    Car, Bus, Motorcycle = 1, 2, 3


class ParkingSpotType(Enum):
    Small, Medium, Large = 1, 2, 3


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class Vehicle():
    def __init__(self, vehicle_number, vehicle_type, parking_spot_type, ticket=None):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.ticket = ticket
        self.parking_spot_type = parking_spot_type
        self.parking_time = datetime.utcnow()
        self.ticket_status = ParkingTicketStatus.ACTIVE
        self.slot_number = None
        self.exit_time = None

    def assign_ticket(self, ticket):
        self.ticket = ticket

    def get_type(self):
        return self.vehicle_type

    def update_parking_status(self):
        self.exit_time = datetime.utcnow()
        self.ticket_status = ParkingTicketStatus.PAID


class Car(Vehicle):
    def __init__(self, vehicle_number, ticket=None):
        super().__init__(vehicle_number, VehicleType.Car, ParkingSpotType.Medium, ticket)


class Bus(Vehicle):
    def __init__(self, vehicle_number, ticket=None):
        super().__init__(vehicle_number, VehicleType.Bus, ParkingSpotType.Large, ticket)


class Motorcycle(Vehicle):
    def __init__(self, vehicle_number, ticket=None):
        super().__init__(vehicle_number, VehicleType.Motorcycle, ParkingSpotType.Small, ticket)

class ParkingLot:

    def __init__(self):
        self.car_spot_count = 0
        self.bus_spot_count = 0
        self.motorcycle_spot_count = 0
        self.max_car_count = 7
        self.max_bus_count = 3
        self.max_motorcycle_count = 10

        # all active parking tickets, identified by their ticket_number
        self.active_tickets = {}
        self.parking_history = {}

    def __getattr__(self):
        return getattr(self.instance)

    def get_new_parking_ticket(self, vehicle):
        """Park vehicle in parking lot if spot is available.
        Args: vehicle object
        Returns: ticket number
        """
        if self.is_full(vehicle.get_type()):
            return 'Parking full!'

        ticket = int(time.time() * 100)  # Generate unique tickets  number
        vehicle.assign_ticket(ticket)
        self._increment_spot_count(vehicle.get_type())
        self.active_tickets[ticket] = vehicle
        self.parking_history[ticket] = vehicle
        return ticket

    def is_full(self, vehicle_type):
        """Check parking lot status.
        Args: string vehicle_type
        Returns: boolean value
        """
        # trucks and vans can only be parked in LargeSpot
        if vehicle_type == VehicleType.Bus:
            return self.bus_spot_count >= self.max_bus_count

        # motorbikes can only be parked at motorbike spots
        if vehicle_type == VehicleType.Motorcycle:
            return self.motorbike_spot_count >= self.max_motorbike_count

        # cars can be parked at compact or large spots
        if vehicle_type == VehicleType.Car:
            return (self.car_spot_count + self.bus_spot_count) >= (
                    self.max_car_count + self.max_bus_count)

    def _increment_spot_count(self, vehicle_type):
        """Update parking spot count.
        Args: string vehicle_type
        Returns None
        """
        if vehicle_type == VehicleType.Bus:
            self.bus_spot_count += 1
        elif vehicle_type == VehicleType.Motorcycle:
            self.motorcycle_spot_count += 1
        elif vehicle_type == VehicleType.Car:
            if self.car_spot_count < self.max_car_count:
                self.car_spot_count += 1
            else:
                self.bus_spot_count += 1

    def _decrement_spot_count(self, vehicle_type):
        """Update parking spot count.
        Args: string vehicle_type
        Returns: None
        """
        if vehicle_type == VehicleType.Bus:
            self.bus_spot_count -= 1
        elif vehicle_type == VehicleType.Motorcycle:
            self.motorcycle_spot_count -= 1
        elif vehicle_type == VehicleType.Car:
            self.car_spot_count -= 1

    def leave_parking(self, ticket_number):
        """Exit vehicle from parking. Remove vehicle from active_tickets.
        Args:
            ticket_number: int ticket_number
        Returns: vehicle_number and parking_charge
        """
        if ticket_number in self.active_tickets:
            vehicle = self.active_tickets[ticket_number]
            self._decrement_spot_count(vehicle.get_type())
            self.parking_history[ticket_number] = vehicle
            self.active_tickets.pop(vehicle.ticket, None)
            return vehicle.vehicle_number
        return 'Invalid ticket number.', None

    def vehicle_status(self, ticket_number):
        """Check vehicle status.
        Args: int ticket_number
        Returns: string vehicle details
        """
        if ticket_number in self.parking_history:
            vehicle = self.parking_history[ticket_number]
            vehicle_details = {
                "Vehicle Number": vehicle.vehicle_number,
                "Vehicle Type": vehicle.vehicle_type.name,
                "Vehicle parking spot type": vehicle.parking_spot_type.name,
                "Vehicle parking time": vehicle.parking_time.strftime("%d-%m-%Y, %H:%M:%S"),
                "vehicle ticket status": vehicle.ticket_status.name,
            }
            return vehicle_details
        return 'Invalid ticket number.'

    def get_empty_spot_number(self):
        """Return available parking spot.
        Returns: available parking space.
        """
        message = ""
        if self.max_car_count - self.car_spot_count > 0:
            message += f"Free Car: {self.max_car_count - self.car_spot_count}"
        else:
            message += "Car Parking is full"
        message += "\n"

        if self.max_bus_count - self.bus_spot_count > 0:
            message += f"Free Bus: {self.max_bus_count - self.bus_spot_count}"
        else:
            message += "Bus is full"
        message += "\n"

        if self.max_motorcycle_count - self.motorcycle_spot_count > 0:
            message += f"Free Motorcycle: {self.max_motorcycle_count - self.motorcycle_spot_count}"
        else:
            message += "Motorcycle is full"
        message += "\n"

        return message


while True:
    choice = input("Enter Parking choice.\n"
                   "1 Parking entry Gate.\n"
                   "2 Parking exit Gate.\n"
                   "3 Check parking status.\n"
                   "4 Check vehicle status.\n"
                   "5 Exit.\n")
    try:
        choice = int(choice)
    except ValueError:
        print('Invalid choice type.')
    else:
        if choice == 1:
            vehicle_type = input("Enter vehicle type. \n"
                                 "1 Car.\n"
                                 "2 Bus, \n"
                                 "3 Motorcycle.\n")
            try:
                vehicle_type = int(vehicle_type)
            except ValueError:
                print('Invalid vehicle type.')
            else:
                if vehicle_type < 0 or vehicle_type > 3:
                    print('Invalid vehicle type.')
                else:
                    vehicle_number = input("Enter vehicle Number: ")
                    parking_lot = ParkingLot()
                    if vehicle_type == 1:
                        vehicle = Car(vehicle_number)
                    elif vehicle_type == 2:
                        vehicle = Bus(vehicle_number)
                    elif vehicle_type == 3:
                        vehicle = Motorcycle(vehicle_number)
                    ticket_number = parking_lot.get_new_parking_ticket(vehicle)
                    print(f"Ticket number: {ticket_number}")
        elif choice == 2:
            ticket_number = input("Enter ticket Number: ")
            try:
                ticket_number = int(ticket_number)
            except ValueError:
                print("Invalid ticket number.")
            else:
                vehicle_number = parking_lot.leave_parking(ticket_number)
                print(f"Vehicle Number: {vehicle_number}.")
        elif choice == 3:
            parking_status = parking_lot.get_empty_spot_number()
            print(parking_status)
        elif choice == 4:
            ticket_number = input("Enter ticket Number: ")
            try:
                ticket_number = int(ticket_number)
            except ValueError:
                print("Invalid ticket number.")
            else:
                vehicle_status = parking_lot.vehicle_status(ticket_number)
                print(vehicle_status)
        elif choice == 5:
            break
        else:
            print('Invalid choice')
