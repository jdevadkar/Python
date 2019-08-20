from Dictionary import dict
import logging 

# This Method Showed All Employee in dictionary.
def show_all_employee():
    logging.info("Showed all Employee in Dictionary")
    for e in dict.keys():
        print(e ,'->',format(dict[e]))