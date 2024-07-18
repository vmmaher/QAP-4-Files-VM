# Description: 4th QAP Assignment for Python Programming class, based on creating a program for the
# One Stop Insurance company to enter and calculate new insurance policy information for its customers.
# Author: Vanessa Maher
# Date(s): July 16th 2024
 
# Define required libraries.
import datetime
import sys
import time

# Define program functions.
def ReadConstants():
    f = open("QAP_4\Const.dat", "r")
    constants = f.readlines()
    f.close()
    return constants

def WriteToFile(data, filename):
    f = open(filename, 'a')
    f.write(f"{data} \n")

# Source: https://handhikayp.medium.com/creating-terminal-progress-bar-using-python-without-external-library-b51dd907129c
def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

def ConvertYesNo(value):
    if value == 'Y':
        return 'Yes'
    elif value == 'N':
        return 'No'
    
def ReadClaimData():
    f = open("QAP_4/Claims.dat", "r")
    claims = f.readlines()
    f.close()
    return claims

def ReadRecords():
    f = open("QAP_4\Records.dat", "r")
    records = f.readlines()
    f.close()
    return records

# Define program constants.
# Program contants are located in file Const.dat. Provide references to this below.
constants = ReadConstants()
POLICY_CONSTANT = int(constants[0].strip())
BASIC_PREMIUM = float(constants[1].strip())
EX_CARS_PERCENT_OFF = float(constants[2].strip())
EX_LIABILITY_COST = float(constants[3].strip())
EX_GLASS_COST = float(constants[4].strip())
EX_LOAN_CAR_COST = float(constants[5].strip())
HST_RATE = float(constants[6].strip())
MONTHLY_FEE = float(constants[7].strip())

# Main program starts here.
while True:
    # Gather user inputs.
    CustomerFirst = input("Enter the customer's first name: ").title()
    CustomerLast = input("Enter the customer's last name: ").title()
    CustomerStreet = input("Enter the customer's street address: ").title()
    CustomerCity = input("Enter the customer's city of residence: ").title()

    # Ensure that the user's inputted province is valid.
    ValidProvince = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YK"]
    while True:
        CustomerProvince = input("Enter the customer's province of residence: ").upper()
        if CustomerProvince in ValidProvince:
            break
        else:
            print("You have entered an invalid province. Please enter the two-letter code for the customer's province.")

    CustomerPostalCode = input("Enter the customer's postal code: ").upper()

    # Ensure that the user's inputted phone number is valid.
    CustomerPhone = input("Enter the customer's phone number. It must be 10 digits: ")
    while True:
        if (CustomerPhone).isdigit() and len(CustomerPhone) == 10:
            break
        else:
            print("You have entered an invalid phone number. Please ensure it is numerical and ten digits.")
            CustomerPhone = input("Enter the customer's phone number: ")

    while True:
        CarsInsured = int(input("Enter how many cars the customer wants insured: "))
        if CarsInsured < 1:
            print("You have entered an incorrect value. Please try again. ")
        else:
            break

    ExLiability = input("Does the customer want extra liability? Please enter Y or N: ").upper()
    ExGlassCov = input("Does the customer want optional glass coverage? Please enter Y or N: ").upper()
    ExLoanerCar = input("Does the customer want an optional loaner car? Please enter Y or N: ").upper()

    PaymentChoices = ["Full", "Monthly", "Down Pay"]
    while True:
        PaymentOption = input("Please indicate how the customer wishes to pay. Full, Monthly, or Down Pay: ").title()
        if PaymentOption not in PaymentChoices:
            print("You have entered an invalid payment choice. Please try again.")
        elif PaymentOption == "Down Pay":
            DownPayAmount = float(input("Please enter the amount of the down payment: "))
            break
        else:
            DownPayAmount = 0
            break

    # Into claim filing for past customers. User will indicate if they wish to proceed or not.
    ClaimWriteConfirm = input("Do you wish to file a claim? Please indicate Y or N: ").upper()
    if ClaimWriteConfirm == "Y":
        while True:
            ClaimNumber = input("Please enter the claim number: ")
            ClaimDate = input("Please enter the claim date in the following format, MM-DD-YYYY: ")
            # Input for claim amount. Will loop and continuously add to total until user indicated no. The total is initialized at 0 before loop begins.
            TotalClaimAmount = 0
            ClaimAmount = float(input("Please enter the claim amount: "))
            TotalClaimAmount += ClaimAmount
            ClaimAdditional = input("Are there additional claim amounts you would like to add to this customer? Please indicate Y or N: ").upper()
            if ClaimAdditional == "N":
                break  
            elif ClaimAdditional != "Y":
                print("You have entered an invalid response. Please try again. ")


    # Perform required calculations.
    # Calculate the insurance premium cost, with one car having a flat rate and additional cars getting a discount.
    if CarsInsured == 1:
        InsurancePremium = BASIC_PREMIUM
    else:
        InsurancePremium = BASIC_PREMIUM + (CarsInsured - 1) * ((1 - EX_CARS_PERCENT_OFF) * BASIC_PREMIUM)

    # Calculate any additional costs if the customer said yes. Otherwise, extra amount is 0.
    ExtraCosts = 0
    if ExLiability == "Y":
        ExtraCosts += (EX_LIABILITY_COST * CarsInsured)
    if ExGlassCov == "Y":
            ExtraCosts += (EX_GLASS_COST * CarsInsured)
    if ExLoanerCar == "Y":
        ExtraCosts += (EX_LOAN_CAR_COST * CarsInsured)

    # Determine the total insurance premium, which is the premium plus all the total extra costs.
    TotalInsurancePremium = InsurancePremium + ExtraCosts
    # Add taxes to get the final cost.
    TaxHST = TotalInsurancePremium * HST_RATE
    TotalCost = TotalInsurancePremium + TaxHST

    # Determine monthly payment amount, for 8 months. If the user selected down payment, calculate how much their payment will be after said payment.
    if PaymentOption == "Down Pay":
        MonthlyPayment = ((TotalCost + MONTHLY_FEE) - DownPayAmount) / 8
        TotalCost -= DownPayAmount
    else:
        MonthlyPayment = (TotalCost + MONTHLY_FEE) / 8

    # Determine the invoice date, which is today's current date. As well, determine the first payment date, the first day of the next month.
    InvoiceDate = datetime.date.today()
    if InvoiceDate.month == 12:
        FirstPaymentDate = InvoiceDate.replace(year=InvoiceDate.year + 1, month=1, day=1)
    else:
        FirstPaymentDate = InvoiceDate.replace(month=InvoiceDate.month + 1, day=1)



    # Define formatting rules for any numerical variables used in printing.
    ExtraCostsDsp = "${:,.2f}".format(ExtraCosts)
    DownPayAmountDsp = "${:,.2f}".format(DownPayAmount)
    InsurancePremiumDsp = "${:,.2f}".format(InsurancePremium)
    TotalInsurancePremiumDsp = "${:,.2f}".format(TotalInsurancePremium)
    TaxHSTDsp = "${:,.2f}".format(TaxHST)
    TotalCostDsp = "${:,.2f}".format(TotalCost)
    MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPayment)

    # Define formatting rules for any string variables used in printing, including dates.
    InvoiceDateDsp = InvoiceDate.strftime("%B %d, %Y")
    FirstPaymentDateDsp = FirstPaymentDate.strftime("%B %d, %Y")
    CustomerPhoneDsp = "(" + CustomerPhone[:3] + ") " + CustomerPhone[3:6] + "-" + CustomerPhone[6:]
    ExLiabilityDsp = ConvertYesNo(ExLiability)
    ExGlassCovDsp = ConvertYesNo(ExGlassCov)
    ExLoanerCarDsp = ConvertYesNo(ExLoanerCar)

    # Display output with specified formatting.
    print()
    print(f"                              One Stop Insurance Company")
    print(f"                                  ---CUSTOMER COPY---")
    print(f"                              --------------------------")
    print()
    print(f"{CustomerFirst} {CustomerLast:<40} Invoice Date:          {InvoiceDateDsp:>18s}")
    print(f"{CustomerStreet}")
    print(f"{CustomerCity}, {CustomerProvince} {CustomerPostalCode}")
    print(f"{CustomerPhoneDsp:<10}                                 Number of insured vehicle(s):          {CarsInsured:>2}")
    print(f"                                               Payment option indicated:        {PaymentOption:>8s}")
    # Add an if statement, so that if down pay was not selected, it will not appear on the invoice.
    if PaymentOption == "Down Pay":
        print(f"Additional options indicated:                  Down payment:                  -{DownPayAmountDsp:>9s}")
    else:
        print(f"Additional options indicated:")
    print(f"Optional liability up to $1,000,000:  {ExLiabilityDsp:>3s}      -----------------------------------------")
    print(f"Optional glass coverage:              {ExGlassCovDsp:>3s}      Extra costs charges:            {ExtraCostsDsp:>9s}")
    print(f"Optional loaner car:                  {ExLoanerCarDsp:>3s}      Insurance premiums:             {InsurancePremiumDsp:>9s}")
    print(f"                                               -----------------------------------------")
    print(f"                                               Sub-total:                      {TotalInsurancePremiumDsp:>9s}")
    print(f"                                               Taxes:                          {TaxHSTDsp:>9s}")
    print(f"                                               -----------------------------------------")
    print(f"                                               Total Due:                      {TotalCostDsp:>9s}")
    print()
    print(f"                      ------------------------------------------")
    print()
    if PaymentOption == "Down Pay" or PaymentOption == "Monthly":
        print(f"                              Monthly Payment: {MonthlyPaymentDsp:>9s}")
        print(f"                             YOUR FIRST PAYMENT IS DUE ON:")
        print(f"                                   {FirstPaymentDateDsp:^18s}")

    print()
    # Write processed data to a file for future use.
    # Begin with prompt to save file and then progress bar.
    while True:
        UserSaveConfirm = input("Would you like to save all inputted values and outputted values to record? Y or N: ").upper()
        if UserSaveConfirm == "Y":

            # Update policy number before output to file.
            records = ReadRecords()
            if records:
                LatestRecord = records[-1].strip()
                PolicyNumber = int(LatestRecord.split()[0].replace(',', ''))
                NextPolicyNumber = PolicyNumber + 1
                NextPolicyNumberStr = str(NextPolicyNumber)
            # If there is nothing in the Records.dat file, default the newest number to 1000.
            else:
                NextPolicyNumber = POLICY_CONSTANT


            print()
            # Code for progress bar. Source above
            TotalIterations = 30
            Message = "Saving Data..."
            for i in range(TotalIterations + 1):
                time.sleep(0.1)
                ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
            print()
            
            # Function for writing information to record.
            # Standard data writing.
            data = (
                f"{str(NextPolicyNumber)}, {str(CustomerFirst).strip()}, {str(CustomerLast).strip()}, {str(CustomerStreet).strip()}, {str(CustomerCity).strip()}, {str(CustomerProvince).strip()}, {str(CustomerPostalCode).strip()}, {str(CustomerPhone).strip()}, "
                f"{str(CarsInsured)}, {str(ExLiability)}, {str(ExGlassCov)}, {str(ExLoanerCar)}, {str(PaymentOption)}, {str(DownPayAmount)}, {str(InsurancePremium)}, {str(ExtraCosts)}, {str(TotalInsurancePremium)}, {str(TotalCost)}, {str(MonthlyPayment)}, "
                f"{str(InvoiceDate)}, {str(FirstPaymentDate)}"
            )
            WriteToFile(data, "QAP_4\Records.dat")
            # Claim data writing.
            if ClaimWriteConfirm == "N":
                break
            else:
                claimdata = f"{str(ClaimNumber)}\n{str(ClaimDate)}\n{str(ClaimAmount)}"
                WriteToFile(claimdata, "QAP_4\Claims.dat")

            print()
            print("Insurance record has been successfully saved to Records.dat.")
            print()
            print()
            break
        elif UserSaveConfirm == "N":
            break
        else:
            print("Invalid response. Please try again.")

    # Display previous claim information, if the user wishes to.
    while True:
        ClaimRecordConfirm = input("Would you like to view previous claim records? Y or N: ").upper()
        print()
        if ClaimRecordConfirm == "Y":
            # Read file and format necessary data.
            print("Claim #   Claim Date      Amount")
            print("---------------------------------")
            claims = ReadClaimData()
            for i in range(0, len(claims), 3):
                print(f" {claims[i].strip()}     {claims[i+1].strip()}     {claims[i+2].strip()}")
            break
        elif ClaimRecordConfirm == "N":
            break
    
    print()
    ProceedConfirm = input("Would you like to enter another customer? Y or N: ").upper()
    if ProceedConfirm == "N":
        print("Thank you!")
        exit()
        
    # Done! :)