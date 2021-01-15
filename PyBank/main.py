import os
import csv

#path to pull from the resource folder
input_path = os.path.join('Resources','budget_data.csv')

#establishing initial lists
Date=[]
Profit_Loss=[]

#convert csv data into list format
with open(input_path,'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for n, row in enumerate(reader):
        if not n:#skip header
            continue
        Date.append(row[0])
        Profit_Loss.append(row[1])
    Total_Month=(len(Date))

    #print(len(Date))
#Loop to calculate the net total of profit and loss
    Net_Total=0
    for row in Profit_Loss:
        Net_Total=Net_Total+int(row)
    #print(Net_Total)

#Loop to calculate the change from month to month
    Change=[]
    for x in range(len(Profit_Loss)-1):
        Monthly_Change=int(Profit_Loss[x+1])-int(Profit_Loss[x])
        Change.append(Monthly_Change)
    #Calculate the average
    Avg_Change=(sum(Change))/(Total_Month-1)
    #print("{:.2f}".format(Avg_Change))

#Loop to calculate the greatest profit and loss along with the corresponding month
    #establishing the initial values
    Max_Profit=0
    Min_loss=0
    Month_Max=''
    Month_Min=''

    for x in range(len(Change)):
        if int(Change[x])>Max_Profit:
            Max_Profit=Change[x]
            Month_Max=Date[x+1]
        elif int(Change[x])<Min_loss:
            Min_loss=Change[x]
            Month_Min=Date[x+1]

    #print(Max_Profit,Min_loss,Month_Max,Month_Min)
#Prints the financial analysis to a text file
import sys
sys.stdout = open('Main_PyBank.txt','w')
                  
#Print out the summary
print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(Total_Month))
print("Total: " + "$"+str(Net_Total))
print("Average Change: " + "$"+str("{:.2f}".format(Avg_Change)))
print("Greatest Increase in Profits: "+ Month_Max+"  ("+str(Max_Profit)+")")
print("Greatest Decrease in Profits: "+Month_Min+ "  ("+str(Min_loss)+")")

sys.stdout.close()
