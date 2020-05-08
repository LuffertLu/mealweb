-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: meal_dev
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('35d5b05c65d9');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cook`
--

DROP TABLE IF EXISTS `cook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cookname` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cook`
--

LOCK TABLES `cook` WRITE;
/*!40000 ALTER TABLE `cook` DISABLE KEYS */;
INSERT INTO `cook` VALUES (1,'蒸'),(2,'煮'),(3,'拌'),(4,'烤'),(5,'炸'),(6,'烧'),(7,'炒'),(8,'爆'),(9,'焖'),(10,'炖'),(11,'烩'),(12,'溜'),(13,'氽'),(14,'卤'),(15,'炝'),(16,'煎'),(17,'煨'),(18,'酱'),(19,'煲'),(20,'砂锅'),(21,'烙'),(22,'焗'),(23,'焯'),(24,'干煸'),(25,'干锅');
/*!40000 ALTER TABLE `cook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuisine`
--

DROP TABLE IF EXISTS `cuisine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cuisine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cuisinename` varchar(64) NOT NULL,
  `cuisine_url` text NOT NULL,
  `cuisine_time` datetime DEFAULT NULL,
  `cook_id` int(11) NOT NULL,
  `taste_id` int(11) NOT NULL,
  `food_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cook_id` (`cook_id`),
  KEY `taste_id` (`taste_id`),
  KEY `food_id` (`food_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `cuisine_ibfk_1` FOREIGN KEY (`cook_id`) REFERENCES `cook` (`id`),
  CONSTRAINT `cuisine_ibfk_2` FOREIGN KEY (`taste_id`) REFERENCES `taste` (`id`),
  CONSTRAINT `cuisine_ibfk_3` FOREIGN KEY (`food_id`) REFERENCES `food` (`id`),
  CONSTRAINT `cuisine_ibfk_4` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuisine`
--

LOCK TABLES `cuisine` WRITE;
/*!40000 ALTER TABLE `cuisine` DISABLE KEYS */;
INSERT INTO `cuisine` VALUES (1,'水煮牛肉','http','2020-02-07 15:58:22',1,1,3,1),(2,'西红柿炒鸡蛋','http','2020-02-07 16:03:06',4,2,2,2),(3,'烤鱼','http','2020-02-07 16:03:06',2,3,5,2),(4,'天妇罗','http','2020-02-07 16:01:33',3,4,4,1),(5,'胡萝卜炖牛肉','http','2020-02-07 16:03:06',1,1,3,2),(6,'蒜茸西兰花','http','2020-02-07 16:03:06',4,2,4,2);
/*!40000 ALTER TABLE `cuisine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `file`
--

DROP TABLE IF EXISTS `file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `path` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file`
--

LOCK TABLES `file` WRITE;
/*!40000 ALTER TABLE `file` DISABLE KEYS */;
INSERT INTO `file` VALUES (2,'f1','example_1.pdf'),(3,'f2','example_2.pdf'),(4,'f3','example_3.pdf');
/*!40000 ALTER TABLE `file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `foodname` varchar(64) DEFAULT NULL,
  `species` varchar(64) DEFAULT NULL,
  `mature_week` int(11) DEFAULT NULL,
  `validweeks` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`
--

LOCK TABLES `food` WRITE;
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
INSERT INTO `food` VALUES (1,'鸡','肉禽类',0,52),(2,'羊','肉禽类',0,52),(3,'牛','肉禽类',0,52),(4,'猪','肉禽类',0,52),(5,'鸭','肉禽类',0,52),(6,'鹅','肉禽类',0,52),(7,'排','肉禽类',0,52),(8,'腿','肉禽类',0,52),(9,'肉','肉禽类',0,52),(10,'骨','肉禽类',0,52),(11,'腩','肉禽类',0,52),(12,'翅','肉禽类',0,52),(13,'蛋','肉禽类',0,52),(14,'脊','肉禽类',0,52);
/*!40000 ALTER TABLE `food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `image`
--

DROP TABLE IF EXISTS `image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `path` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
INSERT INTO `image` VALUES (5,'shizi','lion.jpg'),(6,'baozi','leopard.jpg'),(8,'daxiang','elephant.jpg');
/*!40000 ALTER TABLE `image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `page`
--

DROP TABLE IF EXISTS `page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `page` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `text` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `page`
--

LOCK TABLES `page` WRITE;
/*!40000 ALTER TABLE `page` DISABLE KEYS */;
/*!40000 ALTER TABLE `page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rolename` varchar(64) NOT NULL,
  `default` tinyint(1) DEFAULT NULL,
  `permission` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rolename` (`rolename`),
  KEY `ix_role_default` (`default`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'User',0,7),(2,'Moderator',1,15),(3,'Administrator',0,31);
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taste`
--

DROP TABLE IF EXISTS `taste`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taste` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tastename` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taste`
--

LOCK TABLES `taste` WRITE;
/*!40000 ALTER TABLE `taste` DISABLE KEYS */;
INSERT INTO `taste` VALUES (1,'其他'),(2,'微辣'),(3,'中辣'),(4,'超辣'),(5,'麻辣'),(6,'酸辣'),(7,'甜辣'),(8,'香辣'),(9,'酸甜'),(10,'酸咸'),(11,'咸鲜'),(12,'咸甜'),(13,'甜味'),(14,'苦味'),(15,'原味'),(16,'清淡'),(17,'五香'),(18,'鱼香'),(19,'葱香'),(20,'蒜香'),(21,'奶香'),(22,'酱香'),(23,'糟香'),(24,'咖喱'),(25,'孜然'),(26,'果味'),(27,'香草'),(28,'怪味'),(29,'咸香'),(30,'甜香'),(31,'麻香');
/*!40000 ALTER TABLE `taste` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) NOT NULL,
  `confirmed` tinyint(1) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `_User__password_hash` varchar(128) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `location` varchar(64) DEFAULT NULL,
  `about_me` text,
  `member_since` datetime DEFAULT NULL,
  `last_seen` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_username` (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'appadmin',1,'appdevelopment@126.com','pbkdf2:sha256:150000$2QHj9fjM$2d2718f2c9ebf1e941347f93e1f6a10a7e7daa0e3434885c2303101af9bc145f',3,'北京','管理员','2020-02-07 15:58:22','2020-02-16 14:41:17'),(2,'user2',1,'user2@mealweb.com','pbkdf2:sha256:150000$QuO9nhYs$8c24388312f91b114214104308c2a4773317439819ef2a3f8f56157acdea5675',2,'上海','ertyrewgersgegreagf','2020-02-07 16:03:06','2020-02-07 16:03:06'),(3,'user3',1,'user3@mealweb.com','pbkdf2:sha256:150000$JbhjnR4t$5ce9eaa1e7c10289a1f47e213d1c942ca6f227bc52010b59c384cddbed2929c1',1,'new york','ewtrq43rsfeargwq4g','2020-02-07 16:03:06','2020-02-07 16:03:06');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-16 14:48:58
