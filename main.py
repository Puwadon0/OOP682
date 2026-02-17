class Dog:
    def __init__(self, name ,age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"{self.name} is {self.age} year old.")
        
    def __str__(self):
        return f"{self.name} is {self.age} year old."
        
def main():
    my_dog = Dog("Buddy", 3)
    # my_dog.info()
    your_dog = Dog("paulie" ,2)
    # your_dog.info
    print(my_dog)
    print(your_dog)


# def main():
#     my_dog = Dog
#     print("Hello from week9!")


if __name__ == "__main__":
    main()
