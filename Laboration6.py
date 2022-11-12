while True:
    try:
        fil = str(input("Skriv in namnet på filen: "))
        f = open(fil, "r")
        break
    except:
        print("Filen existerar tyvärr inte på denna dator, försök gärna igen.")

print("Dessa studenter är skrivna på KTH:")

while f:
    a= f.readline().strip()
    b= f.readline().strip()
    c= f.readline().strip()

    class Student:
        def __init__(self, förnamn, efternamn, personnummer):
            self.förnamn = förnamn
            self.efternamn = efternamn
            self.personnummer = personnummer
    student = Student(c, b, a)
    if a == "":
        break
    print("Namn:", student.förnamn, student.efternamn, "Personnummer:", student.personnummer)
f.close()


with open ("students.txt", "a") as g:
    d = ("\n" +input("Vad har studenten för förnamn? "))
    e = ("\n" +input("Vad har studenten för efternamn? "))
    f = ("\n" +input("Vad har studenten för personnummer (ååmmdd-xxxx)? "))
    g.write(f)
    g.write(e)
    g.write(d)
    print("Studenten är tillagd!")
g.close()

ord = input("Skriv in personnumret på studenten som ni söker efter: ")

i = open("students.txt", "r")
for line in i:
    if ord in line:
        line
        h = i.readline().strip()
        g = i.readline().strip()
        print("Studenten som du söker efter studerar på KTH:")
        print("Namn: " +g, h, "Personnummer: " +line)


#Save a object in Python
#Search for an Object in Python
#Gör om det ovanstående till object som sparas i klasser
#Add a object that you save in Python