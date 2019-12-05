import json
a = "aaavvv"
#print(a[5])
#for i in a:
#        print(i)

#print("welcome" in a)

def sum_positive_numbers(num_list):
    my_sum = 0
    for i,num in enumerate(num_list):
       if num > 0:
           my_sum += num
    try:
        print(my_sum)
    except IndexError:
        pass
    json_str = """{"name": 2, "age": 35, "dadsa": 3, "dsada": 70}"""
    parsed_json = json.loads(json_str)
    print(type(parsed_json))
    for key, value in parsed_json.items():
        if value > 30:
            print(key + " is older than 30 ")
        if value > 30:
            print(key + " is younger than 30 ")
        print(value)
    #print(my_dict["name"])
    #print(my_dict["age"])


if __name__ == '__main__':
    list_of_numbers = [12, 1, -7, 23, 80, 214, -9]
    sum_positive_numbers(list_of_numbers)

