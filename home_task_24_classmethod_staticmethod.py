class Hotel:
    occupied_rooms = 0
    empty_rooms = 10
    all_rooms = 10
    guests = 0
    total_guests = 0
    
    def __init__(self, num_of_guests):
        self.num_of_guests = num_of_guests
        if num_of_guests <= Hotel.empty_rooms:
            Hotel.total_guests += num_of_guests  
            Hotel.guests += num_of_guests
            Hotel.empty_rooms = Hotel.all_rooms - Hotel.guests
            Hotel.occupied_rooms += num_of_guests
            print('You are checked in')
        elif Hotel.empty_rooms != 0:
            if Hotel.empty_rooms == 1:
                print('Only 1 room is available')
            else: 
                print(f'Only {Hotel.empty_rooms} rooms is available')
        else:
            print('There are no rooms available')
            
    def check_out(self, num_of_guests):
        if num_of_guests <= Hotel.occupied_rooms:
            Hotel.guests -= num_of_guests
            Hotel.empty_rooms += num_of_guests
            Hotel.occupied_rooms -= num_of_guests
            print(f'You are checked out')
        else:
            print('Invalid number of guests')
            
    @staticmethod
    def welcome():
        print('Welcome to our hotel')
        
    @staticmethod
    def bye(guest):
        print(f'Thank you for visiting our hotel {guest}')
            
    @classmethod
    def guests_of_all_time(cls):
        print(f'Number of guests of all time: {cls.total_guests}')
        
Hotel.welcome()
guest_1 = Hotel(1)
print('-' * 30)
Hotel.welcome()
guest_2 = Hotel(1)
print('-' * 30)
Hotel.welcome()
guest_3 = Hotel(1)
print('-' * 30)
Hotel.welcome()
group_of_guests_1 = Hotel(13)
print('-' * 30)
Hotel.bye('guest_1')
guest_1.check_out(1)
print('-' * 30)
Hotel.welcome()
guest_4 = Hotel(1)
print('-' * 30)
Hotel.welcome()
guest_5 = Hotel(1)
print('-' * 30)
Hotel.welcome()
group_of_guests_2 = Hotel(6)
print('-' * 30)
Hotel.bye('group_of_guests_2')
group_of_guests_2.check_out(6)
print('-' * 30)
Hotel.welcome()
group_of_guests_3 = Hotel(4)
print('-' * 30)

Hotel.guests_of_all_time()
print(f'Guests in hotel now: {Hotel.guests}')
print(f'Number of empty rooms: {Hotel.empty_rooms}')
print(f'Number of occupied rooms: {Hotel.occupied_rooms}')
