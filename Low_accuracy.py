from numpy import*
from scipy import*

print ("We are going to calculate the dates of the solstices and equinoxes of years from around -1000 (or some centuries before) to +1000, in Gregorian years.")
print ("In wich year do you want to start (included)? (Gregorian)")
prompt = '> '
start_year = int(input(prompt))
print ("In which year do you want to end (included)? (Gregorian)")
end_year = int(input(prompt))
print ("\n")
A = [485, 203, 199, 182, 156, 136, 77, 74, 70, 58, 52, 50, 45, 44, 29, 18, 17, 16, 14, 12, 12, 12, 9, 8]
B = [324.96, 337.23, 342.08, 27.85, 73.14, 171.52, 222.54, 296.72, 243.58, 119.81, 297.17, 21.02, 247.54, 325.15, 60.93, 155.12, 288.79, 198.04, 199.76, 95.39, 287.11, 320.81, 227.73, 15.45]
C = [1934.136, 32964.467, 20.186, 445267.112, 45036.886, 22518.443, 65928.934, 3034.906, 9037.513, 33718.147, 150.678, 2281.226, 29929.562, 31555.956, 4443.417, 67555.328, 4562.452, 62894.029, 31436.921, 14577.848, 31931.756, 34777.259, 1222.114, 16859.074]

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


#Converteix Julian years a Gregorian years. Cal passar com a argument el Julian year. Val per QUALSEVOL any
def Conversor(J):
    J2 = J + 0.5
    Z = int(J2) #part entera de J2
    F = J2 - int(J2)  #part decimal de J2
    
    if Z < 2299161:
        A = Z
    elif Z >= 2299161:
        alpha = int((Z-1867216.25)/36524.25)
        A = Z + 1 + alpha - int(alpha/4)
    else:
        print ("There has been an error in the conversion")
    
    B = A + 1524
    C = int((B-122.1)/365.25)
    D = int(365.25*C)
    E = int((B-D)/30.6001)
    
    #day of the month amb decimals
    day = B - D - int(30.6001*E) + F
    #month (number)    
    if E < 14:
        month = E - 1
    elif E == 14 or E == 15:
        month = E - 13
    else:
        print ("Something is wrong in the calculation of the month")
    #month (name)
    Name_month = month_list[month - 1]  #li posc el -1 pq les llistes conten a partir de 0 i els mesos es compten des de 1
    #year
    if month > 2:
        year = C - 4716
    elif month == 1 or month == 2:
        year = C - 4715
    else:
        print ("Something is wrong in the calculation of the year")
    #Hora, minuts i segons
    day_decimal = day - int(day)
    hour = int(day_decimal*24)
    hour_decimal = day_decimal*24 - int(day_decimal*24)
    minuts = int(hour_decimal*60)
    minuts_decimal = hour_decimal*60 - int(hour_decimal*60)
    seconds = minuts_decimal*60
    
    #Summary of the date
    date = "Year " + str(year) + ", " + str(Name_month) + ", day " + str(int(day)) + ", " + str(hour) + " hours, " + str(minuts) + " minuts and " + str(seconds) + " seconds."
    
    return date


#Aquesta funcio calcula els JDE0_i per a els 4 casos (marc, juny, setembre, decembre). Cal passar-li com a parametre l'any de que ho volem calcular
def JDE0(year):
    Y = float(year)/1000     #"year " is in Gregorian and "Y" is in Julian

    JDE0_m = 1721139.29189 + Y*(365242.13740 + Y*(0.06134 + Y*(0.00111 + -0.00071*Y)))
    JDE0_j = 1721233.25401 + Y*(365241.72562 + Y*(-0.05323 + Y*(0.00907 + 0.00025*Y)))
    JDE0_s = 1721325.70455 + Y*(365242.49558 + Y*(-0.11677 + Y*(-0.00297 + 0.00074*Y)))
    JDE0_d = 1721414.39987 + Y*(365242.88257 + Y*(-0.00769 + Y*(-0.00933 - 0.00006*Y)))
    print ("Year " + str(year))
    
    return JDE0_m, JDE0_j, JDE0_s, JDE0_d


#Aquesta funcio calcula la suma S amb totes les A, B, C. Cal passar-li com a parametre un valor de T
def S1(a):
    Sj = 0
    for j in range(0, 24):
        Sj = Sj + A[j]*cos(B[j]*(pi/180) + C[j]*(pi/180)*a)
        #Hey! Com Python calcula el cosinus en radians i jo tenc els angles en graus, faig el canvi
    return Sj

    


for year in range(start_year, end_year + 1):
    JDE0_m, JDE0_j, JDE0_s, JDE0_d = JDE0(year)
    JDE0list = [JDE0_m, JDE0_j, JDE0_s, JDE0_d]

    T = []
    W = []
    lambd = []
    S = []
    JDE = []
    Greg = []
    for i in range(0,4):
        T.append(float((JDE0list[i] - 2451545.0)/36525))
        W.append(float(35999.373*T[i]-2.47))
        lambd.append(float(1 + 0.0334*cos(W[i]*(pi/180)) + 0.0007*cos(2*W[i]*(pi/180))))
        S.append(float(S1(T[i])))
        JDE.append(float(JDE0list[i] + (0.00001*S[i])/lambd[i]))
        #Ara que ja tenim la data en Julian years, la passem a Gregorian years
        Greg.append(Conversor(JDE[i]))
    
    print ("\nInstant of the solstices and equinoxes (March eq, June sols, September eq, December sols respectively):")
    for i in range(0,4):
        print ("In Julian years: " + str(JDE[i]) + ", which is " + str(Greg[i]))
    print ("\n\n")


