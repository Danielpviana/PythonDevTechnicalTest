from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Inventory

@app.route('/')
def index():
    items = Inventory.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        mac_address = request.form['mac_address']
        serial_number = request.form['serial_number']
        manufacturer = request.form['manufacturer']
        description = request.form['description']

        new_item = Inventory(
            name=name, price=price, mac_address=mac_address, 
            serial_number=serial_number, manufacturer=manufacturer, 
            description=description
        )

        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    item = Inventory.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.price = request.form['price']
        item.mac_address = request.form['mac_address']
        item.serial_number = request.form['serial_number']
        item.manufacturer = request.form['manufacturer']
        item.description = request.form['description']

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    item = Inventory.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))
