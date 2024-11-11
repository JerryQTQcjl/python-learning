command = 2

if __name__ == "__main__":
    if command == 1:
        print("1")
    elif command == 2:
        print("2")
    elif command == 3:
        print("3")
    else:
        print("4")

    # 类似 java 三元表达式，但是支持无返回值大表达式（更为强大）
    print("2") if command == 2 else print("other")
    print(2 if command == 2 else "other")