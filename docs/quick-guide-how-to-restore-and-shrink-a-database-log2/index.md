---
layout: default
title: How to Restore and Shrink a Database Log Using SQL Management Studio
nav_order: 280
---

# How to Restore and Shrink a Database Log Using SQL Management Studio

![How to Restore and Shrink a Database Log Using SQL Management Studio image 01](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_01.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 02](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_02.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 03](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_03.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 04](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_04.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 05](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_05.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 06](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_06.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 07](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_07.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 08](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_08.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 09](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_09.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 10](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_10.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 11](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_11.png)

Create a new query in *SQL Studio* using the following script and replace *MYDBNAME* with the site
database name:
USE MYDBNAME;

## GO

-- Truncate the log by changing the database recovery model to SIMPLE.

## ALTER DATABASE MYDBNAME

SET RECOVERY SIMPLE;

## GO

-- Shrink the truncated log file to 1 MB.
DBCC SHRINKFILE (MYDBNAME_Log, 1);

## GO

-- Reset the database recovery model.

## ALTER DATABASE MYDBNAME

SET RECOVERY FULL;

## GO

![How to Restore and Shrink a Database Log Using SQL Management Studio image 12](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_12.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 13](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_13.png)

![How to Restore and Shrink a Database Log Using SQL Management Studio image 14](./images/quick-guide-how-to-restore-and-shrink-a-database-log2_14.png)

---

*© DAQ Electronics, LLC*
