# Jacob L Stewart
# Chapter 07 Assignment 29
# Allows a salesman to enter sales into a text file, then reads the file to display
# the total amount for each service category.
import datetime


def main():
    # get file from user or create a new one
    fileName = getFile()
    # prompts user to input data
    inputSales(fileName)
    # reads file and displays
    serviceTotals = getSales(fileName)
    print(" ----------------------\n", "    Sales Report\n",
          "----------------------")
    # applies formatting of 'Category: $ totalAmount'.
    for x in serviceTotals:
        print("{}: $ {}".format(x, round(serviceTotals.get(x), 2)).strip())


# inputSales() prompts user for data then writes to desired file
def inputSales(filename):
    # checks if file exists, if it doesn't a new file is created.
    fileExists(filename)
    # @done loop key to control when to exit program
    done = False
    # initializing variables
    dateOfSale = ""
    saleTotal = 0.0

    # loop that controls whether the user wants to input data into file or simply get the report
    print("Would you like enter new data? Typing N will print the Sales Report. Type Y or N.")
    invalid = True
    while invalid:
        userResponse = input("")
        if userResponse.upper() == "Y":
            invalid = False
        elif userResponse.upper() == "N":
            invalid = False
            done = True
        else:
            print("Invalid response! Please only type Y or N.")
    # if file is blank overwrite the file with new data
    if fileEmpty(filename):
        openFile = open(filename, "w")
    # if the file already has some information append to file to add data
    else:
        openFile = open(filename, "a")
    # master loop to allow user to input multiple lines until N is entered when prompted
    while not done:
        # getting name of customer and service (or ID)
        custName = input("Input customer name or ID: ")
        # accepted names for services provided
        serviceNames = ["CONFERENCE", "LODGING", "DINNER"]
        invalid = True
        # loop ensure what is typed matches one of the service names pre defined
        while invalid:
            serviceName = input("Input service name or ID: ")
            if serviceName.upper().strip() not in serviceNames:
                print("Service names expected: Conference, Lodging, or Dinner!")
            else:
                invalid = False

        # loop checks that the value entered for saleTotal contains no strings
        invalid = True
        while invalid:
            try:
                saleTotal = float(input("Input sales total: "))
                invalid = False
            except ValueError:
                print("Please only input numbers! EX. 19.99")

        # validates date based on date_format
        date_format = '%m/%d/%Y'
        invalid = True
        while invalid:
            try:
                dateOfSale = input("Input date of sale (MM/DD/YYYY): ")
                # dateObject returns date + 00:00:00, @strftime added to retain only the formatted date
                dateObject = datetime.datetime.strptime(dateOfSale, date_format).strftime(date_format)
                dateOfSale = dateObject
                invalid = False
            except ValueError:
                print("Input '" + dateOfSale + "' does not match format 'MM/DD/YYYY'.")
        openFile.write(custName + ";" + serviceName + ";" + str(saleTotal) + ";" + dateOfSale + "\n")
        # checks that user wants to continue or stop entering data
        print("Would you like to continue entering data? Type Y or N.")
        invalid = True
        while invalid:
            userResponse = input("")
            if userResponse.upper() == "Y":
                invalid = False
            elif userResponse.upper() == "N":
                invalid = False
                done = True
                openFile.close()
            else:
                print("Invalid response! Please only type Y or N.")


# getSales() iterates over file and returns map with category and cost
def getSales(filename):

    salesReport = open(filename, "r")
    # map to attach overall cost to its respecting service
    service_cost = {}
    for line in salesReport:
        # creates array of fields using ; to split the data
        fields = line.split(";")
        # assigns totalCost to float value in file
        try:
            totalCost = float(fields[2])
        except ValueError:
            print("File data for: " + fields[0] + " has incorrect values for cost value. " + fields[2])
            exit()
        date_format = '%m/%d/%Y'
        try:
            dateObject = datetime.datetime.strptime(fields[3].strip(), date_format).strftime(date_format)
        except ValueError:
            print("File data for " + fields[0] + " does not match format 'MM/DD/YYYY'.")
            exit()
        # assigns serviceID to service name in file and strips accidental whitespace
        serviceID = fields[1].upper().strip().replace(" ", "")
        # if service isn't in service_cost{} it adds to it with a value of 0.0
        if serviceID not in service_cost:
            service_cost[serviceID] = 0.0
        service_cost[serviceID] += totalCost
    # closing file
    salesReport.close()
    return service_cost


# force opens a file and throws exception when file is not found
def fileExists(filename):
    try:
        with open(filename) as fileObject:
            fileObject.read()
            return True
    except FileNotFoundError:
        return False


# checks if file is empty to decide later whether to overwrite or append
def fileEmpty(filename):
    fileObj = open(filename, "r")
    if fileObj.readline() == "":
        return True
    else:
        return False


def getFile():
    # loop to make sure the user is selecting the right file
    fileReady = False
    while not fileReady:
        # Retrieve desired filename file will either be found or created later.
        fileName = input("Please enter a file name for this report: ")
        # if file is found exits loop
        if fileExists(fileName):
            print(fileName + " found!")
            fileReady = True
        else:
            # check if user wants to create the file they entered.
            print(fileName + " not found. Do you want to create this file? Y/N. Type Q to quit.")
            invalid = True
            while invalid:
                userResponse = input("")
                if userResponse.upper() == "Y":
                    invalid = False
                    newFile = open(fileName, "w")
                    newFile.close()
                    fileReady = True
                elif userResponse.upper() == "N":
                    invalid = False
                elif userResponse.upper() == "Q":
                    exit()
                else:
                    print("Invalid response! Please only type Y or N.")
    return fileName


main()
