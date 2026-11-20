
class MyName:
    """Клас для роботи з іменами користувачів."""

    total_names = 0

    
    def __init__(self, name=None) -> None:
        """Ініціалізація класу."""
        if name is not None and not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")

        self.name = name.capitalize() if name is not None else self.anonymous_user().name


        MyName.total_names += 1
        self.my_id = self.total_names

    @property
    def whoami(self) -> str:
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        return self.create_email()
    
    @property
    def full_name(self) -> str:
        return f"User #{self.my_id}: {self.name} ({self.my_email})"


    
    def create_email(self, domain="itcollege.lviv.ua") -> str:
        return f"{self.name}@{domain}"


    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        return f"You say: {message}"

    def count_letters(self) -> int:
        return len(self.name)

    
    def save_to_file(self, filename="users.txt"):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(self.full_name + "\n")


print("Розпочинаємо створювати об'єкти!")

names = ("bohdan", "marta", "oleksandr", None)
all_names = {name: MyName(name) for name in names}



for user in all_names.values():
    user.save_to_file("05_OOP_first_class/users.txt")




for name, me in all_names.items():
    print(f"""
{" >*< " * 10}
This is object: {me}
This is object attribute: {me.name} / {me.my_id}
Full name: {me.full_name}
Number of letters in name: {me.count_letters()}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
Custom email: {me.create_email("gmail.com")}
This is static {type(MyName.say_hello)} with custom message: {me.say_hello("Hello from Oleksandr!")}
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{" <*> " * 10}
""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")

print("Number of names in list:", len(names))
print("Total created objects:", MyName.total_names)


try:
    test_user = MyName("Oleksandr123")
except ValueError as error:
    print("Validation error:", error)
