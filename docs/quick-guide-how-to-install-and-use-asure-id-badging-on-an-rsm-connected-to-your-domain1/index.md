---
layout: default
title: How to Install and Use Asure ID Badging on an RSM Connected to Your Domain
nav_order: 230
---

# How to Install and Use Asure ID Badging on an RSM Connected to Your Domain

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 01](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_01.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 02](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_02.png)

## Introduction

One or more workstations on the system will require *Asure ID* badging if you would like to:
a) Design a printable card, ID badge, or visitor pass
b) Print a card or pass
Note: not all workstations require *Asure ID* if design or printing is not needed - all workstations can
view an individual’s photo, take a photo, and view a person’s currently issued or printed card or pass.
Note: this guide should only be used for the installation of *Asure ID* on an *RSM* connected to your
domain.
Note: several of the *Asure ID* installation steps outlined in this guide will need to be completed on both
the *Application Server* and the *RSM* (as indicated in the procedures) – for steps that need to be
completed for both, please begin with those needed for the *Application Server*, then move on to the
*RSM*.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 03](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_03.png)

## Windows Services

Important: this section should be completed for the *Application Server* only.
To begin, it is important to ensure that the *SQL Server Browser* is running.
1. Using the *Start* menu, type “windows services” in the search function and then select the
*Services* icon.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 04](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_04.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 05](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_05.png)

This will call up the *Services* window.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 06](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_06.png)

2. On the right side of the editor, scroll down to find and select the *SQL Server* Browser option.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 07](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_07.png)

3. Right-click on the selected option and choose *Properties* from the drop-down menu. This will
call up the settings window for the *SQL Server Browser* option.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 08](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_08.png)

4. On the *General* tab, check that the *Service Status* indicates that the SQL Server is *Running*. If it
is not running, click the *Start* button followed by the *OK* button. If the service is disabled,
choose *Automatic*, then refresh the screen and start the service.
5. Close out of the *Services* editor.

## Windows Security Policy

Important: this section should be completed for the *RSM* only.
Before installing *Asure ID*, you must check the security policy settings in Windows to make sure that
the following option is disabled:
*System cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing*
HID does not allow or support this option, and it will cause *Asure ID* to fail or crash if enabled.
1. Using the *Start* menu, type “edit group policy” in the search function and then select the *Edit*
*group policy* icon.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 09](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_09.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 10](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_10.png)

This will call up the *Local Group Policy Editor* window.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 11](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_11.png)

2. Using the directory tree on the left side of the editor, navigate to:
*Local Computer Policy/Computer Configuration/Windows Settings/Security*

## Settings/Local Policies/Security Options

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 12](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_12.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 13](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_13.png)

3. On the right side of the editor, scroll down to find and select the *System cryptography* option
relating to FIPS compliant algorithms.
4. Right-click on the selected option and choose *Properties* from the drop-down menu. This will
call up the settings window for the *System cryptography* option.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 14](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_14.png)

5. On the *Local Security Setting* tab, set the option to *Disabled* and hit the *OK* button.
6. Close out of the editor.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 15](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_15.png)

## Registry Editor

Important: this section should be completed for the *Application Server* and the *RSM*.
Next, you need to turn off *FIPS Cryptography* in the *Registry Editor*.
1. Using the *Start* menu, type “run” in the search function and then select the *Run* icon.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 16](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_16.png)

This will call up the *Run* dialog box.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 17](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_17.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 18](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_18.png)

2. Type “regedit” into the dialog box and click the *OK* button.
This will call up the *Registry Editor* window.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 19](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_19.png)

3. Using the directory tree on the left side of the editor, navigate to:
*HKEY_LOCAL_MACHINE/System/CurrentControlSet/Control/Lsa/FIPSAlgorithmPolicy/*

## Enabled

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 20](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_20.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 21](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_21.png)

4. Change the value of this registry entry to 0 to disable it.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 22](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_22.png)

5. Close out of the editor.
6. Repeat this procedure for the second machine (the *Application Server* or *RSM*).

## ISS Crypto GUI Tool

Important: this section should be completed for the *Application Server* and the *RSM*.
To run properly, *Asure ID* requires that a set of specified Windows options are enabled, including
client/server protocols, ciphers, hashes, and key exchange algorithms.
1. For this section, you will need to utilize the *IIS Crypto GUI* program. If it is not already on your
machine, please visit *www.nartec.com* to download and install this free application.
2. Once installed, launch the application by right-clicking on the file and selecting *Run as*
*administrator* from the menu.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 23](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_23.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 24](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_24.png)

3. On the *Schannel* tab, enable/disable the various options, as shown, and click the *Apply* button.

## Server Firewall Rules

Important: this section should be completed for the *Application Server* only.
When using *Microsoft SQL Server*, the TCP access port is allocated dynamically. You will need to add
two *Port-type* rules to control connections for your TCP ports, as shown for *SQL Server 2019*. Later, you
will also need to create a *Program-type* rule and browse to the *sqlserv.exe* program.
1. Using the *Start* menu, type “run” in the search function and then select the *Run* icon.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 25](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_25.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 26](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_26.png)

This will call up the *Run* dialog box.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 27](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_27.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 28](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_28.png)

2. Type “WF.msc” into the dialog box and click the *OK* button.
This will call up the *Windows Defender Firewall with Advanced Security* window.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 29](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_29.png)

3. In the left pane, right-click on the *Inbound Rules* option and then select *New Rule* from the
*drop-down menu*.
This will call up the *New Inbound Rule Wizard*.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 30](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_30.png)

4. Select the *Port* tick-box from the *Rule Type* list and then click the *Next* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 31](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_31.png)

5. In the *Protocol and Ports* dialog box, select *TCP*.
6. Next, select the *Specific local ports* option, and type the port number of the instance of the
Database Engine, such as 1433, for the default instance. Once complete, click the *Next* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 32](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_32.png)

7. In the *Action* dialog box, select *Allow the connection* and then click *Next*.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 33](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_33.png)

8. In the *Profile* dialog box, select *Domain* only and then click *Next*.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 34](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_34.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 35](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_35.png)

9. In the *Name* dialog box, type a name and description for this rule, and then click *Finish*.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 36](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_36.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 37](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_37.png)

10. You now need to repeat this process for port 1434 to facilitate discovery of the *SQL* instance.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 38](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_38.png)

To do this, repeat steps 7, 8, and 9 from this procedure. Starting in the *Windows Defender*
*Firewall with Advanced Security* window, follow the same sequence of steps, but this time type
“1434” in the *Specific local ports* option on the *Protocol and Ports* screen.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 39](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_39.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 40](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_40.png)

11. Next, you need to add a *Program-type* rule and browse to the *sqlserv.exe* program. To begin
this process, return to the *New Inbound Rule Wizard* screen.
In the left pane, right-click on the *Inbound Rules* option and then select *New Rule* from the
drop-down menu.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 41](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_41.png)

12. This time, select the *Program* tick-box from the *Rule Type* list and then click the *Next* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 42](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_42.png)

13. In the *Program* window, select the *This program path* tick-box and then click the *Browse*
button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 43](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_43.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 44](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_44.png)

This will call up the *Open* window.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 45](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_45.png)

14. Using the directory tree, navigate to:
*Program Files/Microsoft SQL Server/MSSQL15.ICIDS/MSSQL/Binn*
15. Select *sqlsever.exe* from the directory and click the *Open* button.
16. Click *Next* to go to the *Action* window.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 46](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_46.png)

17. In the *Action* window, select the *Allow the connection* tick-box and click the *Next* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 47](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_47.png)

18. In the *Profile* window, only select the *Domain* tick-box and click the *Next* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 48](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_48.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 49](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_49.png)

19. In the *Name* window, enter a name for the rule in the *Name* field and click the *Finish* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 50](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_50.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 51](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_51.png)

## Run Installation Wizard

Important: this section should be completed for the *RSM* only.
Once all previous steps have been completed, you can install *Asure ID* if not already installed on your
RSM.
1. When installing a new workstation using the *StarWatch SMS* media, you must check that you
have the current *asure_id_setup* file available.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 52](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_52.png)

This file is provided in a folder called *Redists* located in the *StarWatch* folder installed during
*StarWatch SMS* installation.
2. Before running this file, be sure to disable the computer *McAfee* anti-virus protection. The
default password is *12DOitright!!01*.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 53](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_53.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 54](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_54.png)

3. When running *StarWatch SMS* setup, it is possible to start the setup of *Asure ID* from within the
*StarWatch SMS* setup. Alternatively, simply run (as administrator) the
*Asure_id_setup_v7.6.3.22.exe* program.
Note:  do not use a later version as it may not integrate and function correctly within
*StarWatch SMS*.
Note:  you will need to purchase a product key from DAQ Electronics or from your certified DAQ
partner or reseller.
Important: proceed with the installation of *Asure ID* on the *RSM* only if it has not been
previously installed on the current image. If already installed, please proceed to *Step 7* to run
the Connection Wizard.
4. Sequence through the installation wizard, as follows, by clicking the *Next* button on each
window until you reach the final screen:

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 55](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_55.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 56](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_56.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 57](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_57.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 58](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_58.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 59](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_59.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 60](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_60.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 61](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_61.png)

5. At this point in the process, you may be prompted to activate your license. To do so, follow the
on-screen instructions. If you are not prompted, you can activate your license later.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 62](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_62.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 63](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_63.png)

6. At the final *Asure ID* setup screen, deselect the *Run Asure ID* checkbox before clicking the
*Finish* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 64](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_64.png)

7. After installation, click on the Windows *Start* menu and navigate to *HID Global*. Next, click on
*Data* *Connection Wizard*.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 65](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_65.png)

8. To begin, click the *Next*, button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 66](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_66.png)

9. On the *Select a* *Database Type* screen, select *Microsoft SQL Server* and click the *Next* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 67](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_67.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 68](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_68.png)

10. On the *SQL Database Connection* screen, fill in the following information and click the *Next*
button:
Server Name: this is the name of your computer SMSSERVER1\ (also in the server tab of
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

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 69](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_69.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 70](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_70.png)

11. Click the *Test* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 71](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_71.png)

12. In the *Connection Succeeded* dialog box, click the *OK* button.
13. Click the *Finish* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 72](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_72.png)

## Activation

Important: this section should be completed for the *RSM* only.
1. To activate your product, open *Asure ID* from the Windows *Start* menu, as shown.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 73](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_73.png)

2. You will be prompted to activate. Fill in the *Activate License* information, as required.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 74](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_74.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 75](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_75.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 76](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_76.png)

## Checking Activation in StarWatch SMS

Important: this section should be completed for the *RSM* only.
To check that the *Asure ID* activation was successful, complete the following steps:
1. Open the *StarWatch SMS* operator and login.
2. Next, open the *Admin* console and navigate to the *Card Type* feature*.*
3. In the *Card Type* area, select the *Design* tab.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 77](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_77.png)

4. Click the *Edit Template* button to launch *Asure ID*.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 78](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_78.png)

The following screens are from the ICIDS 5 *StarWatch SMS* product after *Asure ID* opens:

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 79](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_79.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 80](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_80.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 81](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_81.png)

## Using Asure ID in ICIDS 5 StarWatch SMS

Using the tools available on the *Asure ID* screen, you can edit your card design.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 82](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_82.png)

After completing the design, be sure to save your template before closing out of *Asure ID*.
On the *Card* design page, click on the *Refresh* button.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 83](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_83.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 84](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_84.png)

The list of templates will be updated, and you will then be able to select the template for the required
card type.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 85](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_85.png)

Select the new or existing template if updating modifications to the template. You should see the
updated design in the *StarWatch SMS* operator on the *Card* design page. If the card design includes a
back and front design, then both will be shown side by side.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 86](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_86.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 87](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_87.png)

## Asure ID Integration and Diagnostics

## Introduction

It would be helpful to have either a log of all information found via the SDK as a way to verify the
*Asure ID* installation or provide a test application that “dumps” a check list of information.

## SDK Initialization

Check the initialization and report.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 88](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_88.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 89](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_89.png)

## Asure ID Installed Version

Check that the version installed is 7.6.3.22 or the version expected.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 90](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_90.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 91](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_91.png)

## License Level and Type

Check that the activated license is the *Developer* license.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 92](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_92.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 93](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_93.png)

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 94](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_94.png)

## Data Connection

Check that *Asure ID* has a valid data connection to the database used by *StarWatch SMS* and correct the
connection if possible.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 95](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_95.png)

## Set Data Connection

If required, set/update the data connection (as in case of the *su* password being changed).  This can be
done when opening *Admin* or opening the view to *Admin->Card_Type* on initialization.

![How to Install and Use Asure ID Badging on an RSM Connected to Your Domain image 96](./images/quick-guide-how-to-install-and-use-asure-id-badging-on-an-rsm-connected-to-your-domain1_96.png)

---

*© DAQ Electronics, LLC*
