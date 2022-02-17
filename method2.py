"""How to call different methods( Constructor, Instance Method, Class Method & Static 
Method) of parent class or any super class in child's 'Class Method' by using Class Name"""
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
        P.__init__(cls)
        P.m1(cls)
        P.m2()
        P.m3()
        print('#'*30)
C.c2()