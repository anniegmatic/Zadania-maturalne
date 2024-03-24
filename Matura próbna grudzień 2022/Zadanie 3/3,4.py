plik = open("liczby.txt", "rt")

def ile(tab):
    s0=0;s1=0;s2=0;s3=0;s4=0;s5=0;s6=0;s7=0;s8=0;s9=0;sa=0;sb=0;sc=0;sd=0;se=0;sf=0
    for y in tab:
        for x in y:
            match x:
                case "0":
                    s0+=1
                case "1":
                    s1+=1
                case "2":
                    s2+=1
                case "3":
                    s3+=1
                case "4":
                    s4+=1
                case "5":
                    s5+=1
                case "6":
                    s6+=1
                case "7":
                    s7+=1
                case "8":
                    s8+=1
                case "9":
                    s9+=1
                case "a":
                    sa+=1
                case "b":
                    sb+=1
                case "c":
                    sc+=1
                case "d":
                    sd+=1
                case "e":
                    se+=1
                case "f":
                    sf+=1
    wyn= "0:"+str(s0)+"\n1:"+str(s1)+"\n2:"+str(s2)+"\n3:"+str(s3)+"\n4:"+str(s4)+"\n5:"+str(s5)+"\n6:"+str(s6)+"\n7:"+str(s7)+"\n8:"+str(s8)+"\n9:"+str(s9)+"\na:"+str(sa)+"\nb:"+str(sb)+"\nc:"+str(sc)+"\nd:"+str(sd)+"\ne:"+str(se)+"\nf:"+str(sf)
    return wyn
                    
tab = []
for linia in plik:
    rekord = linia.strip()
    heks = str(hex(int(rekord)))
    heks = heks[2:]
    tab.append(heks)

print(ile(tab))
