# QAP-4-Files-VM
This is the 4th QAP Assignment for Software Development. Included are two of three assignments; one is a Python program, the other is Javascriopt.
The Python program was developed for One Stop Insurance company. The program allows users to enter and calculate new insurance policy information for customers.
The JavaScript program is for managing motel customer information and outputting it to the console and html.

## Description
## Python:
The program is designed to gather user inputs such as customer's name, address, phone number, number of cars to be insured, and additional options like extra liability, glass coverage, and loaner cars. It then performs required calculations to determine the insurance premium cost, additional costs, total insurance premium, taxes, total cost, and monthly payment amount. The program also allows the user to save all inputted values and outputted values to a record for future use.
## JavaScript:
The program is designed to gather and display customer information such as name, date of birth, gender, room preference, room number, payment method, mailing address, phone number, email address, check-in date, and check-out date. It also includes functions to determine the length of stay, the age of the customer, and the appropriate pronoun to use based on the customer's gender.

## Usage
Python:
1. Run: `python qap4.py`
2. Enter customer info: First name, Last name, Street address, City, Province (2-letter code), Postal code, Phone number (10 digits)
3. Enter insurance details: Number of cars, Extra liability (Y/N), Optional glass coverage (Y/N), Optional loaner car (Y/N)
4. Choose payment option: Full, Monthly, Down Pay (enter down payment amount if chosen)
5. File a claim (optional): Enter 'Y' to file a claim. Enter claim number, claim date, claim amount. For additional claim amounts, enter 'Y'.
6. Save data: Enter 'Y' to save data.
7. View previous claim records (optional): Enter 'Y' to view previous claim records.
8. Enter another customer (optional): Enter 'Y' to enter another customer.

Note: Program uses data from `Const.dat`, `Claims.dat`, `Records.dat` in `QAP_4` directory. The program writes data to these files.
