def main():
    name = input ("what is your name? ").strip().title()  
    hello( name ) 


def hello(to= "world" ):
    print("hello", to )

def ret():
    x = int(input("what is x? "))
    print( "x square is", square(x))

def square(n):
    return pow(n,2)


def cube(n):
  return  n*n*n

print(cube(round(float(input()))))

