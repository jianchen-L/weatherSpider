DROP TABLE IF EXISTS `weather_spider`;
CREATE TABLE `weather_spider` (
  `time_local` varchar(255) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `weather_type` varchar(255) DEFAULT NULL,
  `temperature` varchar(255) DEFAULT NULL,
  `wind_power` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
