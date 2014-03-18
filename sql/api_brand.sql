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
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `brand` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `agency_id` bigint(20) DEFAULT NULL,
  `brand_name` varchar(255) DEFAULT NULL,
  `url_postback` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_agency_id` (`agency_id`)
) ENGINE=MyISAM AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (2,2,'Jiffy Lube',NULL),(1,1,'Ethereal','www.google.com'),(4,2,'Coke',NULL),(5,2,'Pepsi',NULL),(6,2,'Pep Boys',NULL),(7,3,'Walgreens',NULL),(8,3,'Walmart',NULL),(9,5,'Dish',NULL),(10,6,'E*TRADE',NULL),(11,7,'Chevy',NULL),(12,8,'Expedia',NULL),(13,9,'Realtor.com',NULL),(14,10,'Allstate',NULL),(16,11,'Susquehanna Bank',NULL),(17,12,'Nissan',NULL),(18,13,'Layton Hills Mall',NULL),(19,1,'Applebee\'s',NULL),(20,14,'Nissan',NULL),(21,1,'Google',NULL),(22,29,'Hilton','https://rall.everyscreenmedia.com/visit.gif?p=cl1000926&a=pageview&e=HILTCONV&s=ev10000663&m=1&u=[USER_ID]&d=[DATA_FIELDS]&b=[RANDOM_GENERATOR]'),(71,83,'Henderson Brands',NULL),(70,82,'BrandX',NULL),(69,81,'QA Brand Name',NULL),(67,79,'Acme Co',NULL),(68,80,'BrandX Widgets',NULL),(65,77,'Spinzo',NULL),(72,84,'The Cosmopolitan of Las Vegas',NULL),(73,85,'BrandX Widgets',NULL),(74,86,'CalMHSA',NULL),(75,87,'Army',NULL);
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-01-09 12:47:47
