import csv

def three():
    number = int(input("Enter your number: "))
    f = open(f"answer.csv", 'w')
    writer = csv.writer(f)
    header = ['Step', 'Number']
    writer.writerow(header)
    step = 0;
    data =[step, number]
    writer.writerow(data)
    while number != 1:
        if number !=1:
            if number % 2:
                number*=3
                number+=1
            else:
                number/=2
            step+=1
            data =[step, number]
            writer.writerow(data)
            print(f"{step}: {number}")
    print(f"It took {step} steps to get to 1")

three()