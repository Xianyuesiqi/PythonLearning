
def significant_digits(x):
    a = str(x)
    a = a.replace("." ,"")
    while a[0] == '0':
        a = a. replace(a[0],"")
    return len(a)
    print(a)

print(significant_digits(1.0042))

def remove_operational_symbols(expression):
    expression = str(expression)
    print(expression)

    expression = expression.replace("+", ",")
    expression = expression.replace("-", ",")
    expression = expression.replace("*", ",")
    expression = expression.replace("/", ",")

    return expression
print(remove_operational_symbols(3.0*2.54+2.009))

    # for i in len(expression):
    #     if expression[i] == "+":
    #         expression = expression.replace("+", ",")
    #     elif expression[i] == "-":
    #         expression = expression.replace("-", ",")
    #     elif expression[i] == "*":
    #         expression = expression.replace("*", ",")
    #     elif expression[i] == "/":
    #         expression = expression.replace("/", ",")
    #     break
def  min_sig_count(expression):
    nums = remove_operational_symbols(expression).split(",")
    print("nums is :" + str(nums))
    minimum = 0
    for i in range(len(nums)):
        if i == 0:
            minimum = significant_digits(nums[i])
        else:
            iCount = significant_digits(nums[i])
            if iCount < minimum:
                minimum = iCount
    return minimum

# a =0.000234699
# count = 4
def roundValue(a, count):
    strA = str(a)
    roundTo = 0
    if(strA[0] == '0'):
        sigCount = 0

        shouldCount = False
        for i in range(2, len(strA)):
            iChar=strA[i]
            if (iChar!='0' and  not shouldCount):
                shouldCount = True

            if(shouldCount):
                sigCount+=1

            if(sigCount ==  count):
                roundTo = i
    else:
        #cut the result to  have only number of  digits  as count
      #e.g  1.643 ==> 1.6
        if ("." in strA):
            # find the  digit count  before dot,
            dot_index = strA.index(".")
            strA_before_dot = strA[0: dot_index]  # 1
            # roundTo = count - d.b.dot
            roundTo = count - len(strA_before_dot)+1  # TODO  handle count<d.b.dot
            #  count =2, result =1.643 ==>  1.6
        else:
            # if length of result  == count==>  return
            # elif  length of  result >  count ==> sce...
            #  else length of result < count ,  add dot,  then add 0
            pass


    print('roundTo is: ' + str(roundTo))
    f_output = round(a, roundTo-1)
    print("f_output is:" + str(f_output))

def final_output(expression):
    value = eval(expression)
    min_count = min_sig_count(expression)
    final_value =roundValue(value, min_count)
    return final_value

#b = "0.04*0.51*0.7457"
c = "3.42*0.54*0.89"
print('final_output is : ' + str(final_output(c)))