"""
A "data oriented" Garage and parking spots implementation.

No imports needed.
One simple function.
Not using any state.

Tradeoffs:
less auto-complete
data as strings (the FREE and OCCUPIED values)

"""


def is_full(garage: dict) -> bool:
    spots = garage.get("spots", [])
    free = (spot for spot in spots if spot.get("status") == "FREE")

    return not any(free)


garage_data = {
    "spots": [
        {"number": 1, "status": "OCCUPIED"},
    ]
}

is_full(garage_data)
