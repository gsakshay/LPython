# This explores the option of using generators
# Basically even the normal for loop that iterates over something that is in memory was somewhat created using a generator at some time.
# It is mainly memory efficient, and for use cases where we do not need all the records stored in memory before operating on them, and which works best when we need one record after another, its very useful.
import random

names = ["Abc", "Xyz", "Pqr", "Efg"]
majors = ["CS", "EC", "Math", "Biology"]


def list_records(num_people):
    result = []

    for i in range(num_people):
        record = {
            "id": i + 1,
            "name": random.choice(names),
            "major": random.choice(majors)
        }
        result.append(record)

    return result


def generate_records(num_people):
    for i in range(num_people):
        record = {
            "id": i + 1,
            "name": random.choice(names),
            "major": random.choice(majors)
        }
        yield record
