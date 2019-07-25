BEGIN TRANSACTION;
INSERT INTO `usuario_tipouser` (codTipoUser,tipoUser,estatus) VALUES ('cli','Cliente','A'),
 ('atc','At Cliente','A'),
 ('gpqs','Gestor PQS','A'),
 ('tc','Técnico','A'),
 ('admin','Administrador','A'),
 ('ger','Gerente','A'),
 ('grec','Gestor Reclamos','A');
INSERT INTO `datos_externos_oficina` (codOficina,nombre,direccion,estatus) VALUES ('1','Matriz Barquisimeto','Leones','A');
COMMIT;
