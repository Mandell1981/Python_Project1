def hello():
    print("Hello, How are you Today!")
    


def pack(num1, num2, num3):
    return [num1, num2, num3]

result = pack(3, 1, 6)
print(result)



def eat_lunch(food_list):
    if not food_list:
        print("My belly is empty!")
    else:
        print("First I eat", food_list[0])
        for food_list in food_list[1:]:
            print("Next I eat", food_list[1])



hello()
eat_lunch(["salad", "smoothie", "fruit"])


#just checking to see if it pushed!
           