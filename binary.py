def remove_zeros_in_front(string, zero):
    new_string = ""
    found_first_digit = False
    for i in string:
        if i == zero and not found_first_digit:
            pass
        elif i == zero and found_first_digit:
            new_string += i
        elif i != zero:
            found_first_digit = True
            new_string += i
    return new_string

    
def bin_to_int(num, digit_limit=100):
    num_str = str(num)
    values = []
    
    if len(num_str) > digit_limit:
        raise Exception("The number is too big to be converted.")
    for i in range(len(num_str)):
        values.append(2**((len(num_str) - i)- 1) * int(num_str[i]))
    return sum(values)

def int_to_bin(num, digits_limit=100):
    values = ""
    new_num = int(num)
    for i in range(digits_limit).__reversed__():
        values += str(new_num // 2**i)
        new_num = new_num % 2**i
    return remove_zeros_in_front(values, "0")

def help():
    print("""This is the help menu.
Valid commands are:
    bin_to_int -> convert a binary to integer
    int_to_bin -> convert an integer to binary (TODO)
    quit <or> exit -> quit the application
""")

def main():
    print("Welcome to the binary to int formatter.\n")
    while True:
        answer = input(":command> ")
        match answer:
            case "bin_to_int":
                number = input(":number> ")
                print(bin_to_int(number))
            case "quit" | "exit":
                answer = input("Are you sure you want to quit? Y/N: ")
                if answer.lower()[0] == "y":
                    break
            case "int_to_bin":
                number=input(":number> ")
                print(int_to_bin(number))
            case _:
                help()
    print("Have a good day!")

main()