# This py source file is used to show some class report of the flake8

class MyClass:
  # E111 indentation is not a multiple of four
  def __init__(self,value=2):
    self.value  =  value # E221 multiple spaces before operator
    print("Value is:", self.value)
