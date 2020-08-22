# Given a String find the uppercase

input_str_1 = "AdityaTaksande"
input_str_2 = "rachitKhandelwal"
input_str_3 = "badambadam"

# iterative approach


def finduppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return print("The letter is :", input_str[i])
    return print("No upper case can be found")


finduppercase_iterative(input_str_1)
finduppercase_iterative(input_str_2)
finduppercase_iterative(input_str_3)


# recursive approach

def finduppercase_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No upper case found"
    return finduppercase_recursive(input_str, idx+1)


finduppercase_recursive(input_str_1)
finduppercase_recursive(input_str_2)
finduppercase_recursive(input_str_3)
