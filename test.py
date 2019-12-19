class MyClass:
    """A simple example class"""
    k = 12345;
    def __init__(self, real, imag):
        self.r = real
        self.i = imag
    def f(self):
        return 'hello world'

x = MyClass(3, -4)
m = x.f()

print(m)
print(MyClass.__doc__)
print(x.r)

y = MyClass(2, 70)
y.k = 10

print(y.k)
print(x.k)
