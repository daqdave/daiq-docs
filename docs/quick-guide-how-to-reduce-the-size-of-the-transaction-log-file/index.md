---
layout: default
title: How to Reduce the Size of the Transaction Log File
nav_order: 260
---

# How to Reduce the Size of the Transaction Log File

![How to Reduce the Size of the Transaction Log File image 01](./images/quick-guide-how-to-reduce-the-size-of-the-transaction-log-file_01.png)

1. Open and login to the *Management Console*.

![How to Reduce the Size of the Transaction Log File image 02](./images/quick-guide-how-to-reduce-the-size-of-the-transaction-log-file_02.png)

![How to Reduce the Size of the Transaction Log File image 03](./images/quick-guide-how-to-reduce-the-size-of-the-transaction-log-file_03.png)

2. Click on *Databases* at the bottom of the window to call up the *Database* screen.

![How to Reduce the Size of the Transaction Log File image 04](./images/quick-guide-how-to-reduce-the-size-of-the-transaction-log-file_04.png)

3. In the *Backup Files* area, type the name of the log file you wish to shrink in the *Name* text field (or
select it from your database directory using the drop-down menu) and click *Backup*.

![How to Reduce the Size of the Transaction Log File image 05](./images/quick-guide-how-to-reduce-the-size-of-the-transaction-log-file_05.png)

![How to Reduce the Size of the Transaction Log File image 06](./images/quick-guide-how-to-reduce-the-size-of-the-transaction-log-file_06.png)

4. The following dialog box will appear:

![How to Reduce the Size of the Transaction Log File image 07](./images/quick-guide-how-to-reduce-the-size-of-the-transaction-log-file_07.png)

Select the *Shrink Transaction Log* option, and then click *Backup* (the green checkmark). The file size of
the log file will be reduced.
Note: it is recommended to create a scheduled, automatic backup of the system with the same *Shrink*
*Transaction Log* option selected. This will create backups for disaster recovery, and manage the size of
the log file.

---

*© DAQ Electronics, LLC*
