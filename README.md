# Cours de programmation avancée 

Bienvenue dans le TutoDjango de **Nolhan Dolou**, groupe 31b

-[x] TD1 fini

**-[] TP1 page 8 : amélioration de la DB**




---
## À retenir ...

### 1. Django

- `./manage.py runserver` pour lancer
- `http://127.0.0.1:8000/monApp/home/` la route de base

### 2. Coverage 
- `coverage run --source='monApp' manage.py test`
- `coverage report`

### 3. Tests

- Tests "status" + paramètre : 

    ```
    def test_home_param_status_code(self):

            response = self.client.get(reverse('home', args=["test"]))
            self.assertEqual(response.status_code, 200)
    ```

- Tests "content" + paramètre : 

    ```
    def test_home_param_content(self):
            response = self.client.get(reverse('home', args=["test"]))
            self.assertContains(response, 'Hello test!')
    ```


### 4. ORM

- `./manage.py makemigrations monApp` : créer une migration

- `./manage.py sqlmigrate monApp 0001` : créer le SQL correspondant

- `./manage.py migrate` : applique les migrations


Trois étapes pour effectuer les modifications du modèles :
- Modifiez les modèles (dans models.py).
- Exécutez manage.py makemigrations pour créer des migrations correspondant à ces
changements.
- Exécutez manage.py migrate pour appliquer ces modifications à la base de données.
