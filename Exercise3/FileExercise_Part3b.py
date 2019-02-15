'''
Created on 18 Dec 2018

@author: QA
'''
source_file = "VehicleManufacturers.txt"
sorted_file = "VehicleManufacturers_sorted.txt"
extradata_file = "VehicleManufacturers-Extra.txt"

with open (source_file, 'rt') as f_source:
    manufacturers = f_source.readlines()
    
#     print (manufacturers)
    
    manufacturers.sort()
    
#     print (manufacturers)
    
    f_source.close()

with open (sorted_file,'wt') as f_target:

    for manufacturer in manufacturers :
        f_target.write(manufacturer)
    
    f_target.close()
    

with open ( sorted_file, 'wt') as f_target   :
#     manufacturers.clear()
#     manufacturers2 = f_target2.readlines()
    with open (extradata_file,'rt') as f_extradata:
        manufacturers_extra = f_extradata.readlines()
        
        print (manufacturers)
        print (manufacturers_extra)
        
        manufacturers.extend(manufacturers_extra)
        
        print (manufacturers)
        
        manufacturers.sort()
        
        print (manufacturers)
        
        for manufacturer in manufacturers :
            f_target.write(manufacturer)
    
        f_extradata.close()
    f_target.close()