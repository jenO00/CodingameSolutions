
a, b, c, d = [int(i) for i in input().split()]
n = int(input())
instructions = []
for i in range(n):
    instruction = input()
    instructions.append(instruction)
#always 4 places we can be 
num_dict = {"a": a, "b": b, "c": c, "d": d}
letters = "abcd"
instruction_turn = 0
#for i in instructions:
while instruction_turn < n:
    i = instructions[instruction_turn]

    operation = i[:3]
    if operation == "MOV":
        oper = i[6:].split()[0].strip()
        if oper in letters:
            #not necessarily a number directly.. 
            letter = oper
            curr = num_dict[letter]
            num_dict[i[4]] = curr #move it over
        else:   
            num_dict[i[4]] = int(oper)
        instruction_turn += 1


    elif operation == "JNE":
        desired_destination = int(i.split()[1])
        first_operand = i[6:].split()[0].strip()
        second_operand = i.split()[-1].strip()
        new_first_operand = ""
        new_second_operand = ""
        if first_operand in letters: 
            new_first_operand = num_dict[first_operand]
        else:
            new_first_operand = int(first_operand) #they are the same

        if second_operand in letters:
            new_second_operand = num_dict[second_operand]
        else:
            new_second_operand = int(second_operand) #they are the same
        if new_first_operand != new_second_operand:
            instruction_turn = int(desired_destination) 
        else: 
            instruction_turn += 1

    elif operation == "ADD":
        destination = i[4]
        first_operand = i[6:].split()[0].strip()
        if first_operand in letters: 
            letter = first_operand
            first_num = num_dict[letter] 
        else:
            first_num = first_operand 
        second_operand = i.split()[-1].strip()
        if second_operand in letters:
            letter = second_operand
            sec_num = num_dict[letter]
        else:
            sec_num = second_operand
        addition = int(first_num) + int(sec_num)
        num_dict[destination] = addition
        instruction_turn += 1
    else:
        #SUB
        destination = i[4]
        first_operand = i[6:].split()[0].strip()
        if first_operand in letters: 
            letter = first_operand
            first_num = num_dict[letter] 
        else: 
            first_num = first_operand
        
        second_operand = i.split()[-1].strip()
        if second_operand in letters:
            letter = second_operand
            sec_num = num_dict[letter]
        else:
            sec_num = second_operand
        sub = int(first_num) - int(sec_num)
        num_dict[destination] = sub
        instruction_turn += 1
    res = ""
    count = 0
    for i in num_dict.values():
        if count != 3:
            res += str(i) + " "
            count += 1
        else:
            res += str(i)
print(res)

