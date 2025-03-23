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

INSERT INTO ashdb.parents (parent_type, full_name, phone_number, profile_image, occupation, designation, aadhaar_no, email, student_user_id, created_date, created_by, last_modified_date, last_modified_by, annual_income) VALUES('FATHER', 'My Father ', 9292929922, 'data:image/jpeg;base64,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', 'FARMER', 'OWNER', '223232122222', 'fatheremail@gmail.com', 1, '2025-03-23 14:49:38', -1, '2025-03-23 14:49:38', 1, 123123);
INSERT INTO ashdb.parents (parent_type, full_name, phone_number, profile_image, occupation, designation, aadhaar_no, email, student_user_id, created_date, created_by, last_modified_date, last_modified_by, annual_income) VALUES('MOTHER', 'My Mother', 4444444222, 'data:image/jpeg;base64,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', 'HOUSE WIFE', '', '222222222222', 'motheremail@gmail.com', 1, '2025-03-23 14:49:38', -1, '2025-03-23 14:49:38', 1, 1221312);
