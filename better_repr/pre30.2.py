print("1. About to create 'betterrepr' function")

def betterrepr(c):
    def say_hello(self):
        return "Hello!"

    c.__repr__ = say_hello

    print("2. Class being created...")
    def wrapper():
        print("3. Class is being invoked -- we have a new instance")
        return c()
    return wrapper


print("4. About to create class")

@betterrepr
class Foo(object):
    pass

print("5. About to create instance")

f = Foo()
print(f)

