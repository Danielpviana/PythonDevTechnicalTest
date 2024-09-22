from flask import Flask, render_template, url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Configurar la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:my-secret-pw@host.docker.internal/aht-global-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    mac_address = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f"<Inventory {self.name} {self.price} {self.description}>"
    
@app.before_request
def create_tables():
    db.create_all()

items = [
        {
            "id":1,
            "name":"asdasd",
            "price":100,
            "mac_address":"asdasdasd",
            "serial_number":"asdasd",
            "manufacturer":"asdasdasd",
            "description":"sdasdasd"
        },
        {
            "id":2,
            "name":"asdasd",
            "price":100,
            "mac_address":"asdasdasd",
            "serial_number":"asdasd",
            "manufacturer":"asdasdasd",
            "description":"sdasdasd"
        },
        {
            "id":3,
            "name":"asdasd",
            "price":100,
            "mac_address":"asdasdasd",
            "serial_number":"asdasd",
            "manufacturer":"asdasdasd",
            "description":"sdasdasd"
        }
    ]

@app.route("/")
def base():
    items = Product.query.all()
    return render_template('index.html',items = items)

@app.route("/edit/<int:id>")
def edit(id):
    item = Product.query.get_or_404(id)
    return render_template("add.html",item = item)

@app.route("/delet/<int:id>")
def delete(id):
    db_product = Product.query.get(id)
    try:
        db.session.delete(db_product)
        db.session.commit()
        return redirect(url_for("base"))
    except:
        return 'Error deleting'
    
@app.route("/add")
def add():
    return render_template("add.html", item = None)


@app.route("/create", methods=['POST'])
def create_product():
    name = request.form['name']
    price = request.form['price']
    mac_address = request.form['mac_address']
    serial_number = request.form['serial_number']
    manufacturer = request.form['manufacturer']
    description = request.form.get('description', '')
    new_product = Product(
            name=name,
            price=price,
            mac_address=mac_address,
            serial_number=serial_number,
            manufacturer=manufacturer,
            description=description
        )
    try:
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for("base"))
    except:
        return 'Error creating the product'
    

@app.route("/update/<int:id>", methods=['POST'])
def update_product(id):
    name = request.form['name']
    price = request.form['price']
    mac_address = request.form['mac_address']
    serial_number = request.form['serial_number']
    manufacturer = request.form['manufacturer']
    description = request.form.get('description', '')
    db_product = Product.query.get(id)
    db_product.name = name
    db_product.price = price
    db_product.mac_address = mac_address
    db_product.serial_number = serial_number
    db_product.manufacturer = manufacturer
    db_product.description = description
    try:
        db.session.commit()
        return redirect(url_for("base"))
    except:
        return 'Error updating'
    

if __name__ == "__main__":
    app.run()