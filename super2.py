"""How to call different methods( Constructor, Instance Method, Class Method & Static 
Method) of parent class or any super class in child's 'Class Method' by using super() method"""

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
    @classmethod
    def c2(cls): 
        # super(C,cls).__init__(cls)
        super(C,C).__init__(cls)
        # super(C,cls).m1(cls)
        super(C,C).m1(cls)
        super().m2()
        super().m3()
C.c2()
