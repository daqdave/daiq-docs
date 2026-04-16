---
layout: default
title: RPI Configuration
nav_order: 600
---

# RPI Configuration

![RPI Configuration image 01](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_01.png)

## 1.0 RPI CONFIGURATION

## 1.1 LOGGING INTO SITE BUILDER

RPI configuration is accomplished using the *Site Builder* application. To access *Site Builder*, double-
click on the *Site Builder* icon on the computer desktop if you created a shortcut during installation.

![RPI Configuration image 02](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_02.png)

Alternately, click the Windows *Start* menu, select *All Programs*, and select the DAQ Electronics folder
from the displayed list. From the sub-list of DAQ Electronics installed applications, click the *Site*
*Builder* option.

![RPI Configuration image 03](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_03.png)

![RPI Configuration image 04](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_04.png)

After the *Site Builder* application has been launched, the login screen will appear.

![RPI Configuration image 05](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_05.png)

After filling in the associated username/password and role combination, click the *Login* button to
connect to the system database. If you do not know the correct login settings for your system, see your
Systems Administrator for password and roles information.
The initial default settings for administrators are as follows:

*Username*
admin

*Password*
admin

*Role*
System Administrator
Note: these settings can and should be changed before fielding a live system.

![RPI Configuration image 06](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_06.png)

## 1.2 ADDING THE RPI DRIVER

When you first launch *Site Builder*, the RPI driver and application are not visible on the main screen.
To add an RPI driver to the list of application tiles, complete the following steps:

### Step 1:

From the menu on the left side of the screen, select *Options*.

![RPI Configuration image 07](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_07.png)

![RPI Configuration image 08](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_08.png)

### Step 2:

From the *Options* pop-up window, select the *Support for StarGate III Panels* checkbox and

![RPI Configuration image 09](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_09.png)

click the
button.

![RPI Configuration image 10](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_10.png)

![RPI Configuration image 11](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_11.png)

![RPI Configuration image 12](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_12.png)

![RPI Configuration image 13](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_13.png)

A light blue *RPI Configuration* tile
will be added to the list of tools and
applications available on the main *Site Builder* screen.

![RPI Configuration image 14](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_14.png)

![RPI Configuration image 15](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_15.png)

![RPI Configuration image 16](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_16.png)

### Step 3:

Click the green *Maps and Plans* tile
to call up the site plan creation/editing
screen.

![RPI Configuration image 17](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_17.png)

### Step 4:

In the *Navigator* pane to the left of the screen, expand the *Tree* showing the system panels,
devices, and drivers.

![RPI Configuration image 18](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_18.png)

### Step 5:

Right-click on the appropriate system name and select the *Add Drivers* option.

![RPI Configuration image 19](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_19.png)

![RPI Configuration image 20](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_20.png)

### Step 6:

From the *Add Drivers* pop-up window, select the *RPI Driver* checkbox and click the
button.

![RPI Configuration image 21](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_21.png)

An *RPI Driver (RPIConfig)* line will be added to the system *Tree*.

![RPI Configuration image 22](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_22.png)

![RPI Configuration image 23](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_23.png)

## 1.3 CONFIGURING RPI PANELS

*Panels* refer to the hardware panels that are installed on your site. *Panels* communicate with security
hardware entities and notify the *StarWatch SMS* server and operator applications of system alarms.
Within the *Site Builder* application, you can:

Add a new *Panel* to the site

Rename a *Panel*

Create a *Template* from an existing *Panel* in your system or import from a folder with
saved *Templates* from another system

Add a new *Panel* based on a template

Delete a *Panel*
To begin *Panel* configuration, complete the following steps:

![RPI Configuration image 24](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_24.png)

![RPI Configuration image 25](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_25.png)

### Step 1:

From the main *Site Builder* screen, click the light blue *RPI Configuration* tile
.

![RPI Configuration image 26](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_26.png)

![RPI Configuration image 27](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_27.png)

### Step 2:

From the RPI configuration screen, select the RPI driver in the *Configuration* pane to the left
of the screen to open the RPI editor area.

![RPI Configuration image 28](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_28.png)

![RPI Configuration image 29](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_29.png)

![RPI Configuration image 30](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_30.png)

The editor displays the current device driver settings, which cannot be modified.

![RPI Configuration image 31](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_31.png)

## 1.3.1 ADDING A PANEL

Note: after adding a new *Panel*, you must add hardware *Items*, which consist of alarm points, doors,
alarm zones, etc.
To add a *Panel* to the RPI device driver, complete the following steps:

### Step 1:

In the *Configuration* pane, select the *RPIConfig* device driver from the system *Tree*. The RPI
editor area will populate the main workspace.

![RPI Configuration image 32](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_32.png)

![RPI Configuration image 33](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_33.png)

### Step 2:

Right-click on the *RPIConfig* driver and select *Add Panel* from the menu options.

![RPI Configuration image 34](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_34.png)

A new *Panel* will be added to the configuration.

### Step 3:

To view the details of a new or existing *Panel*, expand the view for the *RPIConfig* driver by

![RPI Configuration image 35](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_35.png)

clicking on the associated
arrow and double-click on the *Panel* in the system *Tree*. The
setup configuration window corresponding with the selected *Panel* will appear in the
workspace.

![RPI Configuration image 36](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_36.png)

![RPI Configuration image 37](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_37.png)

### Step 4:

Once a *Panel* has been added/selected, complete the provided configuration fields to suit
your specific site.

![RPI Configuration image 38](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_38.png)

![RPI Configuration image 39](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_39.png)

**Group**
**Name**
**Description**
**Default**
General
Name
Sets the *Name* of the panel
Panel *<n>* where *<n>*
increments with each
additional panel
(Blank)
Description
Sets a brief text *Description*
of the panel
Panel
Widget
Specifies the type of *Widget*
used for the graphical site
map

Panel Type
Sets the *Type* of panel
StarGateIII/SMS+
(CV5.5.33G/34)

StarGate III/ SMS
Sync Type
Drop-down menu to select the
All credentials
*Sync* type

All credentials

Permitted credentials

Important credentials

Permitted and
important credentials

Credentials on
demand
Host
Station Address
Sets the *Address* of the panel
1
Communications
that is used to communicate
(all panels on the same serial
link must have a different
address)
IP Address
Sets the *IP Address* of the
192.168.0.251:48700
panel
Channel Type
Sets the *Type* of
Serial
communications or protocols
used to communicate with the
panel
Host Name
Sets the *Host Name*
(Blank)
COM Port
Port Type
Sets the *Port Definition* to
COM
Definition
either none or COM
Port Baud Rate
Sets the *Baud Rate* of the COM
19200
port
50 ms
Transmit Delay
Sets the *Transmit Delay*
interval in milliseconds
Receive
Sets the *Timeout* interval in
2000 ms
Timeout
milliseconds for receiving
transmissions
Data Scan
Sets the *Period* in seconds for
300 s
Period
data scanning
Fail Scan
Sets the *Period* in seconds for
150 s
Period
scan failures

![RPI Configuration image 40](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_40.png)

### Step 5:

Once the panel has been configured, the changes must be saved to the system database.
Click the arrow
at the top left of the screen to return to the main *Site Builder* screen.

![RPI Configuration image 41](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_41.png)

![RPI Configuration image 42](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_42.png)

### Step 6:

Next, from the menu on the left side of the screen, select *Update*. The new *Panel* will be
saved to the database.
Note: more than one *Panel* can be added to a driver if the *Panel* is using that specific hardware.

![RPI Configuration image 43](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_43.png)

## 1.3.2 RENAMING A PANEL

To rename an existing *Panel*, complete the following steps:

![RPI Configuration image 44](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_44.png)

### Step 1:

From the main *Site Builder* screen, click the green *Maps and Plans* tile
.

![RPI Configuration image 45](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_45.png)

![RPI Configuration image 46](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_46.png)

The site plan creation/editing screen will be called up.

![RPI Configuration image 47](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_47.png)

### Step 2:

In the *Configuration* pane, expand the view for the *RPIConfig* driver in the system *Tree* by

![RPI Configuration image 48](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_48.png)

clicking on the associated
arrow then right-click on the appropriate *Panel*.

![RPI Configuration image 49](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_49.png)

![RPI Configuration image 50](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_50.png)

### Step 3:

Select *Rename* from the pop-up menu.

![RPI Configuration image 51](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_51.png)

The name of the *Panel* will become highlighted in dark blue.

![RPI Configuration image 52](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_52.png)

![RPI Configuration image 53](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_53.png)

### Step 4:

Type in a new name for the *Panel* and then click anywhere else on the screen.

![RPI Configuration image 54](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_54.png)

The new name will be reflected in the system *Tree* and in the configuration area of the
workspace.
Note: you can also change the name of a *Panel* by typing into the *Name* field in the configuration area.

### Step 5:

Once you have completed any required name modifications, the changes must be saved to
the system database. Click the arrow
at the top left of the screen to return to the main

![RPI Configuration image 55](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_55.png)

*Site Builder* screen.

![RPI Configuration image 56](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_56.png)

![RPI Configuration image 57](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_57.png)

### Step 6:

Next, from the menu on the left side of the screen, select *Update*. The new *Panel* names
will be saved to the database.

![RPI Configuration image 58](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_58.png)

## 1.3.3 ADDING ITEMS TO A PANEL

Once a *Panel* has been added to the RPI device driver, you can add hardware *Items* to the *Panel*. The
types of *Items* that can be added are:

*Access Portals*

*Alarm Points*

*Alarm Zones*

*Output Points*

*Status Points*

*Ternary Points*
Note: There can be only one *Alarm Zone* added per *Panel*. For larger sites, a *Panel* can have *Sub-*
*Panels*. The number of *Panels/Sub-Panels* and *Alarm Zones* in your site depends on how large your site
is and how secure a particular area must be. For example, one *Panel* and one *Alarm Zone* can typically
be used for a small office environment. A larger office with a room that must be secured apart from
other areas, such as a laboratory or safe deposit box room, would require more than one *Alarm Zone*.

![RPI Configuration image 59](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_59.png)

To add an *Item* to a *Panel*, complete the following steps:

![RPI Configuration image 60](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_60.png)

### Step 1:

From the main *Site Builder* screen, click the green *Maps and Plans* tile
.

![RPI Configuration image 61](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_61.png)

![RPI Configuration image 62](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_62.png)

The site plan creation/editing screen will be called up.

![RPI Configuration image 63](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_63.png)

### Step 2:

In the *Configuration* pane, expand the view for the *RPIConfig* driver in the system *Tree* by

![RPI Configuration image 64](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_64.png)

clicking on the associated
arrow then right-click on the appropriate *Panel*.

![RPI Configuration image 65](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_65.png)

![RPI Configuration image 66](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_66.png)

### Step 3:

Select *Add Item* from the pop-up menu then select the appropriate *Item* from the secondary
pop-up menu.

![RPI Configuration image 67](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_67.png)

The *Item* will be added to the *Panel*.

### Step 4:

Repeat the process to add other *Items*, as needed.

![RPI Configuration image 68](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_68.png)

### Step 5:

Once you have added any required *Items* to the *Panel*, the changes must be saved to the
system database. Click the arrow
at the top left of the screen to return to the main *Site*

![RPI Configuration image 69](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_69.png)

*Builder* screen.

![RPI Configuration image 70](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_70.png)

### Step 6:

Next, from the menu on the left side of the screen, select *Update*. The new *Items* will be
saved to the database.

![RPI Configuration image 71](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_71.png)

## 1.3.4 CREATING A TEMPLATE FROM AN EXISTING PANEL/ITEM

Within *Site Builder*, you have the ability to create *Templates* from existing *Panels* or *Items* and use
them in other configurations. *Template* files are portable, meaning they can be moved and shared
between computers and systems.
To create a *Template* from an existing *Panel*, complete the following steps:

![RPI Configuration image 72](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_72.png)

### Step 1:

From the main *Site Builder* screen, click the green *Maps and Plans* tile
.

![RPI Configuration image 73](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_73.png)

![RPI Configuration image 74](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_74.png)

The site plan creation/editing screen will be called up.

![RPI Configuration image 75](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_75.png)

### Step 2:

In the *Configuration* pane, expand the view for the *RPIConfig* driver in the system *Tree* by

![RPI Configuration image 76](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_76.png)

clicking on the associated
arrow then right-click on the appropriate *Panel*.

![RPI Configuration image 77](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_77.png)

![RPI Configuration image 78](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_78.png)

### Step 3:

Select *Create Template* from the pop-up menu.

![RPI Configuration image 79](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_79.png)

The *Panel* is saved as a *Template* and added to the *Template* list that is displayed when you
create a new *Panel* from a *Template*.

![RPI Configuration image 80](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_80.png)

![RPI Configuration image 81](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_81.png)

### Step 4:

Once you have created any required *Templates*, the changes must be saved to the system
database. Click the arrow
at the top left of the screen to return to the main *Site Builder*

![RPI Configuration image 82](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_82.png)

screen.

![RPI Configuration image 83](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_83.png)

### Step 5:

Next, from the menu on the left side of the screen, select *Update*. The new *Templates* will
be saved to the database.

![RPI Configuration image 84](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_84.png)

You can also create *Templates* for *Items*, such as *Access Portals*, *Alarm Points*, *Output Points*, *Alarm*
*Zones* and *Status Points* that have been added in a *Panel* configuration.
To create a *Template* from an existing *Item*, complete the following steps:

![RPI Configuration image 85](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_85.png)

### Step 1:

From the main *Site Builder* screen, click the green *Maps and Plans* tile
.

![RPI Configuration image 86](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_86.png)

![RPI Configuration image 87](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_87.png)

The site plan creation/editing screen will be called up.

![RPI Configuration image 88](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_88.png)

### Step 2:

In the *Configuration* pane, expand the view for the *RPIConfig* driver in the system *Tree* by

![RPI Configuration image 89](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_89.png)

clicking on the associated
arrow then expand the view for the appropriate *Panel* in the
same manner.

![RPI Configuration image 90](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_90.png)

### Step 3:

Right-click on the appropriate *Item* in the *Tree* and select *Create Template* from the pop-up
menu.

![RPI Configuration image 91](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_91.png)

The *Item* is saved as a *Template* and added to the *Template* list that is displayed when you
create a new *Item* from a *Template*.

![RPI Configuration image 92](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_92.png)

![RPI Configuration image 93](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_93.png)

### Step 4:

Once you have created any required *Templates*, the changes must be saved to the system
database. Click the arrow
at the top left of the screen to return to the main *Site Builder*

![RPI Configuration image 94](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_94.png)

screen.

![RPI Configuration image 95](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_95.png)

### Step 5:

Next, from the menu on the left side of the screen, select *Update*. The new *Templates* will
be saved to the database.

![RPI Configuration image 96](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_96.png)

## 1.3.5 ADDING A PANEL FROM A TEMPLATE

If you have previously saved *Panel* configurations as *Template* files, these files can be used to add
identical *Panels* to your site.
Note: an advantage of adding a *Panel* from a *Template* is that any existing sub-entities (*Items*) of the
saved *Panel* configuration are automatically created as well.
To add a *Panel* from a *Template*, complete the following steps:

![RPI Configuration image 97](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_97.png)

### Step 1:

From the main *Site Builder* screen, click the green *Maps and Plans* tile
.

![RPI Configuration image 98](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_98.png)

![RPI Configuration image 99](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_99.png)

The site plan creation/editing screen will be called up.

![RPI Configuration image 100](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_100.png)

### Step 2:

In the *Configuration* pane, right-click on the *RPIConfig* driver and select *Add Item From*
*Template* from the pop-up menu.

![RPI Configuration image 101](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_101.png)

![RPI Configuration image 102](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_102.png)

### Step 2:

From the list provided in the secondary pop-up menu, select a *Template* to add to your
configuration.

![RPI Configuration image 103](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_103.png)

A new *Panel* will be created from the selected *Template*.

![RPI Configuration image 104](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_104.png)

![RPI Configuration image 105](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_105.png)

Note: To rename the added *Panel*, right-click on the *Panel* name in the system *Tree* and select the
*Rename* option from the pop-up menu. Next, enter the new name and hit the *Enter* key on your
keyboard.

![RPI Configuration image 106](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_106.png)

### Step 3:

Once you have added any required *Panels*, the changes must be saved to the system
database. Click the arrow
at the top left of the screen to return to the main *Site Builder*

![RPI Configuration image 107](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_107.png)

screen.

![RPI Configuration image 108](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_108.png)

![RPI Configuration image 109](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_109.png)

### Step 4:

Next, from the menu on the left side of the screen, select *Update*. The new *Panels* will be
saved to the database.

![RPI Configuration image 110](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_110.png)

## 1.3.6 ADDING AN ITEM FROM A TEMPLATE

If you have previously saved *Items* as *Template* files, these files can be used to add identical *Items* to
any *Panel* on your site.
To add an *Item* from a *Template*, complete the following steps:

![RPI Configuration image 111](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_111.png)

### Step 1:

From the main *Site Builder* screen, click the green *Maps and Plans* tile
.

![RPI Configuration image 112](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_112.png)

![RPI Configuration image 113](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_113.png)

The site plan creation/editing screen will be called up.

![RPI Configuration image 114](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_114.png)

### Step 2:

In the *Configuration* pane, expand the view for the *RPIConfig* driver in the system *Tree* by

![RPI Configuration image 115](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_115.png)

clicking on the associated
arrow then right-click on the appropriate *Panel*.

![RPI Configuration image 116](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_116.png)

### Step 3:

Select *Add Item From Template* from the pop-up menu then select an *Item* to add to your
*Panel* from the list provided in the secondary pop-up menu.

![RPI Configuration image 117](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_117.png)

A new *Item* will be created from the selected *Template*.

![RPI Configuration image 118](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_118.png)

Note: To rename the added *Item*, right-click on the *Item* name in the system *Tree* and select the
*Rename* option from the pop-up menu. Next, enter the new name and hit the *Enter* key on your
keyboard.

### Step 4:

Once you have added any required *Items*, the changes must be saved to the system
database. Click the arrow
at the top left of the screen to return to the main *Site Builder*

![RPI Configuration image 119](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_119.png)

screen.

![RPI Configuration image 120](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_120.png)

![RPI Configuration image 121](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_121.png)

### Step 4:

Next, from the menu on the left side of the screen, select *Update*. The new *Items* will be
saved to the database.

![RPI Configuration image 122](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_122.png)

## 1.3.7 IMPORTING A PANEL TEMPLATE FROM ANOTHER SYSTEM

If you have previously saved *Panel* configurations from another system as *Template* files, these files
can be used to add identical *Panels* to your current site.
Note: an advantage of adding a *Panel* from a *Template* is that any existing sub-entities (*Items*) of the
saved *Panel* configuration are automatically created as well.
To import a *Template* from another system, complete the following steps:

![RPI Configuration image 123](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_123.png)

### Step 1:

From the main *Site Builder* screen, click the green *Maps and Plans* tile
.

![RPI Configuration image 124](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_124.png)

![RPI Configuration image 125](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_125.png)

The site plan creation/editing screen will be called up.

![RPI Configuration image 126](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_126.png)

### Step 2:

In the *Configuration* pane, click on the *RPIConfig* driver in the system *Tree* to select it.

![RPI Configuration image 127](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_127.png)

![RPI Configuration image 128](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_128.png)

![RPI Configuration image 129](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_129.png)

### Step 3:

Next, click the *Add Template From Folder*
icon at the top of the pane.

![RPI Configuration image 130](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_130.png)

### Step 4:

In the file selection pop-up window, locate the *Template* you would like to add to the
*Template* list in your system and click on it to select it.

![RPI Configuration image 131](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_131.png)

![RPI Configuration image 132](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_132.png)

![RPI Configuration image 133](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_133.png)

### Step 5:

Click the
button. The selected *Template* will be imported into your system and will
appear in the *Template* list.

### Step 6:

To add the imported *Panel* configuration to your system, right-click on the *RPIConfig* driver
in the system *Tree* and select *Add Items from Template* from the pop-up menu.

![RPI Configuration image 134](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_134.png)

### Step 7:

In the secondary pop-up menu, locate the appropriate *Template* in the list and select it.

![RPI Configuration image 135](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_135.png)

### Step 8:

Once you have imported and incorporated any required *Templates*, the changes must be
saved to the system database. Click the arrow
at the top left of the screen to return to

![RPI Configuration image 136](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_136.png)

the main *Site Builder* screen.

![RPI Configuration image 137](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_137.png)

### Step 9:

Next, from the menu on the left side of the screen, select *Update*. The new configuration
will be saved to the database.

![RPI Configuration image 138](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_138.png)

## 1.3.8 DELETING A PANEL

To delete an existing *Panel*, complete the following steps:

![RPI Configuration image 139](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_139.png)

### Step 1:

From the main *Site Builder* screen, click the green *Maps and Plans* tile
.

![RPI Configuration image 140](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_140.png)

![RPI Configuration image 141](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_141.png)

The site plan creation/editing screen will be called up.

![RPI Configuration image 142](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_142.png)

### Step 2:

In the *Configuration* pane, expand the view for the *RPIConfig* driver in the system *Tree* by

![RPI Configuration image 143](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_143.png)

clicking on the associated
arrow then right-click on the appropriate *Panel*.

![RPI Configuration image 144](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_144.png)

![RPI Configuration image 145](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_145.png)

### Step 3:

Select *Delete* from the pop-up menu.

![RPI Configuration image 146](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_146.png)

![RPI Configuration image 147](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_147.png)

### Step 4:

In the confirmation pop-up window, click the
button.

![RPI Configuration image 148](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_148.png)

The selected *Panel* will be removed from the system *Tree*.

![RPI Configuration image 149](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_149.png)

![RPI Configuration image 150](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_150.png)

### Step 5:

Once you have completed any required *Panel* deletions, the system modifications must be
saved to the database. Click the arrow
at the top left of the screen to return to the main

![RPI Configuration image 151](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_151.png)

*Site Builder* screen.

![RPI Configuration image 152](./images/starwatch-sms-user-guide-rpi-configuration-rev-1_152.png)

### Step 6:

Next, from the menu on the left side of the screen, select *Update*. The deletions will be
saved to the database.

---

*© DAQ Electronics, LLC*
