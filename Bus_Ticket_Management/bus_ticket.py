class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ['empty' for i in range(20)]

# bus = Bus(13, 'kala chan', '10.10AM', '12.30PM', 'Dhaka', 'Delhi')
# print(vars(bus))

class Hanif:
    total_bus = 5
    total_bus_lst = []

    def add_bus(self):
        bus_no = int(input('enter bus No: '))

        flag = 1
        for w in self.total_bus_lst:
            if bus_no == w['coach']:
                print('Bus already added')
                flag = 0
                break
        if flag:
            bus_driver = input('enter bus driver name: ')
            bus_arrival = input('enter bus arrival time: ')
            bus_departure = input('enter bus departure time: ')
            bus_from = input('enter bus start from: ')
            bus_to = input('enter bus destination: ')
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_departure, bus_from, bus_to)
            self.total_bus_lst.append(vars(self.new_bus))
            print('\n Bus added Successfully')

# company = Hanif()
# company.add_bus()

class Counter(Hanif):
    user_list = []
    def seat_reserve(self):
        bus_no = int(input('Enter Bus No: '))
        for w in self.total_bus_lst:
            if bus_no == w['coach']:
                passanger = input('Enter your name: ')
                seat_no = int(input('Enter Seat No: '))

                if seat_no > 20:
                    print('Seat not available')
                elif w['seat'][seat_no-1] != 'empty':
                    print('Seat is already booked')
                else:
                    w['seat'][seat_no-1] = passanger
            else:
                print('Bus not available')

        # for bus in self.total_bus_lst:
        #     print(bus['seat'])
    def show_ticket(self):
        bus_no = int(input('Enter Bus no: '))

        for w in self.total_bus_lst:
            if bus_no == w['coach']:
                print('*' * 50)
                print()
                print(f"{' '*10} {'#'*10} Bus Info {'#'*10}")
                print(f"Bus no: {bus_no} \t\t\t Driver: {w['driver']}")
                print(f"Depart: {w['departure']} \t\t\t Arrival: {w['arrival']}\nFrom: {w['from_des']} \t\t\t To: \t{w['to']}")
                print()

                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{chr(a + 64)}. {w['seat'][a-1]}", end = "  ")
                        a += 1
                    print(end = "\t ")
                    for j in range(2):                
                        print(f"{chr(a + 64)}. {w['seat'][a-1]}", end = "  ")
                        a += 1
                    print('\n')
                print('*' * 50)

    def get_user(self):
        return self.user_list

    def create_account(self):
        name = input('Enter your username: ')
        password = input('Password: ')
        self.new_user = User(name, password)
        self.user_list.append(vars(self.new_user))

    def available_bus(self):
        if len(self.total_bus_lst) == 0:
            print("Bus not available")
        else:
            print('*'*50)
            for bus in self.total_bus_lst:
                print()
                print(f"{' '*10}{'#'*10} BUS {bus['coach']} INFO {' '*10}")
                print(f"Bus Number: {bus['coach']} \t Driver: {bus['driver']}")
                print(f"Depart: {bus['departure']} \t Arrival: {bus['arrival']}")
                print(f"From: \t{bus['from_des']} \t To: \t{bus['to']}")
                print('*'*50)


## ------Global Section------
while True:
    company = Hanif()
    c = Counter()
    print("1. Create an account\n2. login to your account\n3. Exit")

    user_input = int(input('Enter your Choice: '))
    if user_input == 3:
        break
    elif user_input == 1:
        c.create_account()
    elif user_input == 2:
        name = input('Enter your username: ')
        password = input('Password: ')

        flag = 0
        isAdmin = False

        if name == 'admin' and password == '123':
            isAdmin = True
        if isAdmin == False:
            for user in c.get_user():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"\n{'*10'}Welcome to bus ticket booking system")
                    print("1. Available Buses\n2. Show Bus Info\n3. Reservation\n4. Exit")
                    a = int(input('Enter your choice: '))
                    if a == 4:
                        break
                    elif a == 1:
                        c.available_bus()
                    elif a == 2:
                        c.show_ticket()
                    elif a == 3:
                        c.seat_reserve()
            else:
                print('NO Username Found')
        else: 
            while True:
                print(f"\n{''*10} Hello Admin..!  Welcome to bus ticket booking system")
                print("1. Add bus\n2. Available Buses\n3. Show bus Info\n4. Exit")
                a = int(input('Enter your choice: '))
                if a == 4:
                    break
                elif a == 1:
                    c.add_bus()
                elif a == 2:
                    c.available_bus()
                elif a == 3:
                    c.show_ticket()
                
            


# company = Hanif()
# company.add_bus()

# c = Counter()
# c.seat_reserve()
# c.show_ticket()