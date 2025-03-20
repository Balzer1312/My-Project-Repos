-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: carpool
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Max','Mustermann','Finazen'),(2,'Patrick','rick','IH');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiclerental`
--

DROP TABLE IF EXISTS `vehiclerental`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehiclerental` (
  `rental_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `vehicle_id` int NOT NULL,
  `date_from` varchar(10) DEFAULT NULL,
  `date_to` varchar(10) DEFAULT NULL,
  `driven_km` int DEFAULT '0',
  `tanked` decimal(10,2) DEFAULT '0.00',
  PRIMARY KEY (`rental_id`),
  KEY `employee_id` (`employee_id`),
  KEY `vehicle_id` (`vehicle_id`),
  CONSTRAINT `vehiclerental_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`),
  CONSTRAINT `vehiclerental_ibfk_2` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicles` (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiclerental`
--

LOCK TABLES `vehiclerental` WRITE;
/*!40000 ALTER TABLE `vehiclerental` DISABLE KEYS */;
INSERT INTO `vehiclerental` VALUES (1,2,3,'07.01.2025',NULL,NULL,NULL),(3,1,2,'06.02.2025','13.03.2025',2000,20.00);
/*!40000 ALTER TABLE `vehiclerental` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicles`
--

DROP TABLE IF EXISTS `vehicles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicles` (
  `vehicle_id` int NOT NULL,
  `brand` varchar(50) NOT NULL,
  `model` varchar(50) NOT NULL,
  `color` varchar(50) NOT NULL,
  `type` varchar(10) NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `mileage` int DEFAULT NULL,
  `fuelType` varchar(10) DEFAULT NULL,
  `tanked` decimal(5,2) DEFAULT NULL,
  `consumption` decimal(5,2) DEFAULT NULL,
  `loadCapacity` int DEFAULT NULL,
  `engineCapacity` int DEFAULT NULL,
  `seatNumb` int DEFAULT NULL,
  `weehlSize` int DEFAULT NULL,
  PRIMARY KEY (`vehicle_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicles`
--

LOCK TABLES `vehicles` WRITE;
/*!40000 ALTER TABLE `vehicles` DISABLE KEYS */;
INSERT INTO `vehicles` VALUES (2,'Mercedes','Actros','Weiss','Truck',1,182000,'Diesel',320.00,30.00,13,NULL,NULL,NULL),(3,'Yamaha','MT-07','Blau','Motorcycle',0,20000,'Benzin',14.00,4.80,NULL,689,NULL,NULL),(4,'Cube','Nature','Schwarz','Bicycle',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,28),(5,'BMW','M3','Schwarz','Car',1,32000,'Benzin',234.00,4.20,NULL,NULL,5,NULL),(6,'MAN','MTX','Weiß','Truck',1,243456,'Diesel',403.00,5.30,23000,NULL,NULL,NULL);
/*!40000 ALTER TABLE `vehicles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_rental_info`
--

DROP TABLE IF EXISTS `view_rental_info`;
/*!50001 DROP VIEW IF EXISTS `view_rental_info`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_rental_info` AS SELECT 
 1 AS `rental_id`,
 1 AS `employee_id`,
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `vehicle_id`,
 1 AS `brand`,
 1 AS `model`,
 1 AS `type`,
 1 AS `date_from`,
 1 AS `date_to`,
 1 AS `driven_km`,
 1 AS `tanked`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `view_rental_info`
--

/*!50001 DROP VIEW IF EXISTS `view_rental_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_rental_info` AS select `vr`.`rental_id` AS `rental_id`,`vr`.`employee_id` AS `employee_id`,`e`.`first_name` AS `first_name`,`e`.`last_name` AS `last_name`,`vr`.`vehicle_id` AS `vehicle_id`,`v`.`brand` AS `brand`,`v`.`model` AS `model`,`v`.`type` AS `type`,`vr`.`date_from` AS `date_from`,`vr`.`date_to` AS `date_to`,`vr`.`driven_km` AS `driven_km`,`vr`.`tanked` AS `tanked` from ((`vehiclerental` `vr` join `employees` `e` on((`vr`.`employee_id` = `e`.`employee_id`))) join `vehicles` `v` on((`vr`.`vehicle_id` = `v`.`vehicle_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-13 12:23:22
