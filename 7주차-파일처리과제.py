f=open('mbox.txt')
fw=open('Test.txt','w')

for line in f :
    line1=line.rstrip()
    if line.startswith('From ') :
        
        line2=line1.split()
        fline=line2[1],',',line2[6]
        fline=str(fline)
        fw.write(fline)

f.close()
fw.close()

    
    
