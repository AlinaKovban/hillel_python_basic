def geometric_progression(first_el, progression):
    while True:
        yield first_el
        first_el *= progression
        
gp = geometric_progression(1,2)
for i in range(5):
    print(next(gp))