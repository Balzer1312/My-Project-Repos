-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: clupdb
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
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `MID` int NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `birth` varchar(10) NOT NULL,
  `address` varchar(50) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `entryDate` varchar(10) NOT NULL,
  `unit` varchar(50) NOT NULL,
  `playerPos` varchar(25) DEFAULT NULL,
  `playerNumb` int DEFAULT NULL,
  `TeamGroup` varchar(10) DEFAULT NULL,
  `Experience` int DEFAULT NULL,
  `trainingTypes` varchar(25) DEFAULT NULL,
  `team` varchar(25) DEFAULT NULL,
  `competence` varchar(50) DEFAULT NULL,
  `administrationBody` varchar(50) DEFAULT NULL,
  `financeArea` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`MID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'John','Henrick','15.04.1990','Musterweg 18','John.Henri@mail.com','10.01.2020','Player','Stürmer',10,'A',5,NULL,NULL,NULL,NULL,NULL),(3,'Alice','Johnson','10.09.1985','789 Oak St','alice.johnson@email.com','22.03.2020','Trainer',NULL,NULL,'A',7,'Stärke',NULL,NULL,NULL,NULL),(4,'Robert','Brown','05.12.1990','159 Maple St','robert.brown@email.com','30.09.2021','Manager',NULL,NULL,NULL,5,NULL,NULL,'Event Manager','Managment',NULL),(5,'Max','Mustermann','13.12.1998','Mustergasse 13','Max.Muster@mail.com','18.03.2025','Player','Verteidiger',4,NULL,3,NULL,NULL,NULL,NULL,NULL),(6,'Michael','White','30.11.1975','654 Pine St','michael.white@email.com','10.04.2015','Treasurer',NULL,NULL,NULL,5,NULL,NULL,NULL,'Managment','Budgetierung');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_team`
--

DROP TABLE IF EXISTS `member_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_team` (
  `memberID` int NOT NULL,
  `teamID` int NOT NULL,
  PRIMARY KEY (`memberID`,`teamID`),
  KEY `teamID` (`teamID`),
  CONSTRAINT `member_team_ibfk_1` FOREIGN KEY (`memberID`) REFERENCES `member` (`MID`) ON DELETE CASCADE,
  CONSTRAINT `member_team_ibfk_2` FOREIGN KEY (`teamID`) REFERENCES `team` (`TID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_team`
--

LOCK TABLES `member_team` WRITE;
/*!40000 ALTER TABLE `member_team` DISABLE KEYS */;
INSERT INTO `member_team` VALUES (1,1),(3,1);
/*!40000 ALTER TABLE `member_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `TID` int NOT NULL,
  `teamName` varchar(25) NOT NULL,
  `Teamgroup` varchar(10) NOT NULL,
  PRIMARY KEY (`TID`),
  UNIQUE KEY `teamName` (`teamName`),
  UNIQUE KEY `Teamgroup` (`Teamgroup`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES (1,'Alpha','A');
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'clupdb'
--
/*!50003 DROP PROCEDURE IF EXISTS `addMember` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addMember`(
    IN p_firstname VARCHAR(50),
    IN p_lastname VARCHAR(50),
    IN p_birth VARCHAR(10),
    IN p_address VARCHAR(50),
    IN p_mail VARCHAR(50),
    IN p_entryDate VARCHAR(10),
    IN p_unit VARCHAR(50),
    IN p_playerPos VARCHAR(25),
    IN p_playerNumb INT,
    IN p_TeamGroup VARCHAR(10),
    IN p_Experience INT,
    IN p_trainingTypes VARCHAR(25),
    IN p_team VARCHAR(25),
    IN p_competence VARCHAR(50),
    IN p_administrationBody VARCHAR(50),
    IN p_financeArea VARCHAR(50),
    OUT p_newMID INT
)
BEGIN
    DECLARE missing_id INT;
    -- Prüfen, ob MID = 1 fehlt
    SELECT 1 INTO missing_id FROM member WHERE MID = 1 LIMIT 1;
    IF missing_id IS NULL THEN
        
        SET p_newMID = 1;
    ELSE
        
        SELECT MIN(m.MID + 1) INTO p_newMID
        FROM member m
        WHERE NOT EXISTS (SELECT 1 FROM member m2 WHERE m2.MID = m.MID + 1);

        IF p_newMID IS NULL THEN
            SELECT COALESCE(MAX(MID) + 1, 1) INTO p_newMID FROM member;
        END IF;
    END IF;

    -- Neues Mitglied einfügen
    INSERT INTO member (MID, firstname, lastname, birth, address, mail, entryDate, unit, playerPos, playerNumb, TeamGroup, Experience, trainingTypes, team, competence, administrationBody, financeArea)
    VALUES (p_newMID, p_firstname, p_lastname, p_birth, p_address, p_mail, p_entryDate, p_unit, p_playerPos, p_playerNumb, p_TeamGroup, p_Experience, p_trainingTypes, p_team, p_competence, p_administrationBody, p_financeArea);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `assignMemberToTeam` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `assignMemberToTeam`(IN p_memberID INT, IN p_teamID INT)
BEGIN
    DECLARE v_teamGroup VARCHAR(10);

    SELECT TeamGroup INTO v_teamGroup FROM Team WHERE TID = p_teamID;

    INSERT INTO Member_Team (memberID, teamID)
    VALUES (p_memberID, p_teamID)
    ON DUPLICATE KEY UPDATE teamID = p_teamID;

    UPDATE member 
    SET TeamGroup = v_teamGroup
    WHERE MID = p_memberID;
    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `createNewTeam` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `createNewTeam`(
    IN p_teamName VARCHAR(25), 
    IN p_teamGroup VARCHAR(10)
)
BEGIN
    DECLARE nextID INT;

    SELECT MIN(t1.TID + 1) INTO nextID 
    FROM Team t1 
    WHERE NOT EXISTS (SELECT 1 FROM Team t2 WHERE t2.TID = t1.TID + 1);

    IF nextID IS NULL THEN
        SELECT IFNULL(MAX(TID) + 1, 1) INTO nextID FROM Team;
    END IF;

    INSERT INTO Team (TID, teamName, TeamGroup) 
    VALUES (nextID, p_teamName, p_teamGroup);
    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `deleteMember` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteMember`(IN p_mid INT)
BEGIN
    DELETE FROM member WHERE MID = p_mid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `deleteTeam` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteTeam`(IN p_teamID INT)
BEGIN
    DECLARE v_teamGroup VARCHAR(10);

    SELECT TeamGroup INTO v_teamGroup FROM Team WHERE TID = p_teamID;

    IF v_teamGroup IS NOT NULL THEN
        UPDATE member 
        SET TeamGroup = NULL
        WHERE TeamGroup = v_teamGroup;
    END IF;

    DELETE FROM Member_Team WHERE teamID = p_teamID;
    DELETE FROM Team WHERE TID = p_teamID;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `updateMember` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `updateMember`(
    IN p_mid INT,
    IN p_firstname VARCHAR(50),
    IN p_lastname VARCHAR(50),
    IN p_address VARCHAR(50),
    IN p_mail VARCHAR(50),
    IN p_playerPos VARCHAR(10),
    IN p_teamGroup VARCHAR(10),
    IN p_trainingTypes VARCHAR(25),
    IN p_competence VARCHAR(50),
    IN p_financeArea VARCHAR(50),
    IN p_experience INT
)
BEGIN
    UPDATE member
    SET
        firstname = IFNULL(p_firstname, firstname),
        lastname = IFNULL(p_lastname, lastname),
        address = IFNULL(p_address, address),
        mail = IFNULL(p_mail, mail),
        playerPos = IFNULL(p_playerPos, playerPos),
        TeamGroup = IFNULL(p_teamGroup, TeamGroup),
        trainingTypes = IFNULL(p_trainingTypes, trainingTypes),
        competence = IFNULL(p_competence, competence),
        financeArea = IFNULL(p_financeArea, financeArea),
        Experience = IFNULL(p_experience, Experience)
    WHERE MID = p_mid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-18 13:51:31
