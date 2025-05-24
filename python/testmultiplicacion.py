from optparse import Option
def election_number(number):
   
    for i in range (10):
        print ("this is the table of the  ")
        for j in range (10):
             print(f"{i} x {j} = {i*j}") 

def run ():
     menu = """ 
     Welcome to the world of multiplications.
     1 - table of one
     2 - table of two
     3 - table of tree
     4 - table of four
     5 - table of five
     6 - table of six
     7 - table of seven
     8 - table of eight
     9 - table of nine
     
     tell me what your choice is: """
     
     option = int(input(menu))
     
     if option == 1:
         election_number ("i")
     elif option == 2:
         election_number ("i")
     elif option == 3:
         election_number ("i")
     elif option == 4:
         election_number ("i")
     elif option == 5:
         election_number ("i")
     elif option == 6:
         election_number ("i")
     elif option == 7:
         election_number ("i")
     elif option == 8:
         election_number ("i")
     elif option == 9:
         election_number ("i")
     elif option == 10:
         election_number ("i")
    
     else:
        print (" enter the correct option please ")
        """  """



if __name__ == "__main__": 
     run()

