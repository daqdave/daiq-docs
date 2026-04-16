---
layout: default
title: How to Set Up SQL Server for Remote Client Access
nav_order: 310
---

# How to Set Up SQL Server for Remote Client Access

![How to Set Up SQL Server for Remote Client Access image 01](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_01.png)

*A network-related or instance-specific error occurred while establishing a connection to SQL Server.*
*The server was not found or was not accessible. Verify that the instance name is correct and that SQL*
*Server is configured to allow remote connections. (provider: Named Pipes Provider, error: 40 - Could*
*not open a connection to SQL Server)*

![How to Set Up SQL Server for Remote Client Access image 02](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_02.png)

## How to solve this issue?

There are a few things that might be going on here (all of the following configurations are made on the
computer running your *SQL Server 2008* instance).

![How to Set Up SQL Server for Remote Client Access image 03](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_03.png)

## Allow remote connections to this server

The first thing to check is if *Remote Connections* are enabled on your *SQL Server* database. In *SQL*
*Server 2008* you do this by opening SQL Server 2008 Management Studio, connect to the server in
question, right-click the server, and open the *Server Properties*.

![How to Set Up SQL Server for Remote Client Access image 04](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_04.png)

![How to Set Up SQL Server for Remote Client Access image 05](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_05.png)

![How to Set Up SQL Server for Remote Client Access image 06](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_06.png)

Navigate to *Remote Server Connections* and ensure that *Allow remote connections to this server* is
checked. Check if this solves the problem.

![How to Set Up SQL Server for Remote Client Access image 07](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_07.png)

## Protocols for MSSQLServer

If you are still running into issues, the next thing to check is the *SQL Server Network Configuration*.
Open the *SQL Server Configuration Manager*, unfold the node *SQL Server Network Configuration* and
select *Protocols for MSSQLServer* (or whatever the name of your SQL Server instance is).

![How to Set Up SQL Server for Remote Client Access image 08](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_08.png)

Make sure that *TCP/IP* is enabled, and try again.

![How to Set Up SQL Server for Remote Client Access image 09](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_09.png)

## The Firewall

If there is still no communication happening between your computer and the remote *SQL Server*, you
most likely need to configure your firewall settings. A good first step is to figure out which port is being
used by TCP/IP (and which you need to open in your firewall). You can do this by right clicking *TCP/IP*
and selecting *Properties*.

![How to Set Up SQL Server for Remote Client Access image 10](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_10.png)

Click on the *IP Addresses* tab and check the port (Port 1433 in this example). Next, you will need to
allow inbound TCP/IP traffic on this port in your firewall. In Windows 7, this works as follows:

![How to Set Up SQL Server for Remote Client Access image 11](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_11.png)

Open the *Control Panel* and navigate to *Windows Firewall*.

![How to Set Up SQL Server for Remote Client Access image 12](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_12.png)

Click on *Advanced Settings* on the left-hand side and you should see the *Windows Firewall with*
*Advanced Security*.

![How to Set Up SQL Server for Remote Client Access image 13](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_13.png)

Select *Inboud Rules* on the left-hand side and click on *New Rule* on the right-hand side.

![How to Set Up SQL Server for Remote Client Access image 14](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_14.png)

![How to Set Up SQL Server for Remote Client Access image 15](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_15.png)

This opens the *New Inbound Rule Wizard*, which you can use to allow inbound traffic on the required
port for TCP/IP (exactly how you configured your *SQL Server* in the steps above). Proceed with the
following steps:

![How to Set Up SQL Server for Remote Client Access image 16](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_16.png)

![How to Set Up SQL Server for Remote Client Access image 17](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_17.png)

![How to Set Up SQL Server for Remote Client Access image 18](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_18.png)

![How to Set Up SQL Server for Remote Client Access image 19](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_19.png)

![How to Set Up SQL Server for Remote Client Access image 20](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_20.png)

![How to Set Up SQL Server for Remote Client Access image 21](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_21.png)

![How to Set Up SQL Server for Remote Client Access image 22](./images/quick-guide-how-to-set-up-sql-server-for-remote-client-access_22.png)

---

*© DAQ Electronics, LLC*
