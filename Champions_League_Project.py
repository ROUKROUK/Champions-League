import time
import random



def Champions_league():
    
    goals = [0, 1, 2, 3, 4, 5]
    lista_prwton = ["BARCELONA", "LEIPZIG", "JUVENTUS", "BAYERN", "LIVERPOOL",
                    "ATALANTA", "MAN CITY", "PSG"]
    lista_deuteron = ["NAPOLI", "TOTTENHAM", "LYON", "CHELSEA",
                      "ATLETICO", "VALENCIA", "REAL MADRID", "DORTMUND"]
    count = 0
    
    print("          ||||    Κλήρωση των 16   |||   ")
    #lista των 8
    list_8a=[]
    list_8b=[]
    list_41=[]
    list_42=[]
    list_2a=[]
    list_2b=[]
    final1=[]
    final2=[]
    for i in range(8):
        time.sleep(1)
        y = random.choice(lista_prwton)
        lista_prwton.remove(y)
        x = random.choice(lista_deuteron)
        lista_deuteron.remove(x)
        time.sleep(1.5)
        if count == 0:
            print("Πρώτος Αγώνας : ", end="")
            time.sleep(1)
            print(y, end="")
            time.sleep(1.5)
            print(" vs ", x,)
            listaa = [x, y]
            # a = goal ths X
            # b = goal ths Y
            a = random.choice(goals)
            b = random.choice(goals)
            time.sleep(1)
            print("First Leg :      ", a, "            ", b)
            time.sleep(1.5)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_8a.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_8a.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", y)
                    list_8a.append(y)
                else:
                    print("     winner : ", x)
                    list_8a.append(x)
                
        if count == 1:
            print("Δεύτερος Αγώνας : ", y, " vs ", x)
            listaa = [x, y]
            # a = goal ths X
            # b = goal ths Y
            a = random.choice(goals)
            b = random.choice(goals)
            print("First Leg :      ", a, "            ", b)
            time.sleep(1.5)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_8b.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_8b.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", y)
                    list_8b.append(y)
                else:
                    print("     winner : ", x)
                    list_8b.append(x)

                    
        if count == 2:
            print("Τρίτος Αγώνας : ", y, " vs ", x)
            listaa = [x, y]
            # a = goal ths X
            # b = goal ths Y
            a = random.choice(goals)
            b = random.choice(goals)
            print("First Leg :      ", a, "            ", b)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_8a.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_8a.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", x)
                    list_8a.append(x)
                else:
                    print("     winner : ", y)
                    list_8a.append(y)


                    
        if count == 3:
            print("Τέταρτος Αγώνας : ", y, " vs ", x)
            listaa = [x, y]
            # a = goal ths X
            # b = goal ths Y
            a = random.choice(goals)
            b = random.choice(goals)
            print("First Leg :      ", a, "            ", b)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_8b.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_8b.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", x)
                    list_8b.append(x)
                else:
                    print("     winner : ", y)
                    list_8b.append(y)
        if count == 4:
            print("Πέμπτος Αγώνας : ", y, " vs ", x)
            listaa = [x, y]
            # a = goal ths X
            # b = goal ths Y
            a = random.choice(goals)
            b = random.choice(goals)
            print("First Leg :      ", a, "            ", b)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_8a.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_8a.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", x)
                    list_8a.append(x)
                else:
                    print("     winner : ", y)
                    list_8a.append(y)


                
        if count == 5:
            print("Έκτος Αγώνας : ", y, " vs ", x)
            listaa = [x, y]
            # a = goal ths X
            # b = goal ths Y
            a = random.choice(goals)
            b = random.choice(goals)
            print("First Leg :      ", a, "            ", b)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_8b.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_8b.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", x)
                    list_8b.append(x)
                else:
                    print("     winner : ", y)
                    list_8b.append(y)


                    
        if count == 6:
            print("Έβδομος Αγώνας : ", y, " vs ", x)
            listaa = [x, y]
            # a = goal ths X
            # b = goal ths Y
            a = random.choice(goals)
            b = random.choice(goals)
            print("First Leg :      ", a, "            ", b)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_8a.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_8a.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", y)
                    list_8a.append(y)
                else:
                    print("     winner : ", x)
                    list_8a.append(x)


                    
        if count == 7:
            print("Όγδοος Αγώνας : ", y, " vs ", x)
            listaa = [x, y]
            # a = goal ths X
            # b = goal ths Y
            a = random.choice(goals)
            b = random.choice(goals)
            print("First Leg :      ", a, "            ", b)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_8b.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_8b.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", y)
                    list_8b.append(y)
                else:
                    print("     winner : ", x)
                    list_8b.append(x)
        count += 1

        
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    #Κλήρωση των 8
    count_8cl=0
    print("                      Κλήρωση των 8              ")
    for i in range(4):
        #time.sleep(1)
        y = random.choice(list_8a)
        list_8a.remove(y)
        x = random.choice(list_8b)
        list_8b.remove(x)
        #time.sleep(3)
        if count_8cl == 0:
             print("Πρώτος Αγώνας : ", y, " vs ", x)
             listaa = [x,y]
             a = random.choice(goals)
             b = random.choice(goals)
             print("First Leg :      ", a, "            ", b)
             c = random.choice(goals)
             d = random.choice(goals)
             print("Second Leg :     ", c, "            ", d)
             if a + c > b + d:
                print("     Winner : ", y)
                list_41.append(y)
             elif a + c < b + d:
                print("     Winner : ", x)
                list_41.append(x)
             elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", y)
                    list_41.append(y)
                else:
                    print("     winner : ", x)
                    list_41.append(x)
             
             
                
        if count_8cl == 1:
            print("Δεύτερος Αγώνας : ", y, " vs ", x)
            print("Πρώτος Αγώνας : ", y, " vs ", x)
            listaa = [x,y]
            a = random.choice(goals)
            b = random.choice(goals)
            print("First Leg :      ", a, "            ", b)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_42.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_42.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", y)
                    list_42.append(y)
                else:
                    print("     winner : ", x)
                    list_42.append(x)

                    
        if count_8cl == 2:
             print("Πρώτος Αγώνας : ", y, " vs ", x)
             listaa = [x,y]
             a = random.choice(goals)
             b = random.choice(goals)
             print("First Leg :      ", a, "            ", b)
             c = random.choice(goals)
             d = random.choice(goals)
             print("Second Leg :     ", c, "            ", d)
             if a + c > b + d:
                print("     Winner : ", y)
                list_41.append(y)
             elif a + c < b + d:
                print("     Winner : ", x)
                list_41.append(x)
             elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", y)
                    list_41.append(y)
                else:
                    print("     winner : ", x)
                    list_41.append(x)


                    
        if count_8cl == 3:
             print("Πρώτος Αγώνας : ", y, " vs ", x)
             listaa = [x,y]
             a = random.choice(goals)
             b = random.choice(goals)
             print("First Leg :      ", a, "            ", b)
             c = random.choice(goals)
             d = random.choice(goals)
             print("Second Leg :     ", c, "            ", d)
             if a + c > b + d:
                print("     Winner : ", y)
                list_42.append(y)
             elif a + c < b + d:
                print("     Winner : ", x)
                list_42.append(x)
             elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", y)
                    list_42.append(y)
                else:
                    print("     winner : ", x)
                    list_42.append(x)
        count+=1
    
    list_42=list(list_41)
    

    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    list_4cl=0
    print("                      Κλήρωση των 4              ")
    for i in range(2):
        #time.sleep(1)
        y = random.choice(list_41)
        list_41.remove(y)
        list_42.remove(y)
        x = random.choice(list_42)
        list_42.remove(x)
        list_41.remove(x)
        #time.sleep(3)
        if list_4cl == 0:
            print("Πρώτος Αγώνας : ", y, " vs ", x)
            listaa = [x, y]
            # a = goal ths X
            # b = goal ths Y
            a = random.choice(goals)
            b = random.choice(goals)
            print("First Leg :      ", a, "            ", b)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_2a.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_2a.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", y)
                    list_2a.append(y)
                else:
                    print("     winner : ", x)
                    list_2a.append(x)
                
        if list_4cl == 1:
            print("Δεύτερος Αγώνας : ", y, " vs ", x)
            listaa = [x, y]
            # a = goal ths X
            # b = goal ths Y
            a = random.choice(goals)
            b = random.choice(goals)
            print("First Leg :      ", a, "            ", b)
            c = random.choice(goals)
            d = random.choice(goals)
            print("Second Leg :     ", c, "            ", d)
            if a + c > b + d:
                print("     Winner : ", y)
                list_2b.append(y)
            elif a + c < b + d:
                print("     Winner : ", x)
                list_2b.append(x)
            elif a + c == b + d:
                h = random.choice(goals)
                j = random.choice(goals)
                print("Third match :      ", h, "        ",j)
                if h>j:
                    print("     winner : ", y)
                    list_2b.append(y)
                else:
                    print("     winner : ", x)
                    list_2b.append(x)
    list_2b=list(list_2a)
    

    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    count_telikos=0
    print("                     ΤΕΛΙΚΟΣ CHAMPIONS LEAGUE             ")
    for i in range(1):
        #time.sleep(1)
        y = random.choice(list_2a)
        list_2a.remove(y)
        list_2b.remove(y)
        x = random.choice(list_2b)
        list_2a.remove(x)
        list_2b.remove(x)
        #time.sleep(3)
        if count_telikos == 0:
            print("Πρώτος Αγώνας : ", y, " vs ", x)
            listaa = [x, y]
            # a = goal ths X
            
            a = random.choice(goals)
            b = random.choice(goals)
            
            print("Final Match :      ", a, "            ", b)

            if a> b:
                print("     Winner : ", y)
                list_2a.append(y)
            elif a < b :
                print("     Winner : ", x)
                list_2a.append(x)
            elif a == b:
                h = random.choice(goals)
                j = random.choice(goals)
                print("ΠΑΡΑΤΑΣΗ :      ", h, "        ",j)
                while h==j:
                     h = random.choice(goals)
                     j = random.choice(goals)
                if h>j:
                    print("     winner : ", y)
                    final1.append(y)
                else:
                    print("     winner : ", x)
                    final2.append(x)
   
    
    
   

Champions_league()
        

