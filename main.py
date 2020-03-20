import random

def Split_team(number_of_teams):
    #set up individual teams
    f_e =["Liam", "Pav", "Tiago"]
    b_e=["Duncan", "Amitabh", "Sylvain", "Puneet"]
    d_o=["Gavan", "Zong-Pei"]
    p_t=["Satnam", "Tarig", "Michal"]
    f_o=["Tracy", "Zoe", "Tobias"]

    #groupe the teams together. 
    whole_group = [f_e, b_e, d_o, p_t, f_o]

    #create an array with the number of groups we want to split the team into. 
    group_sets =[]
    number_of_groups =number_of_teams
    for t in range (0, number_of_groups,1):
        group_sets.append([])
    g_n=0   #set starting position as 1

    # start with each team, and distribute them first before going to the next team
    for i in range(0,len(whole_group)):
        j=len(whole_group[i])
        while j>0:
            if j>1:
                a=random.randrange(0,j-1,1)
            else:
                a=0
            group_sets[g_n].append(whole_group[i][a])
            whole_group[i].pop(a) #remove person from list
        
            #check is we have gone through all the groups.  start from the beginning is we have
            if g_n<(number_of_groups-1): 
                g_n=g_n+1 
            else:
                g_n=0
            
            j=len(whole_group[i])
    return group_sets

#print the sets.
g_s= Split_team(3)
for b in range (0, len(g_s)):
    print (g_s[b])
    
