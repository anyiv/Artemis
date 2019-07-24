BEGIN TRANSACTION;
INSERT INTO `usuario_user` (id,password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined,birth_date,phone,last_access,type_u_id,address,city) VALUES (2,'pbkdf2_sha256$150000$jANE8Ld8MN0e$exrHgaam9o0O3xrUT56USZU+tK6NzsCBQoQog78TEyM=','2019-07-24 14:38:34.750131',1,'admin','David','Bowie','admin@artemis.com',1,1,'2019-07-14 19:34:16-04','','4266657272','2019-07-14 19:34:16-04','admin','London, UK','Suffragette City'),
 (3,'pbkdf2_sha256$120000$09M1SgJPgyff$jAM8o5gklcpgHSRz8g7dXOyJ8R0iL2Y0dGB1+prUwf4=','2019-07-24 04:03:36.916395',0,'cliente','Helenio','Herrera','helenioherrera@infoglobal.g2a',0,1,'2019-07-15 10:39:04-04','','4266657272','2019-07-14 19:34:16-04','cli','Urb. La Ruezga Norte Vda 15 Casa 47','Barquisimeto'),
 (4,'pbkdf2_sha256$120000$dLyUmgqBFUTr$O5sNNPNMMclVNrFRYcVrcBt1mATNWytpqs6AQXga5jI=','2019-07-24 04:04:16.207115',0,'atencioncli','Light','Yagami','lightyagami@deathnote.com',0,1,'2019-07-15 10:40:11-04','','4266657272','2019-07-15 10:43:53-04','atc','atc',''),
 (5,'pbkdf2_sha256$150000$veVrB6qIEiCo$88V5xeaVK0RSR4AwJJiMdWKODrOZpm1Qp2RCTCZidyo=','2019-07-19 12:53:00.739879-04',0,'gestorr','Frank','Ocean','frankocean@itsmybirthday.com',0,1,'2019-07-15 10:40:48-04','','4266657272','2019-07-15 10:43:53-04','grec','Calle 17 con carrera 17 nro 17-7','Calle 17 con carrera 17 nro 17-7'),
 (6,'pbkdf2_sha256$150000$yJfoETzJerUX$bRdtK6HEl+yHBjtckZbeF7EaMr3tTvxj12363Prexns=','2019-07-21 19:55:46.962154',0,'gestorpqs','Ashton','Kutcher','akutcher@gmail.com',0,1,'2019-07-15 10:41:33-04','','4266657272','2019-07-15 10:43:53-04','gpqs','gpqs',''),
 (7,'pbkdf2_sha256$150000$GPtnc9XkzBvo$XxKHX2/dlYwLyGFsYvbFhcQDixpioylRpg8/rCmPn6M=','2019-07-18 00:21:38.147804-04',0,'tecnico','Romeo','Santos','romeosantos@labachataapesta.com',0,1,'2019-07-15 10:42:22-04','','4266657272','2019-07-15 10:43:53-04','tc','tc',''),
 (8,'pbkdf2_sha256$150000$mdZft4KtvG7F$xmgehMy903XttezOXSkcdldnixs/gZ1AyDO9BEYaGBc=','2019-07-17 11:02:11.401016-04',0,'gerente','Gregory','House','gregoryhouse@gmail.com',0,1,'2019-07-15 10:43:53-04','','4266657272','2019-07-15 10:43:53-04','ger','ger','');
INSERT INTO `usuario_tipo_usuario` (codigo,tipo_usuario,descripcion) VALUES ('cli','Cliente','Cliente Registrado'),
 ('atc','At Cliente','Atencion al Cliente'),
 ('gpqs','Gestor PQS','Gestor de PQS'),
 ('tc','Técnico','Soporte Técnico'),
 ('admin','Admin','Admin del Sistema'),
 ('ger','Gerente','Gerente'),
 ('grec','G Reclamos','Gestor de Reclamos');
INSERT INTO `reclamo_categoria` (codCategoria,descripcion,estatus,nombre) VALUES ('CTR-0000','Se registra un cobro incorrecto al usuario','A','Cobro Incorrecto'),
 ('CTR-0001','La velocidad de internet está siendo deficiente, mucho más lenta de lo habitual','A','Velocidad de internet deficiente'),
 ('CTR-0002','Se cae a cada rato','A','Señal de TV deficiente');
COMMIT;
