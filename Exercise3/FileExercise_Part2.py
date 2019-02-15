'''
Created on 18 Dec 2018

@author: QA
'''
from fileinput import close
source_file = "VehicleManufacturers.txt"
sorted_file = "VehicleManufacturers_sorted.txt"

with open (source_file, 'rt') as f_source:
    manufacturers = f_source.readlines()
    
    print (manufacturers)
    
    manufacturers.sort()
    
    print (manufacturers)
    
    f_source.close()

with open (sorted_file,'wt') as f_target:

    for manufacturer in manufacturers :
        f_target.write(manufacturer)
    
    f_target.close()