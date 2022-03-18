# First Name: Alex
# Last Name: Chhieng-Henson
# Student ID: 003382010


from libraries.cli import return_time_info
from libraries.delivery_simulator import delivery_simulator

time_limit = return_time_info()

if time_limit is None:
    print('Exited program!')
    quit()

delivery_simulator(time_limit)

