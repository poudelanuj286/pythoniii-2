def greetings():
    dash = '-' * 40

    print(dash)
    print('\t''\t''Welcome to Kenjal IT Academy ')
    print(dash)

    name = input('What is your name ? ')

    while len(name) == 0 or name.isspace():
        name = input('Please provide your name : ')

    print('Hello', name, 'hope you are doing well ')
    print(name, 'you can choose any course to study from the following menu : ')

    return name


# Open Text file , Read and Print all it's contents , returns lines ( lines = contents )
def show_menu():
    file_ref = open(courses.txt, 'r')
    lines = file_ref.readlines()

    for line in lines:
        print(line, end='')  # it will print all it's contents one by one

    file_ref.close()
    return lines
def registration():
    print("Student registration fee is Rs.20000. /n You can pay in double installment of Rs.10000 each?")
    choice = print("Do you want to pay your first installment now? y/n")
    if choice == 'y':
        payment = 10000
        return payment
    if choice == 'n':
        print("you can visit us again ")


def student_info(student_name, payment, total_balance):
    dash = '-' * 49
    dash_for_txt_file = '-' * 52

    file_ref = open(student.txt, 'w')
    file_ref.write(dash_for_txt_file + '\n')
    file_ref.write(' ''S.no''\t''Name''\t''\t''\t''  ''remaining payment'\t''  ''Total balance'')
    file_ref.write(dash_for_txt_file + '\n')
    sn = 1
    file_ref.write('{:^8d}{:<17s}{:>6.1f}{:>14.2f}'.format(sn, student_name, payment,
                                                    total_balance))

    print(dash)


    #file_ref.write(dash_for_txt_file + '\n')
    file_ref.close()



def display_info(student_name, payment, total_balance):
    dash = '-' * 49
    print(dash)
    print(' ''S.no''\t''Name''\t''\t''\t''  ''remaining payment'\t''  ''Total balance')
    print(dash)
    for i in range(0, len(student_name)):
        print(
            '{:^8d}{:<17s}{:>6.1f}{:>14.2f}'.format(sn, student_name, payment,
                                                    total_balance))
    print(dash)

def update_info(student_name, payment, total_balance):


    file_ref = open(student.x, 'w')
    file_ref.write(dash_for_txt_file + '\n')
    file_ref.write(' ''S.no''\t''Name''\t''\t''\t''  ''remaining payment'\t''  ''Total balance')
    file_ref.write(dash_for_txt_file + '\n')

    file_ref.write('{:^8d}{:<17s}{:>6.1f}{:>14.2f}'.format(sn, student_name, payment,
                                                    total_balance))

    print(dash)

    file_ref.write('Total Amount = {:>33.2f}'.format(total_amount) + '\n')
    file_ref.write(dash_for_txt_file + '\n')
    file_ref.close()


