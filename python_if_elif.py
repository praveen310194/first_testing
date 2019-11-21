#customer discount based on purchase
item_value = int(input("Enter item value :"))

if item_value >=1000:
  discount = 30
  discount_amount = (item_value/100)*discount
  final_amount = item_value-discount_amount
  print('Congratulations! you got {}% discount and you saved {}, your final amount to pay is {}'.format(discount,discount_amount,final_amount))
elif item_value >=700 and item_value<1000:
  discount = 25
  discount_amount = (item_value/100)*discount
  final_amount = item_value-discount_amount
  print('Congratulations! you got {}% discount and you saved {}, your final amount to pay is {}'.format(discount,discount_amount,final_amount))
elif item_value >=500 and item_value<700:
  discount = 20
  discount_amount = (item_value/100)*discount
  final_amount = item_value-discount_amount
  print('Congratulations! you got {}% discount and you saved {}, your final amount to pay is {}'.format(discount,discount_amount,final_amount))
else:
  print('Sorry you not get any discount and your final_amount to pay is {}'.format(item_value))
