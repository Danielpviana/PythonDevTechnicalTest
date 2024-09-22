from app.app_config import create_app
from app.db_config import db

app = create_app()

if __name__ == "__main__":
    app.run()

@app.before_request
def create_tables():
    db.create_all()
    
# with app.app_context():
#     db.create_all()  # Ensure tables are created
    
    # items = [
#         {
#             "id":1,
#             "name":"asdasd",
#             "price":100,
#             "mac_address":"asdasdasd",
#             "serial_number":"asdasd",
#             "manufacturer":"asdasdasd",
#             "description":"sdasdasd"
#         },
#         {
#             "id":2,
#             "name":"asdasd",
#             "price":100,
#             "mac_address":"asdasdasd",
#             "serial_number":"asdasd",
#             "manufacturer":"asdasdasd",
#             "description":"sdasdasd"
#         },
#         {
#             "id":3,
#             "name":"asdasd",
#             "price":100,
#             "mac_address":"asdasdasd",
#             "serial_number":"asdasd",
#             "manufacturer":"asdasdasd",
#             "description":"sdasdasd"
#         }
#     ]