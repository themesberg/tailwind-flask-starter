from project import create_app
from werkzeug.security import generate_password_hash
from datetime import date

# Créez une instance de l'application Flask
app = create_app()

# Activez le contexte d'application
app.app_context().push()

from project.models import User, db

def create_test_data():
    # Créer des utilisateurs de test
    user1 = User(name='Andreas Touloupis', email='andreas.touloupis@gmail.com',password=generate_password_hash('123456', method='pbkdf2'), dateOfBirth=date(1990, 12, 12))
    user2 = User(name='jane_doe', email='jane@example.com',password=generate_password_hash('123456', method='pbkdf2'), dateOfBirth=date(1990, 12, 12))

    # Ajouter les utilisateurs à la base de données
    db.session.add(user1)
    db.session.add(user2)

    # Committer les changements
    db.session.commit()

if __name__ == '__main__':
    create_test_data()