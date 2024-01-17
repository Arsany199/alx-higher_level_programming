-- make table with attribute id default 1, uniq and the name
CREATE TABLE IF NOT EXISTS `unique_id`(`id` INT DEFAULT 1 UNIQUE, `name` VARCHAR(256));
