from numpy import*
from scipy import*
import pylab
import numpy
import matplotlib

L_A_0 = [175347046, 3341656, 34894, 3497, 3418, 3136, 2676, 2343, 1324, 1237, 1199, 990, 902, 857, 780, 753, 505, 492, 357, 317, 284, 271, 243, 206, 205, 202, 156, 132, 126, 115, 103, 102, 102, 99, 98, 86, 85, 85, 80, 79, 75, 74, 74, 70, 62, 61, 57, 56, 56, 52, 52, 51, 49, 41, 41, 39, 37, 37, 36, 36, 33, 30, 30, 25]
L_B_0 = [0, 4.6692568, 4.62610, 2.7441, 2.8289, 3.6277, 4.4181, 6.1352, 0.7425, 2.0371, 1.1096, 5.233, 2.045, 3.508, 1.179, 2.533, 4.583, 4.205, 2.920, 5.849, 1.899, 0.315, 0.345, 4.806, 1.869, 2.458, 0.833, 3.411, 1.083, 0.645, 0.636, 0.976, 4.267, 6.21, 0.68, 5.98, 1.30, 3.67, 1.81, 3.04, 1.76, 3.50, 4.68, 0.83, 3.98, 1.82, 2.78, 4.39, 3.47, 0.19, 1.33, 0.28, 0.49, 5.37, 2.40, 6.17, 6.04, 2.57, 1.71, 1.78, 0.59, 0.44, 2.74, 3.16]
L_C_0 = [0, 6283.0758500, 12566.15170, 5753.3849, 3.5231, 77713.7715, 7860.4194, 3930.2097, 11506.7698, 529.6910, 1577.3435, 5884.927, 26.298, 398.149, 5223.694, 5507.553, 18849.228, 775.523, 0.067, 11790.629, 796.298, 10977.079, 5486.778, 2544.314, 5573.143, 6069.777, 213.299, 2942.463, 20.775, 0.980, 4694.003, 15720.839, 7.114, 2146.17, 155.42, 161000.69, 6275.96, 71430.70, 17260.15, 12036.46, 5088.63, 3154.69, 801.82, 9437.76, 8827.39, 7084.90, 6286.60, 14143.50, 6279.55, 12139.55, 1748.02, 5856.48, 1194.45, 8429.24, 19651.05, 10447.39, 10213.29, 1059.38, 2352.87, 6812.77, 17789.85, 83996.85, 1349.87, 4690.48]
L_A_1 = [628331966747, 206059, 4303, 425, 119, 109, 93, 72, 68, 67, 59, 56, 45, 36, 29, 21, 19, 19, 17, 16, 16, 15, 12, 12, 12, 12, 11, 10, 10, 9, 9, 8, 6, 6]
L_B_1 = [0, 2.678235, 2.6351, 1.590, 5.796, 2.966, 2.59, 1.14, 1.87, 4.41, 2.89, 2.17, 0.40, 0.47, 2.65, 5.34, 1.85, 4.97, 2.99, 0.03, 1.43, 1.21, 2.83, 3.26, 5.27, 2.08, 0.77, 1.30, 4.24, 2.70, 5.64, 5.30, 2.65, 4.67]
L_C_1 = [0, 6283.075850, 12566.1517, 3.523, 26.298, 1577.344, 18849.23, 529.69, 398.15, 5507.55, 5223.69, 155.42, 796.30, 775.52, 7.11, 0.98, 5486.78, 213.30, 6275.96, 2544.31, 2146.17, 10977.08, 1748.02, 5088.63, 1194.45, 4694.00, 553.57, 6286.60, 1349.87, 242.73, 951.72, 2352.87, 9437.76, 4690.48]
L_A_2 = [52919, 8720, 309, 27, 16, 16, 10, 9, 7, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2]
L_B_2 = [0, 1.0721, 0.867, 0.05, 5.19, 3.68, 0.76, 2.06, 0.83, 4.66, 1.03, 3.44, 5.14, 6.05, 1.19, 6.12, 0.31, 2.28, 4.38, 3.75]
L_C_2 = [0, 6283.0758, 12566.152, 3.52, 26.30, 155.42, 18849.23, 77713.77, 775.52, 1577.34, 7.11, 5573.14, 796.30, 5507.55, 242.73, 529.69, 398.15, 553.57, 5223.69, 0.98] 
L_A_3 = [289, 35, 17, 3, 1, 1, 1]
L_B_3 = [5.844, 0, 5.49, 5.20, 4.72, 5.30, 5.97]
L_C_3 = [6283.076, 0, 12566.15, 155.42, 3.52, 18849.23, 242.73]
L_A_4 = [114, 8, 1]
L_B_4 = [3.142, 4.13, 3.84]
L_C_4 = [0, 6283.08, 12566.15]
L_A_5 = [1]
L_B_5 = [3.14]
L_C_5 = [0]
#......................................................................................
#Error a algun numero de la L
#......................................................................................
B_A_0 = [280, 102, 80, 44, 32]
B_B_0 = [3.199, 5.422, 3.88, 3.70, 4.00]
B_C_0 = [84334.662, 5507.553, 5223.69, 2352.87, 1577.34]
B_A_1 = [9, 6]
B_B_1 = [3.90, 1.73]
B_C_1 = [5507.55, 5223.69]
R_A_0 = [100013989, 1670700, 13956, 3084, 1628, 1576, 925, 542, 472, 346, 329, 307, 243, 212, 186, 175, 110, 98, 86, 86, 65, 63, 57, 56, 49, 47, 45, 43, 39, 38, 37, 37, 36, 35, 33, 32, 32, 28, 28, 26]
R_B_0 = [0, 3.0984635, 3.05525, 5.1985, 1.1739, 2.8469, 5.453, 4.564, 3.661, 0.964, 5.900, 0.299, 4.273, 5.847, 5.022, 3.012, 5.055, 0.89, 5.69, 1.27, 0.27, 0.92, 2.01, 5.24, 3.25, 2.58, 5.54, 6.01, 5.36, 2.39, 0.83, 4.90, 1.67, 1.84, 0.24, 0.18, 1.78, 1.21, 1.90, 4.59]
R_C_0 = [0, 6283.0758500, 12566.15170, 77713.7715, 5753.3849, 7860.4194, 11506.770, 3930.210, 5884.927, 5507.553, 5223.694, 5573.143, 11790.629, 1577.344, 10977.079, 18849.228, 5486.778, 6069.78, 15720.84, 161000.69, 17260.15, 529.69, 83996.85, 71430.70, 2544.31, 775.52, 9437.76, 6275.96, 4694.00, 8827.39, 19651.05, 12139.55, 12036.46, 2942.46, 7084.90, 5088.63, 398.15, 6286.60, 6279.35, 10447.39]
R_A_1 = [103019, 1721, 702, 32, 31, 25, 18, 10, 9, 9]
R_B_1 = [1.107490, 1.0644, 3.142, 1.02, 2.84, 1.32, 1.42, 5.91, 1.42, 0.27]
R_C_1 = [6283.075850, 12566.1517, 0, 18849.23, 5507.55, 5223.69, 1577.34, 10977.08, 6275.96, 5486.78]
R_A_2 = [4359, 124, 12, 9, 6, 3]
R_B_2 = [5.7846, 5.579, 3.14, 3.63, 1.87, 5.47]
R_C_2 = [6283.0758, 12566.152, 0, 77713.77, 5573.14, 18849.23]
R_A_3 = [145, 7]
R_B_3 = [4.273, 3.92]
R_C_3 = [6283.076, 12566.15]
R_A_4 = [4]
R_B_4 = [2.56]
R_C_4 = [6283.08]

A = [118.568, 2.476, 1.376, 0.119, 0.114, 0.086, 0.078, 0.054, 0.052, 0.034, 0.033, 0.023, 0.023, 0.021, 7.311, 0.305, 0.010, 0.309, 0.021, 0.004, 0.010]
B = [87.5287, 85.0651, 27.8502, 73.1375, 337.2264, 222.5400, 162.8136, 82.5823, 171.5189, 30.3214, 119.8105, 247.5418, 325.1526, 155,1241, 333.4515, 330.9814, 328.5170, 241.4518, 205.0482, 297.8610, 154.7066]
C = [359993.7286, 719987.4571, 4452671.1152, 450368.8564, 329644.6718, 659289.3436, 9224659.7915, 1079981.1857, 225184.4282, 4092677.3866, 337181.4711, 299295.6151, 315559.5560, 675553.2846, 359993.7286, 719987.4571, 1079981.1857, 359993.7286, 719987.4571, 4452671.1152, 359993.7286]

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
    date = str(Name_month) + ", day " + str(int(day)) + " at " + str(hour) + "h " + str(minuts) + "min " + str(seconds) + "s"
    
    return date


#Aquesta funcio calcula els JDE0_i per a els 4 casos (marc, juny, setembre, decembre). Cal passar-li com a parametre l'any de que ho volem calcular
def JDE0(year):
    if -1000 <= year and year < +1000:
        Y = float(year)/1000     #"year " is in Gregorian and "Y" is in Julian
        JDE0_m = 1721139.29189 + Y*(365242.13740 + Y*(0.06134 + Y*(0.00111 + -0.00071*Y)))
        JDE0_j = 1721233.25401 + Y*(365241.72562 + Y*(-0.05323 + Y*(0.00907 + 0.00025*Y)))
        JDE0_s = 1721325.70455 + Y*(365242.49558 + Y*(-0.11677 + Y*(-0.00297 + 0.00074*Y)))
        JDE0_d = 1721414.39987 + Y*(365242.88257 + Y*(-0.00769 + Y*(-0.00933 - 0.00006*Y)))
    elif 1000 <= year and year < 3000:
        Y = (float(year)-2000)/1000     #"year " is in Gregorian and "Y" is in Julian
        JDE0_m = 2451623.80984 + Y*(365242.37404 + Y*(0.05169 - Y*(0.00411 + 0.00057*Y)))
        JDE0_j = 2451716.56767 + Y*(365241.62603 + Y*(0.00325 + Y*(0.00888 - 0.00030*Y)))
        JDE0_s = 2451810.21715 + Y*(365242.01767 + Y*(-0.11575 + Y*(0.00337 + 0.00078*Y)))
        JDE0_d = 2451900.05952 + Y*(365242.74049 + Y*(-0.06223 + Y*(-0.00823 + 0.00032*Y)))
    else:
        print ("Your year is out of range")
        
    print ("Year " + str(year))
    
    return JDE0_m, JDE0_j, JDE0_s, JDE0_d
    
    
#Calcula operacio amb cada element de les llistes a, b, c. n es el num d'elements de la llista. Cal passar-li tambe una tau
def G(tau, a, b, c, n):
    Gj = 0
    for j in range(0, n): 
        Gj = Gj + (a[j])*cos(b[j] + c[j]*tau)
        #print ("G[" + str(j) + "]" + str(Gj))
        
    return Gj
    
#Calcula increment de lambda, on a, b, c son llistes de nombres  21
def increment(tau, a, b, c):
    inc = 3548.193
    for i in range(0, 14):
        inc = inc + a[i]*sin(b[i] + c[i]*tau)
    for i in range(14, 17):
        inc = inc + a[i]*tau*sin(b[i] + c[i]*tau)
    for i in range(17, 20):
        inc = inc + a[i]*tau*tau*sin(b[i] + c[i]*tau)
    inc = inc + a[20]*tau*tau*tau*sin(b[20] + c[20]*tau)
    return inc
    
    
#Reduccio de l'angle en graus (que no passi de 360)
def reductor_angles(deg):
    if deg > 360:
        while deg > 360:
            deg = deg - 360
    elif deg < 0:
        while deg < 0:
            deg = deg + 360
    elif deg < 360 and deg > 0:
        deg = deg
    else:
        print ("There has been a mistake in the function \"angles\"")
    
    return deg
        
        
    
#SUN'S APPARENT LONGITUDE (lambda), on li passem un cert any J en juian days. Cap.25
def lambd(J):
    tau = (J - 2451545.0)/365250
    L0_f = G(tau, L_A_0, L_B_0, L_C_0, 64)
    L1_f = G(tau, L_A_1, L_B_1, L_C_1, 34)
    L2_f = G(tau, L_A_2, L_B_2, L_C_2, 20)
    L3_f = G(tau, L_A_3, L_B_3, L_C_3, 7)
    L4_f = G(tau, L_A_4, L_B_4, L_C_4, 3)
    L5_f = G(tau, L_A_5, L_B_5, L_C_5, 1)
    B0_f = G(tau, B_A_0, B_B_0, B_C_0, 5)
    B1_f = G(tau, B_A_1, B_B_1, B_C_1, 2)
    R0_f = G(tau, R_A_0, R_B_0, R_C_0, 40)
    R1_f = G(tau, R_A_1, R_B_1, R_C_1, 10)
    R2_f = G(tau, R_A_2, R_B_2, R_C_2, 6)
    R3_f = G(tau, R_A_3, R_B_3, R_C_3, 2)
    R4_f = G(tau, R_A_4, R_B_4, R_C_4, 1)
    
    L_rad = (L0_f + L1_f*tau + L2_f*tau*tau + L3_f*tau*tau*tau + L4_f*tau*tau*tau*tau + L5_f*tau*tau*tau*tau*tau)/(10*10*10*10*10*10*10*10)
    #print ("L rad = " + str(L_rad))    
    B_rad = (B0_f + B1_f*tau)/(10*10*10*10*10*10*10*10)
    R = (R0_f + R1_f*tau + R2_f*tau*tau + R3_f*tau*tau*tau + R4_f*tau*tau*tau*tau)/(10*10*10*10*10*10*10*10)

    T = 10*tau 
    L_deg =  reductor_angles(L_rad*(180/pi)) #Passem a degrees
    L2 = reductor_angles(L_deg - 1.397*T - 0.00031*T*T) #degrees
    INCR_L = -0.09033*(1/3600) + 0.03916*(1/3600)*(cos(L2*(pi/180)) + sin(L2*pi/180))*tan(B_rad) #L2 en degrees, pero python fa els sin/cos en rad        
    L_final = reductor_angles(L_deg + INCR_L) #degrees
    
    #capítol 25, p.166
    geo_long = reductor_angles(L_final + 180) #degrees
    #Conversio de la geo_long a FKS system
    INCR_geo_long = -0.09033*(1/3600)
    geo_long_final =  reductor_angles(geo_long + INCR_geo_long)
    
    #Correcció de la nutació (increment de psi), cap. 22, p.143
    #........................................................................
    omega = reductor_angles(125.04452 - 1934.136261*T + 0.0020708*T*T + T*T*T/450000) #degrees
    L1_nutation = 280.4665 + 36000.7698*T #degrees
    L2_nutation = 218.3165 + 481267.8813*T #degrees
    nutation = -17.20*(1/3600)*sin(omega*(pi/180)) - 1.32*(1/3600)*sin(2*L1_nutation*(pi/180)) - 0.23*(1/3600)*sin(2*L2_nutation*(pi/180)) + 0.21*(1/3600)*sin(2*omega*(pi/180))      
    
    #.........................................................................
    #Correcció de l'aberració
    #INCR_lambda = increment(tau, A, B, C)
    aberration = -(20.4898*(1/3600))/R #-0.005775518*R*INCR_lambda
    
    #Trobar la lambda final, p.167
    lambd_final = geo_long_final + nutation + aberration
    
    return lambd_final
        
        
#main program
print ("We are going to calculate the dates of the solstices and equinoxes with high accuracy.")
print ("Of which year do you want to calculate them?")
prompt = '> '
year = int(input(prompt))
print ("\n")

JDE0_m, JDE0_j, JDE0_s, JDE0_d = JDE0(year)
JDE0list = [JDE0_m, JDE0_j, JDE0_s, JDE0_d]
JDE = []
Greg = []
    
for i in range (0,4):
    print ("\nJDE0 " + str(i))
    LAMBDA = lambd(JDE0list[i])
    JDE.append(float(JDE0list[i]))
    #FINAL CORRECTION:
    final_correction = 1
    while abs(final_correction) >= 0.0005:
        k = i
        LAMBDA = lambd(JDE[i])
        final_correction = 58*sin((k*90 - LAMBDA)*(pi/180))
        JDE[i] = JDE[i] + final_correction
        print ("Lambda = " + str(LAMBDA))
        print ("final correction = " + str(final_correction))
        print ("JDE[" + str(i) + "] = " + str(JDE[i]))
        print ("Gregorian[" + str(i) + "] = " + str(Conversor(JDE[i])))
        
    #Ara que ja tenim la data en Julian years, la passem a Gregorian years
    Greg.append(Conversor(JDE[i]))
            
print ("\nInstant of the solstices and equinoxes (March eq, June sols, September eq, December sols respectively):")
for i in range(0,4):
    print (str(Greg[i]) + ", which in Julian years is " + str(JDE[i]))





#print ("June 1962:")
#print (str(lambd(JDE0_j)))


#print ("October 1992:")
#print (str(lambd(2448908.5)))

#print ("April 1987:")
#print (str(lambd(2446895.5)))










