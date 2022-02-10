"""How to call methods( Only Class Method & Static Method) of parent class 
or any super class in child's 'Static Method' by using super() method"""

class P:
    def __init__(self):
        print("Calling Parent Constructor")
    def m1(self):
        print("Calling Parent Instance Method")
    @classmethod
    def m2(cls):
        print("Calling Parent Class Method")
    @staticmethod
    def m3():
        print("Calling Parent Static Method")
class C(P):
    @staticmethod
    def c3():
        # super(C,cls).__init__(cls)
        # super(C,cls).m1(cls)
        super(C,C).m2()
        super(C,C).m3()        
C.c3()