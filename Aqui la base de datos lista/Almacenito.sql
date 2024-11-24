-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         11.5.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para almacenito
CREATE DATABASE IF NOT EXISTS `almacenito` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_spanish_ci */;
USE `almacenito`;

-- Volcando estructura para tabla almacenito.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.auth_group: ~0 rows (aproximadamente)

-- Volcando estructura para tabla almacenito.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.auth_group_permissions: ~0 rows (aproximadamente)

-- Volcando estructura para tabla almacenito.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.auth_permission: ~40 rows (aproximadamente)
REPLACE INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add content type', 4, 'add_contenttype'),
	(14, 'Can change content type', 4, 'change_contenttype'),
	(15, 'Can delete content type', 4, 'delete_contenttype'),
	(16, 'Can view content type', 4, 'view_contenttype'),
	(17, 'Can add session', 5, 'add_session'),
	(18, 'Can change session', 5, 'change_session'),
	(19, 'Can delete session', 5, 'delete_session'),
	(20, 'Can view session', 5, 'view_session'),
	(21, 'Can add usuario', 6, 'add_usuario'),
	(22, 'Can change usuario', 6, 'change_usuario'),
	(23, 'Can delete usuario', 6, 'delete_usuario'),
	(24, 'Can view usuario', 6, 'view_usuario'),
	(25, 'Can add categoria', 7, 'add_categoria'),
	(26, 'Can change categoria', 7, 'change_categoria'),
	(27, 'Can delete categoria', 7, 'delete_categoria'),
	(28, 'Can view categoria', 7, 'view_categoria'),
	(29, 'Can add producto', 8, 'add_producto'),
	(30, 'Can change producto', 8, 'change_producto'),
	(31, 'Can delete producto', 8, 'delete_producto'),
	(32, 'Can view producto', 8, 'view_producto'),
	(33, 'Can add proveedor', 9, 'add_proveedor'),
	(34, 'Can change proveedor', 9, 'change_proveedor'),
	(35, 'Can delete proveedor', 9, 'delete_proveedor'),
	(36, 'Can view proveedor', 9, 'view_proveedor'),
	(37, 'Can add cliente', 10, 'add_cliente'),
	(38, 'Can change cliente', 10, 'change_cliente'),
	(39, 'Can delete cliente', 10, 'delete_cliente'),
	(40, 'Can view cliente', 10, 'view_cliente');

-- Volcando estructura para tabla almacenito.clientesapp_cliente
CREATE TABLE IF NOT EXISTS `clientesapp_cliente` (
  `nombre_cliente` varchar(50) NOT NULL,
  `ap_cliente` varchar(50) NOT NULL,
  `am_cliente` varchar(50) NOT NULL,
  `rut_cliente` varchar(12) NOT NULL,
  `direccion_cliente` varchar(80) NOT NULL,
  `numero_dir_cliente` varchar(10) NOT NULL,
  `fono_cliente` varchar(15) NOT NULL,
  `estado` varchar(30) NOT NULL,
  `fecha_pago` date DEFAULT NULL,
  PRIMARY KEY (`rut_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.clientesapp_cliente: ~2 rows (aproximadamente)
REPLACE INTO `clientesapp_cliente` (`nombre_cliente`, `ap_cliente`, `am_cliente`, `rut_cliente`, `direccion_cliente`, `numero_dir_cliente`, `fono_cliente`, `estado`, `fecha_pago`) VALUES
	('Maria Luisa', 'Arroyo', 'Ramos', '10954016-1', 'Pasaje 6 Sur', '336', '123456789', 'Sin pagos pendientes', NULL),
	('Edith', 'Barrera', 'Barrera', '69487823-3', 'Calle Los Castaños', '791', '123456789', 'Por crédito por pagar', '2024-12-31');

-- Volcando estructura para tabla almacenito.clientesapp_cliente_productos_adeudados
CREATE TABLE IF NOT EXISTS `clientesapp_cliente_productos_adeudados` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cliente_id` varchar(12) NOT NULL,
  `producto_id` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ClientesApp_cliente_prod_cliente_id_producto_id_24233ec8_uniq` (`cliente_id`,`producto_id`),
  KEY `ClientesApp_cliente__producto_id_378b0016_fk_gestionAp` (`producto_id`),
  CONSTRAINT `ClientesApp_cliente__cliente_id_f3be3bd1_fk_ClientesA` FOREIGN KEY (`cliente_id`) REFERENCES `clientesapp_cliente` (`rut_cliente`),
  CONSTRAINT `ClientesApp_cliente__producto_id_378b0016_fk_gestionAp` FOREIGN KEY (`producto_id`) REFERENCES `gestionapp_producto` (`codigo_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.clientesapp_cliente_productos_adeudados: ~0 rows (aproximadamente)

-- Volcando estructura para tabla almacenito.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` varchar(12) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `loginapp_usuario` (`rut`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.django_admin_log: ~10 rows (aproximadamente)
REPLACE INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2024-11-08 18:42:52.905772', '10100', 'Lacteos', 1, '[{"added": {}}]', 7, '21557880-1'),
	(2, '2024-11-08 18:42:55.358022', '10100', 'Lacteos', 2, '[]', 7, '21557880-1'),
	(3, '2024-11-08 18:43:05.792307', '10101', 'Gaseosas', 1, '[{"added": {}}]', 7, '21557880-1'),
	(4, '2024-11-08 18:43:33.674547', '10102', 'Fiambre', 1, '[{"added": {}}]', 7, '21557880-1'),
	(5, '2024-11-08 18:44:00.996178', '10103', 'Legrumbres y granos', 1, '[{"added": {}}]', 7, '21557880-1'),
	(6, '2024-11-08 18:51:01.756635', '10104', 'Agua', 1, '[{"added": {}}]', 7, '21557880-1'),
	(7, '2024-11-08 18:51:39.990267', '10105', 'Articulos de aseo', 1, '[{"added": {}}]', 7, '21557880-1'),
	(8, '2024-11-08 18:59:52.066791', '10200', 'Embotelladora Andina S.A', 1, '[{"added": {}}]', 9, '21557880-1'),
	(9, '2024-11-08 19:22:15.439541', '1', 'Coca-Cola 1.25L', 1, '[{"added": {}}]', 8, '21557880-1'),
	(10, '2024-11-12 18:20:23.414335', '10201', 'Soprole', 1, '[{"added": {}}]', 9, '21557880-1');

-- Volcando estructura para tabla almacenito.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.django_content_type: ~10 rows (aproximadamente)
REPLACE INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(10, 'ClientesApp', 'cliente'),
	(4, 'contenttypes', 'contenttype'),
	(7, 'gestionApp', 'categoria'),
	(8, 'gestionApp', 'producto'),
	(9, 'gestionApp', 'proveedor'),
	(6, 'loginApp', 'usuario'),
	(5, 'sessions', 'session');

-- Volcando estructura para tabla almacenito.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.django_migrations: ~39 rows (aproximadamente)
REPLACE INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'loginApp', '0001_initial', '2024-11-01 02:00:21.373221'),
	(2, 'contenttypes', '0001_initial', '2024-11-01 02:00:21.430666'),
	(3, 'admin', '0001_initial', '2024-11-01 02:00:21.536178'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-01 02:00:21.544172'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-01 02:00:21.554276'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-01 02:00:21.639138'),
	(7, 'auth', '0001_initial', '2024-11-01 02:00:21.917979'),
	(8, 'auth', '0002_alter_permission_name_max_length', '2024-11-01 02:00:21.963518'),
	(9, 'auth', '0003_alter_user_email_max_length', '2024-11-01 02:00:21.977277'),
	(10, 'auth', '0004_alter_user_username_opts', '2024-11-01 02:00:21.991356'),
	(11, 'auth', '0005_alter_user_last_login_null', '2024-11-01 02:00:22.008480'),
	(12, 'auth', '0006_require_contenttypes_0002', '2024-11-01 02:00:22.012480'),
	(13, 'auth', '0007_alter_validators_add_error_messages', '2024-11-01 02:00:22.026869'),
	(14, 'auth', '0008_alter_user_username_max_length', '2024-11-01 02:00:22.037866'),
	(15, 'auth', '0009_alter_user_last_name_max_length', '2024-11-01 02:00:22.049868'),
	(16, 'auth', '0010_alter_group_name_max_length', '2024-11-01 02:00:22.081419'),
	(17, 'auth', '0011_update_proxy_permissions', '2024-11-01 02:00:22.101421'),
	(18, 'auth', '0012_alter_user_first_name_max_length', '2024-11-01 02:00:22.115915'),
	(19, 'gestionApp', '0001_initial', '2024-11-01 02:00:22.134809'),
	(20, 'gestionApp', '0002_categoria_producto_proveedor_delete_proyecto_and_more', '2024-11-01 02:00:22.264411'),
	(21, 'gestionApp', '0003_remove_categoria_descripcion_and_more', '2024-11-01 02:00:22.836263'),
	(22, 'loginApp', '0002_alter_usuario_email_alter_usuario_rol', '2024-11-01 02:00:22.896039'),
	(23, 'loginApp', '0003_alter_usuario_rol', '2024-11-01 02:00:22.925487'),
	(24, 'loginApp', '0004_alter_usuario_rut', '2024-11-01 02:00:23.511462'),
	(25, 'loginApp', '0005_usuario_groups_usuario_is_active_usuario_is_staff_and_more', '2024-11-01 02:00:23.916786'),
	(26, 'sessions', '0001_initial', '2024-11-01 02:00:23.978362'),
	(27, 'gestionApp', '0004_alter_producto_categoria_and_more', '2024-11-08 18:34:25.884800'),
	(28, 'loginApp', '0006_alter_usuario_email_alter_usuario_fono', '2024-11-08 18:34:25.933515'),
	(29, 'gestionApp', '0005_alter_proveedor_fono', '2024-11-08 18:58:31.088343'),
	(30, 'loginApp', '0007_alter_usuario_fono_alter_usuario_last_login', '2024-11-08 18:58:31.282720'),
	(31, 'gestionApp', '0006_alter_categoria_codigo_categoria_and_more', '2024-11-08 19:18:03.039603'),
	(32, 'gestionApp', '0007_alter_producto_codigo_producto_and_more', '2024-11-14 22:14:10.950952'),
	(33, 'loginApp', '0008_alter_usuario_last_login', '2024-11-14 22:14:10.966279'),
	(34, 'gestionApp', '0008_categoria_descripcion_categoria_and_more', '2024-11-15 00:27:45.517307'),
	(35, 'loginApp', '0009_alter_usuario_is_active', '2024-11-15 01:49:02.406260'),
	(36, 'loginApp', '0010_alter_usuario_is_active_alter_usuario_last_login', '2024-11-15 01:50:45.179873'),
	(37, 'loginApp', '0011_alter_usuario_last_login_alter_usuario_password_and_more', '2024-11-15 19:09:37.300459'),
	(38, 'ClientesApp', '0001_initial', '2024-11-19 18:36:30.171886'),
	(39, 'ClientesApp', '0002_remove_cliente_producto_cliente_fecha_pago_and_more', '2024-11-20 21:00:32.523300');

-- Volcando estructura para tabla almacenito.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.django_session: ~8 rows (aproximadamente)
REPLACE INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('7zdxy5rb1ivjm1ubqx46sj9t7ygqcxt3', '.eJxVzDkOwjAQheG7uAZrPI43yvScwfIygwMokbJUiLtDpBRQ_997LxHTtra4LTTHoYqLQGWM8x7OSpx-Y07lQeMu6j2Nt0mWaVznIcudyKMu8jpVevaH_TtoaWnftU26mIAFfHBZG4ZqbWHF7JERyXVaZwDLKlfnwYYAyISUCGrovAbx_gAw4zlI:1t9YAw:N5xulmQfYw3VQ-XAhajTby63mprebzCrkKGXOnZC-qc', '2024-11-22 23:13:58.494052'),
	('8twdjf57a1uidag2kz2de3yk4y8g9doi', '.eJxVzEsOwiAUheG9MDaEy6OAQ-eugVy4IFUDSWlHxr1rkw50_H_nvFjAba1hG3kJM7Ezk2CMdU4AO_22iOmR2w7oju3WeeptXebId8KPOvi1U35eDvt3UHHU7xoVSpOcUlMq3gsPvgggibpEi5aKzDBpiB6weNRJOaCcCMjqDFJIx94fHAw5mg:1tBNgO:5o2vxmN-nxtLJFLhQClHfsDIK2ZP-XW8MH0ERm2eKgM', '2024-11-28 00:26:00.341144'),
	('8xgcf80x5rr45hv9ysma17whn4e88efv', '.eJxVzLsOwjAMheF3yYwiJ6kbh5GdZ6ic2CUF1Eq9TIh3h0odYP6_c16m422t3bbo3A1izsY7xEgEzpx-W-by0HEHcufxNtkyjes8ZLsTe9TFXifR5-WwfweVl_pdh0KKjUgM6htQiCIJpMc-EAK3CKTcS4yZWEPiUggDtMlndpiUvHl_ACXcObM:1t84zU:ZjAQl-HDckpjWLjxtbbaVDu_r8Dyz5IwHMOm2QaiSZY', '2024-11-18 21:52:04.508583'),
	('e9yx2y3jnxjeltofa8zzsz8v7vkj9t23', '.eJxVzEEOwiAQheG7sDYEWgYGl-49AxnKIFUDSWlXxrtrky50_X_vvUSgbS1h67yEOYmzGDSAQ1RanH5bpOnBdQfpTvXW5NTqusxR7kQetctrS_y8HPbvoFAv33Vm0N4RWvQ6ugwGwSJFH63RIyWbSSlm7zDTaAY1jJyTV4A6Wx8nA-L9AQ1-OTQ:1tDrUx:PwYKJRtso44oVB_GfEmzJlTNby160lf94M8Ec6Hjqhs', '2024-12-04 20:40:27.192043'),
	('hzqnv1x14yolrz1dhjwlqoavlrf9trx4', '.eJxVzEEOwiAQheG7sDYEWgYGl-49AxnKIFUDSWlXxrtrky50_X_vvUSgbS1h67yEOYmzGDSAQ1RanH5bpOnBdQfpTvXW5NTqusxR7kQetctrS_y8HPbvoFAv33Vm0N4RWvQ6ugwGwSJFH63RIyWbSSlm7zDTaAY1jJyTV4A6Wx8nA-L9AQ1-OTQ:1tDnj9:TOo1gc7y73Sv1J6jOCcLY2HwurF3NSpgT4fBR79mEGo', '2024-12-04 16:38:51.750674'),
	('o2nxbpdzdz4nrnl7nszlsagr7nafnln9', '.eJxVzEsOwiAUheG9MDaEy6OAQ-eugVy4IFUDSWlHxr1rkw50_H_nvFjAba1hG3kJM7Ezk2CMdU4AO_22iOmR2w7oju3WeeptXebId8KPOvi1U35eDvt3UHHU7xoVSpOcUlMq3gsPvgggibpEi5aKzDBpiB6weNRJOaCcCMjqDFJIx94fHAw5mg:1tAz5l:sqLR6KkTk08b3FXjYJqnVAUV6022jdH01Fourxh41IE', '2024-11-26 22:10:33.766436'),
	('rd74vft3hg5hnwzsgx8an8yjfwwogb4t', '.eJxVzEsOwiAUheG9MDaEy6OAQ-eugVy4IFUDSWlHxr1rkw50_H_nvFjAba1hG3kJM7Ezk2CMdU4AO_22iOmR2w7oju3WeeptXebId8KPOvi1U35eDvt3UHHU7xoVSpOcUlMq3gsPvgggibpEi5aKzDBpiB6weNRJOaCcCMjqDFJIx94fHAw5mg:1tBlfN:Qlh_Qjd5QCXUdQ8ZUougzs6tZ893BV4nvmSiHBS1VrU', '2024-11-29 02:02:33.390804'),
	('u6sgq2grib2yos0z9i0lp6qstxson6hc', '.eJxVzEsOwiAUheG9MDaEy6OAQ-eugVy4IFUDSWlHxr1rkw50_H_nvFjAba1hG3kJM7Ezk2CMdU4AO_22iOmR2w7oju3WeeptXebId8KPOvi1U35eDvt3UHHU7xoVSpOcUlMq3gsPvgggibpEi5aKzDBpiB6weNRJOaCcCMjqDFJIx94fHAw5mg:1tAvKC:-ZLnDOOg-IZTiMvpPbXi6ESodB1xq4hfNP8Z8Md9_zs', '2024-11-26 18:09:12.908216');

-- Volcando estructura para tabla almacenito.gestionapp_categoria
CREATE TABLE IF NOT EXISTS `gestionapp_categoria` (
  `codigo_categoria` int(11) NOT NULL,
  `nombre_categoria` varchar(100) NOT NULL,
  `descripcion_categoria` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`codigo_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.gestionapp_categoria: ~4 rows (aproximadamente)
REPLACE INTO `gestionapp_categoria` (`codigo_categoria`, `nombre_categoria`, `descripcion_categoria`) VALUES
	(10100, 'Lacteos', 'Productos obtenidos mediante cualquier elaboración de la leche, que puede contener aditivos alimentarios y otros ingredientes funcionalmente necesarios para la elaboración'),
	(10101, 'Gaseosas', 'Gaseosas, o bebidas carbonatadas. es una bebida saborizada, efervescente (carbonatada) y sin alcohol. Estas bebidas suelen consumirse frías, para ser más refrescantes y para evitar la pérdida de dióxido de carbono, que le otorga la efervescencia.'),
	(10102, 'Fiambre', NULL),
	(10103, 'Legrumbres y granos', NULL);

-- Volcando estructura para tabla almacenito.gestionapp_producto
CREATE TABLE IF NOT EXISTS `gestionapp_producto` (
  `codigo_producto` varchar(5) NOT NULL,
  `nombre_producto` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `stock` int(11) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `categoria_id` int(11) NOT NULL,
  `proveedor_id` int(11) NOT NULL,
  PRIMARY KEY (`codigo_producto`),
  KEY `gestionApp_producto_categoria_id_ed8fe162` (`categoria_id`),
  KEY `gestionApp_producto_proveedor_id_8c43ed9e` (`proveedor_id`),
  CONSTRAINT `gestionApp_producto_categoria_id_ed8fe162_fk_gestionAp` FOREIGN KEY (`categoria_id`) REFERENCES `gestionapp_categoria` (`codigo_categoria`),
  CONSTRAINT `gestionApp_producto_proveedor_id_8c43ed9e_fk` FOREIGN KEY (`proveedor_id`) REFERENCES `gestionapp_proveedor` (`codigo_proveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.gestionapp_producto: ~4 rows (aproximadamente)
REPLACE INTO `gestionapp_producto` (`codigo_producto`, `nombre_producto`, `descripcion`, `stock`, `precio`, `categoria_id`, `proveedor_id`) VALUES
	('10001', 'Coca-Cola 2L', 'Coca-Cola clásica retornable plástica de 2L', 20, 1250.00, 10101, 10200),
	('10003', 'Yoghurt Batido Frutilla bolsa 1Kg', 'Yoghurt Soprole Batido sabor frutilla bolsa 1Kg', 33, 2300.00, 10100, 10203),
	('10004', 'Mantequilla 250G', 'Mantequilla Soprole 250G en barra', 34, 2000.00, 10100, 10203),
	('10005', 'Leche blanca semidescremada 1L', 'Leche Soprole semidescremada 1L', 21, 2550.00, 10100, 10203);

-- Volcando estructura para tabla almacenito.gestionapp_proveedor
CREATE TABLE IF NOT EXISTS `gestionapp_proveedor` (
  `codigo_proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `razon_social_proveedor` varchar(50) NOT NULL,
  `empresa` varchar(100) NOT NULL,
  `fono` bigint(20) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=10204 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.gestionapp_proveedor: ~3 rows (aproximadamente)
REPLACE INTO `gestionapp_proveedor` (`codigo_proveedor`, `razon_social_proveedor`, `empresa`, `fono`, `correo`, `direccion`) VALUES
	(10200, 'Embotelladora Andina S.A', 'Coca-cola Company.', 6003603601, 'Cocacola.chile@cocacola.cl', 'Av. Miraflores 9153 - Renca'),
	(10202, 'CCU', 'CCU Company', 569946578321, 'ccu.chile@ccu.cl', 'Vitacura 2670, Las Condes. Santiago Chile'),
	(10203, 'Soprole', 'Soprole S.A.', 56931820387, 'Soprolesa.chile@soprole.cl', 'Av. Miraflores 9153 - Renca');

-- Volcando estructura para tabla almacenito.loginapp_usuario
CREATE TABLE IF NOT EXISTS `loginapp_usuario` (
  `nombre` varchar(50) NOT NULL,
  `ap_p` varchar(50) NOT NULL,
  `ap_m` varchar(50) NOT NULL,
  `fono` bigint(20) DEFAULT NULL,
  `email` varchar(250) NOT NULL,
  `rut` varchar(12) NOT NULL,
  `rol` varchar(12) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`rut`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.loginapp_usuario: ~4 rows (aproximadamente)
REPLACE INTO `loginapp_usuario` (`nombre`, `ap_p`, `ap_m`, `fono`, `email`, `rut`, `rol`, `password`, `is_active`, `is_staff`, `is_superuser`, `last_login`) VALUES
	('Ignacio', 'Faundez', 'Saes', 56922314563, 'ignacio.faundez05@inacapmail.cl', '19', 'Cajero', 'pbkdf2_sha256$870000$AG8HdGBeoXLyG4dAnDd6vd$5NI+nv5HfCsb1R3QwOgKAt/FM0FZoSMZ7yCWCsqhGc0=', 1, 0, 0, '2024-11-20 15:41:13.771900'),
	('', '', '', NULL, '', '21557880-1', 'Admin', 'pbkdf2_sha256$870000$JRQJk5EgB4Wq8cNmEYSjHw$hR9MP58Wnhro4s1+BHpCgvFIo3dDIqdCTg7C8r4Wmoc=', 1, 1, 1, '2024-11-12 18:17:41.261879'),
	('Guillermo', 'Flores', 'Zamorano', 56931820387, 'guillermo.240gfz@gmail.com', '215578801', 'Admin', 'pbkdf2_sha256$870000$fC5yoeL4vzsX9VhgOq1TEH$XqfQZD14PA6X+jW34q19mVDUwI87pIKiJLyhgxzfy44=', 1, 0, 0, '2024-11-20 20:40:27.189185'),
	('Benjamin', 'Cejas', 'Jorquera', 569223145639, 'benjamin.cejas@inacapmail.cl', '216311434', 'Admin', 'pbkdf2_sha256$870000$epGndLvvlpxSvU146kPMTs$F2RHCo9Xn7q4YIab4IWh+3+Y5DgHMC83IMwhCcWk48E=', 1, 0, 0, '2024-11-19 17:52:10.933766');

-- Volcando estructura para tabla almacenito.loginapp_usuario_groups
CREATE TABLE IF NOT EXISTS `loginapp_usuario_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usuario_id` varchar(12) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `loginApp_usuario_groups_usuario_id_group_id_0a621ccd_uniq` (`usuario_id`,`group_id`),
  KEY `loginApp_usuario_groups_group_id_fd7fc3da_fk_auth_group_id` (`group_id`),
  CONSTRAINT `loginApp_usuario_gro_usuario_id_1eec58b0_fk_loginApp_` FOREIGN KEY (`usuario_id`) REFERENCES `loginapp_usuario` (`rut`),
  CONSTRAINT `loginApp_usuario_groups_group_id_fd7fc3da_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.loginapp_usuario_groups: ~0 rows (aproximadamente)

-- Volcando estructura para tabla almacenito.loginapp_usuario_user_permissions
CREATE TABLE IF NOT EXISTS `loginapp_usuario_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usuario_id` varchar(12) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `loginApp_usuario_user_pe_usuario_id_permission_id_3ffa32eb_uniq` (`usuario_id`,`permission_id`),
  KEY `loginApp_usuario_use_permission_id_12c2e78d_fk_auth_perm` (`permission_id`),
  CONSTRAINT `loginApp_usuario_use_permission_id_12c2e78d_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `loginApp_usuario_use_usuario_id_f0806dc5_fk_loginApp_` FOREIGN KEY (`usuario_id`) REFERENCES `loginapp_usuario` (`rut`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla almacenito.loginapp_usuario_user_permissions: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
