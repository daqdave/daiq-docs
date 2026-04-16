---
layout: default
title: How To Shrink SQL Database Log Files
nav_order: 10
---

# How To Shrink SQL Database Log Files

## Introduction

This document explains how to shrink the database log file on a SQL Server database.

You will need SQL Management Studio.

## Step 1

Open SQL Management Studio, login and find your database.

![HowToShrinkSQLDatabaseLogFiles image 01](./images/HowToShrinkSQLDatabaseLogFiles_01.png)

Or login as Windows authentication.

![HowToShrinkSQLDatabaseLogFiles image 02](./images/HowToShrinkSQLDatabaseLogFiles_02.png)

Find the database.

![HowToShrinkSQLDatabaseLogFiles image 03](./images/HowToShrinkSQLDatabaseLogFiles_03.png)

Here we can see we have a database called SMSDB and it has a 118GB log file that must be released back as disk
space.

## Step 2

Change database to “SIMPLE”.

![HowToShrinkSQLDatabaseLogFiles image 04](./images/HowToShrinkSQLDatabaseLogFiles_04.png)

![HowToShrinkSQLDatabaseLogFiles image 05](./images/HowToShrinkSQLDatabaseLogFiles_05.png)

## Step 3

Release log space.

![HowToShrinkSQLDatabaseLogFiles image 06](./images/HowToShrinkSQLDatabaseLogFiles_06.png)

Make sure that “File type” is changed from “Data” to “Log” (don’t shrink the database otherwise it will run more
slowly.)

![HowToShrinkSQLDatabaseLogFiles image 07](./images/HowToShrinkSQLDatabaseLogFiles_07.png)

Select the “Log” file type.

Make sure the “Release unused space” option is selected.

Click on “OK”.

The log file will be reduced to 1MB.

## Step 4

Restore the database to “FULL”.

![HowToShrinkSQLDatabaseLogFiles image 08](./images/HowToShrinkSQLDatabaseLogFiles_08.png)

---

*© DAQ Electronics, LLC*
