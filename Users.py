class User:
    user_count = 0

    def __init__(self):
        User.user_count += 1
        self.id = User.user_count
        self.username = input("Whats your name? ")
    
user_1 = User()
