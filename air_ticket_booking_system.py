
import pandas as pd
import os

FLIGHTS_FILE = "flights.csv"
BOOKINGS_FILE = "bookings.csv"

def initialize_flights():
    if os.path.exists(FLIGHTS_FILE):
        return pd.read_csv(FLIGHTS_FILE)
    else:
        # Sample data
        flights = pd.DataFrame({
            "Flight Number": ["F101", "F102", "F103"],
            "Destination": ["New York", "London", "Dubai"],
            "Departure Time": ["10:00 AM", "3:00 PM", "8:00 PM"],
            "Price": [500, 700, 600]
        })
        flights.to_csv(FLIGHTS_FILE, index=False)
        return flights

def initialize_bookings():
    if os.path.exists(BOOKINGS_FILE):
        return pd.read_csv(BOOKINGS_FILE)
    else:
        bookings = pd.DataFrame(columns=["Booking ID", "Customer Name", "Flight Number", "Destination", "Price"])
        bookings.to_csv(BOOKINGS_FILE, index=False)
        return bookings

def display_flights(flights):
    print("\nAvailable Flights:")
    print(flights)


def search_flights(flights, destination):
    results = flights[flights["Destination"].str.contains(destination, case=False)]
    if not results.empty:
        print("\nSearch Results:")
        print(results)
    else:
        print("No flights found for the given destination.")

def book_ticket(flights, bookings):
    display_flights(flights)
    flight_no = input("\nEnter the Flight Number to book: ")
    selected_flight = flights[flights["Flight Number"] == flight_no]
    
    if not selected_flight.empty:
        name = input("Enter your name: ")
        booking_id = len(bookings) + 1
        new_booking = pd.DataFrame([{
            "Booking ID": booking_id,
            "Customer Name": name,
            "Flight Number": flight_no,
            "Destination": selected_flight.iloc[0]["Destination"],
            "Price": selected_flight.iloc[0]["Price"]
        }])
        bookings = pd.concat([bookings, new_booking], ignore_index=True)
        bookings.to_csv(BOOKINGS_FILE, index=False)
        print(f"Booking successful! Your Booking ID is {booking_id}")
    else:
        print("Invalid Flight Number.")
    return bookings

def view_bookings(bookings):
    if bookings.empty:
        print("No bookings found.")
    else:
        print("\nYour Bookings:")
        print(bookings)

def cancel_booking(bookings):
    booking_id = int(input("Enter the Booking ID to cancel: "))
    if booking_id in bookings["Booking ID"].values:
        bookings = bookings[bookings["Booking ID"] != booking_id]
        bookings.to_csv(BOOKINGS_FILE, index=False)
        print("Booking cancelled successfully!")
    else:
        print("Invalid Booking ID.")
    return bookings

def main():
    flights = initialize_flights()
    bookings = initialize_bookings()

    while True:
        print("\nAir Ticket Booking System")
        print("1. View Flights")
        print("2. Search Flights")
        print("3. Book a Ticket")
        print("4. View Bookings")
        print("5. Cancel a Booking")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_flights(flights)
        elif choice == "2":
            destination = input("Enter destination to search: ")
            search_flights(flights, destination)
        elif choice == "3":
            bookings = book_ticket(flights, bookings)
        elif choice == "4":
            view_bookings(bookings)
        elif choice == "5":
            bookings = cancel_booking(bookings)
        elif choice == "6":
            print("Thank you for using the Air Ticket Booking System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
