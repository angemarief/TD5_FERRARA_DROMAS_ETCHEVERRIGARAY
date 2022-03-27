import pandas as pd
import numpy as np

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
        
        liste_pandas_sell=[]
        for i in self.liste_sell:
            liste_pandas_sell.append([i.type_ordre,i.quantite,i.prix,i.ID])
        if liste_pandas_sell!=[]:
            df1 = pd.DataFrame(np.array(liste_pandas_sell),columns=['type', 'quantity', 'price','ID'])
            print(df1.to_string(index=False))
        

        liste_pandas_buy=[]
        for i in self.liste_buy:
            liste_pandas_buy.append([i.type_ordre,i.quantite,i.prix,i.ID])
        if liste_pandas_buy!=[]:
            df2 = pd.DataFrame(np.array(liste_pandas_buy),columns=['type', 'quantity', 'price','ID'])
            print(df2.to_string(index=False))
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
    


def main():
    book = Book("TEST")
    book.insert_buy(10, 10.0)
    book.insert_sell(120, 12.0)
    book.insert_buy(5, 10.0)
    book.insert_buy(2, 11.0)
    book.insert_sell(1, 10.0)
    book.insert_sell(10, 10.0)

if __name__ == "__main__":
    main()

