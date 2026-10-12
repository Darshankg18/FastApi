from fastapi import FastAPI,Request
from products import products
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
