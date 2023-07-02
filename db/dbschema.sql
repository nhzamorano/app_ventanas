BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "precios_aluminio" (
	"id"	INTEGER,
	"type_al"	TEXT NOT NULL,
	"cost"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "precios_vidrio" (
	"id"	INTEGER,
	"type_vid"	TEXT NOT NULL,
	"cost"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "modelos_ventana" (
	"id"	INTEGER,
	"modelo"	TEXT NOT NULL,
	"paneles"	INTEGER NOT NULL DEFAULT 1,
	"chapas"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "clients" (
	"nit"	INTEGER NOT NULL UNIQUE,
	"client_name"	TEXT NOT NULL UNIQUE,
	"direccion"	TEXT NOT NULL,
	"telefono1"	TEXT NOT NULL,
	"telefono2"	TEXT,
	"contacto"	TEXT NOT NULL,
	PRIMARY KEY("nit")
);
INSERT INTO "precios_aluminio" ("id","type_al","cost") VALUES (1,'Lacado Brillante',54200),
 (2,'Pulido',50700),
 (3,'Lacado Mate',53600),
 (4,'Anodizado',57300);
INSERT INTO "precios_vidrio" ("id","type_vid","cost") VALUES (1,'Azul',12.75),
 (2,'Bronce',9.15),
 (3,'Transparente',8.25);
INSERT INTO "modelos_ventana" ("id","modelo","paneles","chapas") VALUES (1,'O',1,0),
 (2,'XO',2,1),
 (3,'OXO',3,1),
 (4,'OXXO',4,2);
INSERT INTO "clients" ("nit","client_name","direccion","telefono1","telefono2","contacto") VALUES (800162658,'CONSTRUCTORA PICAPIEDRA','Calle 15 No. 26 - 27','314 826 16 98','316 443 23 89','Pedro Picapiedra'),
 (800348921,'CONSTRUCTORA LA FLORESTA','Carrera 6 No. 10 - 47','318 263 06 89','315 443 23 89','Coronel'),
 (860162658,'CONSTRUCTORA HERRERA & HIJOS','Carrera 25 No. 70 - 47','324 268 16 98','315 443 23 89','Rony Herrera'),
 (900162658,'CONSTRUCTORA MARMOL Y CIA','Avenida 5 No. 66 - 27','340 826 36 98','316 443 23 89','Pablo Marmol');
COMMIT;
