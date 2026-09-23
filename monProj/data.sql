DELETE FROM monApp_categorie;
INSERT INTO monApp_categorie VALUES(2,'Smartphone');
INSERT INTO monApp_categorie VALUES(3,'Sons');
INSERT INTO monApp_categorie VALUES(5,'Jeux Vidéos');
INSERT INTO monApp_categorie VALUES(7,'Informatique');
INSERT INTO monApp_categorie VALUES(8,'Ecouteurs');

DELETE FROM monApp_rayon;
INSERT INTO monApp_rayon VALUES(1,'Téléphonie');
INSERT INTO monApp_rayon VALUES(2,'Multimédia');
INSERT INTO monApp_rayon VALUES(4,'Mobilité');

DELETE FROM monApp_statut;
INSERT INTO monApp_statut VALUES(0,'Offline');
INSERT INTO monApp_statut VALUES(1,'OnLine');
INSERT INTO monApp_statut VALUES(2,'Out Of Stock');

DELETE FROM monApp_produit;
INSERT INTO monApp_produit VALUES(1,'ipods',59.99,8,'2025-08-13',0);
INSERT INTO monApp_produit VALUES(2,'iphone',1299.99,2,'2025-08-12',0);
INSERT INTO monApp_produit VALUES(3,'ipad',499.99,7,'2025-08-11',1);
INSERT INTO monApp_produit VALUES(7,'Switch II',359.99,5,'2025-08-13',1);
INSERT INTO monApp_produit VALUES(8,'Enceinte Bluetooth',199.99,3,'2025-08-15',1);
INSERT INTO monApp_produit VALUES(9,'iMac',1599.99,7,'2025-08-15',1);
INSERT INTO monApp_produit VALUES(10,'PlayStation 5',799.99,5,'2025-08-15',1);





