# string1= "{'a': {'@href': 'https://waterdata.usgs.gov/nwis/inventory/?site_no=03107500', '#text': 'USGS ID: 03107500'}, '#text': 'U."
# print("site_no" in string1)

# from datetime import datetime
 
# # returns current date and time
# now = datetime.now()
# print("now = ", now)

# update = {}
# print(type(update))
# update.update({'test1': 'test1'})
# update.update({'test2': 'test2'})
# update.update({'test3': 'test3'})
# update.update({'test4': 'test4'})
# update.update({'test5': 'test5'})

# print(update)

# x :float = 12.5
# print(x + .0)


def compareFloatNum(a, b):
    return (abs(a - b) < 1e-9)


print(compareFloatNum(12.0,12))    

print(compareFloatNum(12.5,12.00000000001))    

print(compareFloatNum(12.5,12.50000000001))  