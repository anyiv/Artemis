BEGIN TRANSACTION;
INSERT INTO `usuario_user` (password,last_login,nombreUsuario,correo,is_staff,is_superuser,estatus,codTipoUser_id,idCliente_id,idEmpleado_id,foto) VALUES ('pbkdf2_sha256$120000$KKBPpAxLepS1$Qq08dvTbs6kk1cVUKE29sCO5P1CQEbgxphI3rkhUKsw=','2019-07-25 18:20:21.949341','admin','administrador@artemis.com',1,1,'A','admin',NULL,'1','usuarios/fotos/Legado-Bowie.jpg'),
 ('pbkdf2_sha256$120000$09M1SgJPgyff$jAM8o5gklcpgHSRz8g7dXOyJ8R0iL2Y0dGB1+prUwf4=','2019-07-25 18:18:43.485209','cliente','lisbethsalander@yahoo.net',0,0,'A','cli','1',NULL,'usuarios/fotos/DT.jpg'),
 ('pbkdf2_sha256$120000$dLyUmgqBFUTr$O5sNNPNMMclVNrFRYcVrcBt1mATNWytpqs6AQXga5jI=','2019-07-25 15:41:08.509900','atencioncli','natromanoff@vormir.com',0,0,'A','atc',NULL,'2','usuarios/fotos/Nat.jpeg'),
 ('pbkdf2_sha256$120000$KpSbeo4JXilM$0+KN64Ox+OtqkodeJzsL2cSf1Q6ZjiaGvkuNOXjkTrs=','2019-07-25 15:43:32.702798','gestorpqs','jasonmomoa@artemis.com',0,0,'A','gpqs',NULL,'3','usuarios/fotos/gettyimages-1131981370.jpg'),
 ('pbkdf2_sha256$120000$DufGq9iRk9PE$vtY31pecbP+NWud1+5KBJADrv4IXijrFVKRPc9M/0lY=','2019-07-25 15:44:51.027920','tecnico','lunalg@elquisquilloso.com',0,0,'A','tc',NULL,'4','usuarios/fotos/luna.jpg'),
 ('pbkdf2_sha256$120000$LOvWbL2djkK6$K/wDtJZH/Qo17Tf93H/DGp6uZo5zkhDlbF5KJ+xZrm8=','2019-07-25 15:46:35.455217','gerente','edgarramirez@artemis.com',0,0,'A','ger',NULL,'5','usuarios/fotos/153358.jpg'),
 ('pbkdf2_sha256$120000$JgK5lYRPXuWj$VqDrjyhoZ6bvkyf6TlIBlJskrEIHwBZWKqkB80QBc/w=','2019-07-25 15:42:22.012921','gestorr','tsonga@artemis.com',0,0,'A','grec',NULL,'6','usuarios/fotos/tsonga.jpeg'),
 ('daenerys',NULL,'daenerystargaryen','ladany@westeroosimail.com',0,0,'A','cli','7',NULL,'usuarios/fotos/default.jpg');
INSERT INTO `usuario_tipouser` (codTipoUser,tipoUser,estatus) VALUES ('cli','Cliente','A'),
 ('atc','At Cliente','A'),
 ('gpqs','Gestor PQS','A'),
 ('tc','Técnico','A'),
 ('admin','Administrador','A'),
 ('ger','Gerente','A'),
 ('grec','Gestor Reclamos','A');
INSERT INTO `resp_predefinida_respuestapredefinida` (descripcion,categoria,contUso,estatus,codRespuestaP) VALUES ('Probando lo que es una petición','pet',0,'A','REP-0000'),
 ('Muchas gracias por tu queja, la escuchamos, saludos.','que',0,'A','REP-0001');
INSERT INTO `reclamo_categoria` (codCategoria,nombre,descripcion,estatus) VALUES ('CTR-0000','Mal servicio','Mal servicio','A');
INSERT INTO `datos_externos_oficina` (codOficina,nombre,direccion,estatus) VALUES ('OFI-0000','Matriz Barquisimeto','Leones','A');
INSERT INTO `datos_externos_empleado` (identificacion,nombre,apellido,direccion,telefono,estatus,codOficina_id,cargo) VALUES ('1','David','Bowie','Londres','04122222222','A','OFI-0000','Gerente de Informática'),
 ('2','Natasha','Romanoff','Vormir','02125552124','A','OFI-0000','Directora de Atención al Cliente'),
 ('3','Jason','Momoa','Hawaii','04242424242','A','OFI-0000','Gestor de PQS'),
 ('4','Luna','Lovegood','Hogwarts','04242424242','A','OFI-0000','Jefe de Técnicos'),
 ('5','Edgar','Ramírez','Hollywood','04242424242','A','OFI-0000','Presidente de la Compañía'),
 ('6','Jo-Wilfried','Tsonga','Francia','04242424242','A','OFI-0000','Jefe de Reclamos');
INSERT INTO `datos_externos_cliente` (identificacion,nombre,apellido,direccion,telefono,estatus) VALUES ('1','Lisbeth','Salander','UNKNOWN','UNKNOWN','A'),
 ('7','Daenerys','Targaryen','Poniente','04242424242','A');
COMMIT;
