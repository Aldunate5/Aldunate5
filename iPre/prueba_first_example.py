from amplpy import AMPL, Environment

ampl=AMPL(Environment(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\AMPL'))
ampl.read(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\AMPL/models/diet.mod')
ampl.readData(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\AMPL/models/diet.dat')

ampl.solve()

# Get objective entity by AMPL name
totalcost = ampl.getObjective('total_cost')
# Print it
print("Objective is:", totalcost.value())

# Reassign data - specific instances
cost = ampl.getParameter('cost')
cost.setValues({'BEEF': 5.01, 'HAM': 4.55})
print("Increased costs of beef and ham.")
print(cost.getValues())

# Resolve and display objective
ampl.solve()
print("New objective value:", totalcost.value())

# Reassign data - all instances
cost.setValues([3, 5, 5, 6, 1, 2, 5.01, 4.55]) #se actualizan valores de los parametros
print("Updated all costs.")
print(cost.getValues())

# Resolve and display objective
ampl.solve()
print(ampl.getObjective('total_cost'))
print("New objective value:", totalcost.value())

# Get the values of the variable Buy in a dataframe object
buy = ampl.getVariable('Buy')
df = buy.getValues()
print(buy.getValues)
# Print them
print(df)

# Get the values of an expression into a DataFrame object
df2 = ampl.getData('{j in FOOD} 100*Buy[j]/Buy[j].ub')
# Print them
print(df2)

'''
print(ampl.getOption('version'))

restriccion=ampl.getConstraint('Diet')
print(restriccion)
restricciones=ampl.getConstraints()
print(restricciones)


food=ampl.getSet('FOOD')
print(food)
sets=ampl.getSets()
print(sets)
'''