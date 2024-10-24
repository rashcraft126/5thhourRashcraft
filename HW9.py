#Name:
#Class: 5th Hour
#Assignment: HW9
import random

#1. Print Hello World!
print("Hello World")
#2. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

#if temperature > 20
#  yes its hot
# no it is greater than 10
# yes its mild
# no its cold

temp = random.randint(1,30)
if temp >20 :
     print("It's hot!")
elif temp > 10:
     print("It's mild")
else:
     print("Its cold")
print("Thank you")

