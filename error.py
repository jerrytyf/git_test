try:
    print(a) 
except NameError as e:
    print(f"{e}")

try:
    print(1/0)
except ZeroDivisionError as e:
    print(f"{e}")

try:
    key = {"hoost" : 80,"name" : "jerry","k" : 0}
    print(f"{key["j"]}")
except KeyError as e:
    print(f"{e}")