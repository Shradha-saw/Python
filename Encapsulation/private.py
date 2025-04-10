'''
Private var must be allowed inside the same class.
'''

class Demo1:
    def __init__(self):
        self.__name = 'SK' #private variable

    def disp1(self):
        print(self.__name)

d1 = Demo1()
#print(d1.__name) #Error

'''
Public: Whe we want to access variables anyehere in the code.
protected:When we want to access variables inside the same class and inside child class.
private: When we wan to access variables inside the same class.

public: a = 1-
protected: _a = 10
private: __a = 10
'''