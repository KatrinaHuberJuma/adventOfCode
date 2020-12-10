"""
part 1
make inputs into a set (nums)
for num in nums
    is 2020 - num in nums?
        if yes, return num * (2020 - num)

"""
# nums = set()

# f = open('workfile')

# for line in f:
#     line = line.rstrip()
#     num = int(line)

#     if (2020 - num) in nums:
#         print("found it")
#         print((2020 - num) * num)
#     else:
#         nums.add(num)

# f.close()


"""
Part 2
nested for loop version

"""
# nvm, I don't feel like doing this version, I want to build nests

 
""" 
Part 2 using some kind of dict? 

make options_dict
make 

for num
    add num to set
    for set_num in set:
        if set_num + num > 2020:
            at options_dict[set_num + num], save a list of set_num and num
        
            

"""

def find_nums(filepath):
    set_nums = set()

    f = open(filepath)

    opt_dict = {}

    for line in f:
        line = line.rstrip()
        num = int(line)

        if num in opt_dict:
            return num * opt_dict[num]

        for n in set_nums:
            if n + num < 2020:
                opt_dict[2020 - (n + num)] = n * num

        set_nums.add(num)

    f.close()


print(find_nums("workfile"))