class Divide:
    def __init__(self,n,mx,mn):
        self.n = n 
        self.mx = mx 
        self.mn = mn 
    

    @property
    def dividing(self):
        for i in range(self.mx,self.mn +1):
            if(self.n % i == 0):
                print(f"Apples can be divided among {i} student(s)")
                
            elif(self.n % i != 0):
                print(f"Apples cannot be divided among {i} student(s)")






n = int(input("Enter number of apples : "))

mx = int(input("Enter minimum number of students : "))
mn = int(input("Enter maximum number of students : "))


dividing_apples = Divide(n,mx,mn)

dividing_apples.dividing