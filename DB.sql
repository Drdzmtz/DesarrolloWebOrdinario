
-- Volcando estructura de base de datos para ordinario
CREATE DATABASE IF NOT EXISTS `ordinario` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `ordinario`;

-- Volcando estructura para tabla ordinario.houses
CREATE TABLE IF NOT EXISTS `houses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zip_code` varchar(50) NOT NULL,
  `price` float NOT NULL DEFAULT 0,
  `rooms` int(11) NOT NULL DEFAULT 0,
  `bathrooms` int(11) NOT NULL DEFAULT 0,
  `longitude` varchar(20) NOT NULL,
  `latitude` varchar(20) NOT NULL,
  `description` varchar(500) NOT NULL,
  `status` enum('VENDIDO','EN VENTA') NOT NULL DEFAULT 'EN VENTA',
  `type` enum('CASA','TERRENO') NOT NULL DEFAULT 'CASA',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Volcando estructura para tabla ordinario.news
CREATE TABLE IF NOT EXISTS `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Volcando estructura para tabla ordinario.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(32) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;