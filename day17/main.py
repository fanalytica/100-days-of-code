class User:
    def __init__(self, id, username) -> None:
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

# user_1 = User()
# user_1.id = "001"
# user_1.username = "angela"
user1 = User("001","angela")

# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"
user2 = User("002","jack")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
