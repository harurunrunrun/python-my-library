from sys import stdin
pin    =lambda:stdin.readline().rstrip()     #input()
pins   =lambda:pin().split()                 #input().split()
pint   =lambda:int(pin())                    #int(input())
pints  =lambda:map(int,pins())               #map(int,input().split())
pinsl  =lambda:list(pins())                  #list(input().split())
pintsl =lambda:list(pints())                 #list(map(int,input().split()))
gcd    =lambda x,y:gcd(y,x%y)if y else x     #math.gcd
lcm    =lambda x,y:x*y//gcd(x,y)             #math.lcm
fact   =lambda n:n*fact(n-1)if n else 1      #math.factorial
factmod=lambda n,m:n*fact(n-1)%m if n else 1 #factrial_mod

