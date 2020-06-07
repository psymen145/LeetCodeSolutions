class Solution:
    def insertIntoFinalQ(self, q, largest_grp):
        #print('Largest group ', largest_grp)
        if len(q) == 0:
            q = largest_grp
        else:
            for i in range(len(largest_grp)):
                index = largest_grp[i][1]
                
                q = q[:index] + [largest_grp[i]] + q[index:]
                #print(q)

        return q
    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ordered_lst = []
        prev_max_height = 9999999999
        
        while True:
            # first group by height
            max_height = 0
            largest_group = []
            for i in range(len(people)):
                if people[i][0] >= max_height and people[i][0] < prev_max_height:
                    max_height = people[i][0]

            #print('Max Height', max_height)
            if prev_max_height == max_height:
                break
            else:
                prev_max_height = max_height

            # add people with the max height:
            for i in range(len(people)):
                if people[i][0] == max_height:

                    # sort by k in largest group
                    if len(largest_group) == 0:
                        largest_group.append(people[i])
                    else:
                        for j in range(len(largest_group)):
                            if people[i][1] <= largest_group[j][1]:
                                largest_group = largest_group[:j] + [people[i]] + largest_group[j:]
                                break
                            elif j == len(largest_group)-1:
                                largest_group.append(people[i])
                                break

            ordered_lst = self.insertIntoFinalQ(ordered_lst, largest_group)
            
        #print(ordered_lst)
        return(ordered_lst)