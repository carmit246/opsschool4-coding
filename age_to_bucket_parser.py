import json


def get_data():
    with open('hw.json') as input_file:
        data = json.load(input_file)
    people = data["ppl_ages"]
    buckets = data["buckets"]
    buckets.sort()
    return people, buckets


def create_buckets(buckets, minimum, maximum):
    t = {}
    for bucket_age in buckets:
        range = str(minimum) + "-" + str(bucket_age)
        t[range] = []
        minimum = bucket_age+1
    last_range = str(buckets[-1]+1) + "-" + str(maximum)
    t[last_range] = []
    result = dict(t)
    return result


def get_max_age(people):
    max_age = max(zip(people.values(), people.keys()))[0]
    maximum_age = int(max_age)
    return maximum_age


def group_people_by_age(people,result):
    for person,age in people.items():
        for key in result:
            if int(age) >= int(key.split('-')[0]) and int(age) < int(key.split('-')[1]):
                result[key].append(person)
    return result


def print_result(result):
    for key,value in result.items():
        print(key + ":")
        for pers in value:
            print("-  " + pers)


def main():
    minimum_age = 0
    people, buckets = get_data()
    maximum_age = get_max_age(people)
    result = create_buckets(buckets, minimum_age, maximum_age)
    result = group_people_by_age(people, result)
    print_result(result)


if __name__ == '__main__':
    main()