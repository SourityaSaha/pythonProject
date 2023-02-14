#Individually done by Souritya Saha A20145347


# List to store the required data
students_data = []

# Opening the students file
with open("/Users/sourityasaha/PycharmProjects/pythonProject/Students.txt", "r") as file:
    # Skip the header row
    next(file)

    # Reading the file end to end
    for line in file:
        # Split the line
        sid, last_name, first_name, graduating_year, graduating_term, degree_program = line.strip().split("\t")
        # Storing the data as dictionary
        students_data.append({
            "#": sid,
         "last_name": last_name,
            "first_name": first_name,
            "graduating_year": graduating_year,
            "graduating_term": graduating_term,
            "degree_program": degree_program
        })


while True:
    # Printing the items
    print("List of queries to perform:")
    print("1. Display all student records")
    print("2. Display students whose last name begins with a certain string (case insensitive)")
    print("3. Display all records for students whose graduating year is a certain year")
    print("4. Display a summary report of number and percent of students in each program,\n"
          "   for students graduating on/after a certain year")
    print("5. Exit the program")
    ch = input("Choose an option: ")

    print()

    # If user chooeses to display all the items
    if ch == "1":

        print("%-15s%-20s%-20s%-20s%-20s%-20s" % (
            "Student ID", "Last Name", "First Name", "Graduating Year", "Graduating Term",
            "Degree Program"))
        # Iterate through the students_data list
        for s in students_data:
            print("%-15s%-20s%-20s%-20s%-20s%-20s" % (
                s["#"], s["last_name"], s["first_name"], s["graduating_year"], s["graduating_term"],
                s["degree_program"]))

    elif ch == "2":
        # Ask user to enter a string to search for
        string = input("Enter the string: ")

        print("%-15s%-20s%-20s%-20s%-20s%-20s" % (
            "Student ID", "Last Name", "First Name", "Graduating Year", "Graduating Term",
            "Degree Program"))

        for s in students_data:

            if s["last_name"].lower().startswith(string.lower()):
                # Then display the student data
                print("%-15s%-20s%-20s%-20s%-20s%-20s" % (
                    s["#"], s["last_name"], s["first_name"], s["graduating_year"], s["graduating_term"],
                    s["degree_program"]))

    elif ch == "3":
        # Ask user to enter graduating year
        graduating_year = input("Enter the graduating year: ")

        print("%-15s%-20s%-20s%-20s%-20s%-20s" % (
            "Student ID", "Last Name", "First Name", "Graduating Year", "Graduating Term",
            "Degree Program"))

        for s in students_data:
            # If the graduating year of this student is same as the specified graduating year
            if s["graduating_year"] == graduating_year:

                print("%-15s%-20s%-20s%-20s%-20s%-20s" % (
                    s["#"], s["last_name"], s["first_name"], s["graduating_year"], s["graduating_term"],
                    s["degree_program"]))

    elif ch == "4":

        programs = [s["degree_program"] for s in students_data]
        # Counting the number of students in each program
        stu_count = {}
        for p in programs:
            stu_count[p] = stu_count.get(p, 0) + 1

        print("%-15s%-20s%-15s" % ("Program", "No. of Student", "Percentage"))
        for k, v in stu_count.items():
            print("%-15s%-20s%-15.2f" % (k, v, (v * 100) / len(students_data)))


        year = int(input("Enter the year to get number of students graduating on/after: "))

        count = 0
        for s in students_data:
            if int(s["graduating_year"]) >= year:
                count += 1

        print(f"There are {count} students graduating on/after {year}.")

    elif ch == "5":
        print("Exiting...")
        print("ThankYou !")
        break

    else:
        print("Invalid Query ")

    print()
