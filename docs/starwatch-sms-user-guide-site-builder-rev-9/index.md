---
layout: default
title: Site Builder Application
nav_order: 610
---

# Site Builder Application

![Site Builder Application image 01](./images/starwatch-sms-user-guide-site-builder-rev-9_01.png)

## 1.0 INTRODUCTION

The third step in *StarWatch SMS* installation and initial setup workflow is creating a site plan.

![Site Builder Application image 02](./images/starwatch-sms-user-guide-site-builder-rev-9_02.png)

The *Site Builder* tool is used to plan and define the security system that will be installed, configured,
and monitored. Before alarms can be logged and cards can be swiped, you must create a plan of your
site, including all access points and security hardware, such as door or window alarms, cameras,
motion sensors, card readers, and keypads.
Note that *Site Builder* can be utilized prior to security hardware installation, so that a site plan is
already available in the system when the physical installation takes place.

![Site Builder Application image 03](./images/starwatch-sms-user-guide-site-builder-rev-9_03.png)

## 1.1 LOGGING INTO SITE BUILDER

To access *Site Builder*, double-click on the *Site Builder* icon on the computer desktop if you created a
shortcut during installation.

![Site Builder Application image 04](./images/starwatch-sms-user-guide-site-builder-rev-9_04.png)

Alternately, click the Windows *Start* menu, select *All Programs*, and select the DAQ Electronics folder
from the displayed list. From the sub-list of DAQ Electronics installed applications, click the *Site*
*Builder* option.

![Site Builder Application image 05](./images/starwatch-sms-user-guide-site-builder-rev-9_05.png)

![Site Builder Application image 06](./images/starwatch-sms-user-guide-site-builder-rev-9_06.png)

After the *Site Builder* application has been launched, the login screen will appear.

![Site Builder Application image 07](./images/starwatch-sms-user-guide-site-builder-rev-9_07.png)

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

![Site Builder Application image 08](./images/starwatch-sms-user-guide-site-builder-rev-9_08.png)

## 1.2 LOGGING OUT / EXITING SITE BUILDER

To logout of *Site Builder*, click the *Logout* option on the upper left of the main screen.

![Site Builder Application image 09](./images/starwatch-sms-user-guide-site-builder-rev-9_09.png)

To close the *Site Builder* application, click the *X* button at the top right of the screen or select the *Exit*
option at the bottom of the list at the left of the main screen.

![Site Builder Application image 10](./images/starwatch-sms-user-guide-site-builder-rev-9_10.png)

## 2.0 CONNECTING DEVICES

To connect devices to your system configuration, such as access control panels, cameras, 3rd-party
systems, etc., launch the *Site Builder* application.

![Site Builder Application image 11](./images/starwatch-sms-user-guide-site-builder-rev-9_11.png)

From the main *Site Builder* screen, click the red *Devices* tile.

![Site Builder Application image 12](./images/starwatch-sms-user-guide-site-builder-rev-9_12.png)

![Site Builder Application image 13](./images/starwatch-sms-user-guide-site-builder-rev-9_13.png)

To add and configure a device from the device library, click on the small *Plus* icon in the lower right
corner of the *Add Device* box.

![Site Builder Application image 14](./images/starwatch-sms-user-guide-site-builder-rev-9_14.png)

![Site Builder Application image 15](./images/starwatch-sms-user-guide-site-builder-rev-9_15.png)

The device library contains templates for blank devices as well as saved configurations for frequently
used devices. Any device configuration can be saved as a template and added to the device library.

![Site Builder Application image 16](./images/starwatch-sms-user-guide-site-builder-rev-9_16.png)

## 2.1 ADDING ENTROSTAR PANELS

From the device library menu on the left side of the screen, select *EntroStar Driver*.

![Site Builder Application image 17](./images/starwatch-sms-user-guide-site-builder-rev-9_17.png)

Next, double-click on the yellow *EntroStar* tile.

![Site Builder Application image 18](./images/starwatch-sms-user-guide-site-builder-rev-9_18.png)

![Site Builder Application image 19](./images/starwatch-sms-user-guide-site-builder-rev-9_19.png)

An EntroStar driver and a single EntroStar panel will be added to the system and displayed as a yellow
*EntroStar* icon. To configure the panel, double-click on the icon.

![Site Builder Application image 20](./images/starwatch-sms-user-guide-site-builder-rev-9_20.png)

![Site Builder Application image 21](./images/starwatch-sms-user-guide-site-builder-rev-9_21.png)

The panel configuration screen provides basic information about the panel.

*Panel Name*
The name that the panel will be known by in the system

*IP Address*
The IP address to which the panel is configured

*Location*
A reference field that can be used to record and provide information on where a panel is
physically located within a facility

*Time Zone*
The time zone in which the panel is located

![Site Builder Application image 22](./images/starwatch-sms-user-guide-site-builder-rev-9_22.png)

The slider next to each point allows you to configure whether or not the point is active in the system.
For points that are used, slide to the right, for points that are not used, slide to the left.

![Site Builder Application image 23](./images/starwatch-sms-user-guide-site-builder-rev-9_23.png)

To configure the properties of an individual input, click the input row on the screen.

![Site Builder Application image 24](./images/starwatch-sms-user-guide-site-builder-rev-9_24.png)

![Site Builder Application image 25](./images/starwatch-sms-user-guide-site-builder-rev-9_25.png)

## 2.1.1 AUXILIARY INPUTS / TAMPERS / LIGHT SENSORS / GLASS BREAK

![Site Builder Application image 26](./images/starwatch-sms-user-guide-site-builder-rev-9_26.png)

For auxiliary inputs, enclosure tampers, light sensors, and glass break inputs, configure the properties
below.

*Name*
Enter the name that the point will be known by throughout the system.

*Debounce*
This indicates the duration of time that the contact must change in order to generate a change
of state. This can be set to *Long*, *Short*, or *Not Used* via the pull-down menu.

*Active when closed (1K) or Active when open (2K)*
This represents whether an alarm will be generated when the monitored contact is *Open* or
when it is *Closed*.
When all parameters are complete, hit the *Close* button in the bottom right corner, the
*X* button in the top right corner, or the *Back Arrow* in the top left corner to return to the main menu.

## 2.1.2 AUXILIARY OUTPUTS

![Site Builder Application image 27](./images/starwatch-sms-user-guide-site-builder-rev-9_27.png)

![Site Builder Application image 28](./images/starwatch-sms-user-guide-site-builder-rev-9_28.png)

For auxiliary outputs, configure the properties below.

*Name*
Enter the name that the point will be known by throughout the system.

*On activation Energize Relay or De-energize relay*
The auxiliary relays on the EntroStar use normally OPEN contacts. The contacts are OPEN when
the relay is de-energized, and CLOSED when the relay is energized. This parameter establishes
what happens when the relay is turned “on”. It can *Energize* the relay and CLOSE the contacts
or *De-energize* the relay and OPEN its contacts
When all parameters are complete, hit the *Close* button in the bottom right corner, the
*X* button in the top right corner, or the *Back Arrow* in the top left corner to return to the main menu.

![Site Builder Application image 29](./images/starwatch-sms-user-guide-site-builder-rev-9_29.png)

## 2.1.3 PORTALS

![Site Builder Application image 30](./images/starwatch-sms-user-guide-site-builder-rev-9_30.png)

For portals, configure the properties below.

*Name*
Enter the name that the portal will be known by throughout the system.

*Access Type*
This is the type of door that is being used.

*Door release time*
This is the amount of time the door will remain unlocked to allow a person to open the door
and pass through.

*Door release time extended*
This is the amount of time the door will remain unlocked to allow people requiring additional
time to get through the door.

![Site Builder Application image 31](./images/starwatch-sms-user-guide-site-builder-rev-9_31.png)

![Site Builder Application image 32](./images/starwatch-sms-user-guide-site-builder-rev-9_32.png)


*Report door left open after*
This is the amount of time in seconds that the door must remain open after a valid entry for a
*Door Left Open* alarm to be generated.

*Re-lock door*
This defines when the door locks again after a valid access has been granted.
-
*When door closed*
The lock will electrically and mechanically re-engage after the door contact is
determined to be closed again.
-
*When door opened*
The lock will electrically re-engage as soon as the door is opened, allowing the door to
mechanically re-engage when the door closes.

![Site Builder Application image 33](./images/starwatch-sms-user-guide-site-builder-rev-9_33.png)

![Site Builder Application image 34](./images/starwatch-sms-user-guide-site-builder-rev-9_34.png)

-
*After the release time*
The lock will electrically re-engage after the door release time is expired and
mechanically re-engage after the door closes.
-
*Lock type fitted*
o *Energize relay to lock (fail safe like a maglock)*
Fail safe locks need power applied to the lock to remain locked. A fail safe lock
opens and unlocks the door when the power is removed by the system or a power
outage. In order to lock the door, the EntroStar relay will be turned “on”
o *Energize relay to unlock (fail secure)*
Fail secure locks need power applied to the lock to remain unlocked. A fail secure
lock locks the door when power is removed by the system or a power outage. In
order to unlock the door, the EntroStar relay will be turned “on”.

![Site Builder Application image 35](./images/starwatch-sms-user-guide-site-builder-rev-9_35.png)

![Site Builder Application image 36](./images/starwatch-sms-user-guide-site-builder-rev-9_36.png)

-
*Advanced settings*
To view the advanced settings for the door, move the *Advanced Settings* slider in the
top right corner to the ON position.
o *Readers*
This allows selection of entry and exit readers on the door. Each reader can be
configured to not be used (tick-boxes unchecked), to use the reader only, or to use
the reader with a keypad for PIN number.
o *RTE (Request to Exit)*

*In use*
Here we select if a RTE is in use on the door, instead of, or in addition to,
an exit reader.

![Site Builder Application image 37](./images/starwatch-sms-user-guide-site-builder-rev-9_37.png)


*Release door when pressed*
This sets if the door is released when the RTE is pressed.

*Debounce*
This indicates the duration of time that the RTE contact must change in
order to generate a change of state. This can be set to *Long*, *Short*, or *Not*
*Used* via the pull-down menu.

*Normally open or Normally closed*
This allows selection of whether the contact is normally OPEN or normally
CLOSED.
o *Door Contact*

*In use*
Here we select if the door contact is in use.

*Debounce*
This indicates the duration of time that the door contact must change in
order to generate a change of state. This can be set to *Long*, *Short*, or *Not*
*Used* via the pull-down menu.

*Normally open or Normally closed*
This allows selection of whether the contact is normally OPEN or normally
CLOSED.
When all parameters are complete, hit the *Close* button in the bottom right corner, the
*X* button in the top right corner, or the *Back Arrow* in the top left corner to return to the main menu.

![Site Builder Application image 38](./images/starwatch-sms-user-guide-site-builder-rev-9_38.png)

## 2.1.4 DEVICE ICONS

![Site Builder Application image 39](./images/starwatch-sms-user-guide-site-builder-rev-9_39.png)

After configuring the device, the yellow EntroStar icon may display several indicators.

![Site Builder Application image 40](./images/starwatch-sms-user-guide-site-builder-rev-9_40.png)

The broken red paperclip indicates that the panel has not yet been associated with a physical panel in
the system.
The red disk indicates that there are unsaved changes that have been made to the panel.

![Site Builder Application image 41](./images/starwatch-sms-user-guide-site-builder-rev-9_41.png)

## 2.2 ASSOCIATING PANELS TO PHYSICAL DEVICES

To associate configured EntroStar panels with actual device hardware that has been installed in a
facility, you can use one of two provided discovery tools.

## 2.2.1 MULTICAST DISCOVERY (PANELS WITH UNKNOWN IP ADDRESSES)

The multicast tool is used to find EntroStar panels on the network, regardless of their IP settings. Once
panels are discovered, the tool is also utilized to configure the IP of the panel so that it is in a known
condition and can be incorporated into the system.

![Site Builder Application image 42](./images/starwatch-sms-user-guide-site-builder-rev-9_42.png)

![Site Builder Application image 43](./images/starwatch-sms-user-guide-site-builder-rev-9_43.png)

From the EntroStar driver page of the device library, click on the *Multicast Tool*
button.

![Site Builder Application image 44](./images/starwatch-sms-user-guide-site-builder-rev-9_44.png)

![Site Builder Application image 45](./images/starwatch-sms-user-guide-site-builder-rev-9_45.png)

The multicast page will appear and a list of discovered panels will appear in the table to the left of the
screen. To select a panel, click on the appropriate row in the table. Once selected, you can modify the
IP parameters of the panel using the settings fields.

![Site Builder Application image 46](./images/starwatch-sms-user-guide-site-builder-rev-9_46.png)

Once IP settings are complete, click the *Save to Panel* button, which will prompt for a username and
password (the default for both is “ipconfig”).

![Site Builder Application image 47](./images/starwatch-sms-user-guide-site-builder-rev-9_47.png)

After filling in the username and password, click the *Send Changes* button. Next, click the *Close* button
at the bottom right of the screen to exit the multicast tool.

![Site Builder Application image 48](./images/starwatch-sms-user-guide-site-builder-rev-9_48.png)

## 2.2.2 BACNET DISCOVERY (PANELS ALREADY ON SAME IP SUBNET)

The BACnet discovery tool is used to find EntroStar panels that are configured on the same IP subnet as
the server.

![Site Builder Application image 49](./images/starwatch-sms-user-guide-site-builder-rev-9_49.png)

From the EntroStar driver page of the device library, click on the *BACnet Discovery Tool* button which
appears as a pulse icon at the top of the screen. This will cause the system to scan the network and
discover the panels.

![Site Builder Application image 50](./images/starwatch-sms-user-guide-site-builder-rev-9_50.png)

![Site Builder Application image 51](./images/starwatch-sms-user-guide-site-builder-rev-9_51.png)

As the panels are found, they will appear in the table. Once all panels have been discovered, click the
*Stop Scanning* button at the top left of the screen.
The generated panel list will display all the panels on the subnet, whether or not they are part of this
configuration. Their status can be:

*Cleaned*
The panel is available to be associated with an existing panel in the configuration, or can be
added as a new panel into the configuration.

*Associated*
The panel has been discovered and is part of the configuration for this system.

![Site Builder Application image 52](./images/starwatch-sms-user-guide-site-builder-rev-9_52.png)


*Used*
The panel has been previously associated with a configuration from a different system. If the
panel is intended for use in this system, it must be Factory Reset using the multicast tool to
clean the panel. It will then reappear in this list as “Cleaned”.
Cleaned devices can be used to associate with panels that are already in the configuration, or used to
create new devices in the configuration.
To associate with an existing panel in the configuration, highlight the panel you wish to associate and
hit the *Associate* button. Next, select the panel from the pull down menu and click *OK* to associate the
physical panel with the panel in the configuration.

![Site Builder Application image 53](./images/starwatch-sms-user-guide-site-builder-rev-9_53.png)

![Site Builder Application image 54](./images/starwatch-sms-user-guide-site-builder-rev-9_54.png)

The panel will change to “Associated” in the table.

![Site Builder Application image 55](./images/starwatch-sms-user-guide-site-builder-rev-9_55.png)

![Site Builder Application image 56](./images/starwatch-sms-user-guide-site-builder-rev-9_56.png)

You may also select a “Cleaned” panel from the list and hit the *Add Selected* button.

![Site Builder Application image 57](./images/starwatch-sms-user-guide-site-builder-rev-9_57.png)

The panel will become associated with your configuration, and added to the list of devices.

![Site Builder Application image 58](./images/starwatch-sms-user-guide-site-builder-rev-9_58.png)

![Site Builder Application image 59](./images/starwatch-sms-user-guide-site-builder-rev-9_59.png)

The new panel may now be selected and configured for all of its properties.

![Site Builder Application image 60](./images/starwatch-sms-user-guide-site-builder-rev-9_60.png)

![Site Builder Application image 61](./images/starwatch-sms-user-guide-site-builder-rev-9_61.png)

## 2.3 UPDATING FIRMWARE

The BACnet discovery tool is also used for updating firmware on a panel. Before using this procedure,
you must run the EntroStar firmware .exe file located in the StarWatch SMS media folder.

![Site Builder Application image 62](./images/starwatch-sms-user-guide-site-builder-rev-9_62.png)

From the EntroStar driver page of the device library, click on the *BACnet Discovery Tool* button which
appears as a pulse icon at the top of the screen. This will cause the system to scan the network and
discover the panels.

![Site Builder Application image 63](./images/starwatch-sms-user-guide-site-builder-rev-9_63.png)

![Site Builder Application image 64](./images/starwatch-sms-user-guide-site-builder-rev-9_64.png)

As the panels are found, they will appear in the table. Once all panels have been discovered, click the
*Stop Scanning* button at the top left of the screen.
Highlight the panel you wish to update and select the version of firmware you wish to load into the
panel from the *Available Firmware* pull-down in the upper right corner. Next, click the *Update*
*Firmware* button.

![Site Builder Application image 65](./images/starwatch-sms-user-guide-site-builder-rev-9_65.png)

The tool will display a progress indicator for the firmware update.

![Site Builder Application image 66](./images/starwatch-sms-user-guide-site-builder-rev-9_66.png)

![Site Builder Application image 67](./images/starwatch-sms-user-guide-site-builder-rev-9_67.png)

## 2.4 TEMPLATES

One of the benefits of the configuration package is the use of templates. For EntroStar panels, after
determining a typical or standard configuration for your customers, you can save the configuration as a
template. This is done by right-clicking on the EntroStar you want to save and selecting the *Save as*
*Template* option.

![Site Builder Application image 68](./images/starwatch-sms-user-guide-site-builder-rev-9_68.png)

![Site Builder Application image 69](./images/starwatch-sms-user-guide-site-builder-rev-9_69.png)

A pop-up will appear asking you to name the template. Simply enter a name for the new template and
click the *Save* button.

![Site Builder Application image 70](./images/starwatch-sms-user-guide-site-builder-rev-9_70.png)

Once a template has been created, it will be available in the list of devices for the driver.

![Site Builder Application image 71](./images/starwatch-sms-user-guide-site-builder-rev-9_71.png)

![Site Builder Application image 72](./images/starwatch-sms-user-guide-site-builder-rev-9_72.png)

## 2.5 SAVING

All changes made to the configuration are constantly being updated locally. They *are not* being
synchronized to the database. Upon exiting the devices configuration screen (the *Back Arrow* button in
the upper left hand corner), you will be prompted if you would like to update the system.

![Site Builder Application image 73](./images/starwatch-sms-user-guide-site-builder-rev-9_73.png)

If you click the *No* button, you can continue to build your system and can update the database when
you have completed your changes. Clicking the *Yes* button will cause all changes to be updated in the
database and become live.

![Site Builder Application image 74](./images/starwatch-sms-user-guide-site-builder-rev-9_74.png)

If there are changes that have not been saved to the database, a *Save* command will appear in the
main Site Builder menu.

![Site Builder Application image 75](./images/starwatch-sms-user-guide-site-builder-rev-9_75.png)

This can be used to update the database at any time.

![Site Builder Application image 76](./images/starwatch-sms-user-guide-site-builder-rev-9_76.png)

If after doing work that has not been updated you wish to discard the work, you may go to the devices
configuration and click the *Undo Changes* button in the upper right hand corner.

![Site Builder Application image 77](./images/starwatch-sms-user-guide-site-builder-rev-9_77.png)

This will cause your local configuration to be overwritten by the configuration that is currently running
in the live database.

![Site Builder Application image 78](./images/starwatch-sms-user-guide-site-builder-rev-9_78.png)

## 2.6 ADDING ONVIF GANZ CAMERAS

To add an ONVIF Ganz camera to the system, you essentially use the same process as adding any other
device to the system.
Note: for Ganz camera configurations for IP settings, users, time, etc., see the Ganz configuration
manual.
Note: before using *Site Builder*, use the Ganz camera discovery tool MDload-V453.exe to find Ganz
cameras and set their IP addresses as desired.
Next, from the main *Site Builder* screen, click the red *Devices* tile.

![Site Builder Application image 79](./images/starwatch-sms-user-guide-site-builder-rev-9_79.png)

![Site Builder Application image 80](./images/starwatch-sms-user-guide-site-builder-rev-9_80.png)

![Site Builder Application image 81](./images/starwatch-sms-user-guide-site-builder-rev-9_81.png)

Click on the plus sign in the *Add Device* icon near the top of the device manager screen.

![Site Builder Application image 82](./images/starwatch-sms-user-guide-site-builder-rev-9_82.png)

![Site Builder Application image 83](./images/starwatch-sms-user-guide-site-builder-rev-9_83.png)

![Site Builder Application image 84](./images/starwatch-sms-user-guide-site-builder-rev-9_84.png)

From the *Device Library* menu on the left side of the screen, select *Onvif* and click the
icon.

![Site Builder Application image 85](./images/starwatch-sms-user-guide-site-builder-rev-9_85.png)

![Site Builder Application image 86](./images/starwatch-sms-user-guide-site-builder-rev-9_86.png)

Allow the tool to discover all ONVIF cameras and click the *Stop Scanning* button.

![Site Builder Application image 87](./images/starwatch-sms-user-guide-site-builder-rev-9_87.png)

Each line in the list provides information related to the discovered ONVIF cameras:

*Name*
The name that the camera will be identified by in the system.

*IP Address*
The IP address that the camera is set up to use.

*Connection*
The current status of the camera.

*Login*
The default login for Ganz cameras is *ADMIN*.

*Password*
The default password for Ganz cameras is *1234*.

![Site Builder Application image 88](./images/starwatch-sms-user-guide-site-builder-rev-9_88.png)

![Site Builder Application image 89](./images/starwatch-sms-user-guide-site-builder-rev-9_89.png)

Enter the appropriate *Login* and *Password* information for the camera in the list that you would like to
add to your system and click the *Login* button. The connection status for the camera will change to
*Connected* after successful login.
Next, click the checkbox in the first column of the table for the camera you want to add and click the
*Update* button.

![Site Builder Application image 90](./images/starwatch-sms-user-guide-site-builder-rev-9_90.png)

When returned to the *Device Library* screen, click the *Close* button.

![Site Builder Application image 91](./images/starwatch-sms-user-guide-site-builder-rev-9_91.png)

![Site Builder Application image 92](./images/starwatch-sms-user-guide-site-builder-rev-9_92.png)

A video server will be added to the system and displayed as a yellow *Onvif Video* icon. To configure the
camera, double-click on the icon.

![Site Builder Application image 93](./images/starwatch-sms-user-guide-site-builder-rev-9_93.png)

![Site Builder Application image 94](./images/starwatch-sms-user-guide-site-builder-rev-9_94.png)

Selection of the yellow panel in the upper left provides properties associated with connecting to the
camera. Enter an appropriate name in the *Name* field, leaving all other defaults in place.

![Site Builder Application image 95](./images/starwatch-sms-user-guide-site-builder-rev-9_95.png)

Click the *Close* button to return to the devices screen.

![Site Builder Application image 96](./images/starwatch-sms-user-guide-site-builder-rev-9_96.png)

![Site Builder Application image 97](./images/starwatch-sms-user-guide-site-builder-rev-9_97.png)

![Site Builder Application image 98](./images/starwatch-sms-user-guide-site-builder-rev-9_98.png)

Click the *Back*
button in the top left corner to return to the main *Site Builder* screen.

![Site Builder Application image 99](./images/starwatch-sms-user-guide-site-builder-rev-9_99.png)

![Site Builder Application image 100](./images/starwatch-sms-user-guide-site-builder-rev-9_100.png)

Click the *Update* option from the left-side menu to commit the changes to the database.

![Site Builder Application image 101](./images/starwatch-sms-user-guide-site-builder-rev-9_101.png)

![Site Builder Application image 102](./images/starwatch-sms-user-guide-site-builder-rev-9_102.png)

When you access the *Maps and Plans* area of your configuration, the ONVIF camera will now be
available in the system Navigator window.

![Site Builder Application image 103](./images/starwatch-sms-user-guide-site-builder-rev-9_103.png)

## 2.7 ADDING AXIS CAMERAS

To add an Axis camera to the system, you essentially use the same process as adding any other device
to the system. Note: for Axis camera configurations for IP settings, users, time, etc., see the Axis
configuration manual.
From the main *Site Builder* screen, click the red *Devices* tile.

![Site Builder Application image 104](./images/starwatch-sms-user-guide-site-builder-rev-9_104.png)

![Site Builder Application image 105](./images/starwatch-sms-user-guide-site-builder-rev-9_105.png)

![Site Builder Application image 106](./images/starwatch-sms-user-guide-site-builder-rev-9_106.png)

Next, click on the plus sign in the *Add Device* icon near the top of the device manager screen.

![Site Builder Application image 107](./images/starwatch-sms-user-guide-site-builder-rev-9_107.png)

![Site Builder Application image 108](./images/starwatch-sms-user-guide-site-builder-rev-9_108.png)

From the device library menu on the left side of the screen, select *Axis Video* and double-click on the
yellow *IP Camera* tile.

![Site Builder Application image 109](./images/starwatch-sms-user-guide-site-builder-rev-9_109.png)

A video driver and a single camera will be added to the system and displayed as a yellow *Axis Video*
icon. To configure the camera, double-click on the icon.

![Site Builder Application image 110](./images/starwatch-sms-user-guide-site-builder-rev-9_110.png)

![Site Builder Application image 111](./images/starwatch-sms-user-guide-site-builder-rev-9_111.png)

Selection of the yellow panel in the upper left provides properties associated with connecting to the
camera.

![Site Builder Application image 112](./images/starwatch-sms-user-guide-site-builder-rev-9_112.png)

Enter the information for the camera in the pop-up dialog box:

*Name*
Enter the name that the camera will be identified by in the system.

*IP Address*
This is the IP address that the camera will be set up to use. Consult the Axis user manual to
find the address for a specific camera.

*IP Port*
This is typically not required for an Axis Camera

![Site Builder Application image 113](./images/starwatch-sms-user-guide-site-builder-rev-9_113.png)


*User*
The username is set up by the user before first use.

*Password*
The password is set up by the user before first use.

*Name*
Enter the name that the camera will be identified by in the system.

*Video Input*
Indicates which stream is being used.

*Media Type*
The preferred option is H264, but others can be used

*UI Mode*
Used for PTZ settings.

*Presets*
Presets are predefined positions and zoom levels to which a PTZ camera will position itself.
For example, if an alarm occurs at a door, you would want the PTZ camera to point at the
door. StarWatch SMS allows users to define which camera to call up upon alarms and how the
camera should be positioned. Presets are defined using the Web Browser interface to the Axis
Camera. Clicking the *Update* button will import all of the current presets from the camera and
make them available within the system.

![Site Builder Application image 114](./images/starwatch-sms-user-guide-site-builder-rev-9_114.png)

You may also turn on the *Advanced Settings* to display and modify them.

![Site Builder Application image 115](./images/starwatch-sms-user-guide-site-builder-rev-9_115.png)

Consult the Axis user manual for details on these features within your specific camera.
Once all parameters have been defined, click the *Close* button.

![Site Builder Application image 116](./images/starwatch-sms-user-guide-site-builder-rev-9_116.png)

## 3.0 VIEWING AND EDITING POINTS

To access and edit specific points within the system, click the yellow *Points* tile on the main *Site*
*Builder* screen.

![Site Builder Application image 117](./images/starwatch-sms-user-guide-site-builder-rev-9_117.png)

![Site Builder Application image 118](./images/starwatch-sms-user-guide-site-builder-rev-9_118.png)

The *Points* screen is used for viewing a list of all the points and devices that have been added to the
system and quickly editing certain point properties. You can also view and edit the widget assignment
settings of each device and point (please see section **4.7 CREATING WIDGETS** for more details on how
widgets function within the system).

![Site Builder Application image 119](./images/starwatch-sms-user-guide-site-builder-rev-9_119.png)

The screen provides useful filtering and sorting options in the form of grid controls.

![Site Builder Application image 120](./images/starwatch-sms-user-guide-site-builder-rev-9_120.png)

## 3.1 EDITING POINT PROPERTIES

![Site Builder Application image 121](./images/starwatch-sms-user-guide-site-builder-rev-9_121.png)

To edit a point, click on the
button located at the top-center of your screen.

![Site Builder Application image 122](./images/starwatch-sms-user-guide-site-builder-rev-9_122.png)

This will place the list into editing mode, allowing you to edit points and assign widgets to them, if
necessary.

![Site Builder Application image 123](./images/starwatch-sms-user-guide-site-builder-rev-9_123.png)

![Site Builder Application image 124](./images/starwatch-sms-user-guide-site-builder-rev-9_124.png)

Next, click on the point/device in the list that you would like to edit. The point will become
highlighted.

![Site Builder Application image 125](./images/starwatch-sms-user-guide-site-builder-rev-9_125.png)

![Site Builder Application image 126](./images/starwatch-sms-user-guide-site-builder-rev-9_126.png)

There are two ways to edit a point:

You can edit point parameters by clicking on a point and then selecting a field in the
highlighted row that you wish to edit. You can then enter a new value by typing directly into
the field.

You can edit device properties from the right-side *Device Details* pane. The values in some
properties are there by default so be sure you are making the proper changes to the correct
points. For example, doors have multiple widgets available, such as Door, S-Door, and I-Door,
each with different characteristics. In this case, you should check which door widget type is
the best fit for your system.

![Site Builder Application image 127](./images/starwatch-sms-user-guide-site-builder-rev-9_127.png)

![Site Builder Application image 128](./images/starwatch-sms-user-guide-site-builder-rev-9_128.png)

In the example below, the *Airport Panel* device has been selected. The description field has been
edited to be a better indicator of the function of the device and a *PANEL* widget has been assigned.
The *Zone* setting shows that the panel already exists in the *Outside* zone, which the system created by
default during the zone creation process.

![Site Builder Application image 129](./images/starwatch-sms-user-guide-site-builder-rev-9_129.png)

![Site Builder Application image 130](./images/starwatch-sms-user-guide-site-builder-rev-9_130.png)

![Site Builder Application image 131](./images/starwatch-sms-user-guide-site-builder-rev-9_131.png)

In the next example, the *Airport, Door 1* point has been selected. Using the *Widget* drop-down menu,
the *DOOR* widget has been assigned. The door has been previously set to reside in the *Airport Security*
*Check Point* zone using the *Maps and Plans* function. If the point had not been placed in a zone, you
could use the *Zone* drop-down menu to place it.

![Site Builder Application image 132](./images/starwatch-sms-user-guide-site-builder-rev-9_132.png)

![Site Builder Application image 133](./images/starwatch-sms-user-guide-site-builder-rev-9_133.png)

![Site Builder Application image 134](./images/starwatch-sms-user-guide-site-builder-rev-9_134.png)

## 3.2 MULTI-SELECTING POINTS

In cases where multiple points share the same properties, for example they have the same category or
are located in the same zone, you can multi-select points and edit them simultaneously. Simply hold
down the *Ctrl* key on your keyboard, click on the desired points to highlight them in the list, and then
edit their properties. Changes will affect all of the selected points.
In the screenshot below, two doors have been selected from the list. Any changes made in the *Device*
*Details* pane will be applied to both doors.

![Site Builder Application image 135](./images/starwatch-sms-user-guide-site-builder-rev-9_135.png)

![Site Builder Application image 136](./images/starwatch-sms-user-guide-site-builder-rev-9_136.png)

Note: You can always delete or undo changes by hitting the
icon located on the top right side
of the screen.

![Site Builder Application image 137](./images/starwatch-sms-user-guide-site-builder-rev-9_137.png)

To save the changes to the database, click the
icon on the main *Site Builder* screen.

![Site Builder Application image 138](./images/starwatch-sms-user-guide-site-builder-rev-9_138.png)

## 4.0 CREATING MAPS AND PLANS

*Site Plans* are essential to configuring your security site. In order to configure the alarm settings in the
StarWatch SMS *Operator* application, you must create and configure a *Site Plan*. Within a plan, *Site*
*Maps* are used to provide a graphical view of the condition of devices in the system. This view is useful
for indicating where in a facility something is occurring. Maps include widgets that represent the
hardware device drivers used with alarm hardware entities, such as motion sensors, door latches, etc.
To create new maps and plans, you must do the following steps in order:

Create a new *Site Plan*

Create a new *Site Map*

Add *Zones* to an *Area* within a map

Add hardware *Points*, which includes associating widget icons to input/output points

Save the *Site Plan* to the database
Note: before beginning configuration, make sure you are connected and online in your site builder. If
the *Site Builder* status in the upper right-hand corner of the screen says you are offline, make sure
your services are running using your *Management Console* application.
Note: to ensure that changes you make to the configuration are not lost, save your work directly to the
database using:

![Site Builder Application image 139](./images/starwatch-sms-user-guide-site-builder-rev-9_139.png)


icon on the *Site Map* screen
The

![Site Builder Application image 140](./images/starwatch-sms-user-guide-site-builder-rev-9_140.png)


icon on the *Site Builder* screen
The

![Site Builder Application image 141](./images/starwatch-sms-user-guide-site-builder-rev-9_141.png)

Note: for many of these instructions, there is often more than one way to complete a task (ex.
renaming a node or panel). The instructions step you through the default workspace layout and the
most common method of completing the tasks.

## 4.1 CREATING A SITE PLAN

To begin creating or editing maps and plans, click the green *Maps and Plans* tile on the main *Site*
*Builder* screen.

![Site Builder Application image 142](./images/starwatch-sms-user-guide-site-builder-rev-9_142.png)

In the *Navigator* pane of the main *Site Builder* window, click on the *Maps* section. In the blank area of
the *Navigator* pane, right-click and select the *Create New Site Plan* option from the menu.

![Site Builder Application image 143](./images/starwatch-sms-user-guide-site-builder-rev-9_143.png)

Next, type in a name for your site in the *Site Name* field and hit the *Create* button.

![Site Builder Application image 144](./images/starwatch-sms-user-guide-site-builder-rev-9_144.png)

![Site Builder Application image 145](./images/starwatch-sms-user-guide-site-builder-rev-9_145.png)

Note: when you are creating maps and site plans, make sure you are in the *Maps* or *Maps/Zones* view.
This is indicated by the view buttons on the left-hand side of the screen above the *Navigator* pane.

![Site Builder Application image 146](./images/starwatch-sms-user-guide-site-builder-rev-9_146.png)

![Site Builder Application image 147](./images/starwatch-sms-user-guide-site-builder-rev-9_147.png)

## 4.2 CREATING A SITE MAP

In the *Navigator* pane, right-click on the name of the *Site Plan* and select the *Create New Site Map*
option from the drop-down list.

![Site Builder Application image 148](./images/starwatch-sms-user-guide-site-builder-rev-9_148.png)

![Site Builder Application image 149](./images/starwatch-sms-user-guide-site-builder-rev-9_149.png)

In the *General* section of the *Site Map Properties* pop-up screen, enter a name for the new site map in
the *Name* field.

![Site Builder Application image 150](./images/starwatch-sms-user-guide-site-builder-rev-9_150.png)

![Site Builder Application image 151](./images/starwatch-sms-user-guide-site-builder-rev-9_151.png)

The fields of the *Site Map Properties* pop-up screen are described below:
**Section**
**Field Name**
**Description**
**Default**
The name of the site map.
NewSiteMap-<number>
General
Name
The level of the building where the site
1
Levels Count
map resides.
When an alarm occurs, the map will zoom
50
Zoom on Alarm
in by this percentage.
The latitude of your site.
Your current location
Datum Point
Latitude
The longitude of your site.
Longitude
The length of your site.
500
Size
X (meters)
The width of your site.
500
Y (meters)
Make
Specifies whether the site map should be
Disabled
Background
Proportional
proportional to the background image, if
using one.
Click *Browse* to locate a background
Browse
Blank
image file to use. Accepted file types
are gif, bmp, jpg, and pdf.
Import CAD
Click *Import CAD* to locate a CAD-
generated background image file.
Accepted file types are dwg and dxf.
Google
Click *Google* to use a map file from
Google Maps.

![Site Builder Application image 152](./images/starwatch-sms-user-guide-site-builder-rev-9_152.png)

## 4.2.1 IMPORTING A STANDARD IMAGE

If you have a gif, bmp, jpg, or pdf-type image you would like to use as your map background, you can
browse and upload the file using the *Browse* tool in the *Background* section.

![Site Builder Application image 153](./images/starwatch-sms-user-guide-site-builder-rev-9_153.png)

Clicking on the *Browse* button will launch the Windows file browser, where you can locate and select
the appropriate file from your directories.
Note: when importing an image, enable the *Make Proportional* option to ensure your background image
retains its proper proportions and does not become stretched or elongated.

## 4.2.2 IMPORTING A CAD FILE

You can import a CAD-generated file for use as the *Site Map* background at the time of initial map
creation or any time later. The benefit of this type of file is that it allows you to select and modify
what you would like to see on the screen (ex. zoom into a specific section of the drawing, etc.).

![Site Builder Application image 154](./images/starwatch-sms-user-guide-site-builder-rev-9_154.png)

To upload and configure a CAD file, click the *Import CAD* button in the *Background* section.

![Site Builder Application image 155](./images/starwatch-sms-user-guide-site-builder-rev-9_155.png)

Alternately, if you have already closed the *Site Map Properties* pop-up screen, you can click on the
*Import CAD* icon in the *Tools* menu of the *Site Planner* window:

![Site Builder Application image 156](./images/starwatch-sms-user-guide-site-builder-rev-9_156.png)

In the *Import CAD* window, clicking the *Browse* button will launch the standard Windows file browser,
where you can locate and select the appropriate drawing file from your directories.

![Site Builder Application image 157](./images/starwatch-sms-user-guide-site-builder-rev-9_157.png)

Once the CAD file has been designated, you can configure the following settings using the fields on the
right-hand side of the *Import CAD* window:

Background color for the graphic

Rotation of the graphic

Image size, both width and height

Aspect ratio to be locked if desired

![Site Builder Application image 158](./images/starwatch-sms-user-guide-site-builder-rev-9_158.png)

Click *Save As* to save the image as a new graphic.

![Site Builder Application image 159](./images/starwatch-sms-user-guide-site-builder-rev-9_159.png)

To further format the image, you can select or deselect the drawing aspects you would like to upload
and display on the map using the checklist provided in the *Layers* section.
You can also zoom into the picture using your mouse scroll button. To reposition your map, hold your
mouse above the image in the map display area and click and drag the image to the desired location.

![Site Builder Application image 160](./images/starwatch-sms-user-guide-site-builder-rev-9_160.png)

![Site Builder Application image 161](./images/starwatch-sms-user-guide-site-builder-rev-9_161.png)

When you are finished editing the *Site Map*, hit the *OK* button.

![Site Builder Application image 162](./images/starwatch-sms-user-guide-site-builder-rev-9_162.png)

## 4.2.3 CREATING A MAP WITH DRAWING TOOLS

If you do not have a graphics file to import as the background for your *Site Map*, the *Drawing Tools*
area on the right-hand side of the screen contains an assortment of shape and line options to help you
create a map by hand.

![Site Builder Application image 163](./images/starwatch-sms-user-guide-site-builder-rev-9_163.png)

**Icon**
**Tool Name**
**Description**

![Site Builder Application image 164](./images/starwatch-sms-user-guide-site-builder-rev-9_164.png)

Arrow
Select entities on the map, such as widgets, lines, and
rectangles.
Freehand
Pan the site map graphic in the main map management

![Site Builder Application image 165](./images/starwatch-sms-user-guide-site-builder-rev-9_165.png)

window.
Line
Draw a line.

![Site Builder Application image 166](./images/starwatch-sms-user-guide-site-builder-rev-9_166.png)

Ellipse
Draw an ellipse.
Rounded Rectangle
Draw a rounded rectangle.
Line / Fill Color Picker
Pick the line and fill colors.
Rectangle
Draw a rectangle.
Polygon
Draw a polygon.

![Site Builder Application image 167](./images/starwatch-sms-user-guide-site-builder-rev-9_167.png)

Eye Dropper
Select the line and fill properties of an entity.

![Site Builder Application image 168](./images/starwatch-sms-user-guide-site-builder-rev-9_168.png)

Annotation
Add annotations to the site map.
Static Widget
Select a widget from a drop-down list of existing status

![Site Builder Application image 169](./images/starwatch-sms-user-guide-site-builder-rev-9_169.png)

widgets and place it into a graphic.

![Site Builder Application image 170](./images/starwatch-sms-user-guide-site-builder-rev-9_170.png)

The toolbar at the top of the screen is also helpful when laying out and adjusting your drawing.

![Site Builder Application image 171](./images/starwatch-sms-user-guide-site-builder-rev-9_171.png)

**Group**
**Group Icons**
**Description**

![Site Builder Application image 172](./images/starwatch-sms-user-guide-site-builder-rev-9_172.png)

Clipboard
These are tasks typically completed with the
Microsoft Windows clipboard.

Cut

Copy

Paste

Undo

Redo
Navigate
Navigate in the map manager window. Zoom in/out. Pan

![Site Builder Application image 173](./images/starwatch-sms-user-guide-site-builder-rev-9_173.png)

around in four directions. Show/hide grid, annotations,
ioComp controls, and default display area on map.
Align
Align entities based on left, right, top, bottom edge.
Make entities the same size, width, or height.
Z-order
Bring overlapping entities to the front or back of the

![Site Builder Application image 174](./images/starwatch-sms-user-guide-site-builder-rev-9_174.png)

layout.

![Site Builder Application image 175](./images/starwatch-sms-user-guide-site-builder-rev-9_175.png)

Properties
Set the width, color, and fill type of a line or entity.
Annotation
Add text annotations to the map.
Extent
Extend the map size up, down, left, or right.

![Site Builder Application image 176](./images/starwatch-sms-user-guide-site-builder-rev-9_176.png)

Undo
Undo any changes recently made.

![Site Builder Application image 177](./images/starwatch-sms-user-guide-site-builder-rev-9_177.png)

## 4.2.4 SAVING A MAP TO THE SYSTEM DATABASE

After completing your map settings in the *Site Map Properties* window, click the *OK* button.

![Site Builder Application image 178](./images/starwatch-sms-user-guide-site-builder-rev-9_178.png)

![Site Builder Application image 179](./images/starwatch-sms-user-guide-site-builder-rev-9_179.png)

![Site Builder Application image 180](./images/starwatch-sms-user-guide-site-builder-rev-9_180.png)

Next, click the *Save*
icon on the top menu bar in the main *Site Plan* screen. This saves your work
to the computer.

![Site Builder Application image 181](./images/starwatch-sms-user-guide-site-builder-rev-9_181.png)

![Site Builder Application image 182](./images/starwatch-sms-user-guide-site-builder-rev-9_182.png)

To save the changes to the database, click the
icon on the main *Site Builder* screen

![Site Builder Application image 183](./images/starwatch-sms-user-guide-site-builder-rev-9_183.png)

## 4.2.5 UNDERSTANDING LAYERS

Each part of the *Site Map* is built in the system using *Layers*. Each layer represents a grouping of
drawing objects, such as the *Widgets Layer* or the *Background Layer*.

![Site Builder Application image 184](./images/starwatch-sms-user-guide-site-builder-rev-9_184.png)

Layers can be viewed in the *Layers Area* located on the right-hand side of the screen.

![Site Builder Application image 185](./images/starwatch-sms-user-guide-site-builder-rev-9_185.png)

![Site Builder Application image 186](./images/starwatch-sms-user-guide-site-builder-rev-9_186.png)

The icons and functions of the *Layers Area* are described below:
**Icon**
**Tool Name**
**Description**
Up/Down
Moves the active layer up or down

![Site Builder Application image 187](./images/starwatch-sms-user-guide-site-builder-rev-9_187.png)

in the list, depending on which
arrow was clicked.
Layer Properties
Opens the *Layer Properties* window.

![Site Builder Application image 188](./images/starwatch-sms-user-guide-site-builder-rev-9_188.png)

You can change the layer name,

![Site Builder Application image 189](./images/starwatch-sms-user-guide-site-builder-rev-9_189.png)

level, and whether you want it to
be visible on the map.
Add a Layer
Allows you to add a layer and

![Site Builder Application image 190](./images/starwatch-sms-user-guide-site-builder-rev-9_190.png)

designate the layer type, name, and

![Site Builder Application image 191](./images/starwatch-sms-user-guide-site-builder-rev-9_191.png)

site map.
Delete
Deletes a layer.

![Site Builder Application image 192](./images/starwatch-sms-user-guide-site-builder-rev-9_192.png)

![Site Builder Application image 193](./images/starwatch-sms-user-guide-site-builder-rev-9_193.png)

There are three types of layers: static, background, and linked.

![Site Builder Application image 194](./images/starwatch-sms-user-guide-site-builder-rev-9_194.png)


The *Static* layer type is used as the standard layer for drawing objects in your graphic. For indoor
areas,  typical  *Static*  layers  might  include  walls,  windows,  stairs,  and  other  interior  aspects.
Outdoor areas might incorporate roads, walkways, trees, and other landscape features. In most
cases, the majority of the graphic elements included in a *Site Map* are placed in *Static* layers.

The *Background* layer type is used to set a background image for your overall graphic. When
creating  a  *Background*  layer,  you  will  be  asked  to  select  an  existing  graphic  to  set  as  the
background. Any objects you add to other layers will be displayed on top of your background
image. Additional graphic elements cannot be added to a *Background* layer. This layer should
remain positioned at the bottom of the layers list, beneath all other layers. Alternately, you can
set a single color as the background for your map.

The  *Linked*  layer  type  is  used  to  create  interactive  “jump”  areas  that,  when  clicked,  will
automatically open another site map. This linking aspect is utilized when using the *Site Viewer*
function in the main *Operator* interface. When clicked in *Site Viewer*, any graphic element you
include in a *Linked* layer will cause the current view to switch to another designated map.
You should select the type that is applicable for your layer application.

![Site Builder Application image 195](./images/starwatch-sms-user-guide-site-builder-rev-9_195.png)

## 4.3 CREATING A ZONE

In the system, *Zones* can be used for any or all of the following purposes:

*Zones*  can  be  a  collection  of  devices  that  are  located  in  the  same  physical  vicinity  within  a
facility.  These devices can be graphically collected into a zone on a map, and the zone will flash
in alarm whenever any of the devices contained within it go into the alarm state. This is purely a
graphical indication.

*Zones* can be used within the access control feature of the system as an indication of where
someone is located or last went.  Portals can be defined to indicate what zone they lead to/from
and the location of an individual can then be determined by which door they last used.

*Zones* can be used within the intrusion detection feature of the system. In this case, a zone is
managed by a specific alarm panel or piece of hardware in the system, and the zone can be
placed into an armed or disarmed condition. When the zone is armed, alarms will be generated
for  the  points  in  the  zone.  When  the  zone  is  disarmed,  alarms  will  not  be  generated.  These
alarm zones must be linked to a physical panel that will manage them.

![Site Builder Application image 196](./images/starwatch-sms-user-guide-site-builder-rev-9_196.png)

## 4.3.1 ADDING A ZONE TO AN AREA

To create a *Zone*, make sure you are in the *Maps* or *Maps/Zones* view, which displays your *Site Plan* in
the *Navigator* pane.

![Site Builder Application image 197](./images/starwatch-sms-user-guide-site-builder-rev-9_197.png)

In the *Navigator* pane, right-click on the *Area* name displayed beneath the name of your *Site Map* and
select the *Add Zone* menu option from the pop-up menu.
Note: when a map is initially created, the system automatically assigns an area to it and lists it in the
*Navigator* pane.

![Site Builder Application image 198](./images/starwatch-sms-user-guide-site-builder-rev-9_198.png)

Note: *Areas* are visually indicated by the
icon.

![Site Builder Application image 199](./images/starwatch-sms-user-guide-site-builder-rev-9_199.png)

In the *Add Zone* pop-up screen, enter a name for the new zone in the *Name* field.

![Site Builder Application image 200](./images/starwatch-sms-user-guide-site-builder-rev-9_200.png)

The default settings will set the zone to be shown on the previously selected site map.

![Site Builder Application image 201](./images/starwatch-sms-user-guide-site-builder-rev-9_201.png)

The remaining fields of the *Add Zone* pop-up screen are described below:
**Section**
**Field Name**
**Description**
**Default**
Name
The name of the new zone.
NewZone-1
Create a new
Number
The number of the new zone.
1
zone
Show on site
Check this option to show/draw/add the
Checked off
map
zone on the map. This allows the zone to
be used as a collection of widget icons
that are contained within it.
Select site map
Select the area in which you are
Drop down menu
area
selecting/assigning the zone.
Use for access
Check this option to use the zone for
(entry or exit)
entry or exit. Once selected, you will
have options for anti-passback
configuration.
Anti-passback
Defines the anti-passback mode (none,
none
mode
timed, logical)
Anti-passback
Defines the timeout for timed anti-
120
timeout
passback
Anti-passback
Defines the strength of the anti-passback.
hard
strength
Hard anti-passback will not allow an
individual through a door. Soft anti-
passback will allow an individual through
a door, but will generate an anti-
passback alarm in the system.
Select site map
Select the area on which you are adding
none
Add Alarm
area
the alarm zone.
Zone to a
Select Alarm
Select the panel that contains and
none
Site Map
Zone
manages the alarm zone that is being
created on the map.
After completing your zone settings in the *Add Zone* window, click the *OK* button. The new zone will be
added to the tree map in the *Navigator* pane.

![Site Builder Application image 202](./images/starwatch-sms-user-guide-site-builder-rev-9_202.png)

## 4.3.2 SETTING ZONE PROPERTIES

Once you have added a zone, you will have the option to edit/add parameters and configurations.

![Site Builder Application image 203](./images/starwatch-sms-user-guide-site-builder-rev-9_203.png)

To modify a zone, right-click on the zone in the *Navigator* pane and select the *Properties* option.

![Site Builder Application image 204](./images/starwatch-sms-user-guide-site-builder-rev-9_204.png)

The *Modify Zone* window allows you to modify most of the properties set during initial creation of the
zone and also offers additional alarm-related fields.

![Site Builder Application image 205](./images/starwatch-sms-user-guide-site-builder-rev-9_205.png)

![Site Builder Application image 206](./images/starwatch-sms-user-guide-site-builder-rev-9_206.png)

The general fields available on the *Modify Zone* window are described below:
**Section**
**Field Name**
**Description**
**Default**
Name
The name of the new zone.
NewZone-1
Details
Number
The number of the new zone.
1
Show on site
Check this option to show/draw/add the
Checked off
map
zone on the map. This allows the zone to
be used as a collection of widget icons
that are contained within it.
Select site map
Select the area in which you are
Drop down menu
area
selecting/assigning the zone.
Use for access
Check this option to use the zone for
(entry or exit)
entry or exit. Once selected, you will
have options for anti-passback
configuration.
Anti-passback
Defines the anti-passback mode (none,
none
mode
timed, logical)
Anti-passback
Defines the timeout for timed anti-
120
timeout
passback
Anti-passback
Defines the strength of the anti-passback.
hard
strength
Hard anti-passback will not allow an
individual through a door. Soft anti-
passback will allow an individual through
a door, but will generate an anti-
passback alarm in the system.

![Site Builder Application image 207](./images/starwatch-sms-user-guide-site-builder-rev-9_207.png)

The alarm-related fields available on the *Modify Zone* window are described below:
**Section**
**Field Name**
**Description**
**Default**
Alarm zone
Used to designate the zone as an alarm
none
Alarm Zone
checkbox
zone
SCIF
Used to designate the zone as a SCIF
none
Panel Alarm
Selected from the available drop-down
none
Zone
menu
Flashing on
Select the type of alarm you would like
Unacknowledged
General
alarm
your zone to flash on when an alarm has
occurred
Minimum alarm
Select and choose the minimum alarm
0-
severity
severity that triggers the flashing zone
0-No alarm
1-Information
2-Significant
3-Minor
4-Major
5-Serious
6-Critical
Visible
Check this option to make the alarm zone
Checked
visible
Color
Select the color the zone will flash on
State Alarm

![Site Builder Application image 208](./images/starwatch-sms-user-guide-site-builder-rev-9_208.png)

when in the alarm state
Transparency
The level of transparency the visible zone
30
will have when flashing on the map
State Normal
Color
Select the color the zone will have in a

![Site Builder Application image 209](./images/starwatch-sms-user-guide-site-builder-rev-9_209.png)

normal state
Transparency
The level of transparency the visible zone
10
will have  in the normal state
Alarm incident
This gives two options to combine
0
time
alarm incident time
Combine
Alarms
- Combine alarms to incident
- Combine categories to incident

![Site Builder Application image 210](./images/starwatch-sms-user-guide-site-builder-rev-9_210.png)

## 4.3.3 DRAWING A ZONE

After adding a zone and setting any desired properties, you will need to draw the shape of the zone on
your map. Before utilizing the provided drawing tools, make sure you are currently in the *Zone Layer*
using the *Layers* pane on the right-hand side of the screen.

![Site Builder Application image 211](./images/starwatch-sms-user-guide-site-builder-rev-9_211.png)

To make the *Zone Layer* the active layer, click on it in the layers list to highlight it.

![Site Builder Application image 212](./images/starwatch-sms-user-guide-site-builder-rev-9_212.png)

![Site Builder Application image 213](./images/starwatch-sms-user-guide-site-builder-rev-9_213.png)

To physically draw the shape of your zone, use the drawing tools located above the *Layers* pane.

![Site Builder Application image 214](./images/starwatch-sms-user-guide-site-builder-rev-9_214.png)

![Site Builder Application image 215](./images/starwatch-sms-user-guide-site-builder-rev-9_215.png)

![Site Builder Application image 216](./images/starwatch-sms-user-guide-site-builder-rev-9_216.png)

For a simple square or rectangular shape, select the
tool. For an irregular shape, select the
tool. Using click-and-drag functionality, draw your zone on the map being sure to cover the entire area
that the zone will enclose.

![Site Builder Application image 217](./images/starwatch-sms-user-guide-site-builder-rev-9_217.png)

![Site Builder Application image 218](./images/starwatch-sms-user-guide-site-builder-rev-9_218.png)

Note: if you attempt to draw outside the area pane, you will see a
icon indicating that your zone
drawing cannot extend to this on-screen location.

![Site Builder Application image 219](./images/starwatch-sms-user-guide-site-builder-rev-9_219.png)

Once you have completed drawing the zone, click the *Save*
icon on the top menu bar in the main
*Site Plan* screen. This saves your work to the computer.

![Site Builder Application image 220](./images/starwatch-sms-user-guide-site-builder-rev-9_220.png)

To save the changes to the database, click the
icon on the main *Site Builder* screen.

![Site Builder Application image 221](./images/starwatch-sms-user-guide-site-builder-rev-9_221.png)

## 4.3.4 REMOVING A ZONE

To remove a zone, right-click on the zone in the tree list of the *Navigator* pane and select the *Remove*
*from Site Map* option.

![Site Builder Application image 222](./images/starwatch-sms-user-guide-site-builder-rev-9_222.png)

A message will pop up to confirm removing the zone.

![Site Builder Application image 223](./images/starwatch-sms-user-guide-site-builder-rev-9_223.png)

![Site Builder Application image 224](./images/starwatch-sms-user-guide-site-builder-rev-9_224.png)

## 4.4 ADDING POINTS/WIDGETS TO A MAP

Once a *Zone* has been added and drawn within a *Site Map*, you can add widgets, doors, alarms, and
points to your overall plan (please see section **4.7 CREATING WIDGETS** for more details on how widgets
function within the system).

![Site Builder Application image 225](./images/starwatch-sms-user-guide-site-builder-rev-9_225.png)

Before adding a widget or point to your zone, make sure you are currently in the *Zone Layer* using the
*Layers* pane on the right-hand side of the screen. To make the *Zone Layer* the active layer, click on it
in the layers list to highlight it.

![Site Builder Application image 226](./images/starwatch-sms-user-guide-site-builder-rev-9_226.png)

![Site Builder Application image 227](./images/starwatch-sms-user-guide-site-builder-rev-9_227.png)

Also, you will not be able to add points into your zone unless you have previously assigned widgets to
them. To assign widgets, click the yellow *Points* tile on the main *Site Builder* screen.

![Site Builder Application image 228](./images/starwatch-sms-user-guide-site-builder-rev-9_228.png)

Next, hit the *Enable Editing* option, select the *Widget* tab, and select the widget that corresponds to
the point. For more information on this process, please refer to section 3.0 EDITING POINTS that covers
the importing of widgets and assigning them to panels/points in your system.

![Site Builder Application image 229](./images/starwatch-sms-user-guide-site-builder-rev-9_229.png)

![Site Builder Application image 230](./images/starwatch-sms-user-guide-site-builder-rev-9_230.png)

## 4.4.1 SELECTING AND PLACING WIDGETS

Using the *Nodes* section of the *Navigator* pane, expand the tree under the EntroStar driver to access
the hardware points that you added earlier. The device, panel, and points will be listed as previously
configured in the system.

![Site Builder Application image 231](./images/starwatch-sms-user-guide-site-builder-rev-9_231.png)

Note: in the EntroStar driver tree, the icons representing the hardware entities are displayed with a
yellow icon. This indicator will change to green when the associated widget is placed on your map
graphic. If no widget is currently assigned to a point, the indicator will be red and cannot be placed on
a map.
To place a widget into a zone, simply select the device by clicking on it in the *Navigator* pane and drag
it over the map into your zone, dropping it where the hardware entity physically resides in your
facility.

![Site Builder Application image 232](./images/starwatch-sms-user-guide-site-builder-rev-9_232.png)

At this time, you can also resize or rotate the widget icon to build a better map graphic that represents
your actual site. You are able to move the widget, edit the size, and rotate it by clicking on it and
hovering your mouse on the corners of the icon. You can also right-click on the widget and choose the
properties you would like to change from the pop-up menu.
Note: before editing widget size, location, or rotation, make sure you are currently in the *Widget Layer*
using the *Layers* pane on the right-hand side of the screen. To make the *Widget Layer* the active layer,
click on it in the layers list to highlight it.

![Site Builder Application image 233](./images/starwatch-sms-user-guide-site-builder-rev-9_233.png)

Note: to delete a widget from your *Site Map* graphic, select it on the map and hit the *Delete* key on
your keyboard.

![Site Builder Application image 234](./images/starwatch-sms-user-guide-site-builder-rev-9_234.png)

## 4.4.2 ADDING A DOOR

When you drag a door widget into a zone, a pop-up message will ask if you would like to use the zone
as the entry zone for the access point.

![Site Builder Application image 235](./images/starwatch-sms-user-guide-site-builder-rev-9_235.png)

If you select *Yes*, the current zone will be used as the location of the door. If you select *No*, you can
assign a zone to the door at a later time or leave the door without an assigned zone.

![Site Builder Application image 236](./images/starwatch-sms-user-guide-site-builder-rev-9_236.png)

![Site Builder Application image 237](./images/starwatch-sms-user-guide-site-builder-rev-9_237.png)

## 4.5 RENAMING A SITE MAP

To rename a *Site Map*, in the site plans section of the *Navigator* pane, right-click on the map name and
select the *Rename Site Map* option from the pop-up menu.

![Site Builder Application image 238](./images/starwatch-sms-user-guide-site-builder-rev-9_238.png)

The name will become highlighted in dark blue and a cursor field will enable you to enter the new
name.

![Site Builder Application image 239](./images/starwatch-sms-user-guide-site-builder-rev-9_239.png)

Once you have completed renaming the map, click the *Save*
icon on the top menu bar in the
main *Site Plan* screen. This saves your work to the computer.

![Site Builder Application image 240](./images/starwatch-sms-user-guide-site-builder-rev-9_240.png)

To save the changes to the database, click the
icon on the main *Site Builder* screen.

![Site Builder Application image 241](./images/starwatch-sms-user-guide-site-builder-rev-9_241.png)

## 4.6 DELETING A SITE MAP

To delete a *Site Map*, in the site plans section of the *Navigator* pane, right-click on the map name and
select the *Delete Site Map* option from the pop-up menu.

![Site Builder Application image 242](./images/starwatch-sms-user-guide-site-builder-rev-9_242.png)

The delete confirmation window opens. Click the *OK* button to confirm the site map deletion or the
corner *X* button to exit without deleting.

![Site Builder Application image 243](./images/starwatch-sms-user-guide-site-builder-rev-9_243.png)

![Site Builder Application image 244](./images/starwatch-sms-user-guide-site-builder-rev-9_244.png)

Once you have completed deleting the map, click the *Save*
icon on the top menu bar in the main
*Site Plan* screen. This saves your work to the computer.

![Site Builder Application image 245](./images/starwatch-sms-user-guide-site-builder-rev-9_245.png)

To save the changes to the database, click the
icon on the main *Site Builder* screen.

![Site Builder Application image 246](./images/starwatch-sms-user-guide-site-builder-rev-9_246.png)

## 4.7 CREATING WIDGETS

*Widgets* are icons that represent alarm hardware on the *Site Map* graphic. Several types of widgets,
including static and dynamic, represent each hardware point type. You can also create customized
widgets for your specific site.
This section will describe how to:

Create a static widget

Create a dynamic widget

Import customized widgets into the database
When you create customized widgets, you can draw a graphic to associate with each state of the
widget. For example, on an access point such as a door you can create a flashing red image to
associate with a major alarm state and a neutral gray or blue image to indicate that the access point is
in the normal, non-alarmed state.

![Site Builder Application image 247](./images/starwatch-sms-user-guide-site-builder-rev-9_247.png)

## 4.7.1 CREATING A STATIC WIDGET

When the provided widget library does not contain an applicable option, you can create your own
widget that matches the needs of your site. A static widget does not have different states, but can be
used to link site maps together or indicate alarms that affect it.
To begin creating a static widget, click the blue *Widget Library* tile on the main *Site Builder* screen.

![Site Builder Application image 248](./images/starwatch-sms-user-guide-site-builder-rev-9_248.png)

![Site Builder Application image 249](./images/starwatch-sms-user-guide-site-builder-rev-9_249.png)

![Site Builder Application image 250](./images/starwatch-sms-user-guide-site-builder-rev-9_250.png)

![Site Builder Application image 251](./images/starwatch-sms-user-guide-site-builder-rev-9_251.png)

In the *Widget Library* window, click the *Create Widget* icon
located at the top of the *Navigator*
pane. Note: before clicking the *Create Widget* icon, make sure you highlight the folder you would like
the new widget to reside in on the *Navigator* tree list.

![Site Builder Application image 252](./images/starwatch-sms-user-guide-site-builder-rev-9_252.png)

![Site Builder Application image 253](./images/starwatch-sms-user-guide-site-builder-rev-9_253.png)

![Site Builder Application image 254](./images/starwatch-sms-user-guide-site-builder-rev-9_254.png)

In the *Widget Properties* pop-up window, type a name for the new widget in the *Name* field. From the
*Data Class* drop-down list, select the *STATIC* option and click the *Ok* button.

![Site Builder Application image 255](./images/starwatch-sms-user-guide-site-builder-rev-9_255.png)

![Site Builder Application image 256](./images/starwatch-sms-user-guide-site-builder-rev-9_256.png)

![Site Builder Application image 257](./images/starwatch-sms-user-guide-site-builder-rev-9_257.png)

In the bottom left of the main work area, click on the *Shapes*
tab.

![Site Builder Application image 258](./images/starwatch-sms-user-guide-site-builder-rev-9_258.png)

The *Drawing Tools* area on the right-hand side of the screen contains an assortment of shape and line
options to help you create a widget graphic by hand.

![Site Builder Application image 259](./images/starwatch-sms-user-guide-site-builder-rev-9_259.png)

![Site Builder Application image 260](./images/starwatch-sms-user-guide-site-builder-rev-9_260.png)

**Icon**
**Tool Name**
**Description**

![Site Builder Application image 261](./images/starwatch-sms-user-guide-site-builder-rev-9_261.png)

Arrow
Select entities on the drawing, such as lines and rectangles.
Freehand
Pan the graphic in the main widget management window.

![Site Builder Application image 262](./images/starwatch-sms-user-guide-site-builder-rev-9_262.png)

Line
Draw a line.

![Site Builder Application image 263](./images/starwatch-sms-user-guide-site-builder-rev-9_263.png)

Ellipse
Draw an ellipse.
Rounded Rectangle
Draw a rounded rectangle.
Line / Fill Color Picker
Pick the line and fill colors.
Rectangle
Draw a rectangle.
Polygon
Draw a polygon.

![Site Builder Application image 264](./images/starwatch-sms-user-guide-site-builder-rev-9_264.png)

Eye Dropper
Select the line and fill properties of an entity.

![Site Builder Application image 265](./images/starwatch-sms-user-guide-site-builder-rev-9_265.png)

Annotation
Add annotations to the widget.
Static Widget
Select a widget from a drop-down list of existing status

![Site Builder Application image 266](./images/starwatch-sms-user-guide-site-builder-rev-9_266.png)

widgets and place it into a graphic.

![Site Builder Application image 267](./images/starwatch-sms-user-guide-site-builder-rev-9_267.png)

The toolbar at the top of the screen is also helpful when laying out and adjusting your widget drawing.

![Site Builder Application image 268](./images/starwatch-sms-user-guide-site-builder-rev-9_268.png)

**Group**
**Group Icons**
**Description**

![Site Builder Application image 269](./images/starwatch-sms-user-guide-site-builder-rev-9_269.png)

Clipboard
These are tasks typically completed with the
Microsoft Windows clipboard.

Cut

Copy

Paste

Undo

Redo
Navigate
Navigate in the widget manager window. Zoom in/out.

![Site Builder Application image 270](./images/starwatch-sms-user-guide-site-builder-rev-9_270.png)

Pan around in four directions. Show/hide grid,
annotations, ioComp controls, and default display area
on graphic.
Align
Align entities based on left, right, top, bottom edge.

![Site Builder Application image 271](./images/starwatch-sms-user-guide-site-builder-rev-9_271.png)

Make entities the same size, width, or height.
Z-order
Bring overlapping entities to the front or back of the

![Site Builder Application image 272](./images/starwatch-sms-user-guide-site-builder-rev-9_272.png)

layout.
Properties
Set the width, color, and fill type of a line or entity.

![Site Builder Application image 273](./images/starwatch-sms-user-guide-site-builder-rev-9_273.png)

Annotation
Add text annotations to the widget.
Extent
Extend the widget size up, down, left, or right.

![Site Builder Application image 274](./images/starwatch-sms-user-guide-site-builder-rev-9_274.png)

Undo
Undo any changes recently made.

![Site Builder Application image 275](./images/starwatch-sms-user-guide-site-builder-rev-9_275.png)

![Site Builder Application image 276](./images/starwatch-sms-user-guide-site-builder-rev-9_276.png)

Note: while creating your widget graphic, if you need to undo any recent changes, simply click the
icon from the top menu.

![Site Builder Application image 277](./images/starwatch-sms-user-guide-site-builder-rev-9_277.png)

Note: the red flag
symbol next to the widget in the *Navigator* pane indicates that there are
unsaved changes. When you are done creating the new widget, return to the main *Site Builder* screen
and hit the *Update* button to update the system and database. Once the new widget has been saved
and updated, it will be available for placement on your *Site Map* (please see section **4.4 ADDING**
**POINTS/WIDGETS TO A MAP** for more information).

![Site Builder Application image 278](./images/starwatch-sms-user-guide-site-builder-rev-9_278.png)

## 4.7.2 CREATING A DYNAMIC WIDGET

When the provided widget library does not contain an applicable option, you can create your own
widget that matches the needs of your site. A dynamic widget has several layers to indicate its state
changes, such as when alarms occur.
To begin creating a dynamic widget, click the blue *Widget Library* tile on the main *Site Builder* screen.

![Site Builder Application image 279](./images/starwatch-sms-user-guide-site-builder-rev-9_279.png)

![Site Builder Application image 280](./images/starwatch-sms-user-guide-site-builder-rev-9_280.png)

![Site Builder Application image 281](./images/starwatch-sms-user-guide-site-builder-rev-9_281.png)

![Site Builder Application image 282](./images/starwatch-sms-user-guide-site-builder-rev-9_282.png)

In the *Widget Library* window, click the *Create Widget* icon
located at the top of the *Navigator*
pane. Note: before clicking the *Create Widget* icon, make sure you highlight the folder you would like
the new widget to reside in on the *Navigator* tree list.

![Site Builder Application image 283](./images/starwatch-sms-user-guide-site-builder-rev-9_283.png)

![Site Builder Application image 284](./images/starwatch-sms-user-guide-site-builder-rev-9_284.png)

![Site Builder Application image 285](./images/starwatch-sms-user-guide-site-builder-rev-9_285.png)

In the *Widget Properties* pop-up window, type a name for the new widget in the *Name* field. From the
*Data Class* drop-down list, select the correct data class for the widget.

![Site Builder Application image 286](./images/starwatch-sms-user-guide-site-builder-rev-9_286.png)

![Site Builder Application image 287](./images/starwatch-sms-user-guide-site-builder-rev-9_287.png)

Once you have selected a data class, click the *Ok* button. This will launch the configuration window for
the new widget.

![Site Builder Application image 288](./images/starwatch-sms-user-guide-site-builder-rev-9_288.png)

![Site Builder Application image 289](./images/starwatch-sms-user-guide-site-builder-rev-9_289.png)

From the *Category* drop-down list located in the top-center of the work area, select the correct
category for the new widget.

![Site Builder Application image 290](./images/starwatch-sms-user-guide-site-builder-rev-9_290.png)

The categories are described below:
**Category**
**Description**
Access Control System
ACS
Building Management System
BLDG
System Defined Category 1
CAT1
System Defined Category 2
CAT2
System Defined Category 3
CAT3
System Defined Category 4
CAT4
Emergency Response and Mobilization System
EMER
Fire Detection and Response System
FIRE
Intrusion Detection System
IDS
Network Administration and Security System
NETW
SCADA Utility Command and Control System
SCAD
Secure Compartment Information Facility
SCIF
Surveillance and Tracking System
SURV
System Health and Diagnostics
SYS
TERR Activity Monitoring System
TERR
Meteorological and Geological System
WTHR
Next, in the *States and Commands* section of the widget configuration window, modify the values for
the states if necessary. Note: the *States* checkbox needs to be selected to change these settings.

![Site Builder Application image 291](./images/starwatch-sms-user-guide-site-builder-rev-9_291.png)

![Site Builder Application image 292](./images/starwatch-sms-user-guide-site-builder-rev-9_292.png)

The state fields are described below.
**Field**
**Description**
Value
A read-only name of the state which is assigned by the application.
Phrase
The user-assigned name of the state.
Can Clear Alarm
Alarms can be cleared in the current state.
Alarm Type
Sets the alarm type from the drop-down list.
Alarm Severity
Sets the alarm severity from the drop-down list.
Update Alarm
Sets the system to record any new activity within an alarm until the alarm is
acknowledged and cleared.

![Site Builder Application image 293](./images/starwatch-sms-user-guide-site-builder-rev-9_293.png)

The background and text color of the *Phrase* values can be changed to indicate the state of the widget.
To change the text color, click within the *Fore Color* field in the *Visual Style* section to the right of the
work area and select the desired color. To change the background color, click within the *Background*
*Color* field and select the desired color.

![Site Builder Application image 294](./images/starwatch-sms-user-guide-site-builder-rev-9_294.png)

![Site Builder Application image 295](./images/starwatch-sms-user-guide-site-builder-rev-9_295.png)

![Site Builder Application image 296](./images/starwatch-sms-user-guide-site-builder-rev-9_296.png)

Next, in the *States and Commands* section of the widget configuration window, modify the commands
associated with the widget. Note: the *Commands* checkbox needs to be selected to change these
settings.

![Site Builder Application image 297](./images/starwatch-sms-user-guide-site-builder-rev-9_297.png)

The available commands for the previously selected data class are listed.

![Site Builder Application image 298](./images/starwatch-sms-user-guide-site-builder-rev-9_298.png)

![Site Builder Application image 299](./images/starwatch-sms-user-guide-site-builder-rev-9_299.png)

The command fields are outlined below.
**Field**
**Description**
Command Name
A read-only name of the command which is assigned by the application.
Value
The user-assigned name of the command. This will show up in the StarWatch
SMS Operator command screen.
Default Command
Sets this command as the default command for the widget.
Select Control
Makes the control a two-step process.
Password
Designates that a password is required for this command.
Partner
Makes the control require the two-person rule.
Once you have completed the settings in the *States and Commands* section, you can draw shapes to
associate with each widget state.

![Site Builder Application image 300](./images/starwatch-sms-user-guide-site-builder-rev-9_300.png)

In the bottom left of the main work area, click on the *Shapes*
tab. In the *Tools* window on
the right-hand side of the screen, there is a list of all state layers associated with the current widget.

![Site Builder Application image 301](./images/starwatch-sms-user-guide-site-builder-rev-9_301.png)

Select a state layer to draw by clicking on the checkbox next to the name of the layer. The *Drawing*
*Tools* area located above the layer list contains an assortment of shape and line options to help you
create a widget graphic by hand. Utilize these tools to draw the desired shape for the currently
selected layer (please see section **4.7.1 CREATING A STATIC WIDGET** for a description of the various
drawing and formatting tools provided).

![Site Builder Application image 302](./images/starwatch-sms-user-guide-site-builder-rev-9_302.png)

Note: to draw each state separately, make sure you check only one state layer at a time. However, if
two or more states will have the same graphic look, you can select multiple layers and draw them
simultaneously.

![Site Builder Application image 303](./images/starwatch-sms-user-guide-site-builder-rev-9_303.png)

Note: the red flag
symbol next to the widget in the *Navigator* pane indicates that there are
unsaved changes. When you are done creating the new widget, return to the main *Site Builder* screen
and hit the *Update* button to update the system and database. Once the new widget has been saved
and updated, it will be available for placement on your *Site Map* (please see section **4.4 ADDING**
**POINTS/WIDGETS TO A MAP** for more information).

![Site Builder Application image 304](./images/starwatch-sms-user-guide-site-builder-rev-9_304.png)

## 4.7.3 IMPORTING CUSTOMIZED WIDGETS INTO THE WIDGET LIBRARY

If you have configured multiple sites and would like to utilize a previously created custom widget
library, you can import the library to your local site. To import a library, click the blue *Widget Library*
tile on the main *Site Builder* screen.

![Site Builder Application image 305](./images/starwatch-sms-user-guide-site-builder-rev-9_305.png)

![Site Builder Application image 306](./images/starwatch-sms-user-guide-site-builder-rev-9_306.png)

![Site Builder Application image 307](./images/starwatch-sms-user-guide-site-builder-rev-9_307.png)

Next, click on the *Add Widget from Library*
icon at the top of the *Navigator* pane.

![Site Builder Application image 308](./images/starwatch-sms-user-guide-site-builder-rev-9_308.png)

In the *Open* window displayed, navigate to the location of the desired widget library. Typically, the file
is transferred using a removable storage device, such as a USB flash drive, but the file can also be on
your local computer. From the widget library directory, select the widgets that you would like to add
to your local site library and click the *Open* button. Note: each selected widget will be added under
the data class it was originally created in.

![Site Builder Application image 309](./images/starwatch-sms-user-guide-site-builder-rev-9_309.png)

If you are importing a widget that already exists, you will get a pop-up message.

![Site Builder Application image 310](./images/starwatch-sms-user-guide-site-builder-rev-9_310.png)

![Site Builder Application image 311](./images/starwatch-sms-user-guide-site-builder-rev-9_311.png)

You will be given the option of either replacing or keeping the widget currently in your library.
Once the import is complete, the selected widgets will be available in the *Navigator* folder tree and
ready to use in the system.

![Site Builder Application image 312](./images/starwatch-sms-user-guide-site-builder-rev-9_312.png)

Click the “Update”
icon from the “site Builder” screen to update it to your system. You can
now use it in your maps or to assign to point in “Points” from the site builder.
When you are done importing widgets, return to the main *Site Builder* screen and hit the *Update*
button to update the system and database. Once the new widget has been saved and updated, it will
be available for placement on your *Site Map* or to assign to points (please see sections **4.4 ADDING**
**POINTS/WIDGETS TO A MAP** and **3.0 VIEWING AND EDITING POINTS** for more information).

![Site Builder Application image 313](./images/starwatch-sms-user-guide-site-builder-rev-9_313.png)

## 4.7.4 GROUPING WIDGETS BY CLASS

To speed the process of searching for widgets in a larger library, the system offers a *Group by Data*
option, which will organize widgets according to their data class.

![Site Builder Application image 314](./images/starwatch-sms-user-guide-site-builder-rev-9_314.png)

Simply click the *Group by Data* checkbox at the top of the *Navigator* pane, and the widget library will
be displayed beneath each main category according to their data class.

![Site Builder Application image 315](./images/starwatch-sms-user-guide-site-builder-rev-9_315.png)

In the example below, the *Access Control* related widgets are now shown sorted according to each data
class, such as *ACCESSPORTAL*, *ALARMPOINT*, etc.

![Site Builder Application image 316](./images/starwatch-sms-user-guide-site-builder-rev-9_316.png)

![Site Builder Application image 317](./images/starwatch-sms-user-guide-site-builder-rev-9_317.png)

![Site Builder Application image 318](./images/starwatch-sms-user-guide-site-builder-rev-9_318.png)

## 5.0 CONFIGURING ALARM AND EVENT PRESENTATION

The *Presentation* function is used to configure the behavior of objects and points in the system that are
not related to widgets (please see section **4.7 CREATING WIDGETS** for more details on how widgets are
utilized within the system). For example, events related to the status of a zone or access control
events that are not associated with a door being put into a specific condition.
To open the initial *Presentation* screen, click the orange *Presentation* tile on the main *Site Builder*
screen.

![Site Builder Application image 319](./images/starwatch-sms-user-guide-site-builder-rev-9_319.png)

![Site Builder Application image 320](./images/starwatch-sms-user-guide-site-builder-rev-9_320.png)

![Site Builder Application image 321](./images/starwatch-sms-user-guide-site-builder-rev-9_321.png)

The *Presentation* tool allows you to view and modify:

Categories

Alarm Severities

Resolution Codes

Access Events

Zone Events

Zone Status

![Site Builder Application image 322](./images/starwatch-sms-user-guide-site-builder-rev-9_322.png)

Most panel screens can be filtered by the standard grid controls used within *StarWatch SMS*. For
example, to group the *Categories* section by the *Short Name* column, click on the *Short Name* header
and drag it to the *Drag a column header here to group by that column* field.

![Site Builder Application image 323](./images/starwatch-sms-user-guide-site-builder-rev-9_323.png)

Once the mouse button is released, the section will be sorted by the *Short Name* column.

![Site Builder Application image 324](./images/starwatch-sms-user-guide-site-builder-rev-9_324.png)

![Site Builder Application image 325](./images/starwatch-sms-user-guide-site-builder-rev-9_325.png)

The small arrows next to each row name indicate that more information is available. You can access
this information by clicking on a row arrow to expand the displayed details.

![Site Builder Application image 326](./images/starwatch-sms-user-guide-site-builder-rev-9_326.png)

![Site Builder Application image 327](./images/starwatch-sms-user-guide-site-builder-rev-9_327.png)

Note: You can always delete or undo changes by hitting the
icon located on the top right side
of the screen.

![Site Builder Application image 328](./images/starwatch-sms-user-guide-site-builder-rev-9_328.png)

To save *Presentation* changes to the database, click the
icon on the main *Site Builder*
screen.

![Site Builder Application image 329](./images/starwatch-sms-user-guide-site-builder-rev-9_329.png)

## 5.1 SETTING CATEGORIES

To view the *Categories* function, click the *Categories* button at the top of the *Presentation* screen.

![Site Builder Application image 330](./images/starwatch-sms-user-guide-site-builder-rev-9_330.png)

*Categories* are a layer of grouping that is reflected in specific areas of the *Operator Console* when
viewing information in an alarm or object list, providing a level of convenience.

![Site Builder Application image 331](./images/starwatch-sms-user-guide-site-builder-rev-9_331.png)

![Site Builder Application image 332](./images/starwatch-sms-user-guide-site-builder-rev-9_332.png)

**Category**
**Description**
HIDE
Unused or not required
IDS
Intrusion Detection System
FIRE
Fire Detection and Response System
ACS
Access Control System
BLDG
Building Management System
NETW
Network Administration and Security System
SURV
Surveillance and Tracking System
SCAD
SCADA Utility Command and Control System
TERR
TERR Activity Monitoring System
WTHR
Meteorological and Geological System
EMER
Emergency Response and Mobilization System
SYS
System Health and Diagnostics
CAT1
System Defined Category 1
CAT2
System Defined Category 2
CAT3
System Defined Category 3
CAT4
System Defined Category 4
SCIF
Secure Compartment Information Facility

![Site Builder Application image 333](./images/starwatch-sms-user-guide-site-builder-rev-9_333.png)

![Site Builder Application image 334](./images/starwatch-sms-user-guide-site-builder-rev-9_334.png)

To edit category fields, click the
icon in the top center of the screen. From the
*Category* page, you are only able to change the *Alarm Group* number. To accomplish this, highlight the
row that contains the alarm group number you would like to edit and enter a new value in the field.

![Site Builder Application image 335](./images/starwatch-sms-user-guide-site-builder-rev-9_335.png)

![Site Builder Application image 336](./images/starwatch-sms-user-guide-site-builder-rev-9_336.png)

## 5.2 SETTING ALARM SEVERITY

To view the *Alarm Severities* function, click the *Alarm Severities* button at the top of the *Presentation*
screen.

![Site Builder Application image 337](./images/starwatch-sms-user-guide-site-builder-rev-9_337.png)

*Alarm Severities* allow the user to identify and modify alarms based on their level of severity.
Reflecting these settings, alarms will appear in specific areas of the *Operator Console* when viewing
alarm lists. Alarm severities are assigned to each widget in the system. The severity of an alarm
determines where it appears in the alarm list. By default, the unacknowledged alarm with the highest
level of severity will appear at the top of the list.

![Site Builder Application image 338](./images/starwatch-sms-user-guide-site-builder-rev-9_338.png)

![Site Builder Application image 339](./images/starwatch-sms-user-guide-site-builder-rev-9_339.png)

![Site Builder Application image 340](./images/starwatch-sms-user-guide-site-builder-rev-9_340.png)

For each *Alarm Severity*, there are several parameters that set how alarms of that severity need to be
handled in the system:

*Ack Required*
If the selected alarm requires an acknowledgment by the operator

*Comment Required*
If a comment must be entered when an alarm occurs – a comment area will be available on the
operator acknowledge screen when the alarm is selected

*Resolution Code Needed*
If a resolution code must be entered when an alarm occurs - a field for the resolution code will
appear in the operator acknowledge screen when the alarm is selected

*Manage Required*
These options can be selected by clicking the corresponding checkbox in the alarm severity row. Any
selected parameters will become available in the *Operator Console* when viewing and processing
alarms.

![Site Builder Application image 341](./images/starwatch-sms-user-guide-site-builder-rev-9_341.png)

In the example below, we selected the *Major* type of *Alarm Severity*, and selected the *Ack Required*,
*Comment Required*, *Resolution Code Needed*, and *Manage Required* options.

![Site Builder Application image 342](./images/starwatch-sms-user-guide-site-builder-rev-9_342.png)

When an alarm of the *Major* severity level is processed by a system operator, these parameters will be
available, as shown on the operator screen below.

![Site Builder Application image 343](./images/starwatch-sms-user-guide-site-builder-rev-9_343.png)

![Site Builder Application image 344](./images/starwatch-sms-user-guide-site-builder-rev-9_344.png)

![Site Builder Application image 345](./images/starwatch-sms-user-guide-site-builder-rev-9_345.png)

Due to the selections made using the *Alarm Severity* function, the *Alarm List* at the bottom of the
operator screen now includes menu icons for *Manage* and *Acknowledge*. When a *Major* alarm is clicked,
a *Manage Alarm* pop-up screen will appear with *Comment* and *Resolution Code* fields.

![Site Builder Application image 346](./images/starwatch-sms-user-guide-site-builder-rev-9_346.png)

After these fields are completed, the alarm can be cleared.

![Site Builder Application image 347](./images/starwatch-sms-user-guide-site-builder-rev-9_347.png)

![Site Builder Application image 348](./images/starwatch-sms-user-guide-site-builder-rev-9_348.png)

The *Alarm Severity* screen also allows you to set or modify the *Alarm Event Style* for one or all alarm
events that are not associated with widgets, for example an *Unregistered ID* alarm event.

![Site Builder Application image 349](./images/starwatch-sms-user-guide-site-builder-rev-9_349.png)

You can modify the visual presentation of the alarm using the drop-down menu provided in the *Alarm*
*Event Style* column to the right of the screen.

![Site Builder Application image 350](./images/starwatch-sms-user-guide-site-builder-rev-9_350.png)

![Site Builder Application image 351](./images/starwatch-sms-user-guide-site-builder-rev-9_351.png)

## 5.3 SETTING RESOLUTION CODES

To view the *Resolution Codes* function, click the *Resolution Codes* button at the top of the
*Presentation* screen.

![Site Builder Application image 352](./images/starwatch-sms-user-guide-site-builder-rev-9_352.png)

The *Resolution Codes* screen displays a set of alarm types that describe the reasoning and cause behind
each alarm occurrence. This function is part of the process to resolve and clear alarms from the
*Operator Console*.

![Site Builder Application image 353](./images/starwatch-sms-user-guide-site-builder-rev-9_353.png)

![Site Builder Application image 354](./images/starwatch-sms-user-guide-site-builder-rev-9_354.png)

![Site Builder Application image 355](./images/starwatch-sms-user-guide-site-builder-rev-9_355.png)

To edit *Resolution Codes*, click the
icon in the top center of the screen. You are only
able to change the *Name* and *Value Name L2* fields. To accomplish this, highlight the row that contains
the property you would like to edit and enter a new name in the field.

![Site Builder Application image 356](./images/starwatch-sms-user-guide-site-builder-rev-9_356.png)

![Site Builder Application image 357](./images/starwatch-sms-user-guide-site-builder-rev-9_357.png)

## 5.4 SETTING ACCESS EVENTS

To view the *Access Events* function, click the *Access Events* button at the top of the *Presentation*
screen.

![Site Builder Application image 358](./images/starwatch-sms-user-guide-site-builder-rev-9_358.png)

The *Access Events* screen allows you to view and edit all the access related events in the system and
assign alarm severities to each.
Note: these *Access Events* are additional events and are not assigned from a widget.
The screen provides default parameters based on the *Access Events* commonly used by access control
users. Once an event has an alarm severity assigned to it, it will inherit all the rules and settings that
have been set, modified, and assigned from the *Alarm Severity* screen.

![Site Builder Application image 359](./images/starwatch-sms-user-guide-site-builder-rev-9_359.png)

![Site Builder Application image 360](./images/starwatch-sms-user-guide-site-builder-rev-9_360.png)

![Site Builder Application image 361](./images/starwatch-sms-user-guide-site-builder-rev-9_361.png)

To edit *Access Events*, click the
icon in the top center of the screen. Next, highlight
the row that contains the property you would like to edit and enter a modification in the desired field.

![Site Builder Application image 362](./images/starwatch-sms-user-guide-site-builder-rev-9_362.png)

![Site Builder Application image 363](./images/starwatch-sms-user-guide-site-builder-rev-9_363.png)

If *New Incident* is selected for any of the *Access Events* in this screen, a new incident will be created
upon an alarm with this action code. The incident will contain details about this access action and will
be reported as an alarm event in the *Operator Console*.
If *Person Trace* is selected for any of the *Access Events* in this screen (for example *Access* *Denied* or
*Unauthorized*), the operator will be able to trace the associated cardholder using the *CardWatch*
feature of the *Operator Console*.

![Site Builder Application image 364](./images/starwatch-sms-user-guide-site-builder-rev-9_364.png)

![Site Builder Application image 365](./images/starwatch-sms-user-guide-site-builder-rev-9_365.png)

## 5.5 SETTING ZONE EVENTS

To view the *Zone Events* function, click the *Zone Events* button at the top of the *Presentation* screen.

![Site Builder Application image 366](./images/starwatch-sms-user-guide-site-builder-rev-9_366.png)

The *Zone Events* screen allows you to view and modify all the events that can be associated with the
zone. These events have an alarm severity assigned to each of them by default. You can modify the
severity, if necessary.

![Site Builder Application image 367](./images/starwatch-sms-user-guide-site-builder-rev-9_367.png)

![Site Builder Application image 368](./images/starwatch-sms-user-guide-site-builder-rev-9_368.png)

![Site Builder Application image 369](./images/starwatch-sms-user-guide-site-builder-rev-9_369.png)

To edit *Zone Events*, click the
icon in the top center of the screen. Next, highlight the
row that contains the property you would like to edit and enter a modification in the desired field.

![Site Builder Application image 370](./images/starwatch-sms-user-guide-site-builder-rev-9_370.png)

![Site Builder Application image 371](./images/starwatch-sms-user-guide-site-builder-rev-9_371.png)

To assign a different level of alarm severity, choose the desired severity from the drop down menu.

![Site Builder Application image 372](./images/starwatch-sms-user-guide-site-builder-rev-9_372.png)

Note: *Zone Events* will inherit the rules that were previously assigned to them on the *Alarm Severities*
screen.

![Site Builder Application image 373](./images/starwatch-sms-user-guide-site-builder-rev-9_373.png)

## 5.6 SETTING ZONE STATUS

To view the *Zone Status* function, click the *Zone Status* button at the top of the *Presentation* screen.

![Site Builder Application image 374](./images/starwatch-sms-user-guide-site-builder-rev-9_374.png)

The *Zone Status* screen allows you to view the mode, status, and supervision of the zone.

![Site Builder Application image 375](./images/starwatch-sms-user-guide-site-builder-rev-9_375.png)

You will be able to modify the font (color, style) and the background color.

![Site Builder Application image 376](./images/starwatch-sms-user-guide-site-builder-rev-9_376.png)

![Site Builder Application image 377](./images/starwatch-sms-user-guide-site-builder-rev-9_377.png)

To edit the visual settings of the *Zone Status*, click the
icon in the top center of the
screen. Next, modify these parameters using the drop-down menu provided for each.
In the example below, the font and background color for the *Time Exceeded* property is modified.

![Site Builder Application image 378](./images/starwatch-sms-user-guide-site-builder-rev-9_378.png)

![Site Builder Application image 379](./images/starwatch-sms-user-guide-site-builder-rev-9_379.png)

---

*© DAQ Electronics, LLC*
