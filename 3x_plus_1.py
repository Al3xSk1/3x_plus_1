## Import for .csv capabilities
import csv
          
def equation():
    ## Is it a Natural Number
    naturalNumber = False
    while naturalNumber == False:
        try:
            ## Accepting input
            number = int(input("Enter your number: "))
            ## Checking input
            if number >= 1:
                naturalNumber = True
            else:
                print("Please enter a natural number (A number larger than 0 without a decimal)")
        except ValueError: 
            print("Please enter a natural number (A number larger than 0 without a decimal)")
    ## Setup .csv file
    f = open(f"answer.csv", 'w')
    writer = csv.writer(f)
    header = ['Step', 'Number']
    writer.writerow(header)
    step = 0
    data =[step, number]
    writer.writerow(data)
    ## Equation
    while number != 1:
        if number !=1:
            if number % 2:
                number*=3
                number+=1
            else:
                number/=2
            step+=1
            ## Finish .csv Step
            data =[step, number]
            writer.writerow(data)
            ## Print step, number
            print(f"{step}: {number}")
    ## Print the total
    print(f"It took {step} steps to get to 1")

## Run the function
equation()