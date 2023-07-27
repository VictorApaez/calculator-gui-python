class Calculator:
  def __init__(self):
    self.current_value = 0

  def add(self, value):
    self.current_value += value
    return self

  def subtract(self, value):
    self.current_value -= value
    return self

  def multiply(self, value):
    self.current_value *= value
    return self

  def divide(self, value):
    if value != 0:
      self.current_value /= value
      return self
    else:
      raise ValueError("Cannot Divide by Zero")
      
  def result(self):
    return self.current_value
