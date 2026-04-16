---
layout: default
title: Typical Configuration Errors When Using RPI Driver
nav_order: 390
---

# Typical Configuration Errors When Using RPI Driver

![Typical Configuration Errors When Using RPI Driver image 01](./images/quick-guide-typical-config-errors-when-using-rpi-driver_01.png)

## Typical Configuration Errors

These errors were found on an upgraded system and should have been corrected prior to further
commissioning of zones. The screenshots were taken from the backup after it was reported that the
system had been checked for configuration errors by the installer.

![Typical Configuration Errors When Using RPI Driver image 02](./images/quick-guide-typical-config-errors-when-using-rpi-driver_02.png)

## Remote SCIF RADC Channel

In the following example, the remote RADC in BLDG 93A SCIF is configured as a PMUX when it should be
“Serial Class B”.

![Typical Configuration Errors When Using RPI Driver image 03](./images/quick-guide-typical-config-errors-when-using-rpi-driver_03.png)

![Typical Configuration Errors When Using RPI Driver image 04](./images/quick-guide-typical-config-errors-when-using-rpi-driver_04.png)

## PMUX and RADC Sharing Same Port

In the following example, Station 65A is a remote SCIF RADC and it is assigned to COM8, the same port
used by MUX1 to MUX8.

![Typical Configuration Errors When Using RPI Driver image 05](./images/quick-guide-typical-config-errors-when-using-rpi-driver_05.png)

![Typical Configuration Errors When Using RPI Driver image 06](./images/quick-guide-typical-config-errors-when-using-rpi-driver_06.png)

## Invalid or Unknown Com Ports

In the following example, COM0 was somehow configured. This should not cause a problem, but it is
recommended to set any station that is not assigned yet to a valid com port to “None”.

![Typical Configuration Errors When Using RPI Driver image 07](./images/quick-guide-typical-config-errors-when-using-rpi-driver_07.png)

SCIF Computer Using PMUX Remote Station Address
In the following example, a SCIF computer is assigned to a station address greater than 128 and,
therefore, it must be connected to a PMUX.

![Typical Configuration Errors When Using RPI Driver image 08](./images/quick-guide-typical-config-errors-when-using-rpi-driver_08.png)

![Typical Configuration Errors When Using RPI Driver image 09](./images/quick-guide-typical-config-errors-when-using-rpi-driver_09.png)

## Remote Station has Incorrect Channel

In the example below, a remote station connected to a PMUX should have the channel type “Serial
Class B”.

![Typical Configuration Errors When Using RPI Driver image 10](./images/quick-guide-typical-config-errors-when-using-rpi-driver_10.png)

## Invalid Station Addresses

Station addresses below 129 must be in the range 1 to 126. The following addresses are illegal in RPI
and will cause communication errors: Station 0, Station 127, and Station 128 (all impossible addresses).

![Typical Configuration Errors When Using RPI Driver image 11](./images/quick-guide-typical-config-errors-when-using-rpi-driver_11.png)

![Typical Configuration Errors When Using RPI Driver image 12](./images/quick-guide-typical-config-errors-when-using-rpi-driver_12.png)

## Inconsistent Remote Station Port

Stations that are attached to a PMUX should be assigned to the same serial port as their parent PMUX
serial port or assigned to “None”. On systems running on 5.3.462 or greater, this setting can be “None”
for all remote stations and the station will automatically be attached to the correct PMUX.

![Typical Configuration Errors When Using RPI Driver image 13](./images/quick-guide-typical-config-errors-when-using-rpi-driver_13.png)

## Missing PMUX Station

The station address below is configured as 2305 (PMUX 18, Remote Station 1) however no PMUX 18
exists in the database. This example was not found on the upgraded system, but was made up as
another example of a typical error.

![Typical Configuration Errors When Using RPI Driver image 14](./images/quick-guide-typical-config-errors-when-using-rpi-driver_14.png)

---

*© DAQ Electronics, LLC*
