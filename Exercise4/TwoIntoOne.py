'''
Created on 18 Dec 2018

@author: QA
'''
source_makemodel = "Vehicles_MakeModel.csv"
source_desc = "Vehicles_Descriptions.csv"
target_info = "Vehicle_Info_Merged.csv"

with open ( source_makemodel, 'rt') as f_src_makemodel :
    list_makemodel = f_src_makemodel.readlines()
    list_makemodel.sort()
    list_makemodel.reverse()
    f_src_makemodel.close()
    
with open ( source_desc, 'rt') as f_src_desc :
    list_desc = f_src_desc.readlines()
    list_desc.sort()
    list_desc.reverse()
    f_src_desc.close()    

print (list_makemodel)
print ( list_desc)
with open ( target_info, 'wt') as f_target :
    for i in range(len(list_makemodel)):
#         f_target.write ( list_makemodel[i] + list_desc[i])
#         temp = list_desc[i][list_desc[i].find(',') + 1 : ]
        temp = list_desc[i]
        pos = temp.find(',')
        pos = pos + 1
        temp = temp [ pos : ] 
        f_target.write('{},{}'.format(list_makemodel[i].strip("\n"), temp))
    f_target.close()
        
