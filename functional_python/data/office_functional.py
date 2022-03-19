"""
A functional and "data oriented"
approach to the Office and desks implementation.

No imports needed.
One simple function.
Not using any state.

Tradeoffs:
less auto-complete
data as strings (the FREE and BUSY values)

"""


def is_full(office: dict) -> bool:
    desks = office.get("desks", [])
    free = (desk for desk in desks if desk.get("status") == "FREE")

    return not any(free)


office_data = {
    "desks": [
        {"number": 1, "status": "BUSY"},
    ]
}

is_full(office_data)
