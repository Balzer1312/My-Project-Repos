-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: musicalbum
-- ------------------------------------------------------
-- Server version	8.0.40


USE musicalbum;  --

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
-- Table structure for table `album_tracks`
--

DROP TABLE IF EXISTS `album_tracks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_tracks` (
  `album_id` int NOT NULL,
  `track_id` int NOT NULL,
  PRIMARY KEY (`album_id`,`track_id`),
  KEY `track_id` (`track_id`),
  CONSTRAINT `album_tracks_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `albums` (`album_id`) ON DELETE CASCADE,
  CONSTRAINT `album_tracks_ibfk_2` FOREIGN KEY (`track_id`) REFERENCES `tracks` (`track_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_tracks`
--

LOCK TABLES `album_tracks` WRITE;
/*!40000 ALTER TABLE `album_tracks` DISABLE KEYS */;
INSERT INTO `album_tracks` VALUES (1,2),(1,3);
/*!40000 ALTER TABLE `album_tracks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `album_tracks_view`
--

DROP TABLE IF EXISTS `album_tracks_view`;
/*!50001 DROP VIEW IF EXISTS `album_tracks_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `album_tracks_view` AS SELECT 
 1 AS `album_id`,
 1 AS `album_title`,
 1 AS `album_genre`,
 1 AS `publisher`,
 1 AS `track_ids`,
 1 AS `track_titles`,
 1 AS `interpreters`,
 1 AS `track_genres`,
 1 AS `track_lengths`,
 1 AS `next_album_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `albums`
--

DROP TABLE IF EXISTS `albums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albums` (
  `album_id` int NOT NULL,
  `publisher` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `genre` varchar(255) NOT NULL,
  PRIMARY KEY (`album_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albums`
--

LOCK TABLES `albums` WRITE;
/*!40000 ALTER TABLE `albums` DISABLE KEYS */;
INSERT INTO `albums` VALUES (1,'Linkin Park','Hybrid Theory','mix'),(2,'Linkin Park','Greatest Hits','mix');
/*!40000 ALTER TABLE `albums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `next_album_id`
--

DROP TABLE IF EXISTS `next_album_id`;
/*!50001 DROP VIEW IF EXISTS `next_album_id`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `next_album_id` AS SELECT 
 1 AS `next_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `tracks`
--

DROP TABLE IF EXISTS `tracks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tracks` (
  `track_id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `interpreter` varchar(255) NOT NULL,
  `genre` varchar(255) NOT NULL,
  `length` int NOT NULL,
  PRIMARY KEY (`track_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracks`
--

LOCK TABLES `tracks` WRITE;
/*!40000 ALTER TABLE `tracks` DISABLE KEYS */;
INSERT INTO `tracks` VALUES (2,'Crawling','Linkin Park',' Alternative Rock',209),(3,'In the End','Linkin Park',' Alternative Rock',231);
/*!40000 ALTER TABLE `tracks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'musicalbum'
--
/*!50003 DROP PROCEDURE IF EXISTS `add_album` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_album`(
    IN album_title VARCHAR(255),
    IN album_genre VARCHAR(255),
    IN album_publisher VARCHAR(255)
)
BEGIN
    DECLARE new_album_id INT;

    -- Nächste freie ID holen
    SELECT MIN(t1.album_id + 1) INTO new_album_id
    FROM albums t1
    WHERE NOT EXISTS (SELECT * FROM albums t2 WHERE t2.album_id = t1.album_id + 1);

    -- Falls keine freie ID gefunden wird, höchste ID +1 nehmen
    IF new_album_id IS NULL THEN
        SELECT COALESCE(MAX(album_id) + 1, 1) INTO new_album_id FROM albums;
    END IF;
    

    -- Album einfügen
    INSERT INTO albums (album_id, title, genre, publisher)
    VALUES (new_album_id, album_title, album_genre, album_publisher);
    
     IF EXISTS (SELECT 1 FROM album_tracks WHERE album_id = new_album_id) THEN
        INSERT INTO album_tracks (album_id, track_id)
        SELECT new_album_id, new_track_id
        WHERE new_track_id IS NOT NULL;
    END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_track` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_track`(
    IN track_title VARCHAR(255),
    IN track_interpreter VARCHAR(255),
    IN track_genre VARCHAR(255),
    IN track_length INT,
    IN album_id INT
)
BEGIN
    DECLARE new_track_id INT;

    SELECT MIN(t1.track_id + 1) INTO new_track_id
    FROM tracks t1
    WHERE NOT EXISTS (SELECT * FROM tracks t2 WHERE t2.track_id = t1.track_id + 1);

    -- Falls keine freie ID gefunden wird, höchste ID +1 nehmen
    IF new_track_id IS NULL THEN
        SELECT COALESCE(MAX(track_id) + 1, 1) INTO new_track_id FROM tracks;
    END IF;

    -- Track in die Tabelle 'tracks' einfügen
    INSERT INTO tracks (track_id, title, interpreter, genre, length)
    VALUES (new_track_id, track_title, track_interpreter, track_genre, track_length);

    -- Track mit Album verknüpfen
    INSERT INTO album_tracks (album_id, track_id)
    VALUES (album_id, new_track_id);
    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `assign_track_to_album` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `assign_track_to_album`(
    IN album_id_param INT,
    IN track_id_param INT
)
BEGIN
    -- Track-Album-Zuweisung erstellen
    INSERT INTO album_tracks (album_id, track_id)
    VALUES (album_id_param, track_id_param)
    ON DUPLICATE KEY UPDATE album_id = album_id_param, track_id = track_id_param;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_album` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_album`(IN album_id_param INT)
BEGIN
    -- Album löschen
    DELETE FROM albums WHERE album_id = album_id_param;

    -- Verknüpfungen in album_tracks entfernen
    DELETE FROM album_tracks WHERE album_id = album_id_param;

    -- Verwaiste Tracks löschen (Tracks ohne bestehende Verbindung)
    DELETE FROM tracks 
    WHERE track_id NOT IN (SELECT track_id FROM album_tracks);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_track` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_track`(IN track_id_param INT)
BEGIN
    -- 1. Entferne alle Verknüpfungen des Tracks in der Zwischentabelle 'album_tracks'
    DELETE FROM album_tracks WHERE track_id = track_id_param;

    -- 2. Lösche den Track endgültig aus der 'tracks'-Tabelle
    DELETE FROM tracks WHERE track_id = track_id_param;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `remove_track_from_album` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `remove_track_from_album`(
    IN album_id_param INT,
    IN track_id_param INT
)
BEGIN
    -- Entferne nur die Verknüpfung zwischen Album und Track
    DELETE FROM album_tracks 
    WHERE album_id = album_id_param AND track_id = track_id_param;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `album_tracks_view`
--

/*!50001 DROP VIEW IF EXISTS `album_tracks_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `album_tracks_view` AS select `a`.`album_id` AS `album_id`,`a`.`title` AS `album_title`,`a`.`genre` AS `album_genre`,`a`.`publisher` AS `publisher`,group_concat(distinct `t`.`track_id` order by `t`.`track_id` ASC separator '|') AS `track_ids`,group_concat(distinct `t`.`title` order by `t`.`track_id` ASC separator '|') AS `track_titles`,group_concat(`t`.`interpreter` order by `t`.`track_id` ASC separator '|') AS `interpreters`,group_concat(`t`.`genre` order by `t`.`track_id` ASC separator '|') AS `track_genres`,group_concat(`t`.`length` order by `t`.`track_id` ASC separator '|') AS `track_lengths`,(select min((`t1`.`album_id` + 1)) from (`albums` `t1` left join `albums` `t2` on(((`t1`.`album_id` + 1) = `t2`.`album_id`))) where (`t2`.`album_id` is null)) AS `next_album_id` from ((`albums` `a` left join `album_tracks` `at` on((`a`.`album_id` = `at`.`album_id`))) left join `tracks` `t` on((`at`.`track_id` = `t`.`track_id`))) group by `a`.`album_id`,`a`.`title`,`a`.`genre`,`a`.`publisher` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `next_album_id`
--

/*!50001 DROP VIEW IF EXISTS `next_album_id`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `next_album_id` AS select min((`t1`.`album_id` + 1)) AS `next_id` from (`albums` `t1` left join `albums` `t2` on(((`t1`.`album_id` + 1) = `t2`.`album_id`))) where (`t2`.`album_id` is null) */;
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

-- Dump completed on 2025-03-11  9:35:15
