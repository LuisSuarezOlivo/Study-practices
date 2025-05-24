# def  basic_op(operator,value1,value2):
   # if operator == "+":
   #     answer= value1 + value2
   # elif operator == "-":
   #     answer= value1 - value2
   # elif operator == "*":
   #     answer= value1 * value2
   # elif operator == "/":
   #     if value2== 0:
    #        raise ValueError("not possible")
   #     answer= value1 / value2
   # else:
   #     raise ValueError("operation wrong. use '+','-','/', or '*'.")
   # return answer
# try:
   # sum1 = basic_op("+",11,1)
    #print("suma",sum1)

  #  rest1 = basic_op("-",4,2)   
   # print("rest",rest1)

    #mult1 = basic_op("*",8,7)
    #print("multi", mult1)

    #div1 = basic_op("/",2,3)
    #print("divis", div1)

    #div2 = basic_op("/",2,0)
#except ValueError as error:
#    print("divis", error)
def distinct(array):
    special_element = []
    for num in array:
        if num not in special_element:
            special_element.append (num)
    return special_element

array_2 =[1, 1, 1, 2, 3, 4, 5]
answer2 = distinct (array_2)
print (answer2)

array_3 = [1, 1, 2]
answer3 = distinct (array_3)
print (answer3)
array_4 = [1]
answer4 = distinct (array_4)
print(answer4)

array_1 = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7] 
answer = distinct (array_1)
print (answer)
pass