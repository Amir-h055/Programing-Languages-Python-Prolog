class Multi_set_functionaries:

    def Add_element(self , setA , element):
        sA = list(setA)
        sA.append(element)
        sA.sort()
        # Making the format
        result = '{'+str(setA)[1:-1] + '} + '+ str(element) + ' = {'+ str(sA)[1:-1] +'}'
        return result

    def Removing_all_occ_of_a_element(self , Set_A , element):
        new_list = [ele for ele in Set_A if ele != element]
        # Making the format
        result = '{'+ str(Set_A)[1:-1] + "}\\" +str(element) + ' = {' + str(new_list)[1:-1] + '}'
        return result

    def multiplicity(self , Set_A , element):
        # Making the output
        result = 'm({' + str(Set_A)[1:-1] + '}, '+str(element) + ') = '+ str(Set_A.count(element))
        return result

    def Union_with_another_set(self , Set_a , Set_b):
        new_list = []
        large_lst =list(set(Set_a).union(set(Set_b)))
        for i in set(large_lst):
           if i in Set_a and i in Set_b:
            count_a = Set_a.count(i)
            count_b = Set_b.count(i)
            for j in range(max([count_a , count_b])):
                new_list.append(i)

           elif i in Set_a and i not in Set_b:
            for j in range(Set_a.count(i)):
                new_list.append(i)

           elif i not in Set_a and i in Set_b:
            for j in range(Set_b.count(i)):
                new_list.append(i)
    # Making the format
        result = '{' + str(Set_a)[1:-1] + '} U {' + str(Set_b)[1:-1] +'} = {' + str(new_list)[1:-1] + '}'
        return result

    def Intersection_with_another_set(self , Set_A , Set_B):
        new_list = []
        large_lst = list(set(Set_A).intersection(set(Set_B)))
        for ele in large_lst:
            min_occ = Set_A.count(ele) if Set_A.count(ele) <Set_B.count(ele) else Set_B.count(ele)
        # Used Ternary Operator to fing minimum occurences of each element
        for i in range(min_occ):
            new_list.append(ele)
        # Making the format
        result = '{' + str(Set_A)[1:-1] + '} ∩ {' + str(Set_B)[1:-1] +'} = {' + str(new_list)[1:-1] + '}'
        return result

    def Difference_Update(self , Set_A , Set_B):
        new_list = []
        for ele in set(Set_A):
            if ele not in Set_B:
                for j in range(Set_A.count(ele)):
                    new_list.append(ele)
            else:
                a_b = Set_A.count(ele) - Set_B.count(ele)
                for i in range(a_b):
                    new_list.append(ele)
            # Making the format
            result = '{' + str(Set_A)[1:-1] + '} - {' + str(Set_B)[1:-1] +'} = {' + str(new_list)[1:-1] + '}'
            return result

# Check code
obj = Multi_set_functionaries()
print(obj.Add_element([1,2,3],8))
print(obj.Removing_all_occ_of_a_element([1,1,2,3],1))
print(obj.multiplicity([1,1,1,2,2,3],1))
print(obj.Union_with_another_set([1,2] , [2,2,3]))
print(obj.Intersection_with_another_set([1,1,2,2,3] , [2,2,2,3,4]) )
print(obj.Difference_Update([1,1,1,2,2,3] , [1,2,2,2]))
