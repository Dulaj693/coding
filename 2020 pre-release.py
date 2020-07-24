#variables here#
item_code=[]
category=[]
descripition=[]
price=[]

#data entry#
while True:
    itemname=input(str("Item code:"))
    if itemname==(""):
        break
    item_code=item_code+[itemname]
    catename=input(str("Category :"))
    category=category+[catename]
    desname=input(str("Descripition :"))
    descripition=descripition+[desname]
    priname=float(input("price :"))
    price=price+[priname]

#task 1 final#
print(item_code)
print(category)
print(descripition)
print(price)
#print(":category : item_code : descripition : price:")#
#print(":",category," "*(9-len(category)),":",item_code," "*(9-len(item_code)),":",descripition," "*(9-len(descripition)),":",price," "*(9-len(str(price))),":")#

#task 2 customer view#
itemcode=input("Enter required item number:")
total_price=0.00
while itemcode!="":
    found=False
    for count in range(0,len(item_code)):
        if itemcode==item_code[count]:
            print(item_code[count]+"  "+category[count]+"  "+descripition[count]+"  "+str(price[count]))
            total_price=total_price+price[count]
            found=True
            break
    itemcode=input("Enter required item number:")
print("$",total_price)

#task 3#
