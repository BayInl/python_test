def my_function():
    print(x)  # 在赋值之前使用了变量x
    x = 10  # 赋值操作在使用之后


def my_function():
    if condition:
        x = 10
    print(x)  # 在嵌套作用域中定义了x，但在使用之前没有为其赋值
