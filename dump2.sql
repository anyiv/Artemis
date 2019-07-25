BEGIN TRANSACTION;
INSERT INTO `usuario_tipouser` (codTipoUser,tipoUser,estatus) VALUES ('cli','Cliente','A'),
 ('atc','At Cliente','A'),
 ('gpqs','Gestor PQS','A'),
 ('tc','Técnico','A'),
 ('admin','Administrador','A'),
 ('ger','Gerente','A'),
 ('grec','Gestor Reclamos','A');
INSERT INTO `datos_externos_persona` (identificacion,nombre,apellido,direccion,telefono) VALUES ('1','David','Bowie','Londres','0242424242');
INSERT INTO `datos_externos_oficina` (codOficina,nombre,direccion,estatus) VALUES ('1','Matriz Barquisimeto','Leones','A');
INSERT INTO `datos_externos_empleado` (persona_ptr_id,cargo,estatus,codOficina_id) VALUES ('1','admin','A','1');
COMMIT;
