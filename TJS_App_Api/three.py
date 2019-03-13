from io import open


# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print '%s:%s' %(self.name,self.score)
#
#
#
# cats = Student('cat',59)
# cats.print_score()

class open(object):
    try:
        fp = open('null.txt','r')
    except Exception,e:
        print e
        print type(e)
        raise
    finally:
        print 'end'