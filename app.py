from flask import Flask, render_template, url_for, redirect, request, flash
from models import Animal, Adopter, app, db
from forms import AnimalForm, AdopterForm
from datetime import datetime

with app.app_context():
    db.create_all()
    
    # Sample data for at fylde databasen hvis den er tom
    if Animal.query.count() == 0:
        animals = [
            Animal(
                name='Max',
                species='Dog',
                breed='Golden Retriever',
                age=3,
                gender='Male',
                description='Max is a friendly and energetic golden retriever who loves to play fetch and go for long walks. He is great with children and other pets.',
                image_url='https://images.pexels.com/photos/2253275/pexels-photo-2253275.jpeg'
            ),
            Animal(
                name='Luna',
                species='Cat',
                breed='Siamese',
                age=2,
                gender='Female',
                description='Luna is a playful Siamese cat who enjoys sunbathing and chasing toys. She is a bit shy at first but warms up quickly.',
                image_url='https://images.pexels.com/photos/1170986/pexels-photo-1170986.jpeg'
            ),
            Animal(
                name='Buddy',
                species='Dog',
                breed='Beagle',
                age=5,
                gender='Male',
                description='Buddy is a sweet beagle who loves to sniff everything in sight. He is very food-motivated and knows several tricks.',
                image_url='https://images.pexels.com/photos/1254140/pexels-photo-1254140.jpeg'
            )
        ]
        
        db.session.add_all(animals)
        db.session.commit()

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html', title='Home Page')

@app.route("/animals")
def animals():
    page = request.args.get('page', 1, type=int)
    per_page = 6  
    
    species_filter = request.args.get('species', '')
    gender_filter = request.args.get('gender', '')
    status_filter = request.args.get('status', '')
    
    query = Animal.query
    
    if species_filter:
        query = query.filter(Animal.Species == species_filter)
    if gender_filter:
        query = query.filter(Animal.Gender == gender_filter)
    if status_filter:
        query = query.filter(Animal.Status == status_filter)
    
    paginated_animals = query.paginate(page=page, per_page=per_page, error_out=False)
    
    all_species = db.session.query(Animal.Species).distinct().all()
    all_genders = db.session.query(Animal.Gender).distinct().all()
    
    return render_template(
        'animals.html', 
        title='All Animals', 
        animals=paginated_animals.items,
        pagination=paginated_animals,
        species_list=[species[0] for species in all_species if species[0]],
        gender_list=[gender[0] for gender in all_genders if gender[0]],
        current_species=species_filter,
        current_gender=gender_filter,
        current_status=status_filter
    )

@app.route("/animal/<int:id>")
def animal_details(id):
    one_animal = Animal.query.get_or_404(id)
    return render_template("animal_details.html", animal=one_animal)

    # Create dyr
@app.route("/animal/create", methods=['GET', 'POST'])
def create_animal():
    form = AnimalForm()
    
    if form.validate_on_submit():
        new_animal = Animal(
            name=form.name.data,
            species=form.species.data,
            breed=form.breed.data,
            age=form.age.data,
            gender=form.gender.data,
            description=form.description.data,
            image_url=form.image_url.data,
            status=form.status.data
        )
        
        db.session.add(new_animal)
        db.session.commit()
        
        flash(f'{new_animal.Name} has been added!', 'success')
        return redirect(url_for('animals'))
    
    return render_template('animal_form.html', title='Add Animal', form=form, action='create')

    # Opdater dyr
@app.route("/animal/update/<int:id>", methods=['GET', 'POST'])
def update_animal(id):
    animal = Animal.query.get_or_404(id)
    
    form = AnimalForm()
    
    if form.validate_on_submit():
        animal.Name = form.name.data
        animal.Species = form.species.data
        animal.Breed = form.breed.data
        animal.Age = form.age.data
        animal.Gender = form.gender.data
        animal.Description = form.description.data
        animal.ImageUrl = form.image_url.data
        animal.Status = form.status.data
        
        db.session.commit()
        
        flash(f'{animal.Name} has been updated!', 'success')
        return redirect(url_for('animal_details', id=animal.Id))
    
    elif request.method == 'GET':
        form.name.data = animal.Name
        form.species.data = animal.Species
        form.breed.data = animal.Breed
        form.age.data = animal.Age
        form.gender.data = animal.Gender
        form.description.data = animal.Description
        form.image_url.data = animal.ImageUrl
        form.status.data = animal.Status
    
    return render_template('animal_form.html', title='Update Animal', form=form, action='update')

    # Delete dyr
@app.route("/animal/delete/<int:id>", methods=['POST'])
def delete_animal(id):
    animal = Animal.query.get_or_404(id)
    animal_name = animal.Name
    
    db.session.delete(animal)
    db.session.commit()
    
    flash(f'{animal_name} has been deleted!', 'success')
    return redirect(url_for('animals'))

    # Adopter dyr
@app.route("/animal/adopt/<int:id>", methods=['GET', 'POST'])
def adopt_animal(id):
    animal = Animal.query.get_or_404(id)
    
    if animal.Status != 'Available':
        flash(f'Sorry, {animal.Name} is no longer available for adoption.', 'warning')
        return redirect(url_for('animal_details', id=animal.Id))
    
    form = AdopterForm()
    
    if form.validate_on_submit():
        adopter = Adopter(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data
        )
        
        db.session.add(adopter)
        db.session.commit()
        
        animal.Status = 'Pending'
        animal.AdopterId = adopter.Id
        animal.AdoptionDate = datetime.now()
        db.session.commit()
        
        return render_template('adoption_success.html', animal=animal, adopter=adopter)
    
    return render_template('adopt_form.html', title=f'Adopt {animal.Name}', animal=animal, form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About Us')

if __name__ == '__main__':
    app.run(debug=True)