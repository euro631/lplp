#def loe_failist(file:str)->str:
#    """loeme tekst failist
#    """
#    f=open(file,"r")
#    stroka=f.read()#str
#    #stroka=f.readlines()#list
#    f.close()
#    return stroka
#stroka=loe_failist("TextFile1.txt")
#print(stroka)
#def loe_failist_listisse(file:str)->list:
#    """Loeme tekst failist ja salvesta järgemisse
#    """
#    f=open(file,"r")
#    list_=[]
#    for stroka in f:
#        list_.append(stroka.strip())
#    f.close()
#    return list_
#spisok=loe_failist_listisse("TextFile1.txt")
#print(spisok)
#def salvesta_failisse(file:str):
#    f=open(file,"a")
#    text=input("sisesta taksti:")
#    f.write(text+"\n")
#    f.close()
#for i in range(10):
#    salvesta_failisse("Loetelu.txt")
