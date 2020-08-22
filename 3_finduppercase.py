# Given a String find the uppercase

input_str_1 = "AdityaTaksande"
input_str_2 = "RachitKhandelwal"
input_str_3 = "BadamBadam"

# iterative approach


def finduppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return print("The letter is :", input_str[i])
    return print("No upper case can be found")


finduppercase_iterative(input_str_1)


# recursive approach

def finduppercase_recursive(input_str):
    pass
