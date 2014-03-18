CREATE DATABASE  IF NOT EXISTS `api` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `api`;
-- MySQL dump 10.13  Distrib 5.6.13, for osx10.6 (i386)
--
-- Host: 184.172.45.186    Database: api
-- ------------------------------------------------------
-- Server version	5.1.69

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agency`
--

DROP TABLE IF EXISTS `agency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agency` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `suspended` bit(1) DEFAULT b'0',
  `agency_name` varchar(255) DEFAULT NULL,
  `agency_type` enum('Motrixi','Managed','Self_serve','Desk_API') DEFAULT NULL,
  `account_balance` double DEFAULT NULL,
  `url_postback` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agency`
--

LOCK TABLES `agency` WRITE;
/*!40000 ALTER TABLE `agency` DISABLE KEYS */;
INSERT INTO `agency` VALUES (1,'\0','Motrixi','Motrixi',10000,'www.todd.com'),(2,'\0','Square One','Managed',1000000,''),(3,'\0','Shop Local',NULL,1000000,NULL),(4,'\0','New Agency',NULL,0,NULL),(5,'\0','Media8',NULL,0,NULL),(6,'\0','Spark Communication',NULL,0,NULL),(7,'\0','Katz360',NULL,0,NULL),(8,'\0','Amobee',NULL,0,NULL),(9,'\0','Essence Digital',NULL,0,NULL),(11,'\0','A-B-C',NULL,0,NULL),(10,'\0','Tapestry',NULL,0,NULL),(12,'\0','commonground',NULL,0,NULL),(13,'\0','lin-digital',NULL,0,NULL),(14,'\0','OMD Digital',NULL,0,NULL),(29,'\0','iProspect',NULL,0,NULL),(83,'\0','Agency H',NULL,10000,''),(79,'\0','The New Agency',NULL,25000,'www.newagency-postback.con'),(80,'\0','Ad Spinner',NULL,100000,''),(77,'\0','Todd Test Agency',NULL,100000,''),(81,'\0','QA Agency Name',NULL,10000,''),(82,'\0','AgencyX',NULL,10000,''),(84,'\0','Rally Point Solutions, LLC.',NULL,50000,''),(85,'\0','Atif Co',NULL,10000,''),(86,'\0','PROXi Digital',NULL,100000,''),(87,'\0','Media Gravity',NULL,200000,''),(88,'\0','Wayne','Motrixi',1000,'');
/*!40000 ALTER TABLE `agency` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-01-09 12:45:39
