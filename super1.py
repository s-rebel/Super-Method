"""How to call different methods( Constructor, Instance Method, Class Method & Static 
Method) of parent class or any super class in child's 'Constructor' by using super() method"""
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
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        print('#'*30)
    def c1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()  
        print('#'*30)
c=C()
c.c1()
