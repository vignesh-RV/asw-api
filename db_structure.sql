-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: ashdb
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


CREATE DATABASE ashdb;

--
-- Table structure for table `arrear_fees`
--

DROP TABLE IF EXISTS `arrear_fees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `arrear_fees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(100) NOT NULL,
  `fees` bigint NOT NULL DEFAULT '0',
  `due_date` timestamp NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `punch_type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'IN',
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `parents`
--

DROP TABLE IF EXISTS `parents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parents` (
  `parent_id` bigint NOT NULL AUTO_INCREMENT,
  `parent_type` varchar(100) NOT NULL DEFAULT 'FATHER',
  `full_name` varchar(100) NOT NULL,
  `phone_number` bigint NOT NULL,
  `profile_image` longtext,
  `occupation` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `aadhaar_no` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `student_user_id` bigint NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` bigint NOT NULL DEFAULT '-1',
  `last_modified_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_modified_by` bigint NOT NULL DEFAULT '-1',
  `annual_income` bigint DEFAULT NULL,
  PRIMARY KEY (`parent_id`),
  KEY `parents_FK` (`student_user_id`),
  CONSTRAINT `parents_FK` FOREIGN KEY (`student_user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `transaction_type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'TUITION',
  `amount` bigint NOT NULL DEFAULT '0',
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `object_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `payments_FK` (`user_id`),
  CONSTRAINT `payments_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `placement_fees`
--

DROP TABLE IF EXISTS `placement_fees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `placement_fees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `exam_name` varchar(100) NOT NULL,
  `fees` bigint NOT NULL DEFAULT '0',
  `due_date` timestamp NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `revaluation_fees`
--

DROP TABLE IF EXISTS `revaluation_fees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `revaluation_fees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(100) NOT NULL,
  `fees` bigint NOT NULL DEFAULT '0',
  `due_date` timestamp NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rfids`
--

DROP TABLE IF EXISTS `rfids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rfids` (
  `rf_id` bigint NOT NULL AUTO_INCREMENT,
  `holder_id` bigint NOT NULL,
  `balance` bigint NOT NULL DEFAULT '0',
  `max_limit` bigint NOT NULL DEFAULT '0',
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` bigint NOT NULL DEFAULT '-1',
  `last_modified_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_modified_by` bigint NOT NULL DEFAULT '-1',
  `uuid` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `locked` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`rf_id`),
  KEY `rfids_FK` (`holder_id`),
  CONSTRAINT `rfids_FK` FOREIGN KEY (`holder_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` bigint NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `height` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `dob` date NOT NULL,
  `nationality` varchar(100) NOT NULL,
  `religion` varchar(100) DEFAULT NULL,
  `caste` varchar(100) DEFAULT NULL,
  `mother_tongue` varchar(100) DEFAULT NULL,
  `native_place` varchar(100) DEFAULT NULL,
  `mobile_no` bigint NOT NULL,
  `aadhaar` bigint DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `first_graduate` tinyint(1) NOT NULL DEFAULT '0',
  `reg_no` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` bigint NOT NULL DEFAULT '-1',
  `last_modified_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_modified_by` bigint NOT NULL DEFAULT '-1',
  `user_type` varchar(100) NOT NULL DEFAULT 'STUDENT',
  `batch` varchar(100) DEFAULT NULL,
  `semester` int DEFAULT '1',
  `current_year` int DEFAULT '1',
  `section_name` varchar(100) DEFAULT NULL,
  `course` varchar(100) DEFAULT NULL,
  `school` varchar(100) DEFAULT NULL,
  `blood_group` varchar(100) DEFAULT NULL,
  `course_duration_in_years` int NOT NULL DEFAULT '2',
  `course_fees` bigint NOT NULL DEFAULT '100000',
  `profile_image` longtext,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'ashdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-23 22:14:51


INSERT INTO ashdb.users (user_name, gender, height, weight, dob, nationality, religion, caste, mother_tongue, native_place, mobile_no, aadhaar, email, first_graduate, reg_no, password, created_date, created_by, last_modified_date, last_modified_by, user_type, batch, semester, current_year, section_name, course, school, blood_group, course_duration_in_years, course_fees, profile_image) VALUES('Vignesh Rajagopal', 'MALE', 180, 70, '2025-03-01', 'INDIAN', 'HINDU', 'OBC/BC', 'TAMIL', 'CHENNAI', 8056327227, 232323231456, 'rvikky1995@gmail.com', 0, '123456', 'MTIzNDU2Nzg=', '2025-03-17 20:15:11', -1, '2025-03-23 14:40:36', -1, 'STUDENT', '2023-2025', 1, 1, 'A1', 'COMPUTER SCIENCE AND ENGINEERING', 'School of Computing', 'O+', 2, 100000, '');
