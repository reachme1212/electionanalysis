from typing import Counter

#counties=["Arapahoe","denver","jefferson"]
#counties.insert(1,"El Paso")
#counties.pop(0)
#counties[1],counties[2]=counties[2],counties[1]
#counties.append("Arapahoe")
#print(counties)
#counties_tuple=("Arapahoe","Denver","Jefferson")
#print(counties_tuple[:-1])
#counties_dict={"Arapahoe": 422829,"Denver": 463353,"Jefferon":432438 }
#print(len(counties_dict))
#print(counties_dict["Arapahoe"])

voting_data= []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"El Paso", "registered_voters": 461149})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(len(voting_data))
print(voting_data)






