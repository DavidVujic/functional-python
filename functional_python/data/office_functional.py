"""
A functional and "data oriented"
approach to the Office and desks implementation.

Benefits:
No imports needed. One stateless function.

Tradeoffs:
less auto-complete

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
