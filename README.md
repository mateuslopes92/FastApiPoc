# FastAPI POC
In this repository will be exploring FastApi with python.
FastApi Documentation: https://fastapi.tiangolo.com/

I`ve just installed FastApi and uvicorn:
FastApi -> Rest apis with python -> `pip install fastapi`
UviCorn -> Server to run FastApi server -> `pip install uvicorn`

## Running the project
`uvicorn main:app --reload`

This run the app and make it available in `http://127.0.0.1:8000/`

## FastApi vs Flask
FastApi has:
- In built Data Validation
- In built Documentation
- Fast running performance
- Less time to write code, few bugs

### Data Validation
Over this code:
```
@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
  food_items = {
    "indian": ['Samosa', "Dosa"],
    "american": ['Hot Dog', "Apple Pie"],
    "brazilian": ['Barbecue', "Feijoada"],
  }

  return food_items.get(cuisine)
```

in Flask `@app.get("/get_items/{cuisine}")` if want to do data validation need to do:

```
valid_cuisines = food_items.keys()
if cuisine not in valid_cuisines:
  return f""Sopported cuisines are {valid_cuisines}"
```

in FastApi we can do:
```
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
```

and if try to get a invalid cuisine like `http://127.0.0.1:8000/get_items/italian` will return an error object from FastApi telling what is available: `{"detail":[{"type":"enum","loc":["path","cuisine"],"msg":"Input should be 'indian', 'american' or 'brazilian'","input":"italian","ctx":{"expected":"'indian', 'american' or 'brazilian'"}}]}`


Type validation:
```
coupon_code = {
  1: "10%",
  2: "20%",
  3: "30%"
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
  return {'discount_amount': coupon_code.get(code)}
```

if try `http://127.0.0.1:8000/get_coupon/1` return `{"discount_amount":"10%"}`
but if try `http://127.0.0.1:8000/get_coupon/abc` return `{"detail":[{"type":"int_parsing","loc":["path","code"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"abc"}]}`

### FastApi in built documentation
if you access `http://127.0.0.1:8000/docs` will give you a kind of swagger with the methods to be tested.
<img width="1226" height="927" alt="Screenshot 2025-10-31 at 21 06 03" src="https://github.com/user-attachments/assets/4faee27c-c280-4348-9805-64abcd696a90" />
<img width="1260" height="681" alt="Screenshot 2025-10-31 at 21 05 54" src="https://github.com/user-attachments/assets/2addd8c3-be9c-4650-a518-c4d107c0abdc" />


if you access `http://127.0.0.1:8000/redoc` generate another cool and simple documentation for your api.
<img width="1223" height="622" alt="Screenshot 2025-10-31 at 21 07 58" src="https://github.com/user-attachments/assets/7c925d89-0460-4257-b4d0-45392b930c77" />
