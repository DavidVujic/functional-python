from dataclasses import dataclass
from enum import Enum


class ParkingSpotStatus(str, Enum):
    FREE = "FREE"
    OCCUPIED = "OCCUPIED"


@dataclass
class ParkingSpot:
    number: int
    status: ParkingSpotStatus

    @property
    def is_free(self):
        return self.status == ParkingSpotStatus.FREE


@dataclass
class Garage:
    parking_spots: list[ParkingSpot]

    def is_full(self):
        full = True
        for spot in self.parking_spots:
            if spot.is_free:
                full = False
                break

        return full


spot = ParkingSpot(number=1, status=ParkingSpotStatus.OCCUPIED)
garage = Garage(parking_spots=[spot])

garage.is_full()
