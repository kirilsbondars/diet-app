import csv


def import_data(db, Tasks):
    if Tasks.query.first() is None:
        with open('models/data/tasks.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                task = Tasks(id=row['id'], description=row['description'])
                db.session.add(task)

        db.session.commit()
