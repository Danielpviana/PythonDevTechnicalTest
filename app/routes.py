from flask import Blueprint, render_template, request, redirect, url_for
from app.db_config import db
from app.models import Product

router = Blueprint('main', __name__, 
                   template_folder = 'templates',
                   static_folder = 'static')

@router.route("/")
def base():
    items = Product.query.all()
    return render_template('index.html',items = items)

@router.route("/edit/<int:id>")
def edit(id):
    item = Product.query.get_or_404(id)
    return render_template("add.html",item = item)

@router.route("/delet/<int:id>")
def delete(id):
    db_product = Product.query.get(id)
    try:
        db.session.delete(db_product)
        db.session.commit()
        return redirect(url_for("main.base"))
    except:
        return 'Error deleting'
    
@router.route("/add")
def add():
    return render_template("add.html", item = None)


@router.route("/create", methods=['POST'])
def create_product():
    new_product = Product(
            name=request.form['name'],
            price=request.form['price'],
            mac_address=request.form['mac_address'],
            serial_number=request.form['serial_number'],
            manufacturer=request.form['manufacturer'],
            description=request.form.get('description', '')
        )
    try:
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for("main.base"))
    except:
        return 'Error creating the product'
    

@router.route("/update/<int:id>", methods=['POST'])
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
        return redirect(url_for("main.base"))
    except:
        return 'Error updating'