from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# Using annotation to define call method and add parameters
# We can call http://127.0.0.1:8000/hello/Mateus and return is "Welcome Mateus!"
@app.get("/hello/{name}")
async def hello(name):
  return f"Welcome {name}!"

# Data validation example
class AvailableCuisines(str, Enum):
  indian = 'indian'
  american = 'american'
  brazilian = 'brazilian'

food_items = {
  "indian": ['Samosa', "Dosa"],
  "american": ['Hot Dog', "Apple Pie"],
  "brazilian": ['Barbecue', "Feijoada"],
}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
  return food_items.get(cuisine)

# type validation
coupon_code = {
  1: "10%",
  2: "20%",
  3: "30%",
  4: "40%"
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
  return {'discount_amount': coupon_code.get(code)}