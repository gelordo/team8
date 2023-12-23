-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: sys
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `low`
--

DROP TABLE IF EXISTS `low`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `low` (
  `Column1` varchar(255) DEFAULT NULL,
  `Column2` varchar(255) DEFAULT NULL,
  `Column3` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `low`
--

LOCK TABLES `low` WRITE;
/*!40000 ALTER TABLE `low` DISABLE KEYS */;
INSERT INTO `low` VALUES ('3-3','0','210\r'),('3-101','0','88\r'),('3-104','0','94\r'),('3-201','0','30\r'),('3-202','0','32\r'),('3-203','0','26\r'),('3-224','0','34\r'),('3-310','0','76\r'),('3-312','0','24\r'),('3-401','0','60\r'),('3-402','0','60\r'),('3-404','0','24\r'),('3-405','0','24\r'),('3-505','0','24\r'),('3-512','0','24\r'),('3-515','0','24\r'),('3-519','0','28\r'),('3-524','0','24\r'),('6-2','0','180\r'),('5-1','0','25\r'),('3-601','0','15\r'),('3-604','0','60\r'),('3-606','0','28\r'),('3-607','0','30\r'),('3-609','0','56\r'),('3-611','0','30\r'),('3-613','0','30\r'),('3-614','0','60\r'),('3-618','0','25\r'),('3-622','0','25\r'),('3-623','0','30\r'),('3-624','0','30\r'),('3-630','0','30\r'),('3-707','0','25\r'),('3-709','0','25\r'),('3-717','0','25\r'),('3-718','0','25\r'),('3-719','0','25\r'),('3-720','0','60\r'),('3-722','0','25\r'),('3-724','0','25\r'),('3-113','0','48\r'),('3-115','0','20\r'),('3-118','0','50\r'),('D-01','1','25\r'),('D-03','1','25\r'),('D-02','1','25\r'),('D-04','1','25\r'),('110','1','25\r'),('112','1','25\r'),('114','1','25\r'),('212','1','25\r'),('214','1','25\r'),('215','1','25\r'),('217','1','25\r'),('406','1','25\r'),('407','1','25\r'),('409','1','25\r'),('420','1','25\r'),('422','1','25\r'),('427','1','25\r'),('416','1','25\r'),('501A','1','25\r'),('501B','1','25\r'),('503','1','25\r'),('502A','1','25\r'),('502B','1','25\r'),('516','1','25\r'),('513A','1','25\r'),('513B','1','25\r'),('518','1','25\r'),('608','1','25\r'),('619','1','25\r'),('628','1','25\r'),('A-01','1','25\r'),('A-02','1','25\r'),('A-03','1','25');
/*!40000 ALTER TABLE `low` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-23 21:13:13
