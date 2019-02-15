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
        