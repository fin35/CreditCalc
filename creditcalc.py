import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

arguments = sys.argv
print(type(arguments[4]))
#print(arguments)
#print(args)
if len(arguments) != 5:
    print("Incorrect parameters")

elif args.periods < 0:
    print("Incorrect parameters")

else:
    if args.type == "diff":
        if args.payment is not None:
            print("Incorrect parameters")
        else:
            i = (args.interest / 12) / 100
            #print(type(args.interest))
            add_up = 0
            for m in range(1, args.periods + 1):
                D = (args.principal / args.periods) + (i * (args.principal - (args.principal * (m - 1) / args.periods)))
                print("Month " + str(m) + ": paid out " + str(math.ceil(D)))
                add_up += math.ceil(D)
            overpayment = add_up - args.principal
            print("Overpayment = " + str(int(overpayment)))
    elif args.type == "annuity":
        #print(arguments)
        if args.periods is None:
            i = (args.interest / 12) / 100
            n = math.log(args.payment / (args.payment - i * args.principal), 1 + i)
            years = round(n) // 12
            month = math.ceil(n) % 12
            if years == 0:
                print("You need " + str(month) + " months to repay this credit!")
            elif month == 0:
                print("You need " + str(years) + " years to repay this credit!")
            else:
                print("You need " + str(years) + " years and " + str(month) + " months to repay this credit!")
            overpayment = (args.payment * round(n)) - args.principal
            print("Overpayment = " + str(int(overpayment)))
        elif args.payment is None:
            i = (args.interest / 12) / 100
            month_pay = args.principal * (i * math.pow((1 + i), args.periods)) / (math.pow((1 + i), args.periods) - 1)
            A = math.ceil(month_pay)
            print("Your annuity payment = " + str(A) + "!")
            overpayment = (A * args.periods) - args.principal
            print("Overpayment = " + str(int(overpayment)))
        elif args.principal is None:
            i = (args.interest / 12) / 100
            credit_principal = args.payment / (i * math.pow((1 + i), args.periods) / (math.pow((1 + i), args.periods) - 1))
            print("Your credit principal = " + str(math.floor(credit_principal)) + "!")
            overpayment = (args.payment * args.periods) - math.floor(credit_principal)
            print("Overpayment = " + str(int(overpayment)))
    elif args.type is None:
        print("Incorrect parameters")
