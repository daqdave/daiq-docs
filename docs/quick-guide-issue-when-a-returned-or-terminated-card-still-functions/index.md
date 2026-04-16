---
layout: default
title: "Issue: When a Returned/Terminated Card Still Functions"
nav_order: 370
---

# Issue: When a Returned/Terminated Card Still Functions

![Issue: When a Returned/Terminated Card Still Functions image 01](./images/quick-guide-issue-when-a-returned-or-terminated-card-still-functions_01.png)

Within *StarWatch SMS*, system operators have occasionally experienced an issue in their initial setup
and testing phase where cards that have been set to the *Returned* or *Terminated* condition still
function as normal, giving access to previously assigned zones. This problem is easy to diagnose, but
more difficult to fix within the software code.
Example: an operator sets a card to have *Full Access* permissions and then successfully tests
the card at a given zone. When the operator then sets the card to *Returned*, the card still
provides access to the zone, even though the card is no longer displayed in the active system as
a usable/assignable card. Subsequently setting the card to the *Terminated* condition has the
same results. The only way to disable the card is to change the access permission level to *No*
*Access*.
Explanation: When a site is using *Permitted Credentials* to download card information from the
database to an associated *RADC*, the system gets caught in an unusual dilemma. When an
operator sets a card to the *Returned* or *Terminated* condition, the system believes the card is
no longer permitted in the zone and thus blocks any new information about the card from being
downloaded to the zone – including its new condition of *Returned* or *Terminated*. This is
obviously a problem, as the system needs to delete the card before beginning to ignore it. With
no new information, the zone still acts as though the card has access permissions.

![Issue: When a Returned/Terminated Card Still Functions image 02](./images/quick-guide-issue-when-a-returned-or-terminated-card-still-functions_02.png)

Solution: As DAQ works on a permanent software solution, a simple operator workflow change
will correct this issue. When going through the process of returning cards, the operator should
*Suspend* the card before setting any other condition. This will cause the card to stop having
access in the panel. The operator can then set the card to the *Returned*, *Retired*, or
*Terminated* condition within the system. In this manner, the zone will receive the message
that the card is no longer permitted before the new status information is blocked, and the card
will no longer provide access.

---

*© DAQ Electronics, LLC*
