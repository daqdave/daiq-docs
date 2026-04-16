---
layout: default
title: How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation
nav_order: 210
---

# How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 01](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_01.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 02](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_02.png)

## Introduction

One or more workstations on the system will require *Asure ID* badging if you would like to:
a) Design a printable card, ID badge, or visitor pass
b) Print a card or pass
Note: not all workstations require *Asure ID* if design or printing is not needed - all workstations can
view an individual’s photo, take a photo, and view a person’s currently issued or printed card or pass.
Note:  this guide should only be used for the installation of *Asure ID* on a Stand-Alone SCIF Workstation.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 03](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_03.png)

## Windows Services

To begin, it is important to ensure that the *SQL Server Browser* is running.
1. Using the *Start* menu, type “windows services” in the search function and then select the
*Services* icon.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 04](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_04.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 05](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_05.png)

This will call up the *Services* window.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 06](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_06.png)

2. On the right side of the editor, scroll down to find and select the *SQL Server* Browser option.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 07](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_07.png)

3. Right-click on the selected option and choose *Properties* from the drop-down menu. This will
call up the settings window for the *SQL Server Browser* option.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 08](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_08.png)

4. On the *General* tab, check that the *Service Status* indicates that the SQL Server is *Running*. If it
is not running, click the *Start* button followed by the *OK* button. If the service is disabled,
choose *Automatic*, then refresh the screen and start the service.
5. Close out of the *Services* editor.

## Windows Security Policy

Before installing *Asure ID*, you must check the security policy settings in Windows to make sure that
the following option is disabled:
*System cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing*
HID does not allow or support this option, and it will cause *Asure ID* to fail or crash if enabled.
1. Using the *Start* menu, type “edit group policy” in the search function and then select the *Edit*
*group policy* icon.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 09](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_09.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 10](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_10.png)

This will call up the *Local Group Policy Editor* window.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 11](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_11.png)

2. Using the directory tree on the left side of the editor, navigate to:
*Local Computer Policy/Computer Configuration/Windows Settings/Security*

## Settings/Local Policies/Security Options

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 12](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_12.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 13](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_13.png)

3. On the right side of the editor, scroll down to find and select the *System cryptography* option
relating to FIPS compliant algorithms.
4. Right-click on the selected option and choose *Properties* from the drop-down menu. This will
call up the settings window for the *System cryptography* option.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 14](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_14.png)

5. On the *Local Security Setting* tab, set the option to *Disabled* and hit the *OK* button.
6. Close out of the editor.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 15](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_15.png)

## Registry Editor

Next, you need to turn off *FIPS Cryptography* in the *Registry Editor*.
1. Using the *Start* menu, type “run” in the search function and then select the *Run* icon.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 16](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_16.png)

This will call up the *Run* dialog box.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 17](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_17.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 18](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_18.png)

2. Type “regedit” into the dialog box and click the *OK* button.
This will call up the *Registry Editor* window.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 19](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_19.png)

3. Using the directory tree on the left side of the editor, navigate to:
*HKEY_LOCAL_MACHINE/System/CurrentControlSet/Control/Lsa/FIPSAlgorithmPolicy/*

## Enabled

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 20](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_20.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 21](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_21.png)

4. Change the value of this registry entry to 0 to disable it.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 22](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_22.png)

5. Close out of the editor.

## ISS Crypto GUI Tool

To run properly, *Asure ID* requires that a set of specified Windows options are enabled, including
client/server protocols, ciphers, hashes, and key exchange algorithms.
1. For this section, you will need to utilize the *IIS Crypto GUI* program. If it is not already on your
machine, please visit *www.nartec.com* to download and install this free application.
2. Once installed, launch the application.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 23](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_23.png)

3. On the *Schannel* tab, enable/disable the various options, as shown.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 24](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_24.png)

## Server Firewall Rules

When using *SQL Express*, the TCP access port is allocated dynamically. You will need to add a program
type rule and browse to the *sqlserv.exe* program.
1. Using the *Start* menu, type “run” in the search function and then select the *Run* icon.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 25](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_25.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 26](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_26.png)

This will call up the *Run* dialog box.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 27](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_27.png)

2. Type “WF.msc” into the dialog box and click the *OK* button.
This will call up the *Windows Defender Firewall with Advanced Security* window.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 28](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_28.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 29](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_29.png)

3. In the left pane, right-click on the *Inbound Rules* option and then select *New Rule* from the
*drop-down menu*.
This will call up the *New Inbound Rule Wizard*.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 30](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_30.png)

4. Select the *Program* tick-box from the *Rule Type* list and then click the *Next* button.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 31](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_31.png)

5. In the *Program* window, select the *This program path* tick-box and then click the *Browse*
button.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 32](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_32.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 33](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_33.png)

This will call up the *Open* window.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 34](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_34.png)

6. Using the directory tree, navigate to:
*Program Files/Microsoft SQL Server/MSSQL15.SQLEXPRESS/MSSQL/Binn*
7. Select *sqlsever.exe* from the directory and click the *Open* button.
8. Click *Next* to go to the *Action* window.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 35](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_35.png)

9. In the *Action* window, select the *Allow the connection* tick-box and click the *Next* button.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 36](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_36.png)

10. In the *Profile* window, only select the *Domain* tick-box and click the *Next* button.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 37](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_37.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 38](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_38.png)

11. In the *Name* window, enter a name for the rule in the *Name* field and click the *Finish* button.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 39](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_39.png)

## Run Installation Wizard

Once all previous steps have been completed, you can install *Asure ID*.
1. When installing a new workstation using the *StarWatch SMS* media, you must check that you
have the current *asure_id_setup* file available.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 40](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_40.png)

This file is provided in a folder called *Redists* located in the *StarWatch* folder installed during
*StarWatch SMS* installation.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 41](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_41.png)

2. Before running this file, be sure to disable the computer *McAfee* anti-virus protection. The
default password is *12DOitright!!01*.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 42](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_42.png)

3. When running *StarWatch SMS* setup, it is possible to start the setup of *Asure ID* from within the
*StarWatch SMS* setup. Run (as administrator) the *Asure_id_setup_v7.6.3.22.exe* program.
Note:  do not use a later version as it may not integrate and function correctly within
*StarWatch SMS*.
Note:  you will need to purchase a product key from DAQ Electronics or from your certified DAQ
partner or reseller.
4. Sequence through the installation wizard, as follows, by clicking the *Next* button on each
window until you reach the final screen:

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 43](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_43.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 44](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_44.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 45](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_45.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 46](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_46.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 47](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_47.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 48](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_48.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 49](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_49.png)

5. At this point in the process, you may be prompted to activate your license. To do so, follow the
on-screen instructions. If you are not prompted, you can activate your license later.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 50](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_50.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 51](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_51.png)

6. At the final *Asure ID* setup screen, deselect the *Run Asure ID* checkbox before clicking the
*Finish* button.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 52](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_52.png)

7. After installation, click on the Windows *Start* menu and navigate to *HID Global*. Next, click on
*Data* *Connection Wizard*.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 53](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_53.png)

8. To begin, click the *Next*, button.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 54](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_54.png)

9. On the *Select a* *Database Type* screen, select *Microsoft SQL Server* and click the *Next* button.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 55](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_55.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 56](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_56.png)

10. On the *SQL Database Connection* screen, fill in the following information and click the *Next*
button:
Server Name: this is the name of your computer\SQLEXPRESS (also in the server tab of
-
Management Console)
Initial Catalog: this is the name of your database created in Management Console
-
Schema: dbo
-
User Name: sa
-
Password: 12DOitright!!01
-

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 57](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_57.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 58](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_58.png)

11. Click the *Test* button.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 59](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_59.png)

12. In the *Connection Succeeded* dialog box, click the *OK* button.
13. Click the *Finish* button.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 60](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_60.png)

## Activation

1. To activate your product, open *Asure ID* from the Windows *Start* menu, as shown.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 61](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_61.png)

2. You will be prompted to activate. Fill in the *Activate License* information, as required.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 62](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_62.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 63](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_63.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 64](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_64.png)

## Checking Activation in StarWatch SMS

To check that the *Asure ID* activation was successful, complete the following steps:
1. Open the *StarWatch SMS* operator and login.
2. Next, open the *Admin* console and navigate to the *Card Type* feature*.*
3. In the *Card Type* area, select the *Design* tab.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 65](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_65.png)

4. Click the *Edit Template* button to launch *Asure ID*.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 66](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_66.png)

The following screens are from the ICIDS 5 *StarWatch SMS* product after *Asure ID* opens:

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 67](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_67.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 68](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_68.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 69](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_69.png)

## Asure ID Integration and Diagnostics

## Introduction

It would be helpful to have either a log of all information found via the SDK as a way to verify the
*Asure ID* installation or provide a test application that “dumps” a check list of information.

## SDK Initialization

Check the initialization and report.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 70](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_70.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 71](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_71.png)

## Asure ID Installed Version

Check that the version installed is 7.6.3.22 or the version expected.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 72](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_72.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 73](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_73.png)

## License Level and Type

Check that the activated license is the *Developer* license.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 74](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_74.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 75](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_75.png)

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 76](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_76.png)

## Data Connection

Check that *Asure ID* has a valid data connection to the database used by *StarWatch SMS* and correct the
connection if possible.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 77](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_77.png)

## Set Data Connection

If required, set/update the data connection (as in case of the *su* password being changed).  This can be
done when opening *Admin* or opening the view to *Admin->Card_Type* on initialization.

![How to Install and Use Asure ID Badging on a Stand-Alone SCIF Workstation image 78](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-a-stand-alone-scif-workstation-rev-2_78.png)

---

*© DAQ Electronics, LLC*
