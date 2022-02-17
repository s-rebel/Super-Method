"""How to call different methods( Only Class Method & Static Method) 
of parent class or any super class in child's 'Static Method' by using Class Name"""
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
    def c2():
        # P.__init__()
        # P.m1()
        P.m2()
        P.m3()
        print('#'*30)
C.c2()