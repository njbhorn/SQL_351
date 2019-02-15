'''
Created on 18 Dec 2018

@author: QA
'''
source_file = "VehicleManufacturers.txt"
sorted_file = "VehicleManufacturers_sorted.txt"

f_source = open (source_file, 'rt')
manufacturers = f_source.readlines()

print (manufacturers)

manufacturers.sort()

print (manufacturers)

f_source.close()

f_target = open (sorted_file,'wt')

for manufacturer in manufacturers :
    f_target.write(manufacturer)

f_target.close()