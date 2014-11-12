-- MySQL dump 10.13  Distrib 5.6.11, for Win32 (x86)
--
-- Host: localhost    Database: wages
-- ------------------------------------------------------
-- Server version	5.6.12

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
-- Table structure for table `advance_amount`
--

DROP TABLE IF EXISTS `advance_amount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `advance_amount` (
  `advance_amount_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_information_id` int(11) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`advance_amount_id`),
  KEY `employee_information_id` (`employee_information_id`),
  CONSTRAINT `advance_amount_ibfk_1` FOREIGN KEY (`employee_information_id`) REFERENCES `employee_information` (`employee_information_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `advance_amount`
--

LOCK TABLES `advance_amount` WRITE;
/*!40000 ALTER TABLE `advance_amount` DISABLE KEYS */;
/*!40000 ALTER TABLE `advance_amount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allowance`
--

DROP TABLE IF EXISTS `allowance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `allowance` (
  `allowance_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `allowance_type` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `applicable` varchar(255) DEFAULT NULL,
  `regular_wages_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`allowance_id`),
  KEY `regular_wages_id` (`regular_wages_id`),
  CONSTRAINT `allowance_ibfk_1` FOREIGN KEY (`regular_wages_id`) REFERENCES `regular_wages_setup` (`regular_wages_setup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `allowance`
--

LOCK TABLES `allowance` WRITE;
/*!40000 ALTER TABLE `allowance` DISABLE KEYS */;
INSERT INTO `allowance` VALUES (1,'travels','Fix','100','2',1);
/*!40000 ALTER TABLE `allowance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_information_id` int(11) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `regular_wages_setup_id` int(11) DEFAULT NULL,
  `positions_id` int(11) DEFAULT NULL,
  `working_hour` varchar(255) DEFAULT NULL,
  `leaves_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`),
  KEY `employee_information_id` (`employee_information_id`),
  KEY `regular_wages_setup_id` (`regular_wages_setup_id`),
  KEY `positions_id` (`positions_id`),
  KEY `leaves_id` (`leaves_id`),
  CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`employee_information_id`) REFERENCES `employee_information` (`employee_information_id`),
  CONSTRAINT `attendance_ibfk_2` FOREIGN KEY (`regular_wages_setup_id`) REFERENCES `regular_wages_setup` (`regular_wages_setup_id`),
  CONSTRAINT `attendance_ibfk_3` FOREIGN KEY (`positions_id`) REFERENCES `positions` (`positions_id`),
  CONSTRAINT `attendance_ibfk_4` FOREIGN KEY (`leaves_id`) REFERENCES `leaves` (`leaves_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(255) NOT NULL,
  `company_category` varchar(255) NOT NULL,
  `address_line1` varchar(255) NOT NULL,
  `address_line2` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `pin_no` varchar(255) NOT NULL,
  `nationality` varchar(255) NOT NULL,
  `mobile_no1` int(11) NOT NULL,
  `mobile_no2` int(11) NOT NULL,
  `landline_no` int(11) NOT NULL,
  `website` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deduction`
--

DROP TABLE IF EXISTS `deduction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deduction` (
  `deduction_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `deduction_type` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `applicable` varchar(255) DEFAULT NULL,
  `regular_wages_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`deduction_id`),
  KEY `regular_wages_id` (`regular_wages_id`),
  CONSTRAINT `deduction_ibfk_1` FOREIGN KEY (`regular_wages_id`) REFERENCES `regular_wages_setup` (`regular_wages_setup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deduction`
--

LOCK TABLES `deduction` WRITE;
/*!40000 ALTER TABLE `deduction` DISABLE KEYS */;
INSERT INTO `deduction` VALUES (1,'fpnf','%','8','2',1);
/*!40000 ALTER TABLE `deduction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `department_name` varchar(255) NOT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_information`
--

DROP TABLE IF EXISTS `employee_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_information` (
  `employee_information_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `employee_id` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `dob` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `pin_no` varchar(255) NOT NULL,
  `nationality` varchar(255) NOT NULL,
  `mobile_no1` int(11) NOT NULL,
  `mobile_no2` int(11) NOT NULL,
  `landline_no` int(11) NOT NULL,
  `fnpf` varchar(255) NOT NULL,
  `account_no` int(11) NOT NULL,
  `payment_type` varchar(255) DEFAULT NULL,
  `rate` varchar(255) NOT NULL,
  `date_of_joining` varchar(255) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  `regular_wages_setup_id` int(11) DEFAULT NULL,
  `non_regular_wages_setup_id` int(11) DEFAULT NULL,
  `employee_type` varchar(255) DEFAULT NULL,
  `positions_id_positions` int(11) DEFAULT NULL,
  PRIMARY KEY (`employee_information_id`),
  KEY `positions_id_positions` (`positions_id_positions`),
  CONSTRAINT `employee_information_ibfk_2` FOREIGN KEY (`positions_id_positions`) REFERENCES `positions` (`positions_id`),
  CONSTRAINT `employee_information_ibfk_1` FOREIGN KEY (`positions_id_positions`) REFERENCES `positions` (`positions_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_information`
--

LOCK TABLES `employee_information` WRITE;
/*!40000 ALTER TABLE `employee_information` DISABLE KEYS */;
INSERT INTO `employee_information` VALUES (1,'pankaj','asdf','asdf','male','2000-01-01','sdf','asdf','asdf','asdf','asdf','asdf',23,23,23,'23232',23223,'Salary','20000','2000-01-01','splash.png',1,0,'Skilled',1),(2,'mohit','asdf','asdf','male','2000-01-01','asdf','asdf','asdf','dffdf','asdf','asdf',434,3434,3434,'33323232',323232,'Salary','15000','2000-01-01','splash.png',1,0,'Skilled',1),(3,'rajesh','asdf','asdf','male','2000-01-01','asdf','asdf','sadf','asdf','asdfasdf','asdf',1221,12121,12121,'2121212',12111,'Salary','20000','2000-01-01','splash.png',1,0,'Skilled',1),(4,'kanchan','asdfa','sdfasf','female','2000-01-01','asdfdasf','sdf','asdf','asdf','asdf','asdf',11212,1212,112,'232',2232,'Wages','10','2000-01-01','splash.png',1,0,'Unskilled',2),(5,'prachi','asdfa','sdfas','female','2000-01-01','asdfasf','asdf','asdf','asdf','asdf','asdf',343,3434,434,'2323',23232,'Wages','10','2000-01-01','splash.png',1,0,'Unskilled',2);
/*!40000 ALTER TABLE `employee_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_type`
--

DROP TABLE IF EXISTS `employee_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_type` (
  `employee_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`employee_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_type`
--

LOCK TABLES `employee_type` WRITE;
/*!40000 ALTER TABLE `employee_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employer_information`
--

DROP TABLE IF EXISTS `employer_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employer_information` (
  `employer_information_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `dob` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `pin_no` varchar(255) NOT NULL,
  `nationality` varchar(255) NOT NULL,
  `mobile_no1` int(11) NOT NULL,
  `mobile_no2` int(11) NOT NULL,
  `landline_no` int(11) NOT NULL,
  `account_no` int(11) NOT NULL,
  `website` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`employer_information_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employer_information`
--

LOCK TABLES `employer_information` WRITE;
/*!40000 ALTER TABLE `employer_information` DISABLE KEYS */;
/*!40000 ALTER TABLE `employer_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `holiday`
--

DROP TABLE IF EXISTS `holiday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `holiday` (
  `holiday_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `payment_type` varchar(255) DEFAULT NULL,
  `applicable` varchar(255) DEFAULT NULL,
  `regular_wages_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`holiday_id`),
  KEY `regular_wages_id` (`regular_wages_id`),
  CONSTRAINT `holiday_ibfk_1` FOREIGN KEY (`regular_wages_id`) REFERENCES `regular_wages_setup` (`regular_wages_setup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `holiday`
--

LOCK TABLES `holiday` WRITE;
/*!40000 ALTER TABLE `holiday` DISABLE KEYS */;
INSERT INTO `holiday` VALUES (1,'company function','Standard','2',1),(2,'accidantal','Standard','2',1);
/*!40000 ALTER TABLE `holiday` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leaves`
--

DROP TABLE IF EXISTS `leaves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `leaves` (
  `leaves_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `payment_type` varchar(255) NOT NULL,
  `total_leave` varchar(255) NOT NULL,
  `applicable` varchar(255) DEFAULT NULL,
  `shift_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`leaves_id`),
  KEY `shift_id` (`shift_id`),
  CONSTRAINT `leaves_ibfk_1` FOREIGN KEY (`shift_id`) REFERENCES `regular_wages_setup` (`regular_wages_setup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leaves`
--

LOCK TABLES `leaves` WRITE;
/*!40000 ALTER TABLE `leaves` DISABLE KEYS */;
INSERT INTO `leaves` VALUES (1,'Yearly','Standard','12','2',1),(2,'sick leave','Standard','12','2',1),(3,'breavelent','Standard','3','2',1),(4,'voting','Standard','1','2',1),(5,'manager approve','Standard','','2',1),(6,'unapproved','Standard','','2',1);
/*!40000 ALTER TABLE `leaves` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `non_regular_wages_employee_info`
--

DROP TABLE IF EXISTS `non_regular_wages_employee_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `non_regular_wages_employee_info` (
  `non_regular_wages_employee_info_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_name` varchar(255) DEFAULT NULL,
  `employee_id` varchar(255) DEFAULT NULL,
  `salary` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `bonus` varchar(255) DEFAULT NULL,
  `comissions` varchar(255) DEFAULT NULL,
  `tips` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`non_regular_wages_employee_info_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `non_regular_wages_employee_info`
--

LOCK TABLES `non_regular_wages_employee_info` WRITE;
/*!40000 ALTER TABLE `non_regular_wages_employee_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `non_regular_wages_employee_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `non_regular_wages_setup`
--

DROP TABLE IF EXISTS `non_regular_wages_setup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `non_regular_wages_setup` (
  `non_regular_wages_setup_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `bonus` varchar(255) NOT NULL,
  `comissions` varchar(255) NOT NULL,
  `tips` varchar(255) NOT NULL,
  PRIMARY KEY (`non_regular_wages_setup_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `non_regular_wages_setup`
--

LOCK TABLES `non_regular_wages_setup` WRITE;
/*!40000 ALTER TABLE `non_regular_wages_setup` DISABLE KEYS */;
/*!40000 ALTER TABLE `non_regular_wages_setup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pay_advance_amount`
--

DROP TABLE IF EXISTS `pay_advance_amount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pay_advance_amount` (
  `pay_advance_amount_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_information_id` int(11) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `pay_amount` varchar(255) DEFAULT NULL,
  `advance_amount_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`pay_advance_amount_id`),
  KEY `advance_amount_id` (`advance_amount_id`),
  CONSTRAINT `pay_advance_amount_ibfk_1` FOREIGN KEY (`advance_amount_id`) REFERENCES `advance_amount` (`advance_amount_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pay_advance_amount`
--

LOCK TABLES `pay_advance_amount` WRITE;
/*!40000 ALTER TABLE `pay_advance_amount` DISABLE KEYS */;
/*!40000 ALTER TABLE `pay_advance_amount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_type`
--

DROP TABLE IF EXISTS `payment_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment_type` (
  `payment_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `rate` varchar(255) NOT NULL,
  PRIMARY KEY (`payment_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_type`
--

LOCK TABLES `payment_type` WRITE;
/*!40000 ALTER TABLE `payment_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `positions`
--

DROP TABLE IF EXISTS `positions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `positions` (
  `positions_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`positions_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `positions`
--

LOCK TABLES `positions` WRITE;
/*!40000 ALTER TABLE `positions` DISABLE KEYS */;
INSERT INTO `positions` VALUES (1,'hr'),(2,'worker');
/*!40000 ALTER TABLE `positions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `public_holiday`
--

DROP TABLE IF EXISTS `public_holiday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `public_holiday` (
  `public_holiday_leave_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`public_holiday_leave_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `public_holiday`
--

LOCK TABLES `public_holiday` WRITE;
/*!40000 ALTER TABLE `public_holiday` DISABLE KEYS */;
INSERT INTO `public_holiday` VALUES (1,'dfdf','2013-12-02'),(2,'sdsd','2013-12-11'),(3,'sds','2013-12-20');
/*!40000 ALTER TABLE `public_holiday` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regular_wages_setup`
--

DROP TABLE IF EXISTS `regular_wages_setup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `regular_wages_setup` (
  `regular_wages_setup_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `minimum_hour` varchar(255) NOT NULL,
  `maximum_hour` varchar(255) NOT NULL,
  `week_start` varchar(255) NOT NULL,
  `week_end` varchar(255) NOT NULL,
  `double_time` varchar(255) NOT NULL,
  `time_and_half` varchar(255) NOT NULL,
  `public_holiday_leave_id_public_holiday` int(11) DEFAULT NULL,
  PRIMARY KEY (`regular_wages_setup_id`),
  KEY `public_holiday_leave_id_public_holiday` (`public_holiday_leave_id_public_holiday`),
  CONSTRAINT `regular_wages_setup_ibfk_1` FOREIGN KEY (`public_holiday_leave_id_public_holiday`) REFERENCES `public_holiday` (`public_holiday_leave_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regular_wages_setup`
--

LOCK TABLES `regular_wages_setup` WRITE;
/*!40000 ALTER TABLE `regular_wages_setup` DISABLE KEYS */;
INSERT INTO `regular_wages_setup` VALUES (1,'Fix Salary','6','14','Monday','Saturday','9','9',NULL);
/*!40000 ALTER TABLE `regular_wages_setup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tax`
--

DROP TABLE IF EXISTS `tax`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tax` (
  `tax_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `tax_type` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `applicable` varchar(255) DEFAULT NULL,
  `regular_wages_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`tax_id`),
  KEY `regular_wages_id` (`regular_wages_id`),
  CONSTRAINT `tax_ibfk_1` FOREIGN KEY (`regular_wages_id`) REFERENCES `regular_wages_setup` (`regular_wages_setup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tax`
--

LOCK TABLES `tax` WRITE;
/*!40000 ALTER TABLE `tax` DISABLE KEYS */;
INSERT INTO `tax` VALUES (1,'goverment','%','3','2',1),(2,'helth','%','2','2',1);
/*!40000 ALTER TABLE `tax` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `title`
--

DROP TABLE IF EXISTS `title`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `title` (
  `title_id` int(11) NOT NULL AUTO_INCREMENT,
  `title_name` varchar(255) DEFAULT NULL,
  `title_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`title_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `title`
--

LOCK TABLES `title` WRITE;
/*!40000 ALTER TABLE `title` DISABLE KEYS */;
INSERT INTO `title` VALUES (1,'Yearly','Leave'),(2,'sick leave','Leave'),(3,'breavelent','Leave'),(4,'voting','Leave'),(5,'manager approve','Leave'),(6,'unapproved','Leave'),(7,'function','Holiday'),(8,'accidantal','Holiday'),(9,'goverment','Tax'),(10,'helth','Tax'),(11,'fpnf','Deduction'),(12,'travels','Allowance');
/*!40000 ALTER TABLE `title` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-12-23 19:49:10
