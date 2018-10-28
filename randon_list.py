import random

def random_list(alumnis, num, min_value, max_value):
  return [[alumni, [random.randint(min_value, max_value) for cal in range(num)]] for alumni in alumnis ]
