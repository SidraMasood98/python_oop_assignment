class Bank:
    pass
    bank_name = "ABC bank"

    @classmethod
    def change_bank_name(cls, name):
        pass
        cls.bank_name= name

if __name__ == "__main__":
    pass
    user1 = Bank()
    user2 = Bank()

    print("Before changing bank name:")
    print(f"User1 bank name: {user1.bank_name}")
    print(f"User2 bank name: {user2.bank_name}")

    Bank.change_bank_name("Alhabib bank")

    print("\nAfter changing bank name:")
    print(f"User1 bank name: {user1.bank_name}")
    print(f"User2 bank name: {user2.bank_name}")