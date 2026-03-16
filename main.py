from pydantic import BaseModel, ValidationError, validate_call


class User(BaseModel):
    username: str
    email: str
    age: int

    bio: str = ""
    full_name: str | None = None


def greet(name: str) -> str:
    """Greet user."""
    return f"Hello {name}!"


def bubble_sort(numbers: list[int]) -> list[int]:
    """Sort a list of numbers using bubble sort."""
    arr = numbers.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


@validate_call
def calculate_average(numbers: list[int | float]) -> float:
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


if __name__ == "__main__":
    print(calculate_average([33, 33.4, 49, 2, 3, 75]))

    print(greet("AJ"))

    print(bubble_sort([5, 2, 8, 1, 9]))

    user = User(username="ajlesure", email="amariusj.lesure@gmail.com", age=24)

    try:
        user = User(username="connorscott", email="connor.j.scott@gmail.com", age="24")
    except ValidationError as e:
        print(e)

    try:
        user = User(username=1000, email=None, age=False)
    except ValidationError as e:
        print(e)

    print(user.model_dump_json(indent=2))
