---
layout: default
title: EntroStar USB Function
nav_order: 530
---

# EntroStar USB Function

![EntroStar USB Function image 01](./images/starwatch-sms-supplement-entrostar-usb-function-rev-1_01.png)

## 1.0 INTRODUCTION

When the EntroStar panel is in a state in which it is not configurable, a method is needed to physically
restore the panel to a known state.
The cases so far identified that could lead to this condition include the following:

A panel used on one system that has a password that is unknown that would make it impossible
to change the network settings or associate the panel with another system if that panel needs
to be re-used.

A panel that has network settings that make it difficult to discover or unreachable.

A panel that is not working properly because it is in a bad state related to its use and state of
the internal memory and database.
The physical method for restoring a panel is to use the USB interface. This document describes the
requirements and design solution for this method.

![EntroStar USB Function image 02](./images/starwatch-sms-supplement-entrostar-usb-function-rev-1_02.png)

## 2.0 METHOD

The method for restoring a panel shall adhere to the following practice and steps:

### Step 1:

Find a spare USB thumb drive. A formatted USB drive is required (most are already
formatted as FAT32) and inserted into a PC USB port.

### Step 2:

Save a command text file. A special text file should be saved (copied) to the USB drive in the
root of the drive. Details of this text file to be proposed in the design section.

### Step 3:

Power off the EntroStar panel. The EntroStar panel should be powered off by removing the
power connector or supply. In the case of POE, remove the network cable.

### Step 4:

Insert the USB drive. The USB drive containing the special text file must be inserted into the
EntroStar panel.

### Step 5:

Power on the EntroStar panel. The EntroStar panel should be powered on and during startup
it shall detect the USB drive and special file and act accordingly.

![EntroStar USB Function image 03](./images/starwatch-sms-supplement-entrostar-usb-function-rev-1_03.png)

## 3.0 REQUIREMENTS


A USB drive shall be used and formatted as FAT32.

A text file shall be copied to the USB drive in the root folder.

The text file shall be called entrostar.cmd and the file shall contain lines of text that provide
instructions on what to do during the startup and restore process.

The text file shall contain ASCII UTF-8 characters only where each byte of the file represents a
single character in the ASCII character set in the range of values from 0 to 127.

Each line of text shall begin with a command name followed by a list of arguments that are
comma delimited.

Each line of text shall be terminated with both ASCII characters CR and LF to indicate end of
line.

Each line of text shall represent a single command.

The text file shall be read one line at a time and each line shall be interpreted and invoked
before reading the next line.

One command shall simply start a factory reset of the panel so that it restarts.

To provide positive confirmation of results, a log file shall be written containing time stamped
log entries for actions invoked and successful actions where possible.

![EntroStar USB Function image 04](./images/starwatch-sms-supplement-entrostar-usb-function-rev-1_04.png)

## 3.1 ENTROSTAR.CMD

The file “entrostar.cmd” will be used to invoke commands from a USB on startup of the EntroStar
panel. The names of the commands shall not be case sensitive. If and when defined arguments to
specific commands may or may not require case sensitive values.

## 3.2 ENTROSTAR.LOG

The file “entrostar.log” will be used to write log entries (one per line) of text including a time stamp.
If the file does not exist, it should be created and after all log entries shall be appended to the log file
as new lines. Each write to the file shall be flushed (and closed if needed) so that when the USB drive
is removed, the file should contain all the most recent log entries.

## 3.3 LOG FILE TEXT FORMAT

The log file format shall be written as:
<YYYY/MM/DD HH:MM:SS,<function>,<status>,<information>
The function part can be any named function in the panel, as needed. The status part should be one of
the following:
‘ok’,’success’,’fail’,’not permitted’,’error’,’good’
Information should be relevant and helpful to the relevant function.

![EntroStar USB Function image 05](./images/starwatch-sms-supplement-entrostar-usb-function-rev-1_05.png)

## 4.0 STARTUP

## 4.1 USB DRIVE

On startup, the EntroStar shall detect the presence of the USB drive and if found shall mount the drive
as a file system for reading the entrostar.cmd file and for writing the entrostar.log file.

## 4.2 COMMAND FILE

After reading the root of the mounted USB drive, if the file entrostar.cmd is found an entry shall be
written to the log indicating the presence or not of the file.
2015/08/05 15:23:15,USB,ok,entrostar.cmd file found
2015/08/05 15:23:15,USB,ok,entrostar.cmd file not found

## 5.0 FACTORY RESET COMMAND

The command to factory reset any panel shall be encoded as “factory,reset” on one line. The factory
reset command shall rename the entrostar.cmd file to prevent the panel cycling through a factory
reset each time the panel starts. The entrostar.cmd file shall be renamed to entrostar.old.
The following log entries shall be recorded for a factory reset:

Initiated - prior to invoking the factory reset sequence, the following shall be written to the log
file:
2015/08/05 15:23:15,Command,ok,Factory reset requested

![EntroStar USB Function image 06](./images/starwatch-sms-supplement-entrostar-usb-function-rev-1_06.png)

## 6.0 FUTURE REQUIREMENTS

Other commands could be added in future to:

Change IP settings of any panel or a specific panel with a known serial number.

Enable/disable putty.

Reset the IP config password back to default.

Backup the database to the USB drive.

---

*© DAQ Electronics, LLC*
