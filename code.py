#Dollars to euros
#10-31-2024
#The program is Roman A. Vaninger

choice = True

while choice == True:
    #step 2
    dollar = float(input("Enter dollar amount to be converted:"))
    #step 3
    euros = dollar*0.94540
    #step 4
    print("Number of euros:" + str(euros) )
    #step 5
    choice = input("Continue or not ? (True/False): ")



