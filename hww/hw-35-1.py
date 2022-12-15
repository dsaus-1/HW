

def calc_salt(salt):
    try:
        if isinstance(salt, int|float):
            return float(salt) / 100
        elif salt.isdigit():
            return float(salt) / 100
        else:
            raise Exception
    except:
        print(f'invalid literal for int() with base 10: "{salt}"')
        salt = float(0)
        return salt

print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('abc'))
