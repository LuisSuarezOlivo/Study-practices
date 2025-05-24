lista= ['Hello', 'Goodbye', 'Hello Again']
my_list1= [1,2,3,4,5,6,7,8,9]
def Drop_element(lista:list)-> list: 
     del lista[1]
     return (lista)
lista= Drop_element(lista)
print (lista)
def remover_every_other1(my_list1, index =1):
    if len(my_list1) <= index:  
        return my_list1
    my_list1.pop(index)
    return remover_every_other1(my_list1, index + 1)

my_list1=remover_every_other1(my_list1)
print(my_list1)




