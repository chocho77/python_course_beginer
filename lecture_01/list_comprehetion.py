def enter_number(enter_data:str) -> int:
    return int(input(enter_data))


def list_comprehension() -> list[int]:
    mylist: list[int] = [p for p in range(1,100)]
    return mylist

def repeat_times() -> None:
    for i in range(5):
        my_list = list_comprehension()
        check_number_one:int = enter_number("Enter check number one : ")
        check_number_two:int = enter_number("Enter check number two : ")
        if check_number_one > check_number_two:
            print("Wrong input check number two must be more less from check number one : ")
        else:
            my_list_two = [p for p in my_list if check_number_two > p > check_number_one]
            print(my_list)
            print(my_list_two)


def main() -> None:
    repeat_times()


if __name__ == '__main__':
    main()


