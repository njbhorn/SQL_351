'''
Created on 11 Dec 2018

@author: Administrator
'''
class Comment():
    '''
    classdocs
    '''
    
# Details file has the following columns: 
# id, datetime, city, state, country shape, duration (seconds), date posted

# Comments file has the following columns:
# id, comment

    def __init__(self, comment_id, comment):
        '''
        Constructor
        '''
        self.comment_id = comment_id
        self.comment = comment
        
'''
Created on 11 Dec 2018

@author: Administrator
'''

class Detail():
    '''
    classdocs
    '''
    
# Details file has the following columns: 
# id, datetime, city, state, country shape, duration (seconds), date posted

# Comments file has the following columns:
# id, comment

    def __init__(self, detail_id, datetime, city, state, country_shape, duration, date_posted):
        '''
        Constructor
        '''
        self.id = detail_id
        self.datetime = datetime
        self.city = city
        self.state = state
        self.country_shape = country_shape
        self.duration = duration
        self.date_posted = date_posted
                
                

       
       
class MergedInfo():
    '''
    classdocs
    '''
    
# Details file has the following columns: 
# id, datetime, city, state, country shape, duration (seconds), date posted

# Comments file has the following columns:
# id, comment

    def __init__(self, detail_id, datetime, city, state, country_shape, duration, date_posted, comment):
        '''
        Constructor
        '''
        self.id = detail_id
        self.datetime = datetime
        self.city = city
        self.state = state
        self.country_shape = country_shape
        self.duration = duration
        self.date_posted = date_posted
        self.comment = comment
        

# 1 open comments file
# 2 open details file
# 3 read comments into list?
# 4 read details into list
# 5 create a merged list
# 6 loop through comments
# 7 loop through details list
# 8 populate new list with relevant info
# 9 write new list to file

# 1 & 2
f_comments = open ("UFOGB_Comments.txt","r")
f_details = open ("UFOGB_Details.txt","r")

# lines_in_comments = sum ( 1 for line in f_comments )
# lines_in_details = sum ( 1 for line in f_details )
# 
# if ( lines_in_comments != lines_in_details ) :
#     print ("We have a problem Comments has " + lines_in_comments )
#     print (" lines whereas Details has " + lines_in_details)

# 3
d_comments = dict()
for l in f_comments:
    line = l.split("\t")
    key = line[0] 
    line = line [1:len(line) ]
    if ( key == "244" ):
        print(key)
        print(line)
    c = Comment ( key, line )
    d_comments.update( {key : c} )
    
    
    
d_details = dict()
for l in f_details:
    line = l.split("\t")
    key = line[0] 
#     line = line [1:len(line) ]
#     if ( key == "244" ):
#         print(key)
#         print(line)
    d = Detail(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
    d_details.update( {key : d} )
    

print('finished...')  
#print ("comments", d_comments.keys())
# print("\n")
# print ()
# print("\n\n")
print ("details", d_details.keys())
# print("\n")
print (d_details.items())
# print("\n")



# Details file has the following columns: 
# id, datetime, city, state, country shape, duration (seconds), date posted

# Comments file has the following columns:
# id, comment

