def tower(disks,Beg,Aux,End):
    
    if disks == 1:
        print ('Move disk 1 from Beg',Beg,"to distination",Aux)
        
        return
    
    tower(disks - 1,Beg,End,Aux)
    
    print('Move disk 1 from from Beg',Beg,"to distnation",Aux)
    
    tower(disks -1,Aux,Beg,End)

disks = int(input("Enter The Number Of Disks:"))
tower(disks,'A','B','C')
