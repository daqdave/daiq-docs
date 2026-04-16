---
layout: default
title: EntroStar FAQ — Frequently Asked Questions
nav_order: 510
---

# EntroStar FAQ — Frequently Asked Questions

![Entrostar FAQ Frequently Asked Questions image 01](./images/entrostar-faq-frequently-asked-questions-4_01.png)

## 1.0 SPECIFICATIONS

## 1.1 CAPABILITY

**Q.**
**What readers can I use on the EntroStar?**
A.
Any wiegand compatible reader including all forms of biometric. Please note that newer HID
Multi-Class SE readers can each draw as much as 3W for short periods of time and may cause
issues with systems using PoE supplies. If these readers are to be used, it is suggested to either
connect a 12 volt battery to the EntroStar unit, or power it via PoE+, or a conventional 12V
supply (e.g. EN-DC-0003P).
**Q.**
**What is the card capacity of EntroStar?**
A.
There are no fixed capacities within the EntroStar unit and the limits will depend on how many
access rights, actions etc. but potentially 1m+.
**Q.**
**Does EntroStar support 4-state monitoring of alarm inputs?**
A.
Yes, the 3 door contact inputs for each door and the 3 auxiliary inputs are all supervised
(tamper protected). Note that the Enclosure tamper input is 2 state only.
**Q.**
**Does the break glass monitor input unlock the door when in alarm?**
A.
No, the input is for monitoring DPDT break glass units only. Wire the lock through the break
glass unit to drop power to the lock.

![Entrostar FAQ Frequently Asked Questions image 02](./images/entrostar-faq-frequently-asked-questions-4_02.png)

## 1.2 COMMUNICATIONS

**Q.**
**Can EntroStar talk to any BACnet master station?**
A.
Yes, if that master fully supports ANSI/ASHRAE 135-2010.
**Q.**
**Can an EntroStar talk to more than one master station?**
A.
Yes, BACnet supports multiple subscribers.
**Q.**
**If I lose communications to the EntroStar what happens?**
A.
All events are buffered with local time stamping for subsequent upload.

## 2.0 INSTALLATION

**Q.**
**Can EntroStar be installed on a network with fixed IP addresses?**
A.
No, EntroStar will look for a DHCP server by default. If it fails to find one, EntroStar will assign
itself a unique private IP address.
**Q.**
**Can EntroStar units be installed in different time zones?**
A.
Yes, an advanced setting specifies a UTC offset for the EntroStar.
**Q**
**How do I connect a non RJ45 reader to EntroStar?**
A.
Use the RJ45/terminal block adapter and then std. CAT5 cable.

![Entrostar FAQ Frequently Asked Questions image 03](./images/entrostar-faq-frequently-asked-questions-4_03.png)

**Q**
**Do I need to use the Input Terminator Units (ITU) provided when connecting input devices**
**to the EntroStar?**
A.
Yes. All the inputs on the EntroStar, with the exception of the enclosure tamper switch, are
supervised/tamper protected and an ITU must always be used.

## 3.0 POWER

**Q.**
**Do I have to power EntroStar over PoE/PoE+?**
A.
No, an optional 12vPSU with/without battery can be specified.
**Q.**
**If I choose PoE/PoE+ can I still connect a battery?**
A.
Yes, the PoE/PoE+ supply will actually trickle charge the battery.
**Q.**
**Do I need PoE+ to control 2 magnetic locks?**
A.
It depends on the lock. Some newer magnetic locks draw as little as 3.6W. Each EntroStar can
provide up to 9.3W via PoE to power external devices (locks and readers) and up to 24.9W via
PoE+.
**Q.**
**What happens to my card/access data if I lose power to the EntroStar?**
A.
All card/access data is held in non-volatile memory.

![Entrostar FAQ Frequently Asked Questions image 04](./images/entrostar-faq-frequently-asked-questions-4_04.png)

**Q.**
**Why won’t my EnstroStar unit power from a 12VDC battery?**
A.
For the EntroStar power supply and battery, the battery back-up will only work when it
switches over from mains power.  If you have powered up the unit and then lose power, the
battery will take over.  You cannot just connect a battery and turn the unit on. This is because
the unit disconnects the battery from the circuit when the battery gets too low.  Therefore,
when the unit is powered off and there is NO BATTERY, the battery circuit gets disconnected as
there are 0 volts present on the battery line. When the mains power is present, the battery
circuit is connected.  When the mains power disappears, the battery will take over.  After the
battery drains to a certain level, the board will disconnect the battery from the unit.  It will
not reconnect that circuit until mains is reapplied.

## 4.0 MISCELLANEOUS

**Q.**
**If I configure my system to support simple 56 bit, 32 bit, or 16 bit card numbers, my PINs**
**don’t work?**
A.
Upgrade your EntroStar firmware to V1.2 or later.
**Q.**
**How many attempts do I get to enter my PIN?**
A.
EntroStar supports a rolling PIN that will allow up to two initial incorrect numbers to be
entered.

---

*© DAQ Electronics, LLC*
