
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for loupanindexzz
-- ----------------------------
DROP TABLE IF EXISTS `loupanindex`;
CREATE TABLE `loupanindex` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `unit_price` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `tag` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `louaddress` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `city` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `wuye` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `alright` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `alright_note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `other_name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `location` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `part` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `compart` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `property` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `status` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `sale_time` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `delivery_time` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `marker_address` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `phone_plat` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `presale` json DEFAULT NULL,
  `floor_area` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `gross_area` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `gross_area_ratio` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `floor_area_ratio` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `greening_ratio` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `parking` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `counter_buidings` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `counter_households` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `wuye_corp` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `wuye_cost` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `wuye_note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `status_buidings` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `profile` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `history_price` json DEFAULT NULL,
  `history_post` json DEFAULT NULL,
  `history_kaipan` json DEFAULT NULL,
  `huxin_main` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `nearby_loupan` json DEFAULT NULL,
  `with_loupan` json DEFAULT NULL,
  `buiding_type` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `poi` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `note` json DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1204 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

SET FOREIGN_KEY_CHECKS = 1;
