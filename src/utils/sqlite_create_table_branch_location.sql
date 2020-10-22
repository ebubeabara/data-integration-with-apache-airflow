--author:     "Ebube Abara"
--copyright:  "Ebube Abara"
--version:    "1.0"
--maintainer: "Ebube Abara"
--email:      "ebubeabara3@gmail.com"
--status:     "Development"

CREATE TABLE `BRANCH_LOCATION` (
	`id`	    INTEGER NOT NULL UNIQUE,
	`latitude`	FLOAT,
	`longitude`	FLOAT,
	`place`	    TEXT,
	`area_code`	TEXT,
	PRIMARY KEY(`id`)
);

COMMIT;
