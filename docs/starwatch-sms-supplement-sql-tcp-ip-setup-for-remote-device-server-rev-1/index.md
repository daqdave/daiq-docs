---
layout: default
title: SQL TCP/IP Setup for Remote Device Server
nav_order: 620
---

# SQL TCP/IP Setup for Remote Device Server

![SQL TCP/IP Setup for Remote Device Server image 01](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_01.png)

## 1.0 SQL TCP/IP SETUP FOR REMOTE DEVICE SERVER

## 1.1 ALLOW TCP/IP REMOTE CONNECTIONS

On the *Application Server* computer, set up SQL to allow TCP/IP remote connections using the steps
below:
1. Using the *Start* menu on the desktop, call up the *Control Panel* application.

![SQL TCP/IP Setup for Remote Device Server image 02](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_02.png)

2. From the options listed, select *Administrative Tools*.

![SQL TCP/IP Setup for Remote Device Server image 03](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_03.png)

![SQL TCP/IP Setup for Remote Device Server image 04](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_04.png)

3. Next, from the *Administrative Tools* window, select the *Computer Management* option.

![SQL TCP/IP Setup for Remote Device Server image 05](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_05.png)

![SQL TCP/IP Setup for Remote Device Server image 06](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_06.png)

4. In the left pane of the *Computer Management* window, browse to:
*Services and Applications>*
*SQL Server Configuration Manager>*
*SQL Server Network Configuration>*
*Protocols for SQLEXPRESS*

![SQL TCP/IP Setup for Remote Device Server image 07](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_07.png)

5. Next, in the center pane of the *Computer Management* window, right-click on the *TCP/IP*
option and select *Enable*.

![SQL TCP/IP Setup for Remote Device Server image 08](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_08.png)

6. Close the *Computer Management* window.
7. Back in the *Administrative Tools* window, select the *Services* option.

![SQL TCP/IP Setup for Remote Device Server image 09](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_09.png)

8. In the *Services* window, browse to the *SQL Server* option.

![SQL TCP/IP Setup for Remote Device Server image 10](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_10.png)

Right-click on *SQL Server* in the list and select *Stop*.

![SQL TCP/IP Setup for Remote Device Server image 11](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_11.png)

9. After the service has stopped, right-click on *SQL Server* a second time and select *Start*. You can
now connect from the remote machine.
10. Close the *Services* window.
11. Close the *Administrative Tools* window.
12. Close the *Control Panel* application.

## 1.2 ENABLE REMOTE LOGIN FOR THE DEVICE SERVER

On the *Application Server*, update the configuration so that the new *Device Server* machine will be
able to login to the system using the steps below:
1. Login to the *StarWatch SMS* application.
2. Open the *Admin* panel.

![SQL TCP/IP Setup for Remote Device Server image 12](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_12.png)

3. Next, launch the *Workstations* function by clicking on the
icon
located on the *Computers* segment of the *Admin* list on the left side of the screen.

![SQL TCP/IP Setup for Remote Device Server image 13](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_13.png)

![SQL TCP/IP Setup for Remote Device Server image 14](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_14.png)

![SQL TCP/IP Setup for Remote Device Server image 15](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_15.png)

4. Click the
button at the top of the *Workstation* pane to the right of the screen to add a
new *Workstation* to the list.
5. In the *New Workstation* pop-up window, type in a name for the *Workstation* and click the *OK*
button. In this example we used *RDS* to designate the *Remote Device Server*.

![SQL TCP/IP Setup for Remote Device Server image 16](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_16.png)

6. Click on the new *Workstation* in the list to edit the associated properties displayed in the
center workspace.

![SQL TCP/IP Setup for Remote Device Server image 17](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_17.png)

![SQL TCP/IP Setup for Remote Device Server image 18](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_18.png)

7. In the *Workstation Details* area, enter the computer name in the *Host Name* field.

![SQL TCP/IP Setup for Remote Device Server image 19](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_19.png)

8. Again in the *Workstation Details* area, enter the IP address in the *IP Address* field.
9. In the *Roles* area, enter *Access 24x7* for the *Administrator* login calendar. Note: you can use a
different calendar if you wish to restrict login rights.

![SQL TCP/IP Setup for Remote Device Server image 20](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_20.png)

10. Click the
button to save your changes.
11. Close the *StarWatch SMS* application.

![SQL TCP/IP Setup for Remote Device Server image 21](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_21.png)

## 1.3 ADD THE DEVICE SERVER

1. On the *Application Server*, open the *Site Builder* application.

![SQL TCP/IP Setup for Remote Device Server image 22](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_22.png)

2.  Select *Options* from the menu on the left side of the screen.

![SQL TCP/IP Setup for Remote Device Server image 23](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_23.png)

![SQL TCP/IP Setup for Remote Device Server image 24](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_24.png)

3. In the *BACnet Discovery Interface* parameter, select the *LAN* interface option from the
provided drop-down list.

![SQL TCP/IP Setup for Remote Device Server image 25](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_25.png)

![SQL TCP/IP Setup for Remote Device Server image 26](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_26.png)

4. Click the
button.
5. Next, open the *Devices* panel by clicking the red *Devices* tile.

![SQL TCP/IP Setup for Remote Device Server image 27](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_27.png)

![SQL TCP/IP Setup for Remote Device Server image 28](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_28.png)

6. Click on the small *Plus* icon in the lower right corner of the *Add New Node* box.

![SQL TCP/IP Setup for Remote Device Server image 29](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_29.png)

![SQL TCP/IP Setup for Remote Device Server image 30](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_30.png)

7. In the *Add Device Server* window, enter the computer name for the new *Device Server* in the
*Name* field. Note: This can be an IP address if the connection between the two servers is not
WiFi.  For WiFi, it must be the computer name only.

![SQL TCP/IP Setup for Remote Device Server image 31](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_31.png)

![SQL TCP/IP Setup for Remote Device Server image 32](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_32.png)

8. Click the
button.

![SQL TCP/IP Setup for Remote Device Server image 33](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_33.png)

![SQL TCP/IP Setup for Remote Device Server image 34](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_34.png)

![SQL TCP/IP Setup for Remote Device Server image 35](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_35.png)

9. Hit the back arrow
at the top left of the screen to update the system.
10. Close the *Site Builder* application.

![SQL TCP/IP Setup for Remote Device Server image 36](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_36.png)

## 1.4 SET UP THE REMOTE DEVICE SERVER

1. Install *StarWatch SMS* on the remote machine as a *Device Server* using the installation .msi file
that matches the version on the *Application Server*. We will refer to this machine as the
*Remote Device Server (RDS)*.
2. Copy the *C:\Starwatch\Client* folder in its entirety from the *Application Server* onto the *RDS* as
*C:\Starwatch\Client* so we can run the *Site Builder*.
3. On the *RDS*, open the *Management Console* application.

![SQL TCP/IP Setup for Remote Device Server image 37](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_37.png)

![SQL TCP/IP Setup for Remote Device Server image 38](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_38.png)

4. On the *SQL Server* tab, set up the *Primary SQL Server* connection. To get a connection, enter
the data here exactly how it is entered on the *SQL Server* tab of the *Application Server*
management console. Note: you will need to know your sa password (the default is
*Verw@1ter*).

![SQL TCP/IP Setup for Remote Device Server image 39](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_39.png)

![SQL TCP/IP Setup for Remote Device Server image 40](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_40.png)

5. Next, click the
button to make the connection. The *Management Console* will now
display a *Databases* tab.

![SQL TCP/IP Setup for Remote Device Server image 41](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_41.png)

6. Click the *Databases* tab and select the database that is being used by the system from the
drop-down list.

![SQL TCP/IP Setup for Remote Device Server image 42](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_42.png)

7. Click the *Connect* button.

![SQL TCP/IP Setup for Remote Device Server image 43](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_43.png)

8. Click the *Security* tab and change the *User* login to the *Support* option using the drop-down list
provided.

![SQL TCP/IP Setup for Remote Device Server image 44](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_44.png)

9. Supply the associated *Support* password.

![SQL TCP/IP Setup for Remote Device Server image 45](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_45.png)

10. Click the *Services* tab and stop the *Orbit.NET* service.

![SQL TCP/IP Setup for Remote Device Server image 46](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_46.png)

![SQL TCP/IP Setup for Remote Device Server image 47](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_47.png)

11. Click the *Settings* button in the upper right corner and then click the *Discovery* tab within the
settings area.

![SQL TCP/IP Setup for Remote Device Server image 48](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_48.png)

12. Set the *BACnet Discovery Interface* parameter to the adapter that is being used for the LAN
connection to the local EntroStar panels.

![SQL TCP/IP Setup for Remote Device Server image 49](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_49.png)

13. Again within the *Settings* area, click the *OMS* tab.

![SQL TCP/IP Setup for Remote Device Server image 50](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_50.png)

Within this tab, you must set up the connection of the *Device Server* to the *Application Server*.
14. In the *OMS Server Name* field, enter the IP address or computer name of the *Application*
*Server*.
15. In the *Device Server Number(1-16)* field, change the number to *2* (or whatever is the next
*Server* number being added to the system).
16. Close the *Management Console* application.

![SQL TCP/IP Setup for Remote Device Server image 51](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_51.png)

## 1.5 ADD AND DISCOVER DEVICES/PANELS

1. Open the *Site Builder* application on the *RDS*.

![SQL TCP/IP Setup for Remote Device Server image 52](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_52.png)

2. From the *C:\Starwatch\Client* folder, launch the *SMSSiteBuilder.exe* application.
3. Select *Options* from the menu on the left side of the screen.

![SQL TCP/IP Setup for Remote Device Server image 53](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_53.png)

![SQL TCP/IP Setup for Remote Device Server image 54](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_54.png)

4. In the *BACnet Discovery Interface* parameter, select the *LAN* adapter option from the provided
drop-down list.

![SQL TCP/IP Setup for Remote Device Server image 55](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_55.png)

![SQL TCP/IP Setup for Remote Device Server image 56](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_56.png)

5. Click the
button.

![SQL TCP/IP Setup for Remote Device Server image 57](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_57.png)

6. Next, open the *Devices* panel by clicking the red *Devices* tile.

![SQL TCP/IP Setup for Remote Device Server image 58](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_58.png)

7. Add Devices to the *RDS* in the same manner as you would normallly configure your system.
Discover and link panels via the normal interfaces.

![SQL TCP/IP Setup for Remote Device Server image 59](./images/starwatch-sms-supplement-sql-tcp-ip-setup-for-remote-device-server-rev-1_59.png)

8. Hit the back arrow
at the top left of the screen to update the system.
9. Close the *Site Builder* application.

---

*© DAQ Electronics, LLC*
