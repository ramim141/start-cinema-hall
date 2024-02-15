class Star_Cinema:
    _hall_list = []

    def __init__(self) -> None:
        pass

    def entry_hall(self, hall):
        Star_Cinema._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)
        super().__init__()

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[id] = [
            [0 for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, show_id, seat_list):
        seats = self.__seats.get(show_id)
        if not seats:
            print("\nEntered Invalid Show ID!\n")
            return
        
        for row, col in seat_list:
            if not (1 <= row <= len(seats)) or not (1 <= col <= len(seats[0])):
                print("\nInvalid Seat\n")
                continue
            
            if seats[row - 1][col - 1] == 1:
                print("\nThis Seat is already booked\n")
                continue
            
            seats[row - 1][col - 1] = 1
            print("\nSuccessfully Ticket Booked\n")
            return


    def view_show_list(self):
        if len(self.__show_list) == 0:
            print("\nCurrently No Show Is Running\n")
            return
        for show in self.__show_list:
            print(f"\nShow ID:{show[0]}\tMovie:{show[1]}\tTime:{show[2]}")
        print("\n")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("\nEntered Invalid Show ID!\n")
            return
        seatinfo = self.__seats[show_id]
        for i in seatinfo:
            for j in i:
                print(j, end="\t")
            print("\n")


star = Star_Cinema()
star_hall = Hall(3, 5, "star")
star_hall.entry_show("1001", "Deadpool-3", "Feb 20 2022 4:00 PM")
star_hall.entry_show("1002", "Toxic", "March 02 2022 8:00 PM")
star_hall.entry_show("1002", "Devara: Part-1", "June 22 2024 12:00 PM")


while True:
    print("1. View All Show")
    print("2. View Available Seat")
    print("3. Book Tickets")
    print("4. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        star_hall.view_show_list()
    elif ch == 2:
        show_id = input("Enter Show ID: ")
        star_hall.view_available_seats(show_id)
    elif ch == 3:
        show_id = input("Enter Show ID: ")
        num_of_seats = int(input("Enter Number of Tickets:"))
        seats_to_book = []
        for _ in range(num_of_seats):
            row = int(input("Enter Row:"))
            col = int(input("Enter Column:"))
            star_hall.book_seats(show_id, [(row, col)])
    elif ch == 4:
        break
