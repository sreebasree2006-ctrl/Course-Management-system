books = []

# Load data
try:
    books = eval(open("books.txt").read())
except Exception:
    books = []

while True:
    print("\n1 Add  2 Issue  3 Return  4 View All  5 Exit")
    ch = input("Choice: ")

    if ch == "1":   # Add Book
        b = input("Book name: ")
        books.append({"book": b, "status": "Available"})
        print("Added!")

    elif ch == "2":  # Issue Book
        b = input("Book to issue: ")
        for x in books:
            if x["book"] == b and x["status"] == "Available":
                x["status"] = "Issued"
                print("Issued!")
                break
        else:
            print("Not Available!")

    elif ch == "3":  # Return Book
        b = input("Book to return: ")
        for x in books:
            if x["book"] == b and x["status"] == "Issued":
                x["status"] = "Available"
                print("Returned!")
                break
        else:
            print("Not Issued or Not Found!")

    elif ch == "4":  # View All
        for x in books:
            print(x)

    elif ch == "5":
        break

    else:
        print("Invalid option!")

# Save data
open("books.txt", "w").write(str(books))
print("Data saved. Bye!")