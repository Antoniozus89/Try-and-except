def add_everithing_up(a, b):
        try:
                return a + b
        except TypeError:
                return str(a) + str(b)

print(add_everithing_up(3.14, 'Пи'))
print(add_everithing_up('яблоко', 4217))
print(add_everithing_up(123.456, 7))