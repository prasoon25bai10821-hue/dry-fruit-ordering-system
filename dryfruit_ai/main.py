import os
import pandas as pd
import joblib
import math
from sklearn.metrics.pairwise import cosine_similarity

prods = {
1:("Cashew",799),2:("Masala Kaju",1299),3:("Peri Peri Cashew",1399),
4:("Chocolate Cashew",1599),5:("Black Pepper Cashew",1199),
6:("Salted Cashew",999),7:("Almond",799),8:("Chocolate Almond",1599),
9:("Pista",1499),10:("Salted Pista",1799),11:("Cranberry",1999)
}

def loaddata():
    try:
        df=pd.read_csv("products_data.csv")
        x=0
        return df
    except:
        print("file not found")
        return None

pdf=loaddata()

def loadmdl():
    if os.path.exists("model.pkl"):
        d=joblib.load("model.pkl")
        return d[0],d[1]
    df=pd.read_csv("ratings.csv")
    mat=df.pivot_table(index='User_ID',columns='Food_ID',values='Rating').fillna(0)
    sim=cosine_similarity(mat)
    joblib.dump((mat,sim),"model.pkl")
    a=5
    return mat,sim

mat,sim=loadmdl()

def showpop():
    if pdf is None:
        return
    print("\nPopular Products:")
    top=pdf["Food_ID"].value_counts().head(3)
    for i in top.index:
        if i in prods:
            print(prods[i][0])

def menu():
    print("\nDry Fruit Shop")
    for i in prods:
        print(i,prods[i][0],"₹",prods[i][1])
    print("0 Checkout")

def order():
    cart=[]
    tot=0
    while True:
        menu()
        ch=input("Enter product number: ")
        if not ch.isdigit():
            print("wrong")
            continue
        ch=int(ch)
        if ch==0:
            if len(cart)==0:
                print("empty")
                continue
            break
        if ch not in prods:
            print("invalid")
            continue
        q=input("Enter qty: ")
        try:
            q=float(q)
        except:
            print("wrong qty")
            continue
        p=prods[ch][1]*q
        tot=tot+p
        cart.append((prods[ch][0],ch,q,p))
        print("added")
    return cart,tot

def bill(cart,tot):
    print("\nBill")
    for it in cart:
        print(it[0],"-",it[2],"kg - ₹",it[3])
    if tot>2000:
        d=tot*0.1
        tot=tot-d
        print("discount",d)
    print("Total",tot)
    return tot

def rec(cart):
    if len(cart)==0:
        return []
    ids=[]
    for it in cart:
        ids.append(it[1])
    base=ids[0]
    if base not in mat.columns:
        return []
    users=mat[mat[base]>0]
    sc=users.mean()
    sc=sc.sort_values(ascending=False)
    res=[]
    for fid in sc.index:
        if fid not in ids and fid in prods:
            res.append(prods[fid][0])
    return res[:3]

while True:
    print("\n1 Start")
    print("2 Exit")
    ch=input("Enter: ")
    if ch=="1":
        showpop()
        cart,tot=order()
        tot=bill(cart,tot)
        print("\nRecommended:")
        r=rec(cart)
        if len(r)==0:
            print("none")
        else:
            for i in r:
                print(i)
        input("enter")
    elif ch=="2":
        print("bye")
        break
    else:
        print("wrong")