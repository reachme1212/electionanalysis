# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
#counties = ["Arapahoe","Denver","Jefferson"]
# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
# count=7
# while count<1:
#     print("hellow world")
# 0 to 4 is 5 items that is why we call range(5)
# numbers=[0,1,2,3,4]
# for num in range(5):
#         print(num)
# counties_tuple=("Arapahoe","Denver","Jefferson")
# for county in counties_tuple:
#     print(county)
#key0:value0
# counties = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties.items():
#     print(f"{county} county has  {voters}  registered voters")
# [] is list {}is dictionary [{}]= list of dictionaries    
# voting_data=[{"county":"Arapahoe", "registered_voters": 422829}, 
# {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# for county in voting_data:
#     print(f'{county["county"]} county has {county["registered_voters"]:3,}  registered voters')
# # not sure how to print comma in voters number with f string 
#print(f'{i["registered_voters"]:,d}')
# my_votes = int(input("How many votes did you get in the election? \n"))
# total_votes = int(input("What is the total votes in the election? \n"))
# print(f"I received {my_votes / total_votes * 100:.2f}% of thcountyvoters total votes.")
# high_school_types = [{"High School": "Hernandez", "Type": "District"},{"High School": "Figueroa", "Type": "District"},{"High School": "Wilson", "Type": "Charter"},{"High School": "Wright", "Type": "Charter"}]
# for schooltype in high_school_types:
#     print(schooltype)
high_schools = ["Huang High School",  "Figueroa High School", "Shelton High School", "Hernandez High School","Griffin High School","Wilson High School", "Cabrera High School", "Bailey High School", "Holden High School", "Pena High School", "Wright High School","Rodriguez High School", "Johnson High School", "Ford High School", "Thomas High School"]
print(high_schools)
import pandas as pd
pd.Series()
school_series= pd.Series(high_schools)
print(school_series)