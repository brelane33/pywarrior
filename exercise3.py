
def get_run_time():
    '''Asks user for repeatedly for input.
       Prints average time of runs'''
    
    number_of_events = 0
    total_time = 0

    while True:
        run_input = input('Enter 10km run time: ')

        if not run_input:
            break

        number_of_events += 1
        total_time += float(run_input)

    average_time = total_time / number_of_events

    print(f'Average of {average_time}, over {number_of_events} runs')

get_run_time()
