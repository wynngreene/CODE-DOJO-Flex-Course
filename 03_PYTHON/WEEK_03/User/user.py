print("connected")

# class User:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.dual = True

#     def first_method(self, my_stuff):
#         new_Stuff = self.z + my_stuff
#         return new_Stuff

# new_User = User(4, 5, 6)
# old_User = User(6, 7, 8)

# print(old_User.z)

# print(new_User.first_method(10))
# print(old_User.first_method(10))

class User:  
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return
        else:
            print("User already a member.")
    
    def spend_points(self, amount):
        self.gold_card_points -= amount
        if self.gold_card_points < 0:
            self.gold_card_points += amount
            print("Not enough pts.")

#----------------------

user_01_hobbit = User("Bilbo", "Baggins", "ring_dude@email.com", 32, )
user_02_sponge = User("Bob", "SquarePants", "pineappplepen@email.com", 35, )
user_03_turtle = User("Leo", "Nardo", "blueshell@email.com", 15)

user_01_hobbit.enroll()
user_02_sponge.enroll()
user_03_turtle.enroll()

user_01_hobbit.spend_points(50)
user_02_sponge.spend_points(80)
user_03_turtle.spend_points(40)

print("-------------")
print(user_01_hobbit.display_info())
print("-------------")
print(user_02_sponge.display_info())
print("-------------")
print(user_03_turtle.display_info())