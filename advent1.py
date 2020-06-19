

def main():
    
    # list of weight of modules that make up the spaceship
    modules = [136583, 77036, 109200, 142168, 74357, 146941, 129306, 98180, 105195, 129127, 135956, 116070, 89198, 51306, 144552, 109900, 56658, 52478, 115147, 63882, 70342, 98678, 107384, 135359, 87237, 84469, 106477, 104645, 77066, 74143, 76537, 140547, 68128, 116624, 148407, 78276, 117623, 96019, 75825, 75010, 98644, 119641, 139736, 104452, 72599, 63017, 59648, 126163, 69629, 79080, 92195, 58221, 134276, 80301, 89870, 146799, 145702, 138367, 131977, 56781, 85326, 138115, 70241, 60454, 76934, 119321, 93493, 123047, 149941, 141729, 70141, 134525, 93312, 92043, 79582, 115959, 51058, 94686, 70749, 99408, 118560, 95821, 58995, 94906, 98421, 118673, 83575, 83434, 63884, 70575, 134177, 116233, 113954, 52829, 123860, 128020, 126718, 144463, 140192, 143461]
    
    fuel_requirement = fuelcalculator(modules)  # calculates the total fuel requirement of all modules by weight
    # total fuel required in the spaceship is based on the total weight of the craft which includes the weight of all modules plus the weight of
    # plus the weight of fuel

    print("fuel requirement in total {0}".format(fuel_requirement))

def fuelcalculator(array):
    """ Assumes array is a list of the mass of modules in integer
            array.len() > 0
        returns an integer total fuel requirement for the spaceship

        >>> fuelcalculator([12, 14])
        4
        >>> fuelcalculator([12, 14, 1969, 100756])
        34241
    """
    assert isinstance(array, list) and len(array) > 0

    fuel_per_module = [calc(module) for module in array]
    fuel_for_fuel = [fuel_per_weight_of_fuel(fuel) for fuel in fuel_per_module]
    return sum(fuel_per_module) + sum(fuel_for_fuel)

def calc(mass):
    """ Assumes mass is an integer
                mass >= 0
        for a given mass this function calculates the fuel required
        Returns an integer such that (result + 2) * 3 = mass

        >>> calc(12)
        2
        >>> calc(14)
        2
        >>> calc(1969)
        654
        >>> calc(100756)
        33583
    """
    return (mass // 3) - 2


def fuel_per_weight_of_fuel(fuelweight):
    """ Assumes fuelweight is an integer of only one element an integer
            fuelweight >= 0
        returns the total fuel requirement for each gram of fuel and the fuel for each fuel subsequently added
        >>> fuel_per_weight_of_fuel(14)
        2
        >>> fuel_per_weight_of_fuel(12)
        2
    """
    if fuelweight <= 0 :
        return 0
    elif calc(fuelweight) <= 0 :
        return 0
    else:
        res = calc(fuelweight)
        return res + fuel_per_weight_of_fuel(res)

if __name__ == "__main__":
    print(fuel_per_weight_of_fuel(14))
    print(fuel_per_weight_of_fuel(15))
    print(fuel_per_weight_of_fuel(0))
    print(fuel_per_weight_of_fuel(-2))
    import doctest
    #doctest.testmod()
    main()