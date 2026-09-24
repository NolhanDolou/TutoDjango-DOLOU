# Cours de programmation avancée 

Bienvenue dans le TutoDjango de **Nolhan Dolou**, groupe 31b

-[x] TD1 fini
-[X] TP1  fini (juste tests content a faire pour pages listes)

**-[] TD2 p.7**




---
## À retenir ...

### 1. Django

- `./manage.py runserver` pour lancer
- `http://127.0.0.1:8000/monApp/home/` la route de base

### 2. Coverage 
- `coverage run --source='monApp' manage.py test`
- `coverage report`
- si tests regroupés : `coverage run manage.py test monApp/tests`



### 3. Tests
#### 3.1 Classique

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

#### 3.2 Regroupé
- lancement : `./manage.py test monApp/tests`



### 4. ORM

- `./manage.py makemigrations monApp` : créer une migration

- `./manage.py sqlmigrate monApp 0001` : créer le SQL correspondant

- `./manage.py migrate` : applique les migrations


Trois étapes pour effectuer les modifications du modèles :
- Modifiez les modèles (dans models.py).
- Exécutez manage.py makemigrations pour créer des migrations correspondant à ces
changements.
- Exécutez manage.py migrate pour appliquer ces modifications à la base de données.

### 5. Shell

Pour lancer le shell : 
* `python manage.py shell`
* `./manage.py shell`

Importer le modèle : `from monApp.models import *`
Voir tous les produits : `Produit.objects.all()`

Créer un prod : `prdt = Produit()`
Ajouter un intitulé : `prdt.intituleProd="ipod"`
Ajouter un prix : `prdt.prixUnitaireProd = 59.99`
Check le produit créé : `prdt`

On crée un statut : `s=Statut(idStatut=0,libelleStatut="Offline")`
On sauv dans la BD le statut : `s.save()`
On attribut le statut au produit : `prdt.statut=s`
On sauv le prod dans la BD : `prdt.save()`

Ou on peut faire : 
* `Produit(intituleProd="iphone", prixUnitaireProd=1299.99, statut=s).save()`

* `prdt=Produit.objects.create(intituleProd="ipad", prixUnitaireProd=499.69,statut=s)`

### 6. Administration

creer super user : `./manage.py createsuperuser`
(usr : o22403372, pwd : o22403372)

pour ajouter des elements a notre page d'admin : `admin.site.register(Produit)`