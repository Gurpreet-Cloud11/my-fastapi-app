from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "healthy", "service": "my-fastapi-app"}


@app.get("/items")
def get_items():
    return {
        "items": [
            {"id": 1, "name": "Laptop", "price": 999.99},
            {"id": 2, "name": "Mouse", "price": 29.99},
            {"id": 3, "name": "Keyboard", "price": 79.99},
            {"id": 4, "name": "Monitor", "price": 299.99},
        ]
    }