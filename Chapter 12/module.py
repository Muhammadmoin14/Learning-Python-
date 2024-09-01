def myFunc():
    print("Hello World")

print(__name__)

if(__name__ == "module"):
    myFunc()
    print(__name__)         #? It will print running file name