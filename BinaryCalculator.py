def generate_array(n = 1, max_var = 1):
    number1 = 2**max_var
    numbers_zero = number1//2**n
    numbers_ones = number1//2**n
    zeros = [int(i) for i in "0"*numbers_zero]
    ones = [int(i) for i in "1"*numbers_ones]
    return (zeros+ones)*(number1//(len(zeros) + len(ones)))
variables = ["A", "B"]
variables_num = {}
variables_count = 0
equation = "" #
while True:
    cmd = input("Enter command >>> ")
    if cmd.find("var_add") != -1 and len(cmd.split(" ")[0]) == len("var_add"):
        if cmd.split(" ")[1] not in variables:
            variables.append(cmd.split(" ")[1])
            variables_count = len(variables)
        else:
            print("# Variable", cmd.split(" ")[1], "exist")
    elif cmd.find("var_remove") != -1 and len(cmd.split(" ")[0]) == len("var_remove"):
        if cmd.split(" ")[1] not in variables:
            print("# Variable dosen't exist")
        else:
            variables.remove(cmd.split(" ")[1])
            try:
                del variables_num[cmd.split(" ")[1]]
            except:
                pass
    elif cmd.find("var_set") != -1 and len(cmd.split(" ")[0]) == len("var_set"):
        if cmd.split(" ")[1] in variables:
            variables_num[cmd.split(" ")[1]] = int(cmd.split(" ")[2])
        else:
            print("# Variable dosen't exist")
    elif cmd.find("equ_set") != -1 and len(cmd.split(" ")[0]) == len("equ_set"):
        equation = " ".join(cmd.split(" ")[1:])
    elif cmd.find("equ_show") != -1 and len(cmd.split(" ")[0]) == len("equ_show"):
        print(equation)
    elif cmd.find("help") != -1 and len(cmd.split(" ")[0]) == len("help"):
        print("var_add", "->", "Added new variable")
        print("var_remove", "->", "Remove exist variable")
        print("var_set", "->", "Set for varible a number")
        print("var_show", "->", "Show all variables")
        print("equ_oper", "->", "All operations you can use")
        print("equ_set", "->", "Set equations")
        print("equ_solve", "->", "Solve Equations")
        print("equ_solve_find", "->", "Solve Equations where F = X")
        print("equ_show", "->", "Show set equation")
        print("help", "->", "Show this message")
    elif cmd.find("equ_oper") != -1 and len(cmd.split(" ")[0]) == len("equ_oper"):
        print("# and -> Logical AND")
        print("# or -> Logical OR")
        print("# xor -> Logical XOR")
        print("# == -> Logical EQUALS")
        print("# => -> Logical IMPLECATION")
        print("# not -> Logical NOR")
    elif cmd.find("equ_solve") != -1 and len(cmd.split(" ")[0]) == len("equ_solve"):
        try:
            if len(equation) != 0:
                temp = {}
                for i in variables:
                    temp[i] = generate_array(variables.index(i) + 1, len(variables))
                table_start = "|"
                for i in variables:
                    table_start += "{0:^3}".format(i)
                    table_start += "|"
                table_start += ("{0:^" + str(len(equation) + 2) + "}").format(equation) + "|"
                print("-"*len(table_start))
                print(table_start)
                print("-"*len(table_start))
                for i in range(2**len(variables)):
                    equation_temp = equation
                    equation_temp = equation_temp.replace(" => ", " <= ")
                    for j in variables:
                        if j not in variables_num.keys():
                            equation_temp = equation_temp.replace(j, str(temp[j][i]))
                        else:
                            equation_temp = equation_temp.replace(j, str(variables_num[j]))
                    result = eval(equation_temp)
                    for_print = "|"
                    for k in variables:
                        if k not in variables_num.keys():
                            for_print += "{0:^3}".format(str(temp[k][i]))
                            for_print += "|"
                        else:
                            for_print += "{0:^3}".format(str(variables_num[k]))
                            for_print += "|"
                    for_print += ("{0:^" + str(len(equation) + 2) + "}").format(result) + "|"
                    print(for_print)
                print("-"*len(table_start))
                del temp
            else:
                print("Equations dosen't set.")
        except:
            print("# Error in solve")
    elif cmd.find("equ_solve_find") != -1 and len(cmd.split(" ")[0]) == len("equ_solve_find"):
        try:
            if len(cmd.split(" ")) == 2:
                if len(equation) != 0:
                    temp = {}
                    for i in variables:
                        temp[i] = generate_array(variables.index(i) + 1, len(variables))
                    table_start = "|"
                    for i in variables:
                        table_start += "{0:^3}".format(i)
                        table_start += "|"
                    table_start += ("{0:^" + str(len(equation) + 2) + "}").format(equation) + "|"
                    print("-"*len(table_start))
                    print(table_start)
                    print("-"*len(table_start))
                    for i in range(2**len(variables)):
                        equation_temp = equation
                        equation_temp = equation_temp.replace(" => ", " <= ")
                        for j in variables:
                            if j not in variables_num.keys():
                                equation_temp = equation_temp.replace(j, str(temp[j][i]))
                            else:
                                equation_temp = equation_temp.replace(j, str(variables_num[j]))
                        result = eval(equation_temp)
                        if result == int(cmd.split(" ")[1]):
                            for_print = "|"
                            for k in variables:
                                if k not in variables_num.keys():
                                    for_print += "{0:^3}".format(str(temp[k][i]))
                                    for_print += "|"
                                else:
                                    for_print += "{0:^3}".format(str(variables_num[k]))
                                    for_print += "|"
                            for_print += ("{0:^" + str(len(equation) + 2) + "}").format(result) + "|"
                            print(for_print)
                    print("-"*len(table_start))
                    del temp
                else:
                    print("Equations dosen't set.")
            else:
                print("Parametr dosen't set")
        except:
            print("# Error in solve")
    elif cmd.find("var_show") != -1 and len(cmd.split(" ")[0]) == len("var_show"):
        if len(variables) != 0:
            for i in variables:
                if i in variables_num:
                    print("#" ,i, "->", "(Logical variable) equals", variables_num[i])
                else:
                    print("#" ,i, "->", "(Logical variable)")
        else:
            print("# No variables found")
    else:
        print("# Command not found")