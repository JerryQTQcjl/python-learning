import module2

# 当存在__name__ == '__main__'时，被导入时不会自动执行下面的代码，只有在 run 当前文件的时候才会执行
if __name__ == '__main__':
    print("hello, this is module1")