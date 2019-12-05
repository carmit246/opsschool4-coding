import pprint
import json
people = {}
buckets = {}
result = {}
minimum_age = 0
maximum_age = 100

def get_data():
    global people
    global buckets
    with open('hw.json') as input_file:
        data = json.load(input_file)
    people = data["ppl_ages"]
    buckets = data["buckets"]
    buckets.sort()

def create_buckets():
    global result
    global maximum_age
    min = minimum_age
    max = maximum_age
    t = {}
    for bucket_age in buckets:
        range = str(min) + "-" + str(bucket_age)
        t[range] = 0
        min = bucket_age+1
    last_range = str(buckets[-1]+1) + "-" + str(maximum_age)
    t[last_range] = 0


    result = dict(t)

def get_max_age():
    global people
    global maximum_age
    max_age = max(zip(people.values(), people.keys()))[0]
    maximum_age = int(max_age)

def group_people_by_age():
    global result
    global people
    #print(people)
    for person,age in people.items():
        for key in result:
            if int(age) >= int(key.split('-')[0]) and int(age) < int(key.split('-')[1]):
                result[key] += 1

def print_result():
    global result
    for key,value in result.items():
        print(key + ":")
        print("-  " + str(value))

def main():
    get_data()
    get_max_age()
    create_buckets()
    group_people_by_age()
    print_result()


if __name__ == '__main__':
    main()