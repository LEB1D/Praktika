# Add a constructor to the class Vehicle
class Vehicle:
    name = "Mercedes"


if __name__ == "__main__":
    # Assign the needed value to the variable `c`
    # to make the script work without errors
    c = Vehicle()

    assert isinstance(c, Vehicle)
    assert c.name == "Mercedes"
