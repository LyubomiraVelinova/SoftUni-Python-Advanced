def age_assignment(*args, **kwargs):
    name_age = {}
    for name in args:
        for key, value in kwargs.items():
            if key == name[0]:
                name_age[name] = value
    return name_age

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
