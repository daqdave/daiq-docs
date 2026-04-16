---
layout: default
title: Operator Console
nav_order: 580
---

# Operator Console

![Operator Console image 01](./images/starwatch-sms-user-guide-operator-console-rev-6_01.png)

## 1.0 INTRODUCTION

Welcome to *StarWatch SMS*, the premier security management system. This document will lead you
through basic operations, including enrolling on-site personnel and visitors into the system database,
processing alarms, using area maps to track the status of peripheral devices, and creating detailed
reports of system events.

## Roles and Rights

Depending on the roles and rights you have been assigned within the *StarWatch SMS* database, you may
not be able to perform all the processes described in this guide. For example, system operators may
only have rights to enroll personnel and process alarms, while system administrators may be granted
full editing and configuration rights. For information on the specific operations you are permitted to
perform, please see your system administrator.

## Customization

To optimize the efficiency of each security system, *StarWatch SMS* allows users to customize the
various screens and functions available within the software package. Due to this high degree of
flexibility, some of the instructions and screen captures presented in this guide may differ somewhat
from what appears on your screen as you go through the various security management processes. An
attempt has been made to offer the most generic views possible to help avoid confusion.
Note: when dealing with very large databases, it may take the system a moment to refresh after you
have issued a command or clicked on a function button, depending on your system speed. It is not
necessary to click functions multiple times. In fact, doing so may cause the workspace to become
disorganized, as the same window or tab may be unintentionally opened multiple times.

![Operator Console image 02](./images/starwatch-sms-user-guide-operator-console-rev-6_02.png)

## 1.1 LOGGING INTO THE OPERATOR APPLICATION

Before starting a *StarWatch SMS* operating session, it is necessary to log into the system. For the initial
login to the application, you must login on the StarWatch SMS Server computer. Note: if you do not
want to use the default username and password combination, create a personal login for the System
Administrator and use that login for subsequent logins from workstations.
Note: once you have logged in, many of the actions you take during your session will be recorded in the
database with a signifier linking each event with your specific user name. Recorded actions include
alarm processing steps, user enrollment procedures, and other system events.

![Operator Console image 03](./images/starwatch-sms-user-guide-operator-console-rev-6_03.png)

If the *Operator* interface has not already been launched, double-click on the *StarWatch*
icon on
your Windows desktop. If you did not create this shortcut during the installation process, click the
*Start* menu, select the *All Programs* option, and open the *DAQ Electronics* folder.

![Operator Console image 04](./images/starwatch-sms-user-guide-operator-console-rev-6_04.png)

From the list of all installed *DAQ Electronics* applications, select the StarWatch option.

![Operator Console image 05](./images/starwatch-sms-user-guide-operator-console-rev-6_05.png)

After a short loading sequence, the *StarWatch SMS* login screen will appear.

![Operator Console image 06](./images/starwatch-sms-user-guide-operator-console-rev-6_06.png)

![Operator Console image 07](./images/starwatch-sms-user-guide-operator-console-rev-6_07.png)

![Operator Console image 08](./images/starwatch-sms-user-guide-operator-console-rev-6_08.png)

Next, to expand the viewable parameters, click the
button.

![Operator Console image 09](./images/starwatch-sms-user-guide-operator-console-rev-6_09.png)

Additional login details will appear in the window.

![Operator Console image 10](./images/starwatch-sms-user-guide-operator-console-rev-6_10.png)

If Windows authentication is required within your network or you are using Common Access Cards
(CAC), click the *Authentication* drop-down list and select the *Windows Authentication* option.
Otherwise, select the *SMS Server Authentication* option.
In the *User Name* and *Password* fields, type in the login information you created or use the default
login and passwords.
**Field**
**Default**
User Name
admin
Password
admin
Note: see your System Administrator if you do not know your login details.
Note: the *Windows Authentication* option is for Active Directory based setup, while *SMS Server*
*Authentication* applies to logins set by the operator (reference users).
Note: the *Quick Login* option loads no workspace (reference workspaces).

![Operator Console image 11](./images/starwatch-sms-user-guide-operator-console-rev-6_11.png)

After entering your user details, click the
button or press the *Enter* key on your
keyboard. A loading message will appear on the screen, followed by the main *StarWatch SMS* operator
interface.

![Operator Console image 12](./images/starwatch-sms-user-guide-operator-console-rev-6_12.png)

Note: the loading sequence may take several seconds, depending on system speed.

![Operator Console image 13](./images/starwatch-sms-user-guide-operator-console-rev-6_13.png)

![Operator Console image 14](./images/starwatch-sms-user-guide-operator-console-rev-6_14.png)

## 1.2 GENERAL FUNCTIONALITY

The main *StarWatch SMS* screen has been designed to allow operators to easily locate and utilize all
the functions and views available in the system. The system also enables you to customize the screen
layout to match your preferences. Before setting up your specific security configuration, it is
recommended that you familiarize yourself with the various on-screen features and options, as many of
these features will be used in multiple areas of system operation.

## 1.2.1 MAIN RIBBON TAB

Like many new software packages and web browsers, *StarWatch SMS* uses tabs to organize on-screen
content. The goal of this configuration scheme is to provide the user with quick access to required
information and to enable the system to display multiple security aspects simultaneously.

![Operator Console image 15](./images/starwatch-sms-user-guide-operator-console-rev-6_15.png)

## Applications

Appearing in the main workspace, functions display the core content used to configure and operate
*StarWatch SMS*. Functions can be opened by clicking on icons in the *Main Ribbon* toolbar at the top of
the screen. As multiple applications are opened, they will appear as a row of tabs.

![Operator Console image 16](./images/starwatch-sms-user-guide-operator-console-rev-6_16.png)

In the example below, three functions (tabs) have been opened in the main workspace. While all of
these functions remain active, only one can be displayed at the top of the workspace. In this case, the
*Admin* tab is positioned in front of the other open tabs.

![Operator Console image 17](./images/starwatch-sms-user-guide-operator-console-rev-6_17.png)

To bring a function to the top of the workspace, simply click on the associated tab.

![Operator Console image 18](./images/starwatch-sms-user-guide-operator-console-rev-6_18.png)

The order of active functions can be changed by clicking on a tab and dragging it horizontally to the
left or right and dropping it in a new location in the row. Functions can also be detached and moved to
new areas of the workspace using the docking feature (see section 1.2.2 DOCKING).

![Operator Console image 19](./images/starwatch-sms-user-guide-operator-console-rev-6_19.png)

Note: functions will remain open until you click on the *Close*
symbol on the appropriate tab.

![Operator Console image 20](./images/starwatch-sms-user-guide-operator-console-rev-6_20.png)

## Sub Tabs

Appearing at the bottom of functions, sub tabs allow users to access multiple levels of content within
the same function. In the example shown below, there are several sub tabs available at the bottom of
the *Persons* function.

![Operator Console image 21](./images/starwatch-sms-user-guide-operator-console-rev-6_21.png)

To bring the content displayed within a sub tab to the top of the workspace, simply click on the
associated tab.

![Operator Console image 22](./images/starwatch-sms-user-guide-operator-console-rev-6_22.png)

Unlike functions, which can be re-positioned within the workspace, sub tabs are permanently
positioned within their associated function and cannot be dragged to new locations.
Note: depending on the selections you make as you move through various system processes, additional
sub tabs may become available within a function.

![Operator Console image 23](./images/starwatch-sms-user-guide-operator-console-rev-6_23.png)

## Edge Pop-out Tabs

Edge tabs provide access to several critical functions within *StarWatch SMS* and are permanently fixed
to the outer edge of the main workspace. An example is the *Card Watch* tab that appears along the
right-hand edge of the workspace near the top of the screen.

![Operator Console image 24](./images/starwatch-sms-user-guide-operator-console-rev-6_24.png)

![Operator Console image 25](./images/starwatch-sms-user-guide-operator-console-rev-6_25.png)

Another example is *Site* pop-out that appears on the left-hand edge of the workspace near the top of
the screen.

![Operator Console image 26](./images/starwatch-sms-user-guide-operator-console-rev-6_26.png)

To access the system information contained within an edge tab, simply roll your mouse over (hover
over) the tab or click on it directly. A related viewer will appear on the screen and remain until you
roll your mouse off the edge tab or viewer.
Viewers accessed using edge tabs can be affixed to the screen using the pinning function, which
disables the roll off feature.

![Operator Console image 27](./images/starwatch-sms-user-guide-operator-console-rev-6_27.png)

To keep a viewer on your screen, click the *Pin*
icon in the upper right-hand corner of the viewer
space. The viewer will now remain onscreen even when you move your mouse to other areas.

![Operator Console image 28](./images/starwatch-sms-user-guide-operator-console-rev-6_28.png)

![Operator Console image 29](./images/starwatch-sms-user-guide-operator-console-rev-6_29.png)

**NOTE:** once a viewer has been pinned, the sideways *Pin*
icon will change to an upright *Pin*
icon.
Clicking this upright *Pin* icon will return the viewer to the unpinned state.

![Operator Console image 30](./images/starwatch-sms-user-guide-operator-console-rev-6_30.png)

## Start Menu

The *Start* menu is located in the top left corner of the operator screen and includes several
applications that are less frequently used.

![Operator Console image 31](./images/starwatch-sms-user-guide-operator-console-rev-6_31.png)

Clicking on the *Start*
icon will display the available options.

![Operator Console image 32](./images/starwatch-sms-user-guide-operator-console-rev-6_32.png)

![Operator Console image 33](./images/starwatch-sms-user-guide-operator-console-rev-6_33.png)

![Operator Console image 34](./images/starwatch-sms-user-guide-operator-console-rev-6_34.png)

![Operator Console image 35](./images/starwatch-sms-user-guide-operator-console-rev-6_35.png)


New Frame
Usually utilized when a system has been configured for multiple monitors, the *New Frame*
button will launch a *StarWatch SMS* frame window, which can be dragged to the display
area on the monitor of your choice and maximized. The shaded space provided in the
window can now be used as an additional working area. You can drag detached folders
from the main monitor to linked monitors and drop them where desired. You can also re-
position the main *StarWatch SMS* interface on the monitor of your choice. Each monitor will
retain docking and resizing functionality separately, creating a highly flexible work area.

![Operator Console image 36](./images/starwatch-sms-user-guide-operator-console-rev-6_36.png)

![Operator Console image 37](./images/starwatch-sms-user-guide-operator-console-rev-6_37.png)


Save Preferences
The system allows you to save any changes you make to default system settings related to
the display or configuration of data within the *StarWatch SMS* user interface. For example,
the system allows you to alter the appearance of data grids by changing the column order
and to adjust the filtering settings used when displaying devices within a site map. Using
the *Save Preferences* button, these types of preferences can be saved as new default
settings.

![Operator Console image 38](./images/starwatch-sms-user-guide-operator-console-rev-6_38.png)


Save Workspace
Clicking the *Save Workspace* button will save any configuration changes you have made to
the visible user workspace. For example, you may have created a workspace that allows
you to simultaneously view a specific area map and associated alarms. Instead of
recreating this workspace each time you login, you can save the new layout as the new
default setting.

![Operator Console image 39](./images/starwatch-sms-user-guide-operator-console-rev-6_39.png)


Reset Workspace
Clicking the *Reset Workspace* button will discard any configuration changes you have made
to the visible user workspace and revert back to the original settings. Once you have saved
a workspace, this option will not be available.

![Operator Console image 40](./images/starwatch-sms-user-guide-operator-console-rev-6_40.png)


Manage Workspaces
Clicking the *Manage Workspace* button allows you to create new workspaces, delete
existing workspaces, and update and load workspaces that can be called to the screen
depending on the needs of the user.

![Operator Console image 41](./images/starwatch-sms-user-guide-operator-console-rev-6_41.png)


Confidential Fields
The *Confidential Fields* function is used when viewing personnel profiles that contain
confidential information. Only operators who have been assigned appropriate rights will be
able to view these protected user details.

![Operator Console image 42](./images/starwatch-sms-user-guide-operator-console-rev-6_42.png)

![Operator Console image 43](./images/starwatch-sms-user-guide-operator-console-rev-6_43.png)

Change Password

The *Change Password* function allows an operator to change their login password at any
time.

![Operator Console image 44](./images/starwatch-sms-user-guide-operator-console-rev-6_44.png)

Logout

The *Logout* button allows you to logout of the system without closing the *StarWatch SMS*
application. Clicking this button will return you to the main login page.

![Operator Console image 45](./images/starwatch-sms-user-guide-operator-console-rev-6_45.png)

Exit Operator Console

Clicking the *Exit Operator Console* button will shut down the *StarWatch SMS* system at the
current workstation. A warning will appear asking you to confirm that you want to close
the application.

![Operator Console image 46](./images/starwatch-sms-user-guide-operator-console-rev-6_46.png)

Appearing immediately to the right of the *Start*
icon at the top left of the screen, the
customizable *Quick Access* toolbar provides one-click access to the *Start* menu functions. The toolbar
can be modified to include those functions you use most often.

![Operator Console image 47](./images/starwatch-sms-user-guide-operator-console-rev-6_47.png)

![Operator Console image 48](./images/starwatch-sms-user-guide-operator-console-rev-6_48.png)

![Operator Console image 49](./images/starwatch-sms-user-guide-operator-console-rev-6_49.png)

Clicking the *Customize*
icon to the right of the *Quick Access* toolbar will call up a drop-down menu
allowing you to select the various functions for inclusion on the toolbar.

![Operator Console image 50](./images/starwatch-sms-user-guide-operator-console-rev-6_50.png)

![Operator Console image 51](./images/starwatch-sms-user-guide-operator-console-rev-6_51.png)

## 1.2.2 DOCKING

The *StarWatch SMS* docking feature allows system users to customize the look of their workspace by
moving functions to new areas on the screen.

## Detaching Functions

Using simple click and drag functionality, functions can be detached from the main workspace. In the
example shown below, two functions have been opened in the main *StarWatch SMS* workspace.

![Operator Console image 52](./images/starwatch-sms-user-guide-operator-console-rev-6_52.png)

To detach a function to its own separate window, you can simply click on the appropriate tab and drag
it away from the row of tabs at the top of the main workspace. The detached function will act as a
moveable on-screen floating window, appearing in front of all other page content.

![Operator Console image 53](./images/starwatch-sms-user-guide-operator-console-rev-6_53.png)

In the example shown below, the *Persons* application has been detached.

![Operator Console image 54](./images/starwatch-sms-user-guide-operator-console-rev-6_54.png)

![Operator Console image 55](./images/starwatch-sms-user-guide-operator-console-rev-6_55.png)

## Using the Docking Icon

When moving a detached function around the screen, a docking icon will appear in the middle of the
workspace.

![Operator Console image 56](./images/starwatch-sms-user-guide-operator-console-rev-6_56.png)

This icon enables you to place, or “dock”, the function into a new position, dividing the workspace
appropriately. When moving a function, dragging your cursor across one of the four directional

![Operator Console image 57](./images/starwatch-sms-user-guide-operator-console-rev-6_57.png)

![Operator Console image 58](./images/starwatch-sms-user-guide-operator-console-rev-6_58.png)

![Operator Console image 59](./images/starwatch-sms-user-guide-operator-console-rev-6_59.png)

![Operator Console image 60](./images/starwatch-sms-user-guide-operator-console-rev-6_60.png)

indicators on the docking icon (*Left*
, *Right*
, *Up*
, or *Down*
) will cause an area of the
screen to become shaded a transparent blue. This shaded area indicates where the function will be
positioned when you let go of the mouse button.

![Operator Console image 61](./images/starwatch-sms-user-guide-operator-console-rev-6_61.png)

![Operator Console image 62](./images/starwatch-sms-user-guide-operator-console-rev-6_62.png)

In the following example, the detached *Devices* function has been dragged across the *Left*
directional indicator on the docking icon. The left part of the main workspace is now shaded.

![Operator Console image 63](./images/starwatch-sms-user-guide-operator-console-rev-6_63.png)

![Operator Console image 64](./images/starwatch-sms-user-guide-operator-console-rev-6_64.png)

![Operator Console image 65](./images/starwatch-sms-user-guide-operator-console-rev-6_65.png)

Letting go of your mouse at this point would result in the following screen configuration, with the
*Devices* application now docked into position to the left of the *Site Maps* and *Persons* applications.

![Operator Console image 66](./images/starwatch-sms-user-guide-operator-console-rev-6_66.png)

In this manner, the screen can be divided into any number of configurations, depending on the needs of
the user.
Note: to return a detached function to its original position in the row of tabs at the top of the

![Operator Console image 67](./images/starwatch-sms-user-guide-operator-console-rev-6_67.png)

workspace, drag and drop the function on the central indicator
on the docking icon.

![Operator Console image 68](./images/starwatch-sms-user-guide-operator-console-rev-6_68.png)

## 1.2.3 RESIZING

To facilitate clean, easy to navigate workspace configurations, *StarWatch SMS* allows you to resize the
various windows, functions, and work areas that are open on your screen.
When you slowly move your mouse across the dividing line between two workspace sections, a *Resize*

![Operator Console image 69](./images/starwatch-sms-user-guide-operator-console-rev-6_69.png)

icon will appear. With this icon on-screen, you can click and drag dividing lines both vertically and
horizontally to optimize the use of the workspace. Along with adjusting dividing lines between separate
functions, the system also allows you to resize sections that simultaneously appear within a single
function.

![Operator Console image 70](./images/starwatch-sms-user-guide-operator-console-rev-6_70.png)

As with function dividers, you can adjust the position of section dividers using the *Resize*
icon.
Additionally, clicking once on a section divider will cause the divider to move to the far edge of the
screen in the direction indicated by the small black arrows on the divider, effectively covering over any
content in that direction. Clicking a second time will return the divider to the previous position. For
example, you may want to temporarily expand a section to enter specific details and then quickly
return to the prior configuration.

![Operator Console image 71](./images/starwatch-sms-user-guide-operator-console-rev-6_71.png)

## 1.2.4 USING MULTIPLE MONITORS

The docking and resizing aspects of *StarWatch SMS* become especially powerful when more than one
monitor is used to display system information. For example, if your system has been configured with a
dual monitor setup, the main monitor might be used for personnel functions and alarm processing,
while the second monitor is used to display video feed from connected security cameras.
If your system has been set up with a multiple monitor configuration, you can enter multi-screen mode

![Operator Console image 72](./images/starwatch-sms-user-guide-operator-console-rev-6_72.png)

by clicking on the *New Frame*
icon in the *Start* menu at the top left of the screen. This will
launch a *StarWatch SMS* frame window, which can be dragged to the display area on the monitor of
your choice and maximized.

![Operator Console image 73](./images/starwatch-sms-user-guide-operator-console-rev-6_73.png)

The shaded space provided in the window can now be used as an additional working area. You can drag
detached folders from the main monitor to linked monitors and drop them where desired. You can also
re-position the main *StarWatch SMS* interface on the monitor of your choice. Each monitor will retain
docking and resizing functionality separately, creating a highly flexible work area.

![Operator Console image 74](./images/starwatch-sms-user-guide-operator-console-rev-6_74.png)

To add/dock an application to the new frame, you can simply right-click on an active application tab
then select the *Dock to…* option from the pop-up menu and send it to the frame.

![Operator Console image 75](./images/starwatch-sms-user-guide-operator-console-rev-6_75.png)

In the example below, we are docking the *Site Map* application into the new frame we have created.

![Operator Console image 76](./images/starwatch-sms-user-guide-operator-console-rev-6_76.png)

![Operator Console image 77](./images/starwatch-sms-user-guide-operator-console-rev-6_77.png)

This allows us to have multiple applications opened in multiple views.

![Operator Console image 78](./images/starwatch-sms-user-guide-operator-console-rev-6_78.png)

Note: this new configuration can also be saved as a workspace. In this manner, users will not have to
re-create views each time they start a new operating session.
Note: a separate docking icon will be available for each display space.

![Operator Console image 79](./images/starwatch-sms-user-guide-operator-console-rev-6_79.png)

## 1.2.5 GRID CONTROLS

Within the *StarWatch SMS* operator system, many of the individual functions display data in
spreadsheet format. For example, the *Devices* function displays device data separated into several
categories, each represented by a column in the on-screen chart (*Flags*, *Time*, Device, *Name*, *Zone*,
etc.).

![Operator Console image 80](./images/starwatch-sms-user-guide-operator-console-rev-6_80.png)

To make locating information in large databases more convenient, a number of column formatting and
sorting features have been provided for all spreadsheets used in the system.
Note: some grid features may not be available for all spreadsheet sections.

![Operator Console image 81](./images/starwatch-sms-user-guide-operator-console-rev-6_81.png)

## Changing Column Order

You can arrange spreadsheet data to your preference by changing the order of columns. To move a
column, simply click on the header at the top of the column and drag it horizontally to a new location.
When you let go of your mouse button, the column will be dropped in the new location.
In the example below, the *Status* column has been dragged and dropped next to the *Device* and *Name*
tabs.

![Operator Console image 82](./images/starwatch-sms-user-guide-operator-console-rev-6_82.png)

Note: if you move your mouse too far vertically when moving a column, a large black *X* will appear over
your cursor. This warns you that if you drop the column in this location, it will be removed from the
spreadsheet entirely. If you unintentionally drop/remove a column, you can retrieve it using the
*Column Chooser* function described later in this section.

![Operator Console image 83](./images/starwatch-sms-user-guide-operator-console-rev-6_83.png)

## Resizing Columns

To display data more effectively, you can adjust the width of a column by positioning your cursor on
the line separating the header of the column you want to adjust from the header of the column
immediately to the right. When positioned correctly, the *Change Column Width*
symbol will

![Operator Console image 84](./images/starwatch-sms-user-guide-operator-console-rev-6_84.png)

appear. With the *Change Column Width* symbol showing, you can click and drag the edge of the column
horizontally to increase or decrease the width of the column.

## Sort Ascending/Descending

You can sort column data in ascending alphanumeric order by clicking once on the column header. The

![Operator Console image 85](./images/starwatch-sms-user-guide-operator-console-rev-6_85.png)

*Ascending*
symbol will appear in the header.

![Operator Console image 86](./images/starwatch-sms-user-guide-operator-console-rev-6_86.png)

![Operator Console image 87](./images/starwatch-sms-user-guide-operator-console-rev-6_87.png)

To sort in descending alphanumeric order, click on the header a second time. The *Descending*
symbol will appear in the header. The example below, we filtered the *Time* column to have the newest
entry on top.

![Operator Console image 88](./images/starwatch-sms-user-guide-operator-console-rev-6_88.png)

Note: clicking on a column header will sort all of the chart rows according to that parameter, either
using ascending or descending alphanumeric order. To sort by a different parameter, you can simply
click on another column header

![Operator Console image 89](./images/starwatch-sms-user-guide-operator-console-rev-6_89.png)

## Direct Category Selection

Some columns also allow you to directly filter by a certain data type. If a column offers this

![Operator Console image 90](./images/starwatch-sms-user-guide-operator-console-rev-6_90.png)

functionality, the *Filter*
symbol will appear when you click on the header. Clicking the symbol will
call up a drop-down list allowing you to select the data type you want to display in the column.
In the example below, the *Filter* symbol on the header of the *Widget* column has been clicked.

![Operator Console image 91](./images/starwatch-sms-user-guide-operator-console-rev-6_91.png)

Next, the *None* option is selected from the drop-down list.

![Operator Console image 92](./images/starwatch-sms-user-guide-operator-console-rev-6_92.png)

![Operator Console image 93](./images/starwatch-sms-user-guide-operator-console-rev-6_93.png)

The resulting chart has been filtered to show only those rows that contain the *None* designation in the
*Widget* column.

![Operator Console image 94](./images/starwatch-sms-user-guide-operator-console-rev-6_94.png)

Once you select a data type, all rows that include other data types will be removed from the chart. To

![Operator Console image 95](./images/starwatch-sms-user-guide-operator-console-rev-6_95.png)

retrieve these other data types, you can click on the *Filter*
symbol again and select the *All* option
or right-click on the column header and select *Clear Filter*.

![Operator Console image 96](./images/starwatch-sms-user-guide-operator-console-rev-6_96.png)

Note: you can resize a *Filter* drop-down list by rolling your mouse over the *Resize*
symbol in the
bottom right-hand corner of the list and clicking and dragging the corner.

![Operator Console image 97](./images/starwatch-sms-user-guide-operator-console-rev-6_97.png)

![Operator Console image 98](./images/starwatch-sms-user-guide-operator-console-rev-6_98.png)

![Operator Console image 99](./images/starwatch-sms-user-guide-operator-console-rev-6_99.png)

![Operator Console image 100](./images/starwatch-sms-user-guide-operator-console-rev-6_100.png)

## Column Sorting Menu

Additional column sorting features can be accessed by right-clicking on any column header or other
areas of a grid. The *Column Sorting* menu will appear.

![Operator Console image 101](./images/starwatch-sms-user-guide-operator-console-rev-6_101.png)

Note: depending on where you right-click on the screen, you may be presented with slightly different
menu options based upon the object you have clicked on and the current state of your grid. As an
example, the following screenshots show the variety of menu options that become available when
utilizing the grouping function to organize a grid.

![Operator Console image 102](./images/starwatch-sms-user-guide-operator-console-rev-6_102.png)

Right-clicking in a grid that has not been grouped by a column header results in the following menu
options:

![Operator Console image 103](./images/starwatch-sms-user-guide-operator-console-rev-6_103.png)

After a grid has been grouped by a column header, the following menu options are available:

![Operator Console image 104](./images/starwatch-sms-user-guide-operator-console-rev-6_104.png)

![Operator Console image 105](./images/starwatch-sms-user-guide-operator-console-rev-6_105.png)

Clicking on any space in the grouping area will provide the following menu options:

![Operator Console image 106](./images/starwatch-sms-user-guide-operator-console-rev-6_106.png)

This variation in the number and type of menu items available is typical as you sort and organize your
grids to your preferred layout.

![Operator Console image 107](./images/starwatch-sms-user-guide-operator-console-rev-6_107.png)

The following chart offers a brief description for each option in the *Column Sorting* menu and indicates
when each is available based on grouping status.

## Icon

## Name

## Grouped

## Ungrouped

## Grouping

## Description

## Column

## Column

## Area

![Operator Console image 108](./images/starwatch-sms-user-guide-operator-console-rev-6_108.png)

Full
●
●
Expand all data in the tree to show all
Expand
data rows for all points
Full
●
●
Collapse all data in the tree to hide all
Collapse
data rows for all points
Sort
●
●
Sort points in a column/group in an
Ascending
ascending order
Sort
●
●
Sort points in a column/group in a
Descending
descending order
Clear All
●
●
Clear all sorting that was done for
Sorting
selected groups/columns on a grid

![Operator Console image 109](./images/starwatch-sms-user-guide-operator-console-rev-6_109.png)

Group by
List data according to a single
this
column/parameter
Column
Ungroup
●
Ungroup a selected column or header

![Operator Console image 110](./images/starwatch-sms-user-guide-operator-console-rev-6_110.png)

Hide Group
●
●
●
Hide the grouping area

![Operator Console image 111](./images/starwatch-sms-user-guide-operator-console-rev-6_111.png)

by Box

![Operator Console image 112](./images/starwatch-sms-user-guide-operator-console-rev-6_112.png)

Show
●
Show the grouping area
Group by
Box
Hide This
●
●
Hide selected group and column from the
Column
grid – you can retrieve it using *Column*
*Chooser* to drag it back to the screen
Column
●
●
Allows you to directly select data columns

![Operator Console image 113](./images/starwatch-sms-user-guide-operator-console-rev-6_113.png)

Chooser
to appear in the spreadsheet - when you
select this option, the *Customization*
window will appear where you can drag
and drop columns into your grid – note:
when dragging a new column into the
chart, a large black “X” will appear over
your cursor when you are not positioned
over an appropriate drop location - if you
drop the column while the “X” is on-
screen, the column will remain in the
*Customization* window
Best
●
Resizes selected column for the best fit

![Operator Console image 114](./images/starwatch-sms-user-guide-operator-console-rev-6_114.png)

Fit
(width/size) on the screen
Best Fit (all
●
●
Fits data in all columns using the best
columns)
possible configuration

![Operator Console image 115](./images/starwatch-sms-user-guide-operator-console-rev-6_115.png)

Filter
●
●

![Operator Console image 116](./images/starwatch-sms-user-guide-operator-console-rev-6_116.png)

Calls up the *Filter Builder* window - by
Editor
clicking on the various sections of the
filter string and selecting appropriate
settings, you can build and apply
customized filters for the column. Once a
filter is applied, a filter editing row will
be added at the bottom of the data chart
enabling you to quickly adjust filter
settings, if needed.

![Operator Console image 117](./images/starwatch-sms-user-guide-operator-console-rev-6_117.png)

Clear
●
●
Removes any filtering that has been
Filter
applied to a column, returning it to the
original default settings - or you can hit
the X from the bottom of the data chart
to return to the default screen
Show Find
●
●
Launches a screen above the grouping
area where the user can enter/search the
Panel
data displayed in the system (useful for
large databases)

![Operator Console image 118](./images/starwatch-sms-user-guide-operator-console-rev-6_118.png)

Hide Find
●
●
Hides the *Find Panel* window from the
Panel
screen
Show Auto
●
●
Launches an auto filter row allowing you
Filter Row
to filter rows by entered words
Clear
●
Clears all grouping applied to the page

![Operator Console image 119](./images/starwatch-sms-user-guide-operator-console-rev-6_119.png)

Grouping
and to selected columns

![Operator Console image 120](./images/starwatch-sms-user-guide-operator-console-rev-6_120.png)

Further explanations for a number of these options are provided in the following sections.

Sort Ascending / Descending
You can sort column data in ascending alphanumeric order by selecting the *Sort Ascending*

![Operator Console image 121](./images/starwatch-sms-user-guide-operator-console-rev-6_121.png)

option from the menu. The *Ascending*
symbol will appear in the active header.

![Operator Console image 122](./images/starwatch-sms-user-guide-operator-console-rev-6_122.png)

To sort in descending alphanumeric order, select the *Sort Descending* option. The

![Operator Console image 123](./images/starwatch-sms-user-guide-operator-console-rev-6_123.png)

*Descending*
symbol will appear in the header.

![Operator Console image 124](./images/starwatch-sms-user-guide-operator-console-rev-6_124.png)

Note: clicking on a column header will sort all the chart rows according to that parameter,
either using ascending or descending alphanumeric order. To sort by a different parameter,
you can simply click on another column header.

Clear Sorting
Selecting the *Clear Sorting* option will return the column to the original default settings.

Group by This Column
You can list data according to a single parameter exclusively by selecting the *Group by This*
*Column* option. The following captures show a device list before and after it has been
grouped by the *Widget* parameter.

![Operator Console image 125](./images/starwatch-sms-user-guide-operator-console-rev-6_125.png)

![Operator Console image 126](./images/starwatch-sms-user-guide-operator-console-rev-6_126.png)

![Operator Console image 127](./images/starwatch-sms-user-guide-operator-console-rev-6_127.png)

![Operator Console image 128](./images/starwatch-sms-user-guide-operator-console-rev-6_128.png)

![Operator Console image 129](./images/starwatch-sms-user-guide-operator-console-rev-6_129.png)


Full Expand / Full Collapse
Additionally, the device lists within each data class category can be separately expanded
and hidden, making large lists easier to navigate. You can expand a category manually by
selecting the small *Plus*  icon on the left-hand side of the appropriate row. To expand all

![Operator Console image 130](./images/starwatch-sms-user-guide-operator-console-rev-6_130.png)

categories at once to show all hidden rows, right-click on the column header and select the
*Full Expand* option from the drop down menu.

![Operator Console image 131](./images/starwatch-sms-user-guide-operator-console-rev-6_131.png)

![Operator Console image 132](./images/starwatch-sms-user-guide-operator-console-rev-6_132.png)

![Operator Console image 133](./images/starwatch-sms-user-guide-operator-console-rev-6_133.png)

In this example, the *Full Expand* option has been selected for the *Widget* tab.

![Operator Console image 134](./images/starwatch-sms-user-guide-operator-console-rev-6_134.png)

To collapse all categories at once to hide the individual rows within all categories, right-
click on the column header and select the *Full Collapse* option from the drop down menu.

![Operator Console image 135](./images/starwatch-sms-user-guide-operator-console-rev-6_135.png)


Group by Box
The *Group by Box* feature allows you to list data according to a single parameter or by
multiple parameters. If it does not already appear at the top of the spreadsheet, the *Drag a*
*column header here to group by that column* area can be called up by selecting the *Show*
*Group by Box* option.

![Operator Console image 136](./images/starwatch-sms-user-guide-operator-console-rev-6_136.png)

Once the area is active, it can be used to sort data.
Note: selecting the *Hide* *Group by Box* option will remove the *Drag a column header here to*
*group by that column* area from the screen.
To list data according to a single parameter exclusively, drag and drop the appropriate
column header into the *Drag a column header here to group by that column* area at the top
of the tab. The following capture shows a device list after the *Widget* header has been
dragged and dropped.

![Operator Console image 137](./images/starwatch-sms-user-guide-operator-console-rev-6_137.png)

![Operator Console image 138](./images/starwatch-sms-user-guide-operator-console-rev-6_138.png)

The device lists within each data class category can be separately expanded and hidden,
making large lists easier to navigate.
You can also list devices according to several parameters simultaneously by dragging and
dropping multiple column headers into the *Drag a column header here to group by that*
*column* area at the top of the tab. The capture below shows the device list after the *Widget*
header has been dragged and dropped, followed by the *Device* and *Status* categories.

![Operator Console image 139](./images/starwatch-sms-user-guide-operator-console-rev-6_139.png)

When sorting by multiple categories, the device lists within each category and sub category
can be separately expanded and hidden, making large lists easier to navigate.

![Operator Console image 140](./images/starwatch-sms-user-guide-operator-console-rev-6_140.png)

![Operator Console image 141](./images/starwatch-sms-user-guide-operator-console-rev-6_141.png)

Our grouping tree consists of the widgets, then the devices that include points with the
widget type selected (which is *None* in this example), and finally the status of the points in
the devices for the widget type selected.

![Operator Console image 142](./images/starwatch-sms-user-guide-operator-console-rev-6_142.png)

We can display every row that applies to the defined parameters by right-clicking in the
grouping area and selecting the *Full Expand* option from the pop-up menu.

![Operator Console image 143](./images/starwatch-sms-user-guide-operator-console-rev-6_143.png)

![Operator Console image 144](./images/starwatch-sms-user-guide-operator-console-rev-6_144.png)

![Operator Console image 145](./images/starwatch-sms-user-guide-operator-console-rev-6_145.png)


Column Chooser
The *Column Chooser* option allows you to directly select the data columns that appear in
the spreadsheet. When you select this option, the *Customization* window will appear.

![Operator Console image 146](./images/starwatch-sms-user-guide-operator-console-rev-6_146.png)

![Operator Console image 147](./images/starwatch-sms-user-guide-operator-console-rev-6_147.png)

The window displays a list of all the column headers that are currently not included in the
chart. To add one of the listed columns to the chart, you can simply click on the
appropriate header in the window and drag it into the chart. To place the new column
correctly, you must drop it within the row of headers that runs across the top of the chart.
Note: when dragging a new column into the chart, a large black *X* will appear over your
cursor when you are not positioned over an appropriate drop location. If you drop the
column while the *X* is on-screen, the column will remain in the *Customization* window.
You can also click and drag a column header from the current chart and drop it into the
*Customization* window. In this manner, you can move columns in an out of the chart, as
desired.

Best Fit
The *Best Fit* option automatically resizes the column to display all the information
contained in the column cells. For example, if the current column size does not provide
adequate space to display all the data that appears in one or more cells, the *Best Fit* option
will expand the column width to accommodate the entire data sequence. Conversely, if a
column is unnecessarily wide, the *Best Fit* option will reduce the column width
appropriately.

Best Fit (all columns)
The *Best Fit (all columns)* option will attempt to fit data in all columns using the best
possible configuration.

Clear Filter
The *Clear Filter* option removes any filtering that has been applied to a column, returning
it to the original default settings.

![Operator Console image 148](./images/starwatch-sms-user-guide-operator-console-rev-6_148.png)


Filter Editor
Selecting the *Filter Editor* option calls up the *Filter Editor* window.

![Operator Console image 149](./images/starwatch-sms-user-guide-operator-console-rev-6_149.png)

By clicking on the various sections of the filter string and selecting appropriate settings, you
can build and apply customized filters for the column. Once a filter is applied, a filter
editing row will be added at the bottom of the data chart enabling you to quickly adjust
filter settings, if needed.

![Operator Console image 150](./images/starwatch-sms-user-guide-operator-console-rev-6_150.png)

## Saving Your Column Settings

Some grids within the *StarWatch SMS* system allow you to save your column settings for future use. If a
grid offers this functionality, a drop-down list with the *Add*, *Delete*, and *Update* buttons will be
available on the main function bar.

![Operator Console image 151](./images/starwatch-sms-user-guide-operator-console-rev-6_151.png)

![Operator Console image 152](./images/starwatch-sms-user-guide-operator-console-rev-6_152.png)

Once you have configured a grid to your preference, save the setting by clicking the *Add New View*
button. Next, click in the name field to change the name of the grid view and press *Enter* on your
keyboard. The new grid view will be saved in the system and added to the drop-down list.

![Operator Console image 153](./images/starwatch-sms-user-guide-operator-console-rev-6_153.png)

Using the drop-down list, you can quickly return to saved grid views.

![Operator Console image 154](./images/starwatch-sms-user-guide-operator-console-rev-6_154.png)

To delete an existing view, select it from the drop-down list and click the *Delete Current View*
button.

![Operator Console image 155](./images/starwatch-sms-user-guide-operator-console-rev-6_155.png)

If you have made changes to an existing grid view, clicking the *Update View*
button will save the
modifications.

![Operator Console image 156](./images/starwatch-sms-user-guide-operator-console-rev-6_156.png)

## 1.2.6 WORKSPACE MANAGEMENT

Using the *Workspace Management* feature, you can create a series of workspace configurations and
associate them with existing operator roles. When a user logs into the system, the workspace
associated with their assigned role will automatically appear on their monitor(s). This can be used as a
mechanism to automatically provide specific user types with the functions and views they need to
perform their daily tasks. For example, a workspace configuration appropriate for a security guard
might include access control site maps and related alarm queues, while a workspace created for an
operator positioned at an entry/exit point might include the *Persons Management* and *Visit Planner*
functions.
**NOTE:** saved workspaces can include functions and display aspects positioned on multiple monitors.

## Creating a New Workspace

![Operator Console image 157](./images/starwatch-sms-user-guide-operator-console-rev-6_157.png)

To create a new, assignable workspace, set your screen layout as desired and click the *Start*
icon
at the top left of the screen.

![Operator Console image 158](./images/starwatch-sms-user-guide-operator-console-rev-6_158.png)

![Operator Console image 159](./images/starwatch-sms-user-guide-operator-console-rev-6_159.png)

![Operator Console image 160](./images/starwatch-sms-user-guide-operator-console-rev-6_160.png)

option.
Next, from the drop-down menu, select the
The *Workspace Management* window will appear.

![Operator Console image 161](./images/starwatch-sms-user-guide-operator-console-rev-6_161.png)

![Operator Console image 162](./images/starwatch-sms-user-guide-operator-console-rev-6_162.png)

Click the
button located at the top right of the window. A new workspace will be added to the
list with an auto-generated name.

![Operator Console image 163](./images/starwatch-sms-user-guide-operator-console-rev-6_163.png)

![Operator Console image 164](./images/starwatch-sms-user-guide-operator-console-rev-6_164.png)

Edit the name of the workspace by selecting it and typing into the name field. The newly created
workspace will now be available as an option when assigning workspaces to operator roles, as shown
below.

![Operator Console image 165](./images/starwatch-sms-user-guide-operator-console-rev-6_165.png)

![Operator Console image 166](./images/starwatch-sms-user-guide-operator-console-rev-6_166.png)

## Modifying an Existing Workspace

![Operator Console image 167](./images/starwatch-sms-user-guide-operator-console-rev-6_167.png)

To update an existing workspace, set your screen layout as desired and click the *Start*
icon at the
top left of the screen.

![Operator Console image 168](./images/starwatch-sms-user-guide-operator-console-rev-6_168.png)

option.
Next, from the drop-down menu, select the
The *Workspace Management* window will appear.

![Operator Console image 169](./images/starwatch-sms-user-guide-operator-console-rev-6_169.png)

![Operator Console image 170](./images/starwatch-sms-user-guide-operator-console-rev-6_170.png)

Select the appropriate workspace in the list and click the
button. The workspace will now
reflect the modified screen configuration.

![Operator Console image 171](./images/starwatch-sms-user-guide-operator-console-rev-6_171.png)

## Deleting a Workspace

![Operator Console image 172](./images/starwatch-sms-user-guide-operator-console-rev-6_172.png)

To delete an existing workspace, click the *Start*
icon at the top left of the screen.

![Operator Console image 173](./images/starwatch-sms-user-guide-operator-console-rev-6_173.png)

option.
Next, from the drop-down menu, select the
The *Workspace Management* window will appear.

![Operator Console image 174](./images/starwatch-sms-user-guide-operator-console-rev-6_174.png)

![Operator Console image 175](./images/starwatch-sms-user-guide-operator-console-rev-6_175.png)

Select the appropriate workspace in the list and click the
button.
Note: deleting a workspace will remove it from any operator role to which it has been assigned.

![Operator Console image 176](./images/starwatch-sms-user-guide-operator-console-rev-6_176.png)

## Loading an Existing Workspace

![Operator Console image 177](./images/starwatch-sms-user-guide-operator-console-rev-6_177.png)

To load an existing workspace, click the *Start*
icon at the top left of the screen.

![Operator Console image 178](./images/starwatch-sms-user-guide-operator-console-rev-6_178.png)

option.
Next, from the drop-down menu, select the
The *Workspace Management* window will appear.

![Operator Console image 179](./images/starwatch-sms-user-guide-operator-console-rev-6_179.png)

![Operator Console image 180](./images/starwatch-sms-user-guide-operator-console-rev-6_180.png)

Select the appropriate workspace in the list and click the
button. The selected workspace will
be called to the screen.

![Operator Console image 181](./images/starwatch-sms-user-guide-operator-console-rev-6_181.png)

## 1.2.7 SAVING YOUR WORKSPACE

Once you have positioned the various screen elements to your preference, *StarWatch SMS* allows you to
save the screen configuration. Once saved, the configuration will become the default view when you
re-open the application using the same login details.

![Operator Console image 182](./images/starwatch-sms-user-guide-operator-console-rev-6_182.png)

![Operator Console image 183](./images/starwatch-sms-user-guide-operator-console-rev-6_183.png)

Clicking on the *Start*
icon at the top left of the screen and selecting the
option from
the drop-down menu will save any configuration changes you may have made to the visible user
workspace.

![Operator Console image 184](./images/starwatch-sms-user-guide-operator-console-rev-6_184.png)

![Operator Console image 185](./images/starwatch-sms-user-guide-operator-console-rev-6_185.png)

![Operator Console image 186](./images/starwatch-sms-user-guide-operator-console-rev-6_186.png)

Note: alternately, you can click on the *Save Workspace*
icon from the *Quick Access Toolbar* if it has
been configured to be displayed.

![Operator Console image 187](./images/starwatch-sms-user-guide-operator-console-rev-6_187.png)

![Operator Console image 188](./images/starwatch-sms-user-guide-operator-console-rev-6_188.png)

## 1.2.8 GENERAL SAVING FEATURES

When working through the various setup and user related functions of *StarWatch SMS*, it is important to
manually save any changes you want to become a permanent part of your operating database.

## Saving Preferences

The system allows you to save any changes you make to default system settings related to the display
or configuration of data within the *StarWatch SMS* user interface. For example, the system allows you
to alter the appearance of data grids by changing the column order and to adjust the filtering settings
used when displaying devices within a site map. Using *Save Preferences* functionality, these types of
preferences can be saved as new default settings.

![Operator Console image 189](./images/starwatch-sms-user-guide-operator-console-rev-6_189.png)

![Operator Console image 190](./images/starwatch-sms-user-guide-operator-console-rev-6_190.png)

To save preferences, click on the *Start*
icon and select the
option from the drop-
down menu.

![Operator Console image 191](./images/starwatch-sms-user-guide-operator-console-rev-6_191.png)

![Operator Console image 192](./images/starwatch-sms-user-guide-operator-console-rev-6_192.png)

![Operator Console image 193](./images/starwatch-sms-user-guide-operator-console-rev-6_193.png)

## 2.0 PERSONNEL MANAGEMENT

Using the *Persons* function, you can accomplish all registration operations, including enrolling on-site
personnel and visitors into the system database, assigning user details and credentials, printing labels
on identification badges, and terminating card services. Since the process is completed in multiple
stages, you have the option to complete one or all of the main segments during an enrollment session.
For example, if you will be hosting a large number of visitors on a given day, you may want to
streamline the process by pre-registering each person into the system in advance. Credentials might
then be issued upon their arrival on-site, resulting in a less time consuming process.
The diagram presented below outlines the typical procedure for enrolling users into the *StarWatch SMS*
system and issuing access cards. Depending on your application, these steps may vary to some degree.

## Typical Enrollment Flow

Once credentials
Before assigning
User details will be
Once an individual
have been defined
credentials to an
automatically
has been registered,
and registered, the
individual, they must
positioned on the
the individual profile
identification card
first be enrolled and
identification badge
must then be further
can be issued to the
registered into the
template, which can
defined to include
new user.
*StarWatch SMS*
be printed at a local
credential
database.
workstation.
information.
In general, there are two groups of tasks to perform. The first group is person-based and includes
adding a new person, retiring personnel, etc. The second group of tasks is card-based and includes
registering a card to a person, issuing a card, retiring a card, or terminating a damaged card.
Note: to follow these instructions, you must be logged into the *StarWatch SMS Operator* application
under a role with adequate permission levels to input personnel and card information.

![Operator Console image 194](./images/starwatch-sms-user-guide-operator-console-rev-6_194.png)

## 2.1 PERSONS WORKSPACE

Creating new personnel is one person-based task that can be performed as an operator. Other person-
based tasks are retiring personnel, finding the records associated with an individual, adding a
photograph, modifying person-related information, and restoring a profile.

![Operator Console image 195](./images/starwatch-sms-user-guide-operator-console-rev-6_195.png)

To access the *Persons* application window, click the *Persons*
button on the main *Ribbon* menu.
The *Persons* area will appear on the screen displaying the *Details* tab of the first individual in the
current personnel list.

![Operator Console image 196](./images/starwatch-sms-user-guide-operator-console-rev-6_196.png)

![Operator Console image 197](./images/starwatch-sms-user-guide-operator-console-rev-6_197.png)

Using the *Persons* drop-down list, you can also select any *Person Group* that has been created in the
system (ex. employee, visitor).

![Operator Console image 198](./images/starwatch-sms-user-guide-operator-console-rev-6_198.png)

![Operator Console image 199](./images/starwatch-sms-user-guide-operator-console-rev-6_199.png)

Using the search features provided in the *Persons* pane to the left of the screen, you can locate and
select specific individuals. Once you have located the appropriate profile, click on it in the list to
select it. This will cause the fields in the workspace to the right of the list to auto-populate with
information specific to that user. You can now view or edit the profile.

![Operator Console image 200](./images/starwatch-sms-user-guide-operator-console-rev-6_200.png)

There are four information tabs available for capturing information and assigning user details when
setting up a profile.

![Operator Console image 201](./images/starwatch-sms-user-guide-operator-console-rev-6_201.png)

Depending on your site requirements, you may or may not need to fill in all of the fields provided on
these tabs. In most cases, the initial data collected is the personal information of the individual being
added, such as age, gender, height, weight, date of birth, and Social Security number.
Note: if you require that additional fields be displayed and entered when registering, you can modify
the registration screen using custom fields. Please see the *Administration Panel* user guide for details.

![Operator Console image 202](./images/starwatch-sms-user-guide-operator-console-rev-6_202.png)

## 2.1.1 DETAILS TAB

The *Details* tab of the *Persons* window displays a photo and the personal details of the currently
selected person.

![Operator Console image 203](./images/starwatch-sms-user-guide-operator-console-rev-6_203.png)

**Field Header**
**Description**
Overview
Overview of the personal information for an individual registered in
the system
Comments
Lists any comments made in the *CardWatch* pane
Credentials
Selects the type of card that the person should use

![Operator Console image 204](./images/starwatch-sms-user-guide-operator-console-rev-6_204.png)

## 2.1.2 ADDITIONAL TAB

The *Additional* tab of the *Persons* window displays further personal and credential-related information
about the currently selected individual.

![Operator Console image 205](./images/starwatch-sms-user-guide-operator-console-rev-6_205.png)

**Field Header**
**Description**
Credentials
Lists the card type that is associated with the person
Credential Details
Lists the credential details of the card type
Business Information
Lists the business name, address, and contact number if the person
is not a permanent employee of your company
Badge
Displays the front and back of the card  Note: this requires an
Assure ID license

![Operator Console image 206](./images/starwatch-sms-user-guide-operator-console-rev-6_206.png)

## 2.1.3 ACCESS TAB

The *Access* tab of the *Persons* window displays access rights and visitor management related
information for the currently selected individual.

![Operator Console image 207](./images/starwatch-sms-user-guide-operator-console-rev-6_207.png)

**Field Header**
**Description**
Access Right
Sets the access permissions for the person
Common Permission
Sets the global permissions for the person, which are available via a
drop-down menu
Can Sponsor Visits
Allows the person to sponsor visits from non-employees
Can Escort Visitors
Allows the person to escort visitors when on the premises
Groups
Lists the group types that the person is a member of
Card
Displays all the access rights the person has been given, such as
access points and calendars

![Operator Console image 208](./images/starwatch-sms-user-guide-operator-console-rev-6_208.png)

## 2.1.4 USER TAB

The *Users* tab of the *Persons* window displays user password and PIN related information for the
currently selected individual.

![Operator Console image 209](./images/starwatch-sms-user-guide-operator-console-rev-6_209.png)

**Field Header**
**Description**
User Information
Sets the user login information, including username and password
User PIN
Sets the user PIN
Keypad User PIC
Sets the user PIC
Role
Sets the login role for the user

![Operator Console image 210](./images/starwatch-sms-user-guide-operator-console-rev-6_210.png)

## 2.2 PERSON LIST

To the left of the *Persons* screen, the application displays a list of individuals already entered into the
database and provides several options for organizing and searching through the list.

![Operator Console image 211](./images/starwatch-sms-user-guide-operator-console-rev-6_211.png)

![Operator Console image 212](./images/starwatch-sms-user-guide-operator-console-rev-6_212.png)

## 2.2.1 PERSON GROUPS

Each person in the database can be assigned to one or multiple *Person Groups*. These groups are
created to divide and organize personnel into subcategories, facilitating more effective searches of
large databases. For example, you may want to create separate *Person Groups* for employees, visitors,
and contractors.
Note: you must have the appropriate rights to create *Person Groups*.
*Person Groups* should not be confused with *Person Types*, which are functional categories linked with
critical personnel parameters, such as permission levels and credential types. *Person Groups* only
function as part of a chosen naming scheme.
*Person Groups* provide a convenient way to sort and view a selective group of individuals. The list on
the left of the *Persons* screen alphabetically displays all of the profiles that have been stored within
the active *Person Group*. If the profile you wish to view or edit does not reside within the current
*Person Group*, you can change the displayed group using the drop-down list provided at the top of the
column.

![Operator Console image 213](./images/starwatch-sms-user-guide-operator-console-rev-6_213.png)

Once selected, the group will appear in the group *Name* field and all associated profiles will be
displayed in the list alphabetically. If you are not sure which *Person Group* the desired profile is in,
simply select the *All* option from the drop-down list.

![Operator Console image 214](./images/starwatch-sms-user-guide-operator-console-rev-6_214.png)

![Operator Console image 215](./images/starwatch-sms-user-guide-operator-console-rev-6_215.png)

If the active group contains more profiles than can be displayed on the screen at one time, the list can
be sequenced through using the scroll bar provided on the right-hand side of the list.

![Operator Console image 216](./images/starwatch-sms-user-guide-operator-console-rev-6_216.png)

![Operator Console image 217](./images/starwatch-sms-user-guide-operator-console-rev-6_217.png)

To add a new *Person Group*, select the
icon at the top of the list. A new group will be added to
the system with an auto-numbered name and the *New Person Group* dialog box will appear.

![Operator Console image 218](./images/starwatch-sms-user-guide-operator-console-rev-6_218.png)

Enter a new name for the group in the *Name* field, select any additional parameters you require, and
click the *Ok* button. The new group will now be available from the drop-down list when assigning
groups to personnel in the database.

![Operator Console image 219](./images/starwatch-sms-user-guide-operator-console-rev-6_219.png)

![Operator Console image 220](./images/starwatch-sms-user-guide-operator-console-rev-6_220.png)

To change the name of a group, select the group from the drop-down list and click the *Edit*
icon.
Similarly, you can modify the name of an existing group by calling it to the screen, clicking in the *Name*
field at the top of the list, typing in a new name for the group, and hitting the *Enter* key. Note: if you
fail to hit the *Enter* key, the new name will not be recorded.

![Operator Console image 221](./images/starwatch-sms-user-guide-operator-console-rev-6_221.png)

![Operator Console image 222](./images/starwatch-sms-user-guide-operator-console-rev-6_222.png)

To delete a group from the system, select the group from the drop-down list and click the *Delete*
icon. You can also utilize the system navigator feature. In the navigator window, locate the appropriate
group in the *Person Groups* list. Next, right-click on the group and select the *Delete Person Group*
option.

![Operator Console image 223](./images/starwatch-sms-user-guide-operator-console-rev-6_223.png)

## 2.2.2 SEARCH FEATURES

In addition to *Person Groups*, the system provides a filtering function to help you locate specific
persons in the database. This is especially useful when dealing with large databases containing
hundreds or even thousands of profiles.

![Operator Console image 224](./images/starwatch-sms-user-guide-operator-console-rev-6_224.png)

To narrow the list of displayed persons, click on the *Filter*
icon located at the top right of the
*Persons* list. A table will appear allowing you to enter various parameters.

![Operator Console image 225](./images/starwatch-sms-user-guide-operator-console-rev-6_225.png)

![Operator Console image 226](./images/starwatch-sms-user-guide-operator-console-rev-6_226.png)

After entering the appropriate parameters into the table, click the *Update*
icon to filter the list.
Only those profiles matching the parameters you entered into the table will now be displayed.

![Operator Console image 227](./images/starwatch-sms-user-guide-operator-console-rev-6_227.png)

Clicking the *Clear*
icon will remove all previously entered information from the table, allowing you
to conduct a new search.

![Operator Console image 228](./images/starwatch-sms-user-guide-operator-console-rev-6_228.png)

Note: to remove the filtering table from the screen, simply click on the *Filter*
icon a second time.

![Operator Console image 229](./images/starwatch-sms-user-guide-operator-console-rev-6_229.png)

![Operator Console image 230](./images/starwatch-sms-user-guide-operator-console-rev-6_230.png)

Similarly, you can search for individual profiles by clicking on the
button on the top menu of the
main *Persons* workspace. The *Find Person* window will appear.

![Operator Console image 231](./images/starwatch-sms-user-guide-operator-console-rev-6_231.png)

![Operator Console image 232](./images/starwatch-sms-user-guide-operator-console-rev-6_232.png)

As with the *Filter* function, after entering the appropriate parameters into the table, click the
icon to filter the list. Only those profiles matching the parameters you entered into the table will now
be displayed.

![Operator Console image 233](./images/starwatch-sms-user-guide-operator-console-rev-6_233.png)

## 2.3 REGISTERING A PERSON

When you register a person, you are adding a new person profile to the system database.

![Operator Console image 234](./images/starwatch-sms-user-guide-operator-console-rev-6_234.png)

From the top menu of the *Persons* workspace, click on the
button. The fields available in the main
area will become blank allowing you to begin with an empty profile.
Note: the *Person #* field is automatically generated, and you do not have to modify it.

![Operator Console image 235](./images/starwatch-sms-user-guide-operator-console-rev-6_235.png)

![Operator Console image 236](./images/starwatch-sms-user-guide-operator-console-rev-6_236.png)

![Operator Console image 237](./images/starwatch-sms-user-guide-operator-console-rev-6_237.png)

To add an existing photograph of the person to the profile, click the
button. A standard Windows
navigation screen will appear allowing you to locate the image file within your directory structure and
select it.

![Operator Console image 238](./images/starwatch-sms-user-guide-operator-console-rev-6_238.png)

Note: photo files must be one of the following file types: .bmp, .jpg, or .png.

![Operator Console image 239](./images/starwatch-sms-user-guide-operator-console-rev-6_239.png)

Continue by modifying the information on the available sub tabs (see section 2.1 PERSONS
WORKSPACE), as needed, to reflect the individual being added.

![Operator Console image 240](./images/starwatch-sms-user-guide-operator-console-rev-6_240.png)

When all changes are complete, click the
button on the top right menu to save the new
person profile. Note: you can return to the profile at any time to make changes to the information, but
be sure to save any changes.

![Operator Console image 241](./images/starwatch-sms-user-guide-operator-console-rev-6_241.png)

![Operator Console image 242](./images/starwatch-sms-user-guide-operator-console-rev-6_242.png)

## 2.4 REGISTERING AND ISSUING CARDS

After creating a person profile in the system, you can register and then issue cards to the individual.
To register a card to a person, open their profile in the main *Persons* workspace. In the *Credentials*
area of the *Details* tab, select the card type from the *Card* drop-down list.

![Operator Console image 243](./images/starwatch-sms-user-guide-operator-console-rev-6_243.png)

![Operator Console image 244](./images/starwatch-sms-user-guide-operator-console-rev-6_244.png)

Next, in the card format field, type the card number and then click the
button. The card is now
entered in the database as registered to that person.

![Operator Console image 245](./images/starwatch-sms-user-guide-operator-console-rev-6_245.png)

![Operator Console image 246](./images/starwatch-sms-user-guide-operator-console-rev-6_246.png)

After a card has been registered to the individual, you must issue the card before it can be used for
access. In the *Expiry* field, set an expiration date for the card or select the *Never* checkbox.

![Operator Console image 247](./images/starwatch-sms-user-guide-operator-console-rev-6_247.png)

![Operator Console image 248](./images/starwatch-sms-user-guide-operator-console-rev-6_248.png)

To issue the card, click the
button. The card is now issued to that person and activated in the
system, which sends out the card/person data to all security panels connected to the database.

![Operator Console image 249](./images/starwatch-sms-user-guide-operator-console-rev-6_249.png)

Note: multiple cards can be assigned to an individual.

![Operator Console image 250](./images/starwatch-sms-user-guide-operator-console-rev-6_250.png)

## 2.5 VERIFYING AN IDENTITY

*StarWatch SMS* provides the capability to have a profile automatically pop up on the *Persons* screen
when the associated card is swiped at a specific reader. This allows an operator to immediately verify
that the correct person is using the card at that location. For this function, the operator workstation
must have a card reader attached to it.
Note: using the *Card Format* feature of the system, the *Can Identify Person* option must be selected for
the enrollment reader being used. Please see the *Administration Panel* guide for more information.
To verify an identity associated with a card, click the *Identity* button at the top of the *Persons*
workspace. Next, have the person swipe his or her card. The card holder record associated with the
card will populate the window allowing you to visually verify that the card is being utilized by the
proper person.
Note:  businesses may have security procedures associated with this task that involve additional actions
that must be completed by the operator. See your System Administrator or security department for
more information.

![Operator Console image 251](./images/starwatch-sms-user-guide-operator-console-rev-6_251.png)

## 2.6 RETIRING A PERSON

When an individual is retired from the system, he or she is no longer listed with active personnel.
However, the events associated with the person are kept in the database for future reference. If the
person is deleted, associated events are also removed.
Note: when retiring a person, you should first retire any cards associated with the person so there are
no loose, unretired cards remaining (see section 2.10 RETIRING A CARD).

![Operator Console image 252](./images/starwatch-sms-user-guide-operator-console-rev-6_252.png)

To retire a person, open their profile in the *Persons* application and click the
button located at
the top left of the *Persons* workspace. A confirmation window will appear to confirm the retiring of the
person.

![Operator Console image 253](./images/starwatch-sms-user-guide-operator-console-rev-6_253.png)

Click the *Yes* button to proceed.

![Operator Console image 254](./images/starwatch-sms-user-guide-operator-console-rev-6_254.png)

![Operator Console image 255](./images/starwatch-sms-user-guide-operator-console-rev-6_255.png)

## 2.7 RESTORING A PERSON

If you have previously retired a person, you can restore them to the system at any time. The person
will become active again, but will not have an associated card currently issued to them.

![Operator Console image 256](./images/starwatch-sms-user-guide-operator-console-rev-6_256.png)

To restore a person to the active list, click the
button at the top of the *Persons* workspace to
enable the browsing function.

![Operator Console image 257](./images/starwatch-sms-user-guide-operator-console-rev-6_257.png)

In the *Groups* drop-down list, select the *Retired* option and the people defined as retired will be
displayed.

![Operator Console image 258](./images/starwatch-sms-user-guide-operator-console-rev-6_258.png)

Double-click on the person that you want to restore to open their profile and click the
button at
the top of the *Persons* workspace.

![Operator Console image 259](./images/starwatch-sms-user-guide-operator-console-rev-6_259.png)

![Operator Console image 260](./images/starwatch-sms-user-guide-operator-console-rev-6_260.png)

A confirmation window will appear to confirm the restoring of the person. Click the *Yes* button to
proceed.

![Operator Console image 261](./images/starwatch-sms-user-guide-operator-console-rev-6_261.png)

![Operator Console image 262](./images/starwatch-sms-user-guide-operator-console-rev-6_262.png)

## 2.8 ASSIGNING A PIC

A Person Identity Code (PIC) is a numerical sequence up to 16 digits in length that is assigned to a
person (not a card). PICs are useful for tracking purposes, such as knowing who enabled or disabled an
alarm zone. Depending on configuration and usage, you may or may not use PICs in your system.
To assign a PIC to a person, call up the appropriate person profile in the *Persons* workspace and click
on the *User* tab at the bottom of the screen.

![Operator Console image 263](./images/starwatch-sms-user-guide-operator-console-rev-6_263.png)

![Operator Console image 264](./images/starwatch-sms-user-guide-operator-console-rev-6_264.png)

![Operator Console image 265](./images/starwatch-sms-user-guide-operator-console-rev-6_265.png)

In the *Keypad User Person Identity Code (PIC)* field, click on the
button.

![Operator Console image 266](./images/starwatch-sms-user-guide-operator-console-rev-6_266.png)

![Operator Console image 267](./images/starwatch-sms-user-guide-operator-console-rev-6_267.png)

In the *Issue PIC* dialog box, enter the value for the PIC or click the
button to generate a PIC
automatically.

![Operator Console image 268](./images/starwatch-sms-user-guide-operator-console-rev-6_268.png)

Click the *Ok* button to proceed.

![Operator Console image 269](./images/starwatch-sms-user-guide-operator-console-rev-6_269.png)

The new PIC will appear as a row of ************ in the field with an attached issuance date. Click *Save* to
save the change.

![Operator Console image 270](./images/starwatch-sms-user-guide-operator-console-rev-6_270.png)

## 2.9 ASSIGNING A USER/ROLE LOGIN

Using the *Persons* function, you can assign a role or multiple roles to an individual.
To assign a role to a person, call up the appropriate person profile in the *Persons* workspace and click
on the *User* tab at the bottom of the screen.

![Operator Console image 271](./images/starwatch-sms-user-guide-operator-console-rev-6_271.png)

![Operator Console image 272](./images/starwatch-sms-user-guide-operator-console-rev-6_272.png)

![Operator Console image 273](./images/starwatch-sms-user-guide-operator-console-rev-6_273.png)

In the *Role* area to the right of the screen, click the checkboxes that correspond to the roles you would
like to assign.

![Operator Console image 274](./images/starwatch-sms-user-guide-operator-console-rev-6_274.png)

Next, in the *User* *Information* area, fill in the *User Name*, *User Password*, and *Confirm Password* fields
and hit *Save*.

![Operator Console image 275](./images/starwatch-sms-user-guide-operator-console-rev-6_275.png)

The individual will now be given the system rights and privileges associated with the roles selected
upon login.

![Operator Console image 276](./images/starwatch-sms-user-guide-operator-console-rev-6_276.png)

## 2.10 RETIRING A CARD

When a card is no longer needed by a card holder, you can retire it from the system where it will
become disabled. You can later return it to the pool to be assigned to another person or terminate it,
which will render it useless.
Note: to retire a person, you must retire the associated card first.
To retire a card, call the person profile from which you want to retire a card to the *Persons* workspace.

![Operator Console image 277](./images/starwatch-sms-user-guide-operator-console-rev-6_277.png)

![Operator Console image 278](./images/starwatch-sms-user-guide-operator-console-rev-6_278.png)

In the *Credentials* area of the *Details* tab, click the
button.

![Operator Console image 279](./images/starwatch-sms-user-guide-operator-console-rev-6_279.png)

The *Card Details* window pops up.

![Operator Console image 280](./images/starwatch-sms-user-guide-operator-console-rev-6_280.png)

![Operator Console image 281](./images/starwatch-sms-user-guide-operator-console-rev-6_281.png)

In the *Retire Card* area, click the
button.

![Operator Console image 282](./images/starwatch-sms-user-guide-operator-console-rev-6_282.png)

In the confirmation window, click the *Yes* button to proceed. The card will be retired.

![Operator Console image 283](./images/starwatch-sms-user-guide-operator-console-rev-6_283.png)

![Operator Console image 284](./images/starwatch-sms-user-guide-operator-console-rev-6_284.png)

![Operator Console image 285](./images/starwatch-sms-user-guide-operator-console-rev-6_285.png)

## 2.11 RETURNING A CARD

When a card is no longer needed by a card holder, you can return it to the pool to be assigned to
another person.
Note: using the *Card Type* feature of the system, the *Allow Card to be Re-used (Returned)* option must
be selected for the card being used. Please see the *Administration Panel* guide for more information.
To return a card, call the person profile from which you want to return a card to the *Persons*
workspace.

![Operator Console image 286](./images/starwatch-sms-user-guide-operator-console-rev-6_286.png)

![Operator Console image 287](./images/starwatch-sms-user-guide-operator-console-rev-6_287.png)

In the *Credentials* area of the *Details* tab, click the
button.

![Operator Console image 288](./images/starwatch-sms-user-guide-operator-console-rev-6_288.png)

The *Card Details* window pops up.

![Operator Console image 289](./images/starwatch-sms-user-guide-operator-console-rev-6_289.png)

![Operator Console image 290](./images/starwatch-sms-user-guide-operator-console-rev-6_290.png)

In the *Retire Card* area, click the
button.

![Operator Console image 291](./images/starwatch-sms-user-guide-operator-console-rev-6_291.png)

In the confirmation window click the *Yes* button to proceed. The card will be returned and can now be
assigned to another person.

![Operator Console image 292](./images/starwatch-sms-user-guide-operator-console-rev-6_292.png)

## 2.12 VALIDATING A CARD

When you validate a card, you are ensuring that it is being used by the correct person and that all
personal information is correct. The card is first set to be validated by the operator and the next time
the card is swiped, the operator will follow a procedure set up by the System Administrator to ensure
the validity of the card and the person.

![Operator Console image 293](./images/starwatch-sms-user-guide-operator-console-rev-6_293.png)

To validate a card, click on the
button on the main *Ribbon* menu to open the *Cards* function.

![Operator Console image 294](./images/starwatch-sms-user-guide-operator-console-rev-6_294.png)

From the list displayed in the workspace, select the person whose card you want to validate by clicking
on the appropriate name.

![Operator Console image 295](./images/starwatch-sms-user-guide-operator-console-rev-6_295.png)

![Operator Console image 296](./images/starwatch-sms-user-guide-operator-console-rev-6_296.png)

![Operator Console image 297](./images/starwatch-sms-user-guide-operator-console-rev-6_297.png)

In the *Credentials Details* pane on the right side of the screen, click the
button. This
marks the card for validation and will force the card holder to go to a manned workstation to proceed
through the validation process.

![Operator Console image 298](./images/starwatch-sms-user-guide-operator-console-rev-6_298.png)

In the *Persons* application, the profile of the individual will now be marked with a yellow diamond
to indicate that the card must be validated.

![Operator Console image 299](./images/starwatch-sms-user-guide-operator-console-rev-6_299.png)

![Operator Console image 300](./images/starwatch-sms-user-guide-operator-console-rev-6_300.png)

![Operator Console image 301](./images/starwatch-sms-user-guide-operator-console-rev-6_301.png)

When the card holder swipes the card at a workstation manned by an operator, the operator will be
notified.

![Operator Console image 302](./images/starwatch-sms-user-guide-operator-console-rev-6_302.png)

![Operator Console image 303](./images/starwatch-sms-user-guide-operator-console-rev-6_303.png)

The card can be validated in the *Additional* tab in the *Persons* function, by clicking the
button.
The card will then be marked valid for use.

![Operator Console image 304](./images/starwatch-sms-user-guide-operator-console-rev-6_304.png)

![Operator Console image 305](./images/starwatch-sms-user-guide-operator-console-rev-6_305.png)

## 2.13 PRINTING A CARD

In most cases, the last step in issuing a card to a new person is printing information onto the card. The
card is printed on a badge printer and typically has the company logo, a photograph of the individual,
and additional information such as the expiration date of the card and type of group (ex. visitor,
employee).
To print a card, call the appropriate person profile to the *Persons* workspace and click on the
*Additional* tab at the bottom of the screen.

![Operator Console image 306](./images/starwatch-sms-user-guide-operator-console-rev-6_306.png)

![Operator Console image 307](./images/starwatch-sms-user-guide-operator-console-rev-6_307.png)

![Operator Console image 308](./images/starwatch-sms-user-guide-operator-console-rev-6_308.png)

Click on the
button in the *Credential Details* area to print the card.

![Operator Console image 309](./images/starwatch-sms-user-guide-operator-console-rev-6_309.png)

## 2.14 UPDATING THE EXPIRATION DATE OF A CARD

You can update the expiration date of a card or remove the expiration entirely. To update the
expiration of a card, call the appropriate person profile to the *Persons* workspace.
Note: if you are registering a new person, please refer to section 2.4 REGISTERING AND ISSUING CARDS.

![Operator Console image 310](./images/starwatch-sms-user-guide-operator-console-rev-6_310.png)

In the *Credentials* area of the *Details* tab, click the
button. The *Card Details* window will
appear.

![Operator Console image 311](./images/starwatch-sms-user-guide-operator-console-rev-6_311.png)

![Operator Console image 312](./images/starwatch-sms-user-guide-operator-console-rev-6_312.png)

You can set an expiration date for the card using the *Expiry* drop-down list and pop-up calendar.

![Operator Console image 313](./images/starwatch-sms-user-guide-operator-console-rev-6_313.png)

To remove the expiration feature from the card, select the *Never* checkbox.

![Operator Console image 314](./images/starwatch-sms-user-guide-operator-console-rev-6_314.png)

![Operator Console image 315](./images/starwatch-sms-user-guide-operator-console-rev-6_315.png)

When your changes have been set, click the
button followed by the
button.

![Operator Console image 316](./images/starwatch-sms-user-guide-operator-console-rev-6_316.png)

## 2.15 UPDATING THE ACCESS PERMISSIONS OF A CARD

To update the access permissions of a card, call the appropriate person profile to the *Persons*
workspace and click on the *Access* tab at the bottom of the screen.

![Operator Console image 317](./images/starwatch-sms-user-guide-operator-console-rev-6_317.png)

![Operator Console image 318](./images/starwatch-sms-user-guide-operator-console-rev-6_318.png)

In the *Person Access Permissions* area to the left side of the workspace, select the appropriate
permission from the *Common Permission* drop-down menu. The selection you make will be reflected in
the tree for portals and doors shown in the right half of the window.

![Operator Console image 319](./images/starwatch-sms-user-guide-operator-console-rev-6_319.png)

In the screenshot below, the *Airport Access* permission has been selected, giving the individual *24x7*
access to *Airport Door 1*, *Airport Door 2*, and *Main Entrances*.

![Operator Console image 320](./images/starwatch-sms-user-guide-operator-console-rev-6_320.png)

When you have completed updating the permission for the card, click *Save* to save the change.

![Operator Console image 321](./images/starwatch-sms-user-guide-operator-console-rev-6_321.png)

Note: A second way to update the access permissions of a card becomes available when the System
Administrator has set the specific card type as a default. This is accomplished using the *Card Type*
function.

![Operator Console image 322](./images/starwatch-sms-user-guide-operator-console-rev-6_322.png)

![Operator Console image 323](./images/starwatch-sms-user-guide-operator-console-rev-6_323.png)

![Operator Console image 324](./images/starwatch-sms-user-guide-operator-console-rev-6_324.png)

With this setting in place, the access permission can be selected in the *Persons* workspace using the
drop-down list available in the *Details* tab.

![Operator Console image 325](./images/starwatch-sms-user-guide-operator-console-rev-6_325.png)

![Operator Console image 326](./images/starwatch-sms-user-guide-operator-console-rev-6_326.png)

## 2.16 CHANGING THE STATUS OF A CARD

You can change the status of a card to indicate one of the following:

*Lost/Stolen* - this indicates that the card number should be terminated and can no longer be
used.

*Suspend* - this temporarily suspends the access permissions for the card. The operator may do
this if an area must be temporarily off-limits to a person for some reason.

*Revoke* - this revokes the access permissions for the card. The operator may do this if the
person has been terminated and no longer works for the company.

*Expire* - this expires the card and it is no longer valid for use by the card holder. The operator
can either issue a new card or enter a new expiration date for the card.

*Re-issue* - this reissues the card into a valid state after being in an invalid state, such as those
listed above.
To change the status of a card, call the appropriate person profile to the *Persons* workspace.

![Operator Console image 327](./images/starwatch-sms-user-guide-operator-console-rev-6_327.png)

![Operator Console image 328](./images/starwatch-sms-user-guide-operator-console-rev-6_328.png)

![Operator Console image 329](./images/starwatch-sms-user-guide-operator-console-rev-6_329.png)

![Operator Console image 330](./images/starwatch-sms-user-guide-operator-console-rev-6_330.png)

In the *Credentials* area of the *Details* tab, click the
button.

![Operator Console image 331](./images/starwatch-sms-user-guide-operator-console-rev-6_331.png)

The *Card Details* window will appear.

![Operator Console image 332](./images/starwatch-sms-user-guide-operator-console-rev-6_332.png)

In the *Status Change* area, select one the options provided.

![Operator Console image 333](./images/starwatch-sms-user-guide-operator-console-rev-6_333.png)

![Operator Console image 334](./images/starwatch-sms-user-guide-operator-console-rev-6_334.png)

When changes are complete, click the
button.

![Operator Console image 335](./images/starwatch-sms-user-guide-operator-console-rev-6_335.png)

## 2.17 ASSIGNING A PIN TO A CARD

When Personal Identification Numbers (PINs) are required, in addition to swiping a card, a card holder
must enter his/her PIN on a keypad near the card reader. PINs follow a card in the system, not a
person.
To assign a PIN to a card, call the appropriate person profile to the *Persons* workspace and click on the
*User* tab at the bottom of the screen.

![Operator Console image 336](./images/starwatch-sms-user-guide-operator-console-rev-6_336.png)

![Operator Console image 337](./images/starwatch-sms-user-guide-operator-console-rev-6_337.png)

![Operator Console image 338](./images/starwatch-sms-user-guide-operator-console-rev-6_338.png)

![Operator Console image 339](./images/starwatch-sms-user-guide-operator-console-rev-6_339.png)

![Operator Console image 340](./images/starwatch-sms-user-guide-operator-console-rev-6_340.png)

In the *User PIN* field, click the
button.

![Operator Console image 341](./images/starwatch-sms-user-guide-operator-console-rev-6_341.png)

In the *Change PIN* window, type in a value for the PIN in the *PIN* field and retype it in the *Confirm PIN*
field.

![Operator Console image 342](./images/starwatch-sms-user-guide-operator-console-rev-6_342.png)

Next, click the
button.
Note: if the system determines that the entered PIN is too weak, you will be prompted to enter a
stronger PIN.

![Operator Console image 343](./images/starwatch-sms-user-guide-operator-console-rev-6_343.png)

Note: if you can also remove the PIN assignment by hitting the
button.

![Operator Console image 344](./images/starwatch-sms-user-guide-operator-console-rev-6_344.png)

## 2.18 ISSUING MULTIPLE CARDS TO AN INDIVIDUAL

To register additional cards to a person, call the appropriate person profile to the *Persons* workspace
and click on the *Additional* tab at the bottom of the screen.

![Operator Console image 345](./images/starwatch-sms-user-guide-operator-console-rev-6_345.png)

![Operator Console image 346](./images/starwatch-sms-user-guide-operator-console-rev-6_346.png)

![Operator Console image 347](./images/starwatch-sms-user-guide-operator-console-rev-6_347.png)

Next, in the *Credentials* area in the center left of the screen, select the card type from the *Select Card*
*Type* drop-down menu.

![Operator Console image 348](./images/starwatch-sms-user-guide-operator-console-rev-6_348.png)

Depending on the card type selected, the system will provide new registration options in the
*Credentials* area. Either type in the card number manually or read the card number using the card
reader.

![Operator Console image 349](./images/starwatch-sms-user-guide-operator-console-rev-6_349.png)

![Operator Console image 350](./images/starwatch-sms-user-guide-operator-console-rev-6_350.png)

Once you have completed the action appropriate for the card type, click the
button.
After the card has been registered to the individual, the *Credential Details* area will become populated
with issuance options. You must issue the card before it can be used for access. In the *Expiry* field, set
an expiration date for the card or select the *Never* checkbox. You can also set the *Access Permission*.

![Operator Console image 351](./images/starwatch-sms-user-guide-operator-console-rev-6_351.png)

![Operator Console image 352](./images/starwatch-sms-user-guide-operator-console-rev-6_352.png)

![Operator Console image 353](./images/starwatch-sms-user-guide-operator-console-rev-6_353.png)

To issue the card, click the
button. The card is now issued to that person and activated in the
system, which sends out the card/person data to all security panels connected to the database.

![Operator Console image 354](./images/starwatch-sms-user-guide-operator-console-rev-6_354.png)

Once the additional card has been issued, the *Issue* tab in the *Credentials* area will display a list of all
cards issued to the individual.

![Operator Console image 355](./images/starwatch-sms-user-guide-operator-console-rev-6_355.png)

## 2.19 VIEWING A HISTORY OF CARDS ISSUED TO AN INDIVIDUAL

To view a history of the cards that have been previously assigned to a specific person, call the
appropriate person profile to the *Persons* workspace and click on the *Additional* tab at the bottom of
the screen.

![Operator Console image 356](./images/starwatch-sms-user-guide-operator-console-rev-6_356.png)

![Operator Console image 357](./images/starwatch-sms-user-guide-operator-console-rev-6_357.png)

![Operator Console image 358](./images/starwatch-sms-user-guide-operator-console-rev-6_358.png)

![Operator Console image 359](./images/starwatch-sms-user-guide-operator-console-rev-6_359.png)

In the *Credentials* area to the center left of the screen, click on the
tab.

![Operator Console image 360](./images/starwatch-sms-user-guide-operator-console-rev-6_360.png)

All cards that have been registered to the person are displayed with card details, including the current
status of each card.
Note: the *Credential Details* area enables you to restore cards, if the card type allows.

![Operator Console image 361](./images/starwatch-sms-user-guide-operator-console-rev-6_361.png)

![Operator Console image 362](./images/starwatch-sms-user-guide-operator-console-rev-6_362.png)

## 3.0 MANAGING DEVICES

The *Devices* function provides a single place to view all the devices connected to your system and
manually issue commands. This interface provides a list of all the access points and associated device
details that have been previously configured in the *Site Builder* application.

![Operator Console image 363](./images/starwatch-sms-user-guide-operator-console-rev-6_363.png)

From this window, you can view the status of individual *Access Points*, *Alarm Zones*, and *Panels* and
issue commands to various hardware components. You can also view the details associated with a
selected point in the *Device Details* pane located on the right side of the screen.
Note: To access the *Devices* window, you must be logged into the *Operator* application as a user with
sufficient authority to perform Administrator functions.

![Operator Console image 364](./images/starwatch-sms-user-guide-operator-console-rev-6_364.png)

Note: You cannot modify device parameters from the *Devices* window. You can only make device
changes (*Name*, *Description*, *Zone*, etc.) via the *Site Builder* application. In the screenshot below,
notice that the *Name*, *Description*, *PIN*, *Widget*, *Category*, and *Zone* parameters have been grayed out
and are unavailable to modify from the *Devices* window.

![Operator Console image 365](./images/starwatch-sms-user-guide-operator-console-rev-6_365.png)

![Operator Console image 366](./images/starwatch-sms-user-guide-operator-console-rev-6_366.png)

## 3.1 VIEWING DEVICE DETAILS

![Operator Console image 367](./images/starwatch-sms-user-guide-operator-console-rev-6_367.png)

To open the *Device* window, click on the
button on the *Main Ribbon* toolbar at the top of the
screen.

![Operator Console image 368](./images/starwatch-sms-user-guide-operator-console-rev-6_368.png)

Next, select any point in the list that you would like to display by clicking on it. The *Device Details*
pane located on the right side of the screen will become populated with information related to the
selected point.

![Operator Console image 369](./images/starwatch-sms-user-guide-operator-console-rev-6_369.png)

In the example below, we are viewing details for the *Building 2, Door 2* point within the *Airport Panel*
device.

![Operator Console image 370](./images/starwatch-sms-user-guide-operator-console-rev-6_370.png)

![Operator Console image 371](./images/starwatch-sms-user-guide-operator-console-rev-6_371.png)

![Operator Console image 372](./images/starwatch-sms-user-guide-operator-console-rev-6_372.png)

Note: Using the drop-down lists provided for the parameters at the bottom of the *Device Details* pane,
the user can attach an *Alarm Procedure*, *Camera*, or *Preset* to the device point and/or switch the video
view to the point. The user also can set the system to capture a recorded video when an alarm occurs
at the point by clicking the *Capture Video* checkbox.

![Operator Console image 373](./images/starwatch-sms-user-guide-operator-console-rev-6_373.png)

The
button at the top of the *Device* window enables the user to add more information to the
displayed list of devices. Clicking this button calls up a list of additional column options that can be
selected and added to the grid.

![Operator Console image 374](./images/starwatch-sms-user-guide-operator-console-rev-6_374.png)

Note: columns can be dragged left or right to change their location in the grid and can be filtered to
show only the information most relevant to the user (see section 1.2.5 GRID CONTROLS).

![Operator Console image 375](./images/starwatch-sms-user-guide-operator-console-rev-6_375.png)

Clicking the
button will update the device list to include the latest changes to the system that
have occurred since the *Devices* window was opened.

![Operator Console image 376](./images/starwatch-sms-user-guide-operator-console-rev-6_376.png)

## 3.2 ISSUING COMMANDS TO DEVICES

Using the *Devices* window, you can issue commands to the various access points in the system when
needed. For example, if the access point is a door, you can directly control its operation in response to
a live situation. For example, you can lock or unlock the door when a registered person has forgotten
his/her card or to allow an approved visitor inside the building.

![Operator Console image 377](./images/starwatch-sms-user-guide-operator-console-rev-6_377.png)

To issue a command, click on an alarm point or device to select it and right-click to open the options
menu. From the list, select *Control* to open up the command menu for the selected point or device.
Note: the list of command options presented will vary depending on the type of point or device
selected.

![Operator Console image 378](./images/starwatch-sms-user-guide-operator-console-rev-6_378.png)

The user can also click the
icon in the upper right of the *Devices* window to open the command
menu for the currently selected device. Alternately, the user can open up the command menu by
double-clicking in the selected device/point row.

![Operator Console image 379](./images/starwatch-sms-user-guide-operator-console-rev-6_379.png)

![Operator Console image 380](./images/starwatch-sms-user-guide-operator-console-rev-6_380.png)

Next, select a command from the presented options to execute the command action.

![Operator Console image 381](./images/starwatch-sms-user-guide-operator-console-rev-6_381.png)

Once you have completed your commands, you can exit the window by clicking the
button.

![Operator Console image 382](./images/starwatch-sms-user-guide-operator-console-rev-6_382.png)

## 3.2.1 DOOR COMMANDS

When issuing a command for a *Door*, the following menu options will be available:

![Operator Console image 383](./images/starwatch-sms-user-guide-operator-console-rev-6_383.png)

## Name

## Icon

## Description

*Releases* the access point from a forced state.

![Operator Console image 384](./images/starwatch-sms-user-guide-operator-console-rev-6_384.png)

Release

![Operator Console image 385](./images/starwatch-sms-user-guide-operator-console-rev-6_385.png)

*Enables* that a *PIN* is required for the access point.
Enable PIN
*Disables* that a *PIN* is required for the access point.

![Operator Console image 386](./images/starwatch-sms-user-guide-operator-console-rev-6_386.png)

Disable PIN
*Locks* the access point until it is released.

![Operator Console image 387](./images/starwatch-sms-user-guide-operator-console-rev-6_387.png)

Lock
Returns the access point to *Normal* operating status.

![Operator Console image 388](./images/starwatch-sms-user-guide-operator-console-rev-6_388.png)

Normal

![Operator Console image 389](./images/starwatch-sms-user-guide-operator-console-rev-6_389.png)

*Unlocks* the access point until the operator issues the *Lock* or
Unlock
*Normal* command.

![Operator Console image 390](./images/starwatch-sms-user-guide-operator-console-rev-6_390.png)

## 3.2.2 BREAK GLASS COMMANDS

When issuing a command for a *Break* *Glass* point, the following menu options will be available:

![Operator Console image 391](./images/starwatch-sms-user-guide-operator-console-rev-6_391.png)

![Operator Console image 392](./images/starwatch-sms-user-guide-operator-console-rev-6_392.png)

## 3.2.3 PANEL COMMANDS

When issuing a command for a *Panel*, the following menu options will be available:

![Operator Console image 393](./images/starwatch-sms-user-guide-operator-console-rev-6_393.png)

**Name**
**Icon**
**Description**
Enable
*Enables* connection and communication to the panel.

![Operator Console image 394](./images/starwatch-sms-user-guide-operator-console-rev-6_394.png)

Disable
*Disables* connection and communication to the panel.

![Operator Console image 395](./images/starwatch-sms-user-guide-operator-console-rev-6_395.png)

Refresh
Forces an immediate scan to *Refresh* the current status.

![Operator Console image 396](./images/starwatch-sms-user-guide-operator-console-rev-6_396.png)

Update
Forces an immediate *Update* of any pending configuration or

![Operator Console image 397](./images/starwatch-sms-user-guide-operator-console-rev-6_397.png)

access control.
Restore
*Restores* all configuration and access control information.

![Operator Console image 398](./images/starwatch-sms-user-guide-operator-console-rev-6_398.png)

Factory Reset
*Factory resets* to the default configuration and wipes all access

![Operator Console image 399](./images/starwatch-sms-user-guide-operator-console-rev-6_399.png)

control information.

![Operator Console image 400](./images/starwatch-sms-user-guide-operator-console-rev-6_400.png)

## 3.3 CREATING/UPDATING A DEVICE VIEW

The *Devices* window can be customized to suit the needs of the user. You can create new views, share
views with other operators, update an existing view, or display details about a zone and access points.
To create a new device *View*, open the *Devices* window and modify the on-screen view, as needed.

![Operator Console image 401](./images/starwatch-sms-user-guide-operator-console-rev-6_401.png)

![Operator Console image 402](./images/starwatch-sms-user-guide-operator-console-rev-6_402.png)

For example, you can group devices by *Device Zone* or any other column parameter to create a new
view. In our example, we will group by device. To group by device, simply click on the *Device* column
header and drag it to the *Drag a column header here to group by that column* area.

![Operator Console image 403](./images/starwatch-sms-user-guide-operator-console-rev-6_403.png)

The resulting view will display the information according to device.

![Operator Console image 404](./images/starwatch-sms-user-guide-operator-console-rev-6_404.png)

![Operator Console image 405](./images/starwatch-sms-user-guide-operator-console-rev-6_405.png)

You can also group by multiple column headers at the same time, such as grouping by devices, zones,
and names in the same view. Simply click and drag each column header and drag it to the *Drag a*
*column header here to group by that column* area in succession. The device view will display the
information in a tree format.

![Operator Console image 406](./images/starwatch-sms-user-guide-operator-console-rev-6_406.png)

Note: see section 1.2.5 GRID CONTROLS for more details on setting up and modifying your grid.

![Operator Console image 407](./images/starwatch-sms-user-guide-operator-console-rev-6_407.png)

Once you have configured your device view to suit your needs, the next step is to add the *View* to the
system database.

![Operator Console image 408](./images/starwatch-sms-user-guide-operator-console-rev-6_408.png)

In the top left of the *Devices* window, click the
button. The new *View* will be added with an auto-
generated name.

![Operator Console image 409](./images/starwatch-sms-user-guide-operator-console-rev-6_409.png)

![Operator Console image 410](./images/starwatch-sms-user-guide-operator-console-rev-6_410.png)

Click the
button to save the *View*.

![Operator Console image 411](./images/starwatch-sms-user-guide-operator-console-rev-6_411.png)

To rename the *View*, type a new name in the *View* field at the top left of the workspace.

![Operator Console image 412](./images/starwatch-sms-user-guide-operator-console-rev-6_412.png)

![Operator Console image 413](./images/starwatch-sms-user-guide-operator-console-rev-6_413.png)

Click the
button to push the name change to the system.

![Operator Console image 414](./images/starwatch-sms-user-guide-operator-console-rev-6_414.png)

You can update the configuration of a device *View* by calling it to the screen using the *View* drop-down
list provided in the *View* field. Once you have made changes to the on-screen layout, such as moving
columns or grouping by specific categories, you can save it for future use.

![Operator Console image 415](./images/starwatch-sms-user-guide-operator-console-rev-6_415.png)

Click the
button to save the modified *View*.

![Operator Console image 416](./images/starwatch-sms-user-guide-operator-console-rev-6_416.png)

Click the
button to push the layout changes to the system.

![Operator Console image 417](./images/starwatch-sms-user-guide-operator-console-rev-6_417.png)

## 3.4 DELETING A DEVICE VIEW

To delete a device *View*, call it to the screen using the *View* drop-down list provided in the *View* field.

![Operator Console image 418](./images/starwatch-sms-user-guide-operator-console-rev-6_418.png)

The selected *View* will be displayed.

![Operator Console image 419](./images/starwatch-sms-user-guide-operator-console-rev-6_419.png)

![Operator Console image 420](./images/starwatch-sms-user-guide-operator-console-rev-6_420.png)

Next, click the
button in the top left of the *Devices* window. The *View* will be permanently
removed from the list.

![Operator Console image 421](./images/starwatch-sms-user-guide-operator-console-rev-6_421.png)

## 3.5 SHARING A DEVICE VIEW

When you share a device view, you are sharing it globally with any other system users.
To share a device *View* with other operators, call it to the screen using the *View* drop-down list
provided in the *View* field.

![Operator Console image 422](./images/starwatch-sms-user-guide-operator-console-rev-6_422.png)

The selected *View* will be displayed.

![Operator Console image 423](./images/starwatch-sms-user-guide-operator-console-rev-6_423.png)

![Operator Console image 424](./images/starwatch-sms-user-guide-operator-console-rev-6_424.png)

![Operator Console image 425](./images/starwatch-sms-user-guide-operator-console-rev-6_425.png)

Next, click the
button in the top left of the *Devices* window. The icon will turn green
to
indicate that this *View* has been shared with other users.

---

*© DAQ Electronics, LLC*
