from statistics import quantiles

type_of_product1=input('What is the type of the product 1:')
price_product1=input('what is the price of the product 1:')
quantity_product1=input('what is the quantity_product 1:')

type_of_product2=input('What is the type of the product 2:')
price_product2=input('what is the price of the product 2:')
quantity_product2=input('what is the quantity_product 2 :')

type_of_product3=input('What is the type of the product 3:')
price_product3=input('what is the price of the product 3:')
quantity_product3=input('what is the quantity_product 3:')

result_product1=round(float(price_product1)*float(quantity_product1))
print('The price of the product 1 which is  ' + type_of_product1 +'is for' + str(result_product1) + '$')   

result_product2=round(float(price_product2)*float(quantity_product2))
print('The price of the product 2 which is '+ type_of_product2 +'is for' + str(result_product2) + '$')   

result_product3=round(float(price_product3)*float(quantity_product3))
print('The price of the product 3 which is '+ type_of_product3 +'is for  ' + str(result_product3) + '$')    
