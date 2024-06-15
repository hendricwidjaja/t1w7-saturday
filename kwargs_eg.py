def personal_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} --> {value}")

personal_details(name="Alice", age="25", address="Sydney")

def myFunction(*onestar, **twostars):
    print("args: ", onestar)
    print("kwargs: ", twostars)

myFunction("I", "Love", "Coding", first = "I", second = "love", third = "coding!!!")