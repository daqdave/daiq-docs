---
layout: default
title: How to Manually Update EntroStar Firmware
nav_order: 250
---

# How to Manually Update EntroStar Firmware

![How to Manually Update EntroStar Firmware image 01](./images/quick-guide-how-to-manually-update-entrostar-firmware2_01.png)

Warning: this reset should only be performed if specifically instructed to do so by DAQ

## Step 1- Unzip supplied update file

Unzip *EntroStarFirmWare.x.x.x.zip* to any folder.

## Step 2 – Determine EntroStar panel IP address

Using *BACNET* browser or *wireshark*, find out the address of your EntroStar panel.

![How to Manually Update EntroStar Firmware image 02](./images/quick-guide-how-to-manually-update-entrostar-firmware2_02.png)

## Step 3 – Login to EntroStar with WinSCP

Use the *WinSCP.exe* program to connect to the EntroStar panel as shown below using:
Username:
*root*
Password:
*sooperrute*
Make sure you have the protocol selected as *SCP*.

![How to Manually Update EntroStar Firmware image 03](./images/quick-guide-how-to-manually-update-entrostar-firmware2_03.png)

Click on *Login* to login and say *Yes* or *OK* to any reported errors about security, keys, or folders.

![How to Manually Update EntroStar Firmware image 04](./images/quick-guide-how-to-manually-update-entrostar-firmware2_04.png)

For example:.

![How to Manually Update EntroStar Firmware image 05](./images/quick-guide-how-to-manually-update-entrostar-firmware2_05.png)

## Step 4 – Copy firmware files to the EntroStar panel

a) Make sure that the folder selected on the left side is the *Firmware* folder contents as supplied
in the zipped update file and extracted to your own folder.
b) Make sure that the folder selected on the right side is the *tmp* folder in the EntroStar panel.

![How to Manually Update EntroStar Firmware image 06](./images/quick-guide-how-to-manually-update-entrostar-firmware2_06.png)

c) Carefully select all the files on the left side including the file *install.sh* and drag them to the
folder called *entrostarupgradefiles* on the right side.

![How to Manually Update EntroStar Firmware image 07](./images/quick-guide-how-to-manually-update-entrostar-firmware2_07.png)

d) This should present a dialog as follows asking for confirmation prior to copying the files:

![How to Manually Update EntroStar Firmware image 08](./images/quick-guide-how-to-manually-update-entrostar-firmware2_08.png)

Click *OK* and the files should start copying.

![How to Manually Update EntroStar Firmware image 09](./images/quick-guide-how-to-manually-update-entrostar-firmware2_09.png)

![How to Manually Update EntroStar Firmware image 10](./images/quick-guide-how-to-manually-update-entrostar-firmware2_10.png)

After the files have copied, you should be able to see the files as shown in the folder
*entrowatchupgradefiles*.

![How to Manually Update EntroStar Firmware image 11](./images/quick-guide-how-to-manually-update-entrostar-firmware2_11.png)

After the files are copied using *WinSCP*, the files will be automatically detected and will
automatically invoke the upgrade process. Please allow 10 to 20 seconds before moving on to
the next step (cleaning the database and rebooting).

![How to Manually Update EntroStar Firmware image 12](./images/quick-guide-how-to-manually-update-entrostar-firmware2_12.png)

## Step 5 – Reboot with PUTTY

Use PUTTY to connect to the EntroStar panel and login:
Username:
*root*
Password:
*sooperrute*
Next, enter the commands as shown:
*cd /db*
*ssentro stop*
*rm *.db*
*dbmanager*
*reboot*
After the reboot has completed and the panel restarted, it should now have the newly updated
firmware and database.

![How to Manually Update EntroStar Firmware image 13](./images/quick-guide-how-to-manually-update-entrostar-firmware2_13.png)

The following screenshots show the actual sequence of doing an update successfully:

![How to Manually Update EntroStar Firmware image 14](./images/quick-guide-how-to-manually-update-entrostar-firmware2_14.png)

![How to Manually Update EntroStar Firmware image 15](./images/quick-guide-how-to-manually-update-entrostar-firmware2_15.png)

![How to Manually Update EntroStar Firmware image 16](./images/quick-guide-how-to-manually-update-entrostar-firmware2_16.png)

![How to Manually Update EntroStar Firmware image 17](./images/quick-guide-how-to-manually-update-entrostar-firmware2_17.png)

![How to Manually Update EntroStar Firmware image 18](./images/quick-guide-how-to-manually-update-entrostar-firmware2_18.png)

![How to Manually Update EntroStar Firmware image 19](./images/quick-guide-how-to-manually-update-entrostar-firmware2_19.png)

![How to Manually Update EntroStar Firmware image 20](./images/quick-guide-how-to-manually-update-entrostar-firmware2_20.png)

![How to Manually Update EntroStar Firmware image 21](./images/quick-guide-how-to-manually-update-entrostar-firmware2_21.png)

![How to Manually Update EntroStar Firmware image 22](./images/quick-guide-how-to-manually-update-entrostar-firmware2_22.png)

After the panel comes back on-line, you may need to re-synchronize the database – this can be done
from *Site Planner*, as follows:

![How to Manually Update EntroStar Firmware image 23](./images/quick-guide-how-to-manually-update-entrostar-firmware2_23.png)

---

*© DAQ Electronics, LLC*
