def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    number_of_bills = int(budget // denomination)
    return number_of_bills


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    return budget % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    fees = exchange_rate * spread / 100
    exchange_rate += fees
    exchange_money_after_fees = exchange_money(budget, exchange_rate)
    
    # number of bills of the avaialbe denomination
    number_bills = int(exchange_money_after_fees / denomination)
    money_the_client_gets = number_bills * denomination
    return money_the_client_gets
    pass


print("exchange_money() output test")
print(exchange_money(100000, 0.8))
print(exchange_money(700000, 10.0))
# output should be [125000, 70000]
print("\n")

print("get_change() output test")
print(get_change(127.5, 120))
print(get_change(463000, 5000))
print(get_change(1250, 120))
print(get_change(15000, 1380))
# output should be [7.5, 458000, 1130, 13620]
print("\n")

print("get_value_of_bills() output test")
print(get_value_of_bills(5, 128))
print(get_value_of_bills(10000, 128))
print(get_value_of_bills(50, 360))
print(get_value_of_bills(200, 200))
# output should be [640, 1280000, 18000, 40000]
print("\n")


print("get_number_of_bills() output test")
print(get_number_of_bills(127.5, 5))
print(get_number_of_bills(163270, 50000))
print(get_number_of_bills(54361, 1000))
# output should be [25, 3, 54]
print("\n")


print("get_leftover_of_bills() output test")
print(get_leftover_of_bills(127.5, 20))
print(get_leftover_of_bills(10.1, 10))
print(get_leftover_of_bills(654321.0, 5))
print(get_leftover_of_bills(3.14, 2))
#output should be [7.5, 0.1, 1.0, 1.14]
print("\n")


print("exchangeable_value() output test")
print(exchangeable_value(127.25, 1.20, 10, 20))
print(exchangeable_value(127.25, 1.20, 10, 5))
print(exchangeable_value(100000, 10.61, 10, 1))
print(exchangeable_value(1500, 0.84, 25, 40))
print(exchangeable_value(470000, 1050, 30, 10000000000))
print(exchangeable_value(470000, 0.00000009, 30, 700))
print(exchangeable_value(425.33, 0.0009, 30, 700))
#output should be [80, 95, 8568, 1400, 0, 4017094016600, 363300]
print("\n")