-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'meters'
-- 
-- ---

DROP TABLE IF EXISTS `meters`;
        
CREATE TABLE `meters` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `wh_adr` VARCHAR(10) NULL DEFAULT NULL,
  `wh_num` VARCHAR(50) NULL DEFAULT NULL,
  `wh_pass` VARCHAR(50) NULL DEFAULT NULL,
  `object_id` INTEGER NULL DEFAULT NULL,
  `wh_desc` VARCHAR(255) NULL DEFAULT NULL,
  `wh_settings` VARCHAR(255) NULL DEFAULT NULL,
  `protocol_id` INTEGER NULL DEFAULT NULL,
  `channel_id` INTEGER NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'channels'
-- 
-- ---

DROP TABLE IF EXISTS `channels`;
        
CREATE TABLE `channels` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `ch_desc` VARCHAR(255) NULL DEFAULT NULL,
  `ch_ip` VARCHAR(50) NULL DEFAULT NULL,
  `ch_port` INTEGER NULL DEFAULT NULL,
  `is_active` INTEGER NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'protocols'
-- 
-- ---

DROP TABLE IF EXISTS `protocols`;
        
CREATE TABLE `protocols` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `pr_name` VARCHAR(15) NULL DEFAULT NULL,
  `pr_desc` VARCHAR(255) NULL DEFAULT NULL,
  `pr_settings` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'objects'
-- 
-- ---

DROP TABLE IF EXISTS `objects`;
        
CREATE TABLE `objects` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `obj_desc` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'values'
-- 
-- ---

DROP TABLE IF EXISTS `values`;
        
CREATE TABLE `values` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `meter_id` INTEGER NULL DEFAULT NULL,
  `param_num` INTEGER NULL DEFAULT NULL,
  `datetim_rcv` DATETIME NULL DEFAULT NULL,
  `datetime_value` DATETIME NULL DEFAULT NULL,
  `value` DECIMAL NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table Properties
-- ---

ALTER TABLE `meters` ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `channels` ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `protocols` ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `objects` ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `values` ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Foreign Keys 
-- ---

ALTER TABLE `meters` ADD FOREIGN KEY (object_id) REFERENCES `objects` (`id`);
ALTER TABLE `meters` ADD FOREIGN KEY (protocol_id) REFERENCES `protocols` (`id`);
ALTER TABLE `meters` ADD FOREIGN KEY (channel_id) REFERENCES `channels` (`id`);
ALTER TABLE `values` ADD FOREIGN KEY (meter_id) REFERENCES `meters` (`id`);



-- ---
-- Test Data
-- ---

-- INSERT INTO `meters` (`id`,`wh_adr`,`wh_num`,`wh_pass`,`object_id`,`wh_desc`,`wh_settings`,`protocol_id`,`channel_id`) VALUES
-- ('','','','','','','','','');
-- INSERT INTO `channels` (`id`,`ch_desc`,`ch_ip`,`ch_port`) VALUES
-- ('','','','');
-- INSERT INTO `protocols` (`id`,`pr_name`,`pr_desc`,`pr_settings`) VALUES
-- ('','','','');
-- INSERT INTO `objects` (`id`,`obj_desc`) VALUES
-- ('','');
-- INSERT INTO `values` (`id`,`meter_id`,`param_num`,`datetim_rcv`,`datetime_value`,`value`) VALUES
-- ('','','','','','');