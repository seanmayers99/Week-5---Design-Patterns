# Sean Mayers
# 11/22/2020
# Week 5 Design Patterns - Singleton Design Patterns

""" Only want one object to be instantiated from class --> Employee Access to database  """

class Singleton(object):
   __instance = None # private variable instance

   def __new__(cls): # override new method
      # first time instantiated object, means no one has asked for this connection
      if cls.__instance == None:  # if None set it
        cls.__instance = "My Database Connection"
      return cls.__instance  # return instance


def main():
   s1 = Singleton()
   s2 = Singleton()
   print(s1 == s2) # this will show true result
   print (s1)

main()