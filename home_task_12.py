from datetime import datetime

def dec_tracking_time(func):
    def wrapping(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        print(end_time - start_time)
    return wrapping


@dec_tracking_time   
def numbers_multiplication (num_1, num_2):
    print(num_1 * num_2)

   
@dec_tracking_time  
def numbers_sum (num_3, num_4):
    print (num_3 + num_4)
    

numbers_multiplication(1, 1)
numbers_sum(5, 5)

