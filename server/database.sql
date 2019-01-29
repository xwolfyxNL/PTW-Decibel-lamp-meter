CREATE DATABASE IF NOT EXISTS `lampapplication`;

USE `lampapplication`;

CREATE TABLE `profiles` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `minimum` int(11) NOT NULL,
  `maximum` int(11) NOT NULL
);

INSERT INTO `profiles` (`id`, `name`, `minimum`, `maximum`) VALUES
(1, 'current', 50, 70),
(2, 'default', 50, 70),
(3, 'stil', 40, 60),
(4, 'druk', 55, 75);

ALTER TABLE `profiles`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `profiles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
