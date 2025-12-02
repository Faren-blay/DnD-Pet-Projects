import random
player_amount = int(input("Enter amount of charcters ")) 

#Making a list with every character initiative bonus
chr_bonuses = [0, 0, 0, 0]

#Add values to the list, if the players number >4
cycle_time = 0
if player_amount > 4:
    while cycle_time != player_amount:
        chr_bonuses.append(0)
        cycle_time += 1

    

#ask for bonuses by cycle and add bonuses to list
cycle_time = 0
while cycle_time != player_amount: 
    bonus = int(input("Enter Initiative Bonus "))
    chr_bonuses[cycle_time] = bonus
    cycle_time += 1
print(chr_bonuses)


#Roll initiative by cycle that adds every bonus sequentially. 
cycle_time = 0
initiative = []
while cycle_time != player_amount:
    #Make the dice roll
    d20 = random.randint(1, 20)
    init = d20 + chr_bonuses[cycle_time]
    initiative.append(init)
    cycle_time += 1

initiative.sort(reverse=True)
print(initiative)
