CREATE DATABASE IF NOT EXISTS `lampapplication`;

USE `lampapplication`;

CREATE TABLE `profiles` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `minimum` int(11) NOT NULL,
  `maximum` int(11) NOT NULL
);

INSERT INTO `profiles` (`id`, `name`, `minimum`, `maximum`) VALUES
(1, 'current', 60, 100),
(2, 'default', 50, 70);

ALTER TABLE `profiles`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `profiles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
