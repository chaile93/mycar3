from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')
@login_required
def cars():
    form = CarForm()
    if form.validate_on_submit():
        new_car = Car(
            make=form.make.data,
            model=form.model.data,
            year=form.year.data,
            owner=current_user.id
        )
        db.session.add(new_car)
        db.session.commit()
        flash('Car added successfully!', 'success')
        return redirect(url_for('main.cars'))

    cars = Car.query.filter_by(owner=current_user.id).all()
    return render_template('cars.html', form=form, cars=cars)

@main_bp.route('/cars/<int:car_id>', methods=['GET', 'POST'])
@login_required
def edit_car(car_id):
    car = Car.query.get_or_404(car_id)
    form = CarForm()
    if form.validate_on_submit():
        car.make = form.make.data
        car.model = form.model.data
        car.year = form.year.data
        db.session.commit()
        flash('Car updated successfully!', 'success')
        return redirect(url_for('main.cars'))
    elif request.method == 'GET':
        form.make.data = car.make
        form.model.data = car.model
        form.year.data = car.year
    return render_template('edit_car.html', form=form, car=car)

@main_bp.route('/cars/delete/<int:car_id>', methods=['POST'])
@login_required
def delete_car(car_id):
    car = Car.query.get_or_404(car_id)
    db.session.delete(car)
    db.session.commit()
    flash('Car deleted successfully!', 'success')
    return redirect(url_for('main.cars'))