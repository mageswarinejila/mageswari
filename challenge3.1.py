def   linearSearchProduct(productlist,targetproduct):
  indices=[]

  for index,product in enumerate(productlist):
    if product == targetproduct:
       indices. append(index) 

  return indices



products=["shoes","boot","loafar","shoes","sandal","shoes"]
target="shoes"
result= linearSearchProduct(products, target)
print(result)