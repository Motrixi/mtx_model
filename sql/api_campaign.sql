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
-- Table structure for table `campaign`
--

DROP TABLE IF EXISTS `campaign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `campaign` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `brand_id` bigint(20) DEFAULT NULL,
  `campaign_name` varchar(255) DEFAULT NULL,
  `date_start` datetime DEFAULT NULL,
  `date_end` datetime DEFAULT NULL,
  `budget_total` double DEFAULT NULL,
  `budget_daily` double DEFAULT NULL,
  `impression_total` bigint(20) DEFAULT NULL,
  `impression_daily` bigint(20) DEFAULT NULL,
  `state` enum('running','paused','completed','rejected') DEFAULT 'paused',
  PRIMARY KEY (`id`),
  KEY `idx_brand_id` (`brand_id`),
  KEY `idx_date_start` (`date_start`),
  KEY `idx_date_end` (`date_end`)
) ENGINE=MyISAM AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaign`
--

LOCK TABLES `campaign` WRITE;
/*!40000 ALTER TABLE `campaign` DISABLE KEYS */;
INSERT INTO `campaign` VALUES (1,2,'Expand to Video','2013-05-13 00:00:00','2013-09-01 00:00:00',80000,5000,NULL,NULL,'completed'),(2,1,'Email Capture','2013-01-01 00:00:00','2013-01-31 00:00:00',400,13,NULL,NULL,'completed'),(3,5,'Choice of a New Generation','2013-01-01 00:00:00','2013-12-31 00:00:00',100000,5000,NULL,NULL,'completed'),(4,5,'Pepsi Challenge','2013-01-01 00:00:00','2013-12-31 00:00:00',100000,5000,NULL,NULL,'completed'),(5,4,'Coca Cola Classic','2013-01-01 00:00:00','2013-12-31 00:00:00',100000,5000,NULL,NULL,'completed'),(6,4,'Diet Coke','2013-01-01 00:00:00','2013-12-31 00:00:00',100000,5000,NULL,NULL,'completed'),(7,6,'Summer Blast','2013-05-01 00:00:00','2013-09-30 00:00:00',100000,5000,NULL,NULL,'completed'),(8,6,'$5 off with recycled battery','2013-05-01 00:00:00','2013-09-30 00:00:00',100000,5000,NULL,NULL,'completed'),(9,8,'SL Mobi API','2013-05-07 00:00:00','2013-06-02 00:00:00',500000,72000,NULL,NULL,'completed'),(11,9,'DSH','2013-06-03 00:00:00','2013-06-30 00:00:00',10000,1000,NULL,NULL,'completed'),(12,10,'DR','2013-06-01 00:00:00','2013-12-31 00:00:00',0,0,NULL,NULL,'rejected'),(13,11,'Nebraska','2013-06-01 00:00:00','2013-12-31 00:00:00',0,0,NULL,NULL,'completed'),(14,12,'App DL','2013-06-01 00:00:00','2013-12-31 00:00:00',0,0,NULL,NULL,'completed'),(15,13,'App DL','2013-07-01 00:00:00','2013-07-31 00:00:00',0,0,NULL,NULL,'completed'),(16,14,'HSP MNT','2013-03-15 00:00:00','2013-10-31 00:00:00',0,0,NULL,NULL,'completed'),(22,19,'Segments','2013-07-01 00:00:00','2013-12-31 00:00:00',NULL,NULL,NULL,NULL,'completed'),(21,18,'Summer Mobile','2013-07-15 00:00:00','2013-08-30 00:00:00',NULL,NULL,NULL,NULL,'completed'),(19,16,'Mobile Deposit Sweeps','2013-07-01 00:00:00','2013-08-31 00:00:00',0,0,NULL,NULL,'completed'),(23,20,'AFAM FY13 Jul-Aug Mobile','2013-08-01 00:00:00','2013-08-31 00:00:00',0,0,NULL,NULL,'completed'),(24,10,'Long Form','2013-07-01 00:00:00','2013-12-31 00:00:00',0,0,NULL,NULL,'rejected'),(25,21,'AdX Test','2013-07-01 00:00:00','2013-12-31 00:00:00',0,0,NULL,NULL,'completed'),(28,10,'Form v2','2013-07-01 00:00:00','2013-12-31 00:00:00',0,0,NULL,NULL,'completed'),(43,4,'Coke Test','2013-09-04 00:00:00','2013-09-04 00:00:00',1000,100,NULL,NULL,'paused'),(42,4,'Coke Test','2013-09-04 00:00:00','2013-09-04 00:00:00',1000,100,NULL,NULL,'paused'),(41,4,'Coke API Test','2013-09-04 00:00:00','2013-09-05 00:00:00',1000,100,NULL,NULL,'paused'),(40,8,'walmrtscmmig','2013-09-11 00:00:00','2013-09-20 00:00:00',12345678,567890,NULL,NULL,'paused'),(44,10,'UI TEST','2013-09-04 00:00:00','2013-09-04 00:00:00',1000,10,NULL,NULL,'paused'),(45,21,'Motrixi tester','2013-09-05 00:00:00','2013-09-06 00:00:00',50,25,NULL,NULL,'paused'),(46,1,'Walmart test 1','2013-09-05 00:00:00','2013-09-06 00:00:00',100,25,NULL,NULL,'paused'),(47,65,'Todd Test','2013-09-04 00:00:00','2013-09-04 00:00:00',100,10,NULL,NULL,'paused'),(48,67,'Q4 Rockets and Roller Skates','2013-09-09 00:00:00','2013-12-31 00:00:00',1234567,1234,NULL,NULL,'completed'),(49,5,'Slucker financial','2013-09-10 00:00:00','2013-09-11 00:00:00',100,100,NULL,NULL,'completed'),(50,68,'Fall Campaign','2013-09-14 00:00:00','2013-10-31 00:00:00',1000,10,NULL,NULL,'completed'),(51,69,'QA Campaign Name','2013-09-16 00:00:00','2013-10-31 00:00:00',1000,100,NULL,NULL,'rejected'),(52,69,'QA Campaign Name 2','2013-09-16 00:00:00','2013-10-31 00:00:00',1000,100,NULL,NULL,'completed'),(53,70,'CampaignX','2013-09-23 00:00:00','2013-10-31 00:00:00',10000,100,NULL,NULL,'paused'),(54,70,'CampaignY','2013-09-23 00:00:00','2013-10-31 00:00:00',10000,100,NULL,NULL,'running'),(55,71,'Campaign H','2013-09-23 00:00:00','2013-10-31 00:00:00',10000,100,NULL,NULL,'paused'),(56,71,'Camp H','2013-09-23 00:00:00','2013-10-31 00:00:00',10000,100,NULL,NULL,'completed'),(57,2,'New Campaign','0000-00-00 00:00:00','0000-00-00 00:00:00',100000,1000,NULL,NULL,'paused'),(58,67,'Test for Atif','2013-10-24 00:00:00','2013-11-30 00:00:00',10000,100,NULL,NULL,'paused'),(59,73,'Test for Atif 2','2013-10-24 00:00:00','2013-11-30 00:00:00',10000,100,NULL,NULL,'paused'),(60,72,'Cosmo 2013-Q4 Mobile Campaign ','2013-10-30 00:00:00','2013-12-31 00:00:00',50000,500,NULL,NULL,'paused'),(61,10,'test 123','2013-10-31 00:00:00','2013-10-31 00:00:00',100,10,NULL,NULL,'paused'),(62,74,'Inoculation Sweeps winshoes','2013-11-14 00:00:00','2013-12-31 00:00:00',100000,2000,NULL,NULL,'running'),(63,75,'AACM','2013-12-13 00:00:00','2013-12-31 00:00:00',200000,2000,NULL,NULL,'running'),(64,2,'New Campaign','0000-00-00 00:00:00','0000-00-00 00:00:00',100000,1000,1000000,10000,'paused');
/*!40000 ALTER TABLE `campaign` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-01-09 12:45:15
