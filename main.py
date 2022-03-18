# First Name: Alex
# Last Name: Chhieng-Henson
# Student ID: 003382010

from libraries.cli import return_time_info
from libraries.delivery_simulator import delivery_simulator

# Retrieves time info from user to display package information
time_limit = return_time_info()

# If 'X' is entered by user, program will exit
if time_limit is None:
    print('Exited program!')
    quit()

# Runs a simulation of the deliveries based on user input's time constraints
delivery_simulator(time_limit)
