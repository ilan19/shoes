class Dog:
  def __init__(self, name):
    self.name = name

  def bark(self):
    print( "Woof! My name is {}".format(self.name) )


  @classmethod
  def describe_dog(cls):
    print("A dog has 4 legs and a tail.")



rufus = Dog('Rufus')
rufus.bark()

Dog.describe_dog()