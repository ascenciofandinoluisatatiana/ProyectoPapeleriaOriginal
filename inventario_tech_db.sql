-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Servidor: mysql
-- Tiempo de generación: 23-09-2026 a las 16:24:56
-- Versión del servidor: 8.0.46
-- Versión de PHP: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inventario_tech_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(2, 'Administradores'),
(4, 'Consultores'),
(3, 'Gestores'),
(1, 'Técnicos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(2, 1, 37),
(3, 1, 38),
(4, 1, 39),
(1, 1, 40),
(61, 2, 1),
(62, 2, 2),
(63, 2, 3),
(64, 2, 4),
(65, 2, 5),
(66, 2, 6),
(67, 2, 7),
(68, 2, 8),
(69, 2, 9),
(70, 2, 10),
(71, 2, 11),
(72, 2, 12),
(73, 2, 13),
(74, 2, 14),
(75, 2, 15),
(76, 2, 16),
(77, 2, 17),
(78, 2, 18),
(79, 2, 19),
(80, 2, 20),
(81, 2, 21),
(82, 2, 22),
(83, 2, 23),
(84, 2, 24),
(85, 2, 25),
(86, 2, 26),
(87, 2, 27),
(88, 2, 28),
(89, 2, 29),
(90, 2, 30),
(91, 2, 31),
(92, 2, 32),
(93, 2, 33),
(94, 2, 34),
(95, 2, 35),
(96, 2, 36),
(97, 2, 37),
(98, 2, 38),
(99, 2, 39),
(100, 2, 40),
(101, 2, 41),
(102, 2, 42),
(103, 2, 43),
(104, 2, 44),
(105, 2, 45),
(106, 2, 46),
(107, 2, 47),
(108, 2, 48),
(109, 2, 49),
(110, 2, 50),
(111, 2, 51),
(112, 2, 52),
(113, 2, 53),
(114, 2, 54),
(115, 2, 55),
(116, 2, 56),
(19, 3, 1),
(20, 3, 2),
(21, 3, 4),
(22, 3, 5),
(23, 3, 6),
(24, 3, 8),
(25, 3, 9),
(26, 3, 10),
(27, 3, 12),
(28, 3, 13),
(29, 3, 14),
(30, 3, 16),
(31, 3, 17),
(32, 3, 18),
(33, 3, 20),
(34, 3, 21),
(35, 3, 22),
(36, 3, 24),
(37, 3, 25),
(38, 3, 26),
(39, 3, 28),
(40, 3, 29),
(41, 3, 30),
(42, 3, 32),
(43, 3, 33),
(44, 3, 34),
(45, 3, 36),
(46, 3, 37),
(47, 3, 38),
(48, 3, 40),
(49, 3, 41),
(50, 3, 42),
(51, 3, 44),
(52, 3, 45),
(53, 3, 46),
(54, 3, 48),
(55, 3, 49),
(56, 3, 50),
(57, 3, 52),
(58, 3, 53),
(59, 3, 54),
(60, 3, 56),
(6, 4, 4),
(8, 4, 8),
(10, 4, 12),
(12, 4, 16),
(14, 4, 20),
(17, 4, 24),
(18, 4, 28),
(5, 4, 32),
(7, 4, 36),
(9, 4, 40),
(11, 4, 44),
(13, 4, 48),
(15, 4, 52),
(16, 4, 56);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
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
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Categoría', 7, 'add_categoria'),
(26, 'Can change Categoría', 7, 'change_categoria'),
(27, 'Can delete Categoría', 7, 'delete_categoria'),
(28, 'Can view Categoría', 7, 'view_categoria'),
(29, 'Can add Ubicación', 8, 'add_ubicacion'),
(30, 'Can change Ubicación', 8, 'change_ubicacion'),
(31, 'Can delete Ubicación', 8, 'delete_ubicacion'),
(32, 'Can view Ubicación', 8, 'view_ubicacion'),
(33, 'Can add Estado', 9, 'add_estado'),
(34, 'Can change Estado', 9, 'change_estado'),
(35, 'Can delete Estado', 9, 'delete_estado'),
(36, 'Can view Estado', 9, 'view_estado'),
(37, 'Can add Activo', 10, 'add_activo'),
(38, 'Can change Activo', 10, 'change_activo'),
(39, 'Can delete Activo', 10, 'delete_activo'),
(40, 'Can view Activo', 10, 'view_activo'),
(41, 'Can add Historial de Movimiento', 11, 'add_historialmovimiento'),
(42, 'Can change Historial de Movimiento', 11, 'change_historialmovimiento'),
(43, 'Can delete Historial de Movimiento', 11, 'delete_historialmovimiento'),
(44, 'Can view Historial de Movimiento', 11, 'view_historialmovimiento'),
(45, 'Can add Mantenimiento', 12, 'add_mantenimiento'),
(46, 'Can change Mantenimiento', 12, 'change_mantenimiento'),
(47, 'Can delete Mantenimiento', 12, 'delete_mantenimiento'),
(48, 'Can view Mantenimiento', 12, 'view_mantenimiento'),
(49, 'Can add Perfil', 13, 'add_perfil'),
(50, 'Can change Perfil', 13, 'change_perfil'),
(51, 'Can delete Perfil', 13, 'delete_perfil'),
(52, 'Can view Perfil', 13, 'view_perfil'),
(53, 'Can add Log de Auditoría', 14, 'add_log'),
(54, 'Can change Log de Auditoría', 14, 'change_log'),
(55, 'Can delete Log de Auditoría', 14, 'delete_log'),
(56, 'Can view Log de Auditoría', 14, 'view_log');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$1000000$OvLulYseVzEBGAJenq95sW$+zrtNaDNA+syoo6G61uetyv0fDmfw/s7BwgOVoS7qlo=', '2026-09-23 01:43:50.763880', 1, 'admin', '', '', 'ascenciofandinoluisatatiana10@gmail.com', 1, 1, '2026-08-26 00:26:04.332360'),
(2, 'pbkdf2_sha256$1000000$XMuiymuUgzwXQg25DPIxQb$Z8iRBTHWWYHbiFb3+3fv9gg0Rb+UIVdQG6ZnwCAUh1E=', '2026-09-23 00:09:00.327167', 1, 'root', '', '', 'admin@sena.edu.co', 1, 1, '2026-09-11 00:28:35.944206'),
(3, 'pbkdf2_sha256$1000000$HObSUPbQnMbSX6vH8YHu07$PhyTKUmvXOtmqZc0DZC3CNm27LI2jgJBaMbT73faVmI=', '2026-09-11 00:39:39.084681', 0, 'tecnico1', 'Juan', 'Pérez', 'tecnico1@sena.edu.co', 0, 1, '2026-09-11 00:29:16.500910'),
(4, 'pbkdf2_sha256$1000000$cgGpRH5h3e6V7I0f46MGr8$uFjTRi9fUY4AunU8NK6JA0NJ6qJS4hcVMCYbyU8xdpU=', '2026-09-23 00:04:45.781616', 0, 'tatisssssssssssssssssssssssss1', 'Luisa', 'fandiño', 'kankjxnskjncks@gmail.com', 0, 1, '2026-09-11 01:31:17.413531'),
(5, 'pbkdf2_sha256$1000000$6VAsDc1MqwPhyFNXxV7Uhb$+ldlVmK8Ea3m9ofeR3AYa3ywV6upIQXVDFx60JO6D9s=', '2026-09-23 00:46:26.118482', 0, 'tatiana', 'Tatiana', 'Fandiño', 'LTAF33329227@soy.sena.edu.co', 0, 1, '2026-09-23 00:46:25.789352'),
(6, 'pbkdf2_sha256$1000000$66OWQ3Z6bPEVGdpT2rLcZp$6Aogb/XWLZJ+DrAw9RQtgT2TFIgr0OJUWlMGLXOEosU=', '2026-09-23 00:51:50.916509', 0, 'tecnico2', 'Tecnico2', 'fandiño', 'ascenciofandinoluisatatiana@gmail.com', 0, 1, '2026-09-23 00:51:50.625997'),
(7, 'pbkdf2_sha256$1000000$MCvwX8nsWex4ibM9qIOsyM$ecqqSYnxDY+0PIqgBwNv/LsGP1pa+lNXHsK1bOg1PbQ=', '2026-09-23 01:57:01.949777', 0, 'Tecnico3', 'Tecnico', '3', 'ascenciodinoluisatatiana10@gmail.com', 0, 1, '2026-09-23 01:49:29.300710'),
(8, 'pbkdf2_sha256$1000000$5EVpEBKrVJtWInDY5GEM4P$5dNlQtrOARNIbDtoqrF6PdzNGfqYD+M+YUUd96GhwQY=', '2026-09-23 01:55:17.999318', 0, 'tatis', 'tatiana', 'ascencio', 'ascenciofandinotatiana10@gmail.com', 0, 1, '2026-09-23 01:55:17.739979');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 3, 1),
(4, 3, 3),
(2, 3, 4),
(3, 6, 4),
(5, 7, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2026-09-02 00:07:57.275156', '1', 'ACT-2024-001 - Computador HP EliteDesk', 1, '[{\"added\": {}}]', 10, 1),
(2, '2026-09-02 00:25:30.688091', '1', 'ACT-2024-001 - Computador HP EliteDesk', 2, '[{\"changed\": {\"fields\": [\"Fotograf\\u00eda\"]}}]', 10, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'inventario', 'activo'),
(7, 'inventario', 'categoria'),
(9, 'inventario', 'estado'),
(11, 'inventario', 'historialmovimiento'),
(14, 'inventario', 'log'),
(12, 'inventario', 'mantenimiento'),
(13, 'inventario', 'perfil'),
(8, 'inventario', 'ubicacion'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'inventario', '0001_initial', '2026-08-26 00:09:44.089851'),
(2, 'contenttypes', '0001_initial', '2026-08-26 00:23:22.521813'),
(3, 'auth', '0001_initial', '2026-08-26 00:23:25.652529'),
(4, 'admin', '0001_initial', '2026-08-26 00:23:26.470545'),
(5, 'admin', '0002_logentry_remove_auto_add', '2026-08-26 00:23:26.542739'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2026-08-26 00:23:26.589453'),
(7, 'contenttypes', '0002_remove_content_type_name', '2026-08-26 00:23:27.029727'),
(8, 'auth', '0002_alter_permission_name_max_length', '2026-08-26 00:23:27.326393'),
(9, 'auth', '0003_alter_user_email_max_length', '2026-08-26 00:23:27.416126'),
(10, 'auth', '0004_alter_user_username_opts', '2026-08-26 00:23:27.455357'),
(11, 'auth', '0005_alter_user_last_login_null', '2026-08-26 00:23:27.665285'),
(12, 'auth', '0006_require_contenttypes_0002', '2026-08-26 00:23:27.675859'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2026-08-26 00:23:27.704319'),
(14, 'auth', '0008_alter_user_username_max_length', '2026-08-26 00:23:27.954508'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2026-08-26 00:23:28.255570'),
(16, 'auth', '0010_alter_group_name_max_length', '2026-08-26 00:23:28.322276'),
(17, 'auth', '0011_update_proxy_permissions', '2026-08-26 00:23:28.356472'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2026-08-26 00:23:28.606921'),
(19, 'sessions', '0001_initial', '2026-08-26 00:23:28.815130'),
(20, 'inventario', '0002_ubicacion', '2026-08-27 23:58:44.124733'),
(21, 'inventario', '0003_estado', '2026-08-28 01:38:26.936073'),
(22, 'inventario', '0004_activo', '2026-09-01 23:59:23.284606'),
(23, 'inventario', '0005_historialmovimiento_mantenimiento', '2026-09-03 23:52:45.610655'),
(24, 'inventario', '0006_perfil', '2026-09-11 00:27:20.312252'),
(25, 'inventario', '0007_log', '2026-09-11 01:37:59.561631'),
(26, 'inventario', '0008_perfil_biografia', '2026-09-22 23:47:18.784747');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('fysdjmk5n1ybsduidngmfn2z48nccukd', '.eJxVjDsOwjAQRO_iGln-xTaU9JzB2vWucQA5UpxUiLuTSCmgnHlv5i0SrEtNa-c5jSQuQovTb4eQn9x2QA9o90nmqS3ziHJX5EG7vE3Er-vh_h1U6HVbs8PCFDnnMFBArRxY5R2bUnwkBA4OcizeDG4L6K01iMb6ElU4a1Ti8wUZkDi5:1wz1TF:HxkUWdoC4iw7bXnoVJ6ovNBZCttfaL1y_2bTiCC5Bww', '2026-09-09 00:26:25.393355'),
('v6cezsjzbd7z8b2bf3z9agb13vwulfvq', '.eJxVjDsOwjAQRO_iGln-xTaU9JzB2vWucQA5UpxUiLuTSCmgnHlv5i0SrEtNa-c5jSQuQovTb4eQn9x2QA9o90nmqS3ziHJX5EG7vE3Er-vh_h1U6HVbs8PCFDnnMFBArRxY5R2bUnwkBA4OcizeDG4L6K01iMb6ElU4a1Ti8wUZkDi5:1wzkLJ:OLvIaljojcxA_FTn5rvkvFw5fWhm_xS-8bdPtLLSeSY', '2026-09-11 00:21:13.062089');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_activo`
--

CREATE TABLE `inventario_activo` (
  `id` bigint NOT NULL,
  `codigo_inventario` varchar(50) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `descripcion` longtext,
  `marca` varchar(100) DEFAULT NULL,
  `modelo` varchar(100) DEFAULT NULL,
  `numero_serie` varchar(100) DEFAULT NULL,
  `fecha_adquisicion` date DEFAULT NULL,
  `valor_adquisicion` decimal(12,2) DEFAULT NULL,
  `responsable` varchar(200) DEFAULT NULL,
  `observaciones` longtext,
  `foto` varchar(100) DEFAULT NULL,
  `activo` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `categoria_id` bigint NOT NULL,
  `estado_id` bigint NOT NULL,
  `ubicacion_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `inventario_activo`
--

INSERT INTO `inventario_activo` (`id`, `codigo_inventario`, `nombre`, `descripcion`, `marca`, `modelo`, `numero_serie`, `fecha_adquisicion`, `valor_adquisicion`, `responsable`, `observaciones`, `foto`, `activo`, `fecha_creacion`, `fecha_modificacion`, `categoria_id`, `estado_id`, `ubicacion_id`) VALUES
(1, 'ACT-2024-001', 'Computador HP EliteDesk', '', 'HP', NULL, NULL, NULL, NULL, NULL, '', 'activos/fotos/2026/09/sanrio.jpg', 1, '2026-09-02 00:07:57.273456', '2026-09-02 00:25:30.685019', 1, 1, 1),
(2, 'ACT-2024-002', 'Monitor Dell 24\"', 'Monitor para estación de trabajo', 'Dell', 'P2422H', 'DELL2024002', '2024-02-10', 850000.00, 'Ana López', NULL, '', 1, '2026-09-02 00:23:36.118532', '2026-09-02 00:23:36.118571', 1, 1, 1),
(3, 'ACT-2024-003', 'Impresora HP LaserJet', 'Impresora laser multifuncional', 'HP', 'LaserJet Pro M404', 'HP2024003', '2024-03-05', 1200000.00, 'Carlos Ramirez', NULL, '', 1, '2026-09-02 00:32:51.881996', '2026-09-02 00:32:51.882056', 6, 1, 3),
(4, 'ACT-2024-004', 'Taladro Industrial', 'Taladro de banco para taller', 'Bosch', 'GBM 32-4', 'BOSCH2024004', '2023-11-20', 650000.00, 'Luis Torres', 'En mantenimiento preventivo programado.', '', 1, '2026-09-02 00:32:51.915005', '2026-09-02 00:32:51.915030', 4, 2, 4),
(5, 'ACT-2024-005', 'Teclado Mecanico Logitech', 'Teclado reservado para nuevo puesto de trabajo', 'Logitech', 'MX Keys', 'LOGI2024005', '2024-04-12', 320000.00, 'Sofia Gomez', NULL, '', 1, '2026-09-02 00:32:51.944345', '2026-09-04 00:00:32.125973', 2, 5, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_categoria`
--

CREATE TABLE `inventario_categoria` (
  `id` bigint NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext,
  `codigo` varchar(10) NOT NULL,
  `activa` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `inventario_categoria`
--

INSERT INTO `inventario_categoria` (`id`, `nombre`, `descripcion`, `codigo`, `activa`, `fecha_creacion`, `fecha_modificacion`) VALUES
(1, 'Computadores', 'Equipos de cómputo: desktops, laptops, all-in-one', 'COMP', 1, '2026-08-26 00:14:41.060970', '2026-08-26 00:14:41.061012'),
(2, 'Periféricos', 'Dispositivos periféricos: mouse, teclados, monitores', 'PERIF', 1, '2026-08-26 00:15:47.495035', '2026-08-26 00:15:47.495076'),
(3, 'Redes', 'Equipos de red: routers, switches, access points', 'RED', 1, '2026-08-26 00:20:48.647089', '2026-08-26 00:20:48.647132'),
(4, 'Herramientas', 'Herramientas electrónicas y de mantenimiento', 'HERR', 1, '2026-08-26 00:21:07.406286', '2026-08-26 00:21:07.406313'),
(5, 'Consumibles', 'Materiales consumibles: cables, conectores', 'CONS', 1, '2026-08-26 00:21:19.235159', '2026-08-26 00:21:19.235190'),
(6, 'Impresoras', 'Impresoras láser e inyección', 'IMPR', 1, '2026-08-26 01:17:11.508183', '2026-08-26 01:17:11.508224'),
(7, 'Mobiliario', 'Sillas, escritorios', 'MOBI', 1, '2026-08-26 01:17:15.974776', '2026-08-26 01:17:15.974804'),
(8, 'Proyectores', 'Proyectores y pantallas', 'PROY', 1, '2026-08-26 01:17:19.518397', '2026-08-26 01:17:19.518429'),
(9, 'Útiles Escolares', 'Productos utilizados para actividades escolares y académicas.', '1001', 1, '2026-09-10 23:32:59.061556', '2026-09-10 23:32:59.061731'),
(10, 'Cuadernos', 'Cuadernos, libretas y agendas para escritura y apuntes.', '1002', 1, '2026-09-10 23:32:59.078623', '2026-09-10 23:32:59.078671'),
(11, 'Papelería', 'Hojas, papel, cartulina y otros productos de papel.', '1003', 1, '2026-09-10 23:32:59.095506', '2026-09-10 23:32:59.095537'),
(12, 'Escritura', 'Lápices, lapiceros, marcadores y elementos para escribir.', '1004', 1, '2026-09-10 23:32:59.113286', '2026-09-10 23:32:59.113326'),
(13, 'Arte y Dibujo', 'Materiales para dibujo, pintura y actividades artísticas.', '1005', 1, '2026-09-10 23:32:59.132871', '2026-09-10 23:32:59.132920'),
(14, 'Oficina', 'Artículos utilizados para trabajos administrativos y de oficina.', '1006', 1, '2026-09-10 23:32:59.151332', '2026-09-10 23:32:59.151379'),
(15, 'Archivo y Organización', 'Carpetas, archivadores, sobres y productos para organizar documentos.', '1007', 1, '2026-09-10 23:32:59.169731', '2026-09-10 23:32:59.169779'),
(16, 'Manualidades', 'Materiales para realizar trabajos manuales y decorativos.', '1008', 1, '2026-09-10 23:32:59.187442', '2026-09-10 23:32:59.187512'),
(19, 'Impresión y Copiado', 'Papel y materiales utilizados para impresión y fotocopiado.', '1011', 1, '2026-09-10 23:32:59.250094', '2026-09-10 23:32:59.250126'),
(20, 'Tecnología', 'Accesorios tecnológicos como memorias USB, cables y otros.', '1012', 1, '2026-09-10 23:32:59.266166', '2026-09-10 23:32:59.266198'),
(21, 'Borradores', 'Diferentes diseños de borradores', '1014', 1, '2026-09-10 23:52:23.459902', '2026-09-10 23:52:23.459953');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_estado`
--

CREATE TABLE `inventario_estado` (
  `id` bigint NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `codigo` varchar(20) NOT NULL,
  `descripcion` longtext,
  `color` varchar(7) NOT NULL,
  `es_operativo` tinyint(1) NOT NULL,
  `requiere_accion` tinyint(1) NOT NULL,
  `orden` int NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `inventario_estado`
--

INSERT INTO `inventario_estado` (`id`, `nombre`, `codigo`, `descripcion`, `color`, `es_operativo`, `requiere_accion`, `orden`, `activo`, `fecha_creacion`, `fecha_modificacion`) VALUES
(1, 'Operativo', 'OPER', 'El activo está funcionando correctamente', '#28a745', 1, 0, 1, 1, '2026-08-28 01:41:12.696595', '2026-08-28 01:41:12.696721'),
(2, 'En Mantenimiento', 'MANT', 'En mantenimiento preventivo', '#ffc107', 0, 1, 2, 1, '2026-08-28 01:41:12.714275', '2026-08-28 01:41:12.714321'),
(3, 'En Reparación', 'REP', 'En reparación por falla', '#ff9800', 0, 1, 3, 1, '2026-08-28 01:41:12.740322', '2026-08-28 01:41:12.740359'),
(4, 'Dado De Baja', 'BAJA', 'El activo ha sido dado de baja', '#dc3545', 0, 0, 5, 1, '2026-08-28 01:41:12.757824', '2026-08-28 01:41:12.757885'),
(5, 'Reservado', 'RESV', 'Reservado para uso específico', '#007bff', 1, 0, 4, 1, '2026-08-28 01:41:12.786124', '2026-08-28 01:41:12.786171');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_historial_movimiento`
--

CREATE TABLE `inventario_historial_movimiento` (
  `id` bigint NOT NULL,
  `fecha_movimiento` datetime(6) NOT NULL,
  `usuario` varchar(200) NOT NULL,
  `motivo` varchar(20) NOT NULL,
  `observaciones` longtext,
  `aprobado` tinyint(1) NOT NULL,
  `activo_id` bigint NOT NULL,
  `ubicacion_destino_id` bigint NOT NULL,
  `ubicacion_origen_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `inventario_historial_movimiento`
--

INSERT INTO `inventario_historial_movimiento` (`id`, `fecha_movimiento`, `usuario`, `motivo`, `observaciones`, `aprobado`, `activo_id`, `ubicacion_destino_id`, `ubicacion_origen_id`) VALUES
(1, '2026-09-04 00:00:32.139772', 'Sistema', 'TRASLADO', 'Registrado automáticamente', 1, 5, 1, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_log`
--

CREATE TABLE `inventario_log` (
  `id` bigint NOT NULL,
  `usuario_nombre` varchar(150) NOT NULL,
  `accion` varchar(20) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `objeto_id` varchar(100) DEFAULT NULL,
  `objeto_repr` varchar(200) NOT NULL,
  `fecha_hora` datetime(6) NOT NULL,
  `descripcion` longtext NOT NULL,
  `datos_anteriores` json DEFAULT NULL,
  `datos_nuevos` json DEFAULT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `user_agent` varchar(255) NOT NULL,
  `usuario_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `inventario_log`
--

INSERT INTO `inventario_log` (`id`, `usuario_nombre`, `accion`, `modelo`, `objeto_id`, `objeto_repr`, `fecha_hora`, `descripcion`, `datos_anteriores`, `datos_nuevos`, `ip_address`, `user_agent`, `usuario_id`) VALUES
(1, 'tatisssssssssssssssssssssssss1', 'LOGIN', 'User', NULL, '', '2026-09-11 01:45:11.484679', 'Inició sesión en el sistema', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 4),
(2, 'tatisssssssssssssssssssssssss1', 'LOGOUT', 'User', NULL, '', '2026-09-11 01:45:57.563819', 'Cerró sesión', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 4),
(3, 'admin', 'LOGIN', 'User', NULL, '', '2026-09-11 01:46:00.615471', 'Inició sesión en el sistema', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(4, 'admin', 'CREATE', 'Activo', '6', 'ACT-2024-009 - Borrador Hello Kitty', '2026-09-11 01:51:49.016120', 'Creó el activo ACT-2024-009', NULL, '{\"codigo\": \"ACT-2024-009\", \"estado\": \"OPER - Operativo\", \"categoria\": \"1014 - Borradores\", \"ubicacion\": \"BOD-01 - Bodega Principal\", \"descripcion\": \"HELLO\", \"valor_adquisicion\": 799.75}', '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(5, 'admin', 'UPDATE', 'Activo', '6', 'ACT-2024-009 - Borrador Hello', '2026-09-11 01:52:14.933667', 'Actualizó ACT-2024-009. Cambios: Sin cambios', '{\"codigo\": \"ACT-2024-009\", \"estado\": \"OPER - Operativo\", \"categoria\": \"1014 - Borradores\", \"ubicacion\": \"BOD-01 - Bodega Principal\", \"descripcion\": \"HELLO\", \"valor_adquisicion\": 799.75}', '{\"codigo\": \"ACT-2024-009\", \"estado\": \"OPER - Operativo\", \"categoria\": \"1014 - Borradores\", \"ubicacion\": \"BOD-01 - Bodega Principal\", \"descripcion\": \"HELLO\", \"valor_adquisicion\": 799.75}', '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(6, 'admin', 'LOGIN', 'User', NULL, '', '2026-09-16 20:55:04.911324', 'Inició sesión en el sistema', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(7, 'admin', 'CREATE', 'Activo', '7', 'ACT-2024-0010 - prueba', '2026-09-16 21:13:10.283773', 'Creó el activo ACT-2024-0010', NULL, '{\"codigo\": \"ACT-2024-0010\", \"estado\": \"OPER - Operativo\", \"categoria\": \"1014 - Borradores\", \"ubicacion\": \"BOD-01 - Bodega Principal\", \"descripcion\": \"\", \"valor_adquisicion\": 2999.69}', '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(8, 'admin', 'DELETE', 'Activo', '7', 'ACT-2024-0010 - prueba', '2026-09-16 21:13:19.580173', 'Eliminó el activo ACT-2024-0010', '{\"codigo\": \"ACT-2024-0010\", \"estado\": \"OPER - Operativo\", \"categoria\": \"1014 - Borradores\", \"ubicacion\": \"BOD-01 - Bodega Principal\", \"descripcion\": \"\", \"valor_adquisicion\": 2999.69}', NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(9, 'admin', 'EXPORT', 'Activo', NULL, '', '2026-09-16 21:32:36.168037', 'Generó reporte PDF de inventario general', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(10, 'admin', 'EXPORT', 'Activo', NULL, '', '2026-09-16 21:32:48.069624', 'Generó reporte PDF de activos por ubicación', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(11, 'admin', 'EXPORT', 'Activo', NULL, '', '2026-09-16 21:33:01.823078', 'Exportó activos a Excel', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(12, 'admin', 'EXPORT', 'Log', NULL, '', '2026-09-16 21:33:22.025689', 'Exportó logs de auditoría a Excel', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(13, 'admin', 'LOGIN', 'User', NULL, '', '2026-09-22 15:31:19.597855', 'Inició sesión en el sistema', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(14, 'admin', 'EXPORT', 'Activo', NULL, '', '2026-09-22 15:31:52.009348', 'Generó reporte PDF de inventario general', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(15, 'admin', 'EXPORT', 'Activo', NULL, '', '2026-09-22 15:31:54.128669', 'Generó reporte PDF de activos por ubicación', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(16, 'admin', 'EXPORT', 'Activo', NULL, '', '2026-09-22 15:31:55.475340', 'Exportó activos a Excel', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(17, 'admin', 'EXPORT', 'Log', NULL, '', '2026-09-22 15:31:56.567071', 'Exportó logs de auditoría a Excel', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(18, 'admin', 'EXPORT', 'Log', NULL, '', '2026-09-22 15:36:20.406587', 'Exportó logs de auditoría a Excel', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(19, 'admin', 'LOGOUT', 'User', NULL, '', '2026-09-23 00:04:40.323680', 'Cerró sesión', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(20, 'tatisssssssssssssssssssssssss1', 'LOGIN', 'User', NULL, '', '2026-09-23 00:04:45.804383', 'Inició sesión en el sistema', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 4),
(21, 'tatisssssssssssssssssssssssss1', 'LOGOUT', 'User', NULL, '', '2026-09-23 00:08:56.256549', 'Cerró sesión', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 4),
(22, 'root', 'LOGIN', 'User', NULL, '', '2026-09-23 00:09:00.352804', 'Inició sesión en el sistema', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 2),
(23, 'root', 'LOGOUT', 'User', NULL, '', '2026-09-23 00:09:47.663662', 'Cerró sesión', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 2),
(24, 'admin', 'LOGIN', 'User', NULL, '', '2026-09-23 00:09:51.221574', 'Inició sesión en el sistema', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 1),
(25, 'tatiana', 'CREATE', 'User', NULL, '', '2026-09-23 00:46:26.108225', 'Nuevo usuario registrado: tatiana', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 5),
(26, 'tatiana', 'UPDATE', 'Perfil', NULL, '', '2026-09-23 00:49:23.164585', 'Actualizó su perfil', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 5),
(27, 'tatiana', 'LOGOUT', 'User', NULL, '', '2026-09-23 00:50:15.299587', 'Cerró sesión', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 5),
(28, 'tecnico2', 'CREATE', 'User', NULL, '', '2026-09-23 00:51:50.907043', 'Nuevo usuario registrado: tecnico2', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 6),
(29, 'Tecnico3', 'CREATE', 'User', NULL, '', '2026-09-23 01:49:29.587673', 'Nuevo usuario registrado: Tecnico3', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 7),
(30, 'Tecnico3', 'UPDATE', 'Perfil', NULL, '', '2026-09-23 01:50:24.956392', 'Actualizó su perfil', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 7),
(31, 'Tecnico3', 'LOGOUT', 'User', NULL, '', '2026-09-23 01:53:26.772414', 'Cerró sesión', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 7),
(32, 'tatis', 'CREATE', 'User', NULL, '', '2026-09-23 01:55:17.990771', 'Nuevo usuario registrado: tatis', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 8),
(33, 'tatis', 'LOGOUT', 'User', NULL, '', '2026-09-23 01:56:56.482588', 'Cerró sesión', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 8),
(34, 'Tecnico3', 'LOGIN', 'User', NULL, '', '2026-09-23 01:57:01.982666', 'Inició sesión en el sistema', NULL, NULL, '172.18.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36', 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_mantenimiento`
--

CREATE TABLE `inventario_mantenimiento` (
  `id` bigint NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date DEFAULT NULL,
  `tecnico` varchar(200) NOT NULL,
  `costo` decimal(12,2) DEFAULT NULL,
  `descripcion` longtext NOT NULL,
  `repuestos` longtext,
  `estado_mantenimiento` varchar(20) NOT NULL,
  `observaciones` longtext,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `activo_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_perfil`
--

CREATE TABLE `inventario_perfil` (
  `id` bigint NOT NULL,
  `cargo` varchar(10) NOT NULL,
  `departamento` varchar(10) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `usuario_id` int NOT NULL,
  `biografia` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `inventario_perfil`
--

INSERT INTO `inventario_perfil` (`id`, `cargo`, `departamento`, `telefono`, `foto`, `fecha_creacion`, `fecha_modificacion`, `usuario_id`, `biografia`) VALUES
(1, 'AUX', 'TI', NULL, '', '2026-09-11 00:28:36.352067', '2026-09-23 00:09:00.342349', 2, ''),
(2, 'TEC', 'TI', '3001234567', '', '2026-09-11 00:29:16.941119', '2026-09-11 00:39:39.117510', 3, ''),
(3, 'AUX', 'TI', NULL, '', '2026-09-11 01:28:33.419897', '2026-09-23 01:43:50.797059', 1, ''),
(4, 'AUX', 'TI', NULL, 'perfiles/ChatGPT_Image_9_sept_2026_12_45_53.png', '2026-09-11 01:31:17.667578', '2026-09-23 00:04:45.796791', 4, ''),
(5, 'AUX', 'TI', NULL, 'perfiles/ChatGPT_Image_9_sept_2026_12_45_53_oVVO66d.png', '2026-09-23 00:46:26.089801', '2026-09-23 00:49:23.153015', 5, ''),
(6, 'AUX', 'TI', NULL, '', '2026-09-23 00:51:50.888887', '2026-09-23 00:51:50.930662', 6, ''),
(7, 'AUX', 'TI', NULL, 'perfiles/ChatGPT_Image_9_sept_2026_11_50_39.png', '2026-09-23 01:49:29.568577', '2026-09-23 01:57:01.971303', 7, ''),
(8, 'AUX', 'TI', NULL, '', '2026-09-23 01:55:17.974264', '2026-09-23 01:55:18.007210', 8, '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_ubicacion`
--

CREATE TABLE `inventario_ubicacion` (
  `id` bigint NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `codigo` varchar(20) NOT NULL,
  `capacidad` int NOT NULL,
  `responsable` varchar(100) DEFAULT NULL,
  `observaciones` longtext,
  `activa` tinyint(1) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `inventario_ubicacion`
--

INSERT INTO `inventario_ubicacion` (`id`, `nombre`, `tipo`, `codigo`, `capacidad`, `responsable`, `observaciones`, `activa`, `fecha_creacion`, `fecha_modificacion`) VALUES
(1, 'Bodega Principal', 'BODEGA', 'BOD-01', 100, 'Juan Pérez', 'Bodega central de almacenamiento', 1, '2026-08-28 00:14:43.351984', '2026-08-28 00:14:43.352160'),
(2, 'Laboratorio De Redes', 'LABORATORIO', 'LAB-RED-01', 30, 'María González', 'Laboratorio equipado para prácticas de redes', 1, '2026-08-28 00:14:43.379784', '2026-08-28 00:14:43.379846'),
(3, 'Oficina De Sistemas', 'OFICINA', 'OFI-SIS-01', 20, 'Carlos Ramírez', NULL, 1, '2026-08-28 00:14:43.406154', '2026-08-28 00:14:43.406211'),
(4, 'Taller De Mantenimiento', 'TALLER', 'TAL-MAN-01', 15, 'Ana Torres', 'Taller para reparación y mantenimiento', 1, '2026-08-28 00:14:43.434399', '2026-08-28 00:14:43.434460'),
(5, 'Bodega Secundaria', 'BODEGA', 'BOD-02', 50, 'Luis Martínez', NULL, 1, '2026-08-28 00:14:43.460338', '2026-08-28 00:14:43.461295');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `inventario_activo`
--
ALTER TABLE `inventario_activo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo_inventario` (`codigo_inventario`),
  ADD UNIQUE KEY `numero_serie` (`numero_serie`),
  ADD KEY `inventario_activo_categoria_id_d5b14ae7_fk_inventari` (`categoria_id`),
  ADD KEY `inventario_activo_estado_id_16d893e7_fk_inventario_estado_id` (`estado_id`),
  ADD KEY `inventario_activo_ubicacion_id_04e01473_fk_inventari` (`ubicacion_id`);

--
-- Indices de la tabla `inventario_categoria`
--
ALTER TABLE `inventario_categoria`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD UNIQUE KEY `codigo` (`codigo`),
  ADD KEY `idx_categoria_nombre` (`nombre`),
  ADD KEY `idx_categoria_codigo` (`codigo`);

--
-- Indices de la tabla `inventario_estado`
--
ALTER TABLE `inventario_estado`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `inventario_historial_movimiento`
--
ALTER TABLE `inventario_historial_movimiento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventario_historial_activo_id_1cd756fd_fk_inventari` (`activo_id`),
  ADD KEY `inventario_historial_ubicacion_destino_id_dc8151a7_fk_inventari` (`ubicacion_destino_id`),
  ADD KEY `inventario_historial_ubicacion_origen_id_899b7203_fk_inventari` (`ubicacion_origen_id`);

--
-- Indices de la tabla `inventario_log`
--
ALTER TABLE `inventario_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventario__fecha_h_ccf3f7_idx` (`fecha_hora` DESC),
  ADD KEY `inventario__usuario_441826_idx` (`usuario_id`,`fecha_hora` DESC),
  ADD KEY `inventario__modelo_cff00b_idx` (`modelo`,`fecha_hora` DESC);

--
-- Indices de la tabla `inventario_mantenimiento`
--
ALTER TABLE `inventario_mantenimiento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventario_mantenimi_activo_id_d17975b9_fk_inventari` (`activo_id`);

--
-- Indices de la tabla `inventario_perfil`
--
ALTER TABLE `inventario_perfil`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `inventario_ubicacion`
--
ALTER TABLE `inventario_ubicacion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD UNIQUE KEY `codigo` (`codigo`),
  ADD KEY `idx_ubicacion_nombre` (`nombre`),
  ADD KEY `idx_ubicacion_codigo` (`codigo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=117;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `inventario_activo`
--
ALTER TABLE `inventario_activo`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `inventario_categoria`
--
ALTER TABLE `inventario_categoria`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `inventario_estado`
--
ALTER TABLE `inventario_estado`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `inventario_historial_movimiento`
--
ALTER TABLE `inventario_historial_movimiento`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `inventario_log`
--
ALTER TABLE `inventario_log`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT de la tabla `inventario_mantenimiento`
--
ALTER TABLE `inventario_mantenimiento`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inventario_perfil`
--
ALTER TABLE `inventario_perfil`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `inventario_ubicacion`
--
ALTER TABLE `inventario_ubicacion`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `inventario_activo`
--
ALTER TABLE `inventario_activo`
  ADD CONSTRAINT `inventario_activo_categoria_id_d5b14ae7_fk_inventari` FOREIGN KEY (`categoria_id`) REFERENCES `inventario_categoria` (`id`),
  ADD CONSTRAINT `inventario_activo_estado_id_16d893e7_fk_inventario_estado_id` FOREIGN KEY (`estado_id`) REFERENCES `inventario_estado` (`id`),
  ADD CONSTRAINT `inventario_activo_ubicacion_id_04e01473_fk_inventari` FOREIGN KEY (`ubicacion_id`) REFERENCES `inventario_ubicacion` (`id`);

--
-- Filtros para la tabla `inventario_historial_movimiento`
--
ALTER TABLE `inventario_historial_movimiento`
  ADD CONSTRAINT `inventario_historial_activo_id_1cd756fd_fk_inventari` FOREIGN KEY (`activo_id`) REFERENCES `inventario_activo` (`id`),
  ADD CONSTRAINT `inventario_historial_ubicacion_destino_id_dc8151a7_fk_inventari` FOREIGN KEY (`ubicacion_destino_id`) REFERENCES `inventario_ubicacion` (`id`),
  ADD CONSTRAINT `inventario_historial_ubicacion_origen_id_899b7203_fk_inventari` FOREIGN KEY (`ubicacion_origen_id`) REFERENCES `inventario_ubicacion` (`id`);

--
-- Filtros para la tabla `inventario_log`
--
ALTER TABLE `inventario_log`
  ADD CONSTRAINT `inventario_log_usuario_id_0cdb0633_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `inventario_mantenimiento`
--
ALTER TABLE `inventario_mantenimiento`
  ADD CONSTRAINT `inventario_mantenimi_activo_id_d17975b9_fk_inventari` FOREIGN KEY (`activo_id`) REFERENCES `inventario_activo` (`id`);

--
-- Filtros para la tabla `inventario_perfil`
--
ALTER TABLE `inventario_perfil`
  ADD CONSTRAINT `inventario_perfil_usuario_id_ff29f016_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
