#Exercise 4
#create the following classes 
#Head
#Torso
#Arm
#Hand
#Leg
#Feet
#Now create a class Human and connect all the other classes logically using attributes 

class Head():
    def __init__(self):
        pass


class Torso():
    def __init__(self,head,right_arm,left_arm,right_leg,left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Arm():
    def __init__(self,hand):
        self.hand = hand
        

class Hand():
    def __init__(self):
        pass

class Leg():
    def __init__(self,feet):
        self.feet = feet

class Feet():
    def __init__(self):
        pass

#Creation of hands
right_hand = Hand()
lef_hand = Hand()

#Creation of arms
right_arm = Arm(right_hand)
left_arm = Arm(lef_hand)

#Creation of feet
right_fee = Feet()
left_fee = Feet()

#Creation of legs
right_leg = Leg(right_fee)
left_leg = Leg(left_fee)

head = Head()

torso = Torso(head,right_arm,left_arm,right_leg,left_leg)


