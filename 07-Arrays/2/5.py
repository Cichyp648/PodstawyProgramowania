# Cinema Seating Information Program
# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

# Calculate total seats
def seats_total(seats):
    return sum(len(row) for row in seats)

# Calculate available seats
def seats_available(seats):
    return sum(row.count('A') for row in seats)

# Calculate booked seats
def seats_booked(seats):
    return sum(row.count('B') for row in seats)

# Get status of a specific seat
def seat_status(seats, row, place):
    if seats[row - 1][place - 1] == 'A':
        return "Available"
    else:
        return "Booked"

# Output cinema seating information
print("CINEMA INFORMATION TABLE")
print("Total seats:", seats_total(cinema_seats))
print("Seats available:", seats_available(cinema_seats))
print("Seats booked:", seats_booked(cinema_seats))
print("Seat in row 1, place 1:", seat_status(cinema_seats, 1, 1))
print("Seat in row 5, place 5:", seat_status(cinema_seats, 5, 5))
print("Seat in row 3, place 5:", seat_status(cinema_seats, 3, 5))
