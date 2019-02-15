'''
Created on 18 Dec 2018

@author: QA
'''
from fileinput import close
source_file = "VehicleManufacturers.txt"
sorted_file = "VehicleManufacturers_sorted.txt"
extradata_file = "VehicleManufacturers-Extra.txt"

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

with open ( sorted_file, 'a') as f_target   :
    with open (extradata_file,'rt') as f_extradata:
        manufacturers_extra = f_extradata.readlines()
        
        print (manufacturers_extra)
        
        for manufacturer in manufacturers_extra :
            f_target.write(manufacturer)
    
        f_extradata.close()
    f_target.close()