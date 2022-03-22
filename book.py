class Book:
    
    def __init__(self,name,liste_order=[]):
        self.name=name
        self.liste_execute=[]
        self.liste_sell=[]
        self.liste_buy=[]
        self.index=0

        
    def insert_buy (self,q,p, type_ordre="BUY"):
        self.index=self.index+1
        ordre=Order(q,self.index,p,type_ordre)
        self.liste_buy.append(ordre)
        self.liste_buy=sorted(self.liste_buy,key=lambda x:x.prix,reverse=True)
        self.affichage(ordre)
        
    
    def insert_sell(self,q,p, type_ordre="SELL"):
        self.index=self.index+1
        ordre=Order(q,self.index,p,type_ordre)
        self.liste_sell.append(ordre)
        self.liste_sell=sorted(self.liste_sell,key=lambda x:x.prix,reverse=True)
        self.affichage(ordre)
        
    def affichage(self,ordre):
        print("--- Insert " + str(ordre.type_ordre) + " "+str(ordre.quantite)+"@"+str(ordre.prix)+" id="+str(ordre.ID)+ " on "+self.name )
        self.check_execute()
        for i in range(len(self.liste_execute)):
            print("Execute "+str(self.liste_execute[i-1].quantite)+" at "+str(self.liste_execute[i-1].prix)+" on "+str(self.name))
            self.liste_execute.pop(i-1)
        print("Book on "+self.name)
        
        for i in self.liste_sell:
            print("          "+str(i.type_ordre)+" "+ str(i.quantite) +"@"+str(i.prix) + " id="+str(i.ID))
        for i in self.liste_buy:
            print("          "+str(i.type_ordre)+" "+ str(i.quantite) +"@"+str(i.prix) + " id="+str(i.ID))
        print("----------------------------------")

    def check_execute(self):
        if len(self.liste_buy)>0 and len(self.liste_sell)>0:
            while self.liste_buy[0].prix >= self.liste_sell[-1].prix:
                diff=self.liste_buy[0].quantite-self.liste_sell[-1].quantite

                if diff==0:
                    self.liste_execute.append(Order(self.liste_buy[0].quantite,-1,self.liste_buy[0].prix,"EXECUTE"))

                    self.liste_sell.pop(-1)
                    self.liste_buy.pop(0)

                if diff>0:
                    self.liste_execute.append(Order(diff,-1,self.liste_buy[0].prix,"EXECUTE"))
                    self.liste_sell.pop(-1)
                    self.liste_buy[0]=self.liste_buy[0].set_quantity(self.liste_buy[0].quantite-diff)

                if diff<0:
                    self.liste_execute.append(Order(self.liste_buy[0].quantite,-1,self.liste_buy[0].prix,"EXECUTE"))
                    self.liste_buy.pop(0)
                    self.liste_sell[-1]=self.liste_sell[-1].set_quantity(self.liste_sell[-1].quantite+diff)

    
class Order:

    def __init__(self,quantite,ID, prix, type_ordre):
        self.quantite=quantite
        self.prix=prix
        self.ID=ID
        self.type_ordre=type_ordre

    def set_quantity(self,newquantity):
        return Order(newquantity,self.ID,self.prix,self.type_ordre)
