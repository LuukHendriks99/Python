#Vars/list
cijferICOR = 7
cijferPROG = 7.5
cijferCSN = 7
lst = [cijferPROG,cijferICOR,cijferCSN]

#Average
avg= sum(lst)/len(lst)
print(avg)

#Reward
reward = sum(lst)/len(lst) *30 *len(lst)

print(reward)

print('Mijn cijfer', round(avg), 'leveren een beloning van', reward, 'op!')