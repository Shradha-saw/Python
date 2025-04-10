class InvalidAge(Exception):
    pass


def checkAge(age):
    if age < 18:
        raise InvalidAge("age must be greater than 18")
try:
    checkAge(12)
except InvalidAge as e:
    print("Exception occured details are: ", e)