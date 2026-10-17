from fastapi import FastAPI,Request
from products import products
from dtos import productDTO
app=FastAPI()

@app.get("/")
def home():
    return "Welcome to fastapi"

@app.get("/product")
def product():
    return products

#path parameters
@app.get("/product/{product_id}")
def get_one(product_id:int):
    ## if product available with the id,return product.else return error message
    for oneproduct in products:
        if oneproduct.get("id")==product_id:
            return oneproduct
    return {
        "error":"Product not Found"
    }
#Query parameter
# @app.get("/greet")
# def get_query(name:str,age:int):
#     return {
#         "message":f"Hello {name},Your age is {age}"
#     }

@app.get("/greet")
def get_query(request:Request):
    query=dict(request.query_params)
    return {
        "message":f"Hello {query.get('name')}, Your age is{query.get('age')}"
    }



## body,headers-request headers,query params
#Different types of http methods
@app.post("/create")
def create_product(product_data:productDTO):
    product_data=product_data.model_dump()
    products.append(product_data)
    return {"status":"Product Created Succesfully" ,"data":products}

@app.put('/update/{product_id}')
def update(product_data:productDTO,product_id:int):
    for index,Oneproduct in enumerate(products):
        if Oneproduct.get("id")==product_id:
            products[index]=product_data.model_dump()
            return {"message": "Product updated succesfully", "product": product_data}

    return{
        "error":"Product not found for this ID"
    }

@app.delete("/delete/{product_id}")
def delete(product_id:int):
    for index,OneProduct in enumerate(products):
        if OneProduct.get("id")==product_id:
            deleted_product=products.pop(index)
            return{
            "message":"Product deleted succesfully","product":deleted_product
            }
    return {
        "error":"Product not found"
    }
##POSTMAN
#How to validate data.-DTOS(data transfer objects)
#How to call different HTTP methods.-Any TOOL?



