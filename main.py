# This is to learn Python and get some insights on Advanced Python.
# Also learning PyCharm and the module and package systems in Python

# Topics covered
# 1. Decorators
# 2. Generators

from Decorators.time_information import time_information
from Generators.sample_records import generate_records, list_records
from Generators.CustomRange import MyRange

if __name__ == '__main__':
    print("Hello world")

    # List records first formulates all the records and then sends it over
    @time_information
    def list_1000_records():
        records = list_records(1000)
        print(records)

    list_1000_records()

    @time_information
    def generate_1000_records():
        record = generate_records(1000)
        print(next(record))
        print(next(record))
        print(next(record))

    generate_1000_records()

    # In the above example we saw how when we do not need all the values but need them one by one for some
    # calculation, we use generator And save memory mainly and also time for that span If we need all the records and
    # use them all, then the effect of generator wears down

    # Using generator to create a custom range function
    for i in MyRange(0, 100, 2):
        print(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
