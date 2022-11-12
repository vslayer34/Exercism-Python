"""
Functions to prevent a nuclear meltdown.
https://exercism.org/tracks/python/exercises/meltdown-mitigation
"""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    critical_condition = False
    product_of_temperature_and_neutrons = temperature * neutrons_emitted
    if (temperature < 800 and neutrons_emitted > 500
        and product_of_temperature_and_neutrons < 500000):
        critical_condition = True

    return critical_condition


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    efficiency = generated_power / theoretical_max_power * 100
    if efficiency >= 80:
        return 'green'
    elif 80 > efficiency >= 60:
        return 'orange'
    elif 60 > efficiency >= 30:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    if temperature * neutrons_produced_per_second < 0.9 * threshold:
        return 'LOW'
    elif (threshold - 0.1 * threshold <= temperature * neutrons_produced_per_second <= threshold + 0.1 * threshold):
        return 'NORMAL'
    else:
        return 'DANGER'



# Test 1
# MeltdownMitigation > is criticality balanced [variation #1] (expected=True, neutrons emitted=650, temp=750)
print(is_criticality_balanced(750, 650), "\n")

# Test 2
# MeltdownMitigation > is criticality balanced [variation #2] (expected=True, neutrons emitted=501, temp=799)
print(is_criticality_balanced(799, 501), "\n")

# Test 3
# MeltdownMitigation > is criticality balanced [variation #3] (expected=True, neutrons emitted=600, temp=500)
print(is_criticality_balanced(500, 600), "\n")

# Test 4
# MeltdownMitigation > is criticality balanced [variation #4] (expected=False, neutrons emitted=800, temp=1000)
print(is_criticality_balanced(1000, 800), "\n")

# Test 5
# MeltdownMitigation > is criticality balanced [variation #5] (expected=False, neutrons emitted=500, temp=800)
print(is_criticality_balanced(800, 500), "\n")

# Test 6
# MeltdownMitigation > is criticality balanced [variation #6] (expected=False, neutrons emitted=500.01, temp=800)
print(is_criticality_balanced(800, 500.01), "\n")

# Test 7
# MeltdownMitigation > is criticality balanced [variation #7] (expected=False, neutrons emitted=500, temp=799.99)
print(is_criticality_balanced(799.99, 500), "\n")

# Test 8
# MeltdownMitigation > is criticality balanced [variation #8] (expected=False, neutrons emitted=999.99, temp=500.01)
print(is_criticality_balanced(500.01, 999.99), "\n")

# Test 9
# MeltdownMitigation > is criticality balanced [variation #9] (expected=False, neutrons emitted=800, temp=625)
print(is_criticality_balanced(625, 800), "\n")

# Test 10
# MeltdownMitigation > is criticality balanced [variation #10] (expected=False, neutrons emitted=800, temp=625.99)
print(is_criticality_balanced(625.99, 800), "\n")

# Test 11
# MeltdownMitigation > is criticality balanced [variation #11] (expected=False, neutrons emitted=799.99, temp=625.01)
print(is_criticality_balanced(625.01, 799.99), "\n")

# Test 12
# MeltdownMitigation > is criticality balanced [variation #12] (expected=True, neutrons emitted=500.01, temp=799.99)
print(is_criticality_balanced(799.99, 500.01), "\n")

# Test 13
# MeltdownMitigation > is criticality balanced [variation #13] (expected=True, neutrons emitted=799.99, temp=624.99)
print(is_criticality_balanced(624.99, 799.99), "\n")

# Test 14
# MeltdownMitigation > is criticality balanced [variation #14] (expected=False, neutrons emitted=1000, temp=500)
print(is_criticality_balanced(500, 1000), "\n")

# Test 15
# MeltdownMitigation > is criticality balanced [variation #15] (expected=False, neutrons emitted=1000, temp=500.01)
print(is_criticality_balanced(500.01, 1000), "\n")

# Test 16
# MeltdownMitigation > is criticality balanced [variation #16] (expected=True, neutrons emitted=1000, temp=499.99)
print(is_criticality_balanced(499.99, 1000), "\n")