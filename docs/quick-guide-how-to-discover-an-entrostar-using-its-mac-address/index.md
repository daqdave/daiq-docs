---
layout: default
title: How to Discover an EntroStar Using Its Mac Address
nav_order: 160
---

# How to Discover an EntroStar Using Its Mac Address

![How to Discover an EntroStar Using Its Mac Address image 01](./images/quick-guide-how-to-discover-an-entrostar-using-its-mac-address_01.png)

![How to Discover an EntroStar Using Its Mac Address image 02](./images/quick-guide-how-to-discover-an-entrostar-using-its-mac-address_02.png)

Using the discovery capabilities within *StarWatch SMS*, installed EntroStar panels can be automatically
found and recognized by the system. This can be accomplished using either the network tools within
the *Site Planner* application or via the BACnet browser.
If you experience trouble getting the panel to be recognized, there are several options to try before
sending in for repair. If your EntroStar is running on any 1.4.x version, you can try resetting the panel
via the USB port feature. You will need a DAQ-provided USB drive that is formatted for FAT32 and has a
file called "entrostar.cmd" on it containing a single line of text "factory,reset".
Alternately, a good way to find a panel in Wireshark is to set up a Mac address filter for the panel and
power it on to see what network traffic or IP state it is in.

![How to Discover an EntroStar Using Its Mac Address image 03](./images/quick-guide-how-to-discover-an-entrostar-using-its-mac-address_03.png)

The screenshot below shows a way to filter and capture a single EntroStar using its Mac address. Note
that the Mac address filter requires the first three parts to be "00:04:a3", then simply add the last six
digits of the serial number. So for a serial ending in 447BCF, the Mac address filter would be
"00:04:a3:44:7b:cf".

![How to Discover an EntroStar Using Its Mac Address image 04](./images/quick-guide-how-to-discover-an-entrostar-using-its-mac-address_04.png)

![How to Discover an EntroStar Using Its Mac Address image 05](./images/quick-guide-how-to-discover-an-entrostar-using-its-mac-address_05.png)

---

*© DAQ Electronics, LLC*
