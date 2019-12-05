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


def group_people_by_age():
    global result
    global people
    #print(people)
    for person,age in people.items():
        for key in result:
            #print(key.split('-')[0] + "-"+key.split('-')[1])
            if int(age) >= int(key.split('-')[0]) and int(age) < int(key.split('-')[1]):
                #print(person)
                result[key] += 1
    #print(result)

def print_result():
    global result
    for key,value in result.items():
        print(key + ":")
        print("-  " + str(value))

def main():
    get_data()
    create_buckets()
    group_people_by_age()
    print_result()


if __name__ == '__main__':
    main()