---
layout: default
title: New EntroStar PICS
nav_order: 570
---

# New EntroStar PICS

![New Entrostar PICS image 01](./images/new-entrostar-pics_01.png)

## 1.0 INTRODUCTION

## 1.1 ABOUT THIS DOCUMENT

This is the PICS (Protocol Implementation Conformance Statement) for the BACnet® protocol used by
EntroStar™. The PICS is based on ANSI/ASHRAE Standard 135-2010 and uses the layout given in Annex A
of this standard.

## 1.2 NOTATION

The following notation is used throughout the PICS:
 = ‘Supported’ or ‘Yes’
 = ‘Not supported’ or ‘No’.

![New Entrostar PICS image 02](./images/new-entrostar-pics_02.png)

## 2.0 PICS

## 2.1 GENERAL


Date: January 31, 2019

Vendor Name: DAQ Electronics, LLC

Product Name: EntroStar

Product Model Number: EN-DC-0001P

EntroStar Software Version: 3.0 and onwards

BACnet Protocol Revision: 13

Product Description: EntroStar is a two-door, PoE+ enabled access control and alarm
management panel. It uses a Linux kernel and SQLite database for scalable performance. It
supports up to four readers across the two doors, for example an entry and exit reader on each
door.

![New Entrostar PICS image 03](./images/new-entrostar-pics_03.png)

## 2.2 BACNET STANDARDIZED DEVICE PROFILE

   BACnet Operator Workstation (B-OWS)
   BACnet Advanced Operator Workstation (B-AWS)
   BACnet Operator Display (B-OD)
   BACnet Building Controller (B-BC)
   BACnet Advanced Application Controller (B-AAC)
   BACnet Application Specific Controller (B-ASC)
   BACnet Smart Sensor (B-SS)
   BACnet Smart Actuator (B-SA)

![New Entrostar PICS image 04](./images/new-entrostar-pics_04.png)

## 2.3 BACNET INTEROPERABILITY BUILDING BLOCKS (BIBBs)

## 2.3.1 DATA SHARING

## BIBB

## Name

## Supported

DS-RP-A
Read Property

DS-RP-B
Read Property

DS-RPM-A
Read Property Multiple

DS-RPM-B
Read Property Multiple

DS-WP-A
Write Property

DS-WP-B
Write Property

DS-WPM-A
Write Property Multiple

DS-WPM-B
Write Property Multiple

DS-COV-A
COV Subscribe

DS-COV-B
COV Subscribe

DS-COVP-A
COV Property Subscribe

DS-COVP-B
COV Property Subscribe

DS-COVU-A
COV Unsolicited

DS-COVU-B
COV Unsolicited

DS-V-A
View

DS-AV-A
Advanced View

DS-M-A
Modify

DS-AM-A
Advanced Modify


![New Entrostar PICS image 05](./images/new-entrostar-pics_05.png)

## 2.3.2 ALARM AND EVENT MANAGEMENT

## BIBB

## Name

## Supported

AE-N-A
Event Notification

AE-N-I-B
Event Notification (Internal)

AE-N-E-B
Event Notification (External)

AE-ACK-A
Acknowledge Alarm

AE-ACK-B
Acknowledge Alarm

AE-ASUM-A
Alarm Summary

AE-ASUM-B
Alarm Summary

AE-ESUM-A
Enrolment Summary

AE-ESUM-B
Enrolment Summary

AE-INFO-A
Event Information

AE-INFO-B
Event Information

AE-LS-A
Life Safety

AE-LS-B
Life Safety

AE-VN-A
View Notification

AE-AVN-A
Advanced View Notification

AE-VM-A
View and Modify

AE-AVM-A
Advanced View and Modify

AE-AS-A
Alarm Summary View

AE-ELV-A
Event Log View

AE-ELVM-A
Event Log View and Modify

AE-EL-I-B
Event Log (Internal)

AE-EL-E-B
Event Log (External)

AE-NF-B
Notification Forwarder

AE-NF-I-B
Notification Forwarder (Internal)


![New Entrostar PICS image 06](./images/new-entrostar-pics_06.png)

## 2.3.3 SCHEDULING

## BIBB

## Name

## Supported

SCHED-A
Scheduling

SCHED-I-B
Scheduling (Internal)

SCHED-E-B
Scheduling (External)

SCHED-R-B
Scheduling (ReadOnly)

SCHED-AVM-A
Advanced View and Modify

SCHED-VM-A
View and Modify

SCHED-WS-A
Weekly Schedule

SCHED-WS-I-B
Weekly Schedule (Internal)


![New Entrostar PICS image 07](./images/new-entrostar-pics_07.png)

## 2.3.4 DEVICE MANAGEMENT

## BIBB

## Name

## Supported

DM-DDB-A
Dynamic Device Binding

DM-DDB-B
Dynamic Device Binding

DM-DOB-A
Dynamic Object Binding

DM-DOB-B
Dynamic Object Binding

DM-DCC-A
Device Communications Control

DM-DCC-B
Device Communications Control

DM-TM-A
Text Message

DM-TM-B
Text Message

DM-TS-A
Time Synchronization

DM-TS-B
Time Synchronization

DM-UTC-A
UTC Time Synchronization

DM-UTC-B
UTC Time Synchronization

DM-RD-A
Re-initialize Device

DM-RD-B
Re-initialize Device

DM-BR-A
Backup and Restore

DM-BR-B
Backup and Restore

DM-R-A
Restart (Indication)

DM-R-B
Restart (Indication)

DM-LM-A
List Manipulation

DM-LM-B
List Manipulation

DM-OCD-A
Object Create and Delete

DM-OCD-B
Object Create and Delete

DM-VT-A
Virtual Terminal

DM-VT-B
Virtual Terminal

DM-ANM-A
Automatic Network Mapping

DM-ADM-A
Automatic Device Mapping

DM-ATS-A
Automatic Time Synchronization

DM-MTS-A
Manual Time Synchronization


![New Entrostar PICS image 08](./images/new-entrostar-pics_08.png)

## 2.3.5 NETWORK MANAGEMENT

## BIBB

## Name

## Supported

NM-CE-A
Connection Establishment

NM-CE-B
Connection Establishment

NM-RC-A
Router Configuration

NM-RC-B
Router Configuration


## 2.3.6 NETWORK SECURITY

## BIBB

## Name

## Supported

NS-SD
Secure Device

NS-ED
Encrypted Device

NS-MAD
Multi Application Device

NS-DMK-A
Device Master Key

NS-DMK-B
Device Master Key

NS-KS
Key Server

NS-TKS
Temporary Key Server

NS-SR
Secure Router

NS-SP
Secure Proxy


## 2.4 SEGMENTATION CAPABILITY

  Able to transmit segmented messages
Windows size: 4
  Able to receive segmented messages
Windows size: 4

![New Entrostar PICS image 09](./images/new-entrostar-pics_09.png)

## 2.5 STANDARD OBJECT TYPES

## 2.5.1 ‘ACCESS CREDENTIAL’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Description

Global_Identifier

Status_Flags

Reliability

Credential_Status

Reason_For_Disable

Authentication_Factors

Activation_Time

Expiry_Time

Credential_Disable

Days_Remaining

Uses_Remaining

Absentee_Limit

Belongs_To

Assigned_Access_Rights

Last_Access_Point

Last_Access_Event


![New Entrostar PICS image 10](./images/new-entrostar-pics_10.png)

Last_Use_Time

Trace_Flag

Threat_Authority

Extended_Time_Enable

Authorization_Exemptions

Profile_Name

*PROPRIETARY PROPERTIES*
Disabled_Date_Time:
**ID**
8165
Timestamp when a credential was locked due to consecutive
**Meaning**
invalid PIN entries
**Data Type**
BACnetDateTime

## Writeable


Invaild_Pin_Count:
**ID**
8164
How many times an invalid PIN has been entered consecutively for
**Meaning**
a credential
**Data Type**
Unsigned

## Writeable



![New Entrostar PICS image 11](./images/new-entrostar-pics_11.png)

## 2.5.2 ‘ACCESS DOOR’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Present_Value

Description

Status_Flags

Event_State

Reliability
*
Out_Of_Service

Priority_Array

Relinquish_Default

Door_Status
*
Lock_Status
*
Secured_Status

Door_Members

Door_Pulse_Time

Door_Extended_Pulse_Time

Door_Unlock_Delay_Time

Door_Open_Too_Long_Time

Door_Alarm_State
*
Masked_Alarm_Values

Maintenance_Required


![New Entrostar PICS image 12](./images/new-entrostar-pics_12.png)

Time_Delay

Notification_Class

Alarm_Values

Fault_Values

Event_Enable

Acked_Transitions

Notify_Type

Event_Time_Stamps

Event_Detection_Enable

Profile_Name

*Writable when out of service; otherwise read-only.
*PROPRIETARY PROPERTIES*
Active_Command_Priority:
**ID**
8163

## Meaning

Priority of the currently active command

## Data Type

Unsigned

## Writeable


Auto_Airlock_Unlock_Delay_Period:
**ID**
8007
Timeperiod in seconds that must elapse before an automatically
**Meaning**
operated airlock process opens this door after an access operation
at the other door in the airlock
**Data Type**
Unsigned

## Writeable



![New Entrostar PICS image 13](./images/new-entrostar-pics_13.png)

Common_Unlock_Security:
**ID**
8015
Whether or not the common unlock inhibits the common unlock
**Meaning**
operations on this door under off-normal conditions
**Data Type**
Boolean

## Writeable


Door_Strike_Direction:
**ID**
8169
Enables specification of the door strike output to use for
**Meaning**
turnstiles and airlocks
**Data Type**
Enumeration

## Writeable


Drop_Pulse_Unlock:
**ID**
8150

## Meaning

Defines when to drop a 'pulse unlock' door strike

## Data Type

DropPulseUnlock (see Section 2.7.2)

## Writeable


Minimum_Door_Strike_Period:
**ID**
8006

## Meaning

Minimum period in seconds for which the door strike is held

## Data Type

Unsigned

## Writeable



![New Entrostar PICS image 14](./images/new-entrostar-pics_14.png)

## 2.5.3 ‘ACCESS POINT’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Description

Status_Flags

Event_State

Reliability

Out_Of_Service

Authentication_Status

Active_Authentication_Policy

Number_Of_Authentication_Policies

Authentication_Policy_List

Authentication_Policy_Names

Authorization_Mode

Verification_Time

Lockout

Lockout_Relinquish_Time

Failed_Attempts

Failed_Attempt_Events

Max_Failed_Attempts

Failed_Attempts_Time

Threat_Level

Occupancy_Upper_Limit_Enforced


![New Entrostar PICS image 15](./images/new-entrostar-pics_15.png)

Occupancy_Lower_Limit_Enforced

Occupancy_Count_Adjust

Accompaniment_Time

Access_Event

Access_Event_Tag

Access_Event_Time

Access_Event_Credential

Access_Event_Authentication_Factor

Access_Doors

Priority_For_Writing

Muster_Point

Zone_To

Zone_From

Notification_Class

Transaction_Notification_Class

Access_Alarm_Events

Access_Transaction_Events

Event_Enable

Acked_Transitions

Notify_Type

Event_Time_Stamps

Event_Detection_Enable

Profile_Name

*PROPRIETARY PROPERTIES*
Inhibited:
**ID**
8016
Whether or not an access point is inhibited from being used for
**Meaning**
access control
**Data Type**
Boolean

## Writeable



![New Entrostar PICS image 16](./images/new-entrostar-pics_16.png)

## 2.5.4 ‘ACCESS RIGHTS’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Description

Global_Identifier

Status_Flags

Reliability

Enable

Negative_Access_Rules

Positive_Access_Rules

Accompaniment

Profile_Name

*PROPRIETARY PROPERTIES*
None.

![New Entrostar PICS image 17](./images/new-entrostar-pics_17.png)

## 2.5.5 ‘ACCESS USER’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Description

Global_Identifier

Status_Flags

Reliability

User_Type

User_Name

User_External_Identifier

User_Information_Reference

Members

Member_Of

Credentials

Profile_Name


![New Entrostar PICS image 18](./images/new-entrostar-pics_18.png)

*PROPRIETARY PROPERTIES*
Class:
**ID**
8020
Optional classification of access users. The intended use for this is
for users to be granted exit from an access zone only if a user of

## Meaning

class X is present in the access zone. [A practical application of
this is where you want at least one supervisor in a control room at
all times.]
See also the 'Occupancy_Required_Class' proprietary property in
**Data Type**
'Access Zone' (Section 2.5.6).
**Writeable**

Expires_On:
**ID**
8023

## Meaning

Expiry date for device access, for an account

## Data Type

BACnetTimeDate

## Writeable


Home_Directory:
**ID**
8022

## Meaning

User account home directory for a user

## Data Type

CharacterString

## Writeable


Password:
**ID**
8021

## Meaning

User account password for a device account

## Data Type

CharacterString

## Writeable



![New Entrostar PICS image 19](./images/new-entrostar-pics_19.png)

Primary_Group:
**ID**
8024

## Meaning

Object profile to which an object conforms

## Data Type

Unsigned

## Writeable



![New Entrostar PICS image 20](./images/new-entrostar-pics_20.png)

## 2.5.6 ‘ACCESS ZONE’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Description

Global_Identifier

Occupancy_State

Status_Flags

Event_State

Reliability
*
Out_Of_Service

Occupancy_Count
*
Occupancy_Count_Enable

Adjust_Value

Occupancy_Upper_Limit

Occupancy_Lower_Limit

Credentials_In_Zone

Last_Credential_Added

Last_Credential_Added_Time

Last_Credential_Removed

Last_Credential_Removed_Time

Passback_Mode

Passback_Timeout


![New Entrostar PICS image 21](./images/new-entrostar-pics_21.png)

Entry_Points

Exit_Points

Time_Delay

Notification_Class

Alarm_Values

Event_Enable

Acked_Transitions

Notify_Type

Event_Time_Stamps

Event_Detection_Enable

Profile_Name

*Writable when out of service; otherwise read-only.
*PROPRIETARY PROPERTIES*
Antipassback_Time_Range:
**ID**
8158
Reference to a BACnetObjectPropertyReference object. This
**Meaning**
proprietary property defines the timeperiods when anti-passback
is active.
**Data Type**
BACnetObjectPropertyReference

## Writeable


*Exempt_Adjust_Value*:
**ID**
8027
If written with non-zero value, then adjusts the
**Meaning**
'Occupancy_Exempt_Credential_Count' property up and down
accordingly (but not below 0).
If written as '0', then sets the
**Data Type**
'Occupancy_Exempt_Credential_Count' property to '0'.
**Writeable**


![New Entrostar PICS image 22](./images/new-entrostar-pics_22.png)

*Maximum_Occupancy_Alert_Output*:
**ID**
8028
Reference to a Binary Output object. This proprietary property
**Meaning**
operates when the maximum occupancy limits are reached and
relieved.
**Data Type**
BACnetDeviceObjectReference

## Writeable


*Minimum_Occupancy_Alert_Output*:
**ID**
8029
Reference to a Binary Output object. This proprietary property
**Meaning**
operates when the minimum occupancy limits are reached and
relieved.
**Data Type**
BACnetDeviceObjectReference

## Writeable


*Occupancy_Exempt_Credential_Count*:
**ID**
8026

## Meaning

Number of occupancy exempt credentials within an access zone

## Data Type

Unsigned

## Writeable


*Occupancy_Required_Class*:
**ID**
8030
Reference to a Group object. This proprietary property contains a
list of access users or access credentials that identify a collection
**Meaning**
of access objects, at least one of which is required to be a part of
the occupancy of this access zone.
See also the 'Class' proprietary property in 'Access User' (Section
**Data Type**
2.5.5).
**Writeable**


![New Entrostar PICS image 23](./images/new-entrostar-pics_23.png)

*Occupancy_Strict_Minimum*:
**ID**
8031
Whether or not minimum occupancy limits are strictly enforced,
**Meaning**
to deny exit from an access zone
**Data Type**
Boolean

## Writeable



![New Entrostar PICS image 24](./images/new-entrostar-pics_24.png)

## 2.5.7 ‘ANALOG INPUT’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Present_Value
*
Description

Device_Type

Status_Flags

Event_State

Reliability
*
Out_Of_Service

Update_Interval

Units

Min_Pres_Value

Max_Pres_Value

Resolution

COV_Increment

Time_Delay

Notification_Class

High_Limit

Low_Limit

Deadband

Limit_Enable

Event_Enable


![New Entrostar PICS image 25](./images/new-entrostar-pics_25.png)

Acked_Transitions

Notify_Type

Event_Time_Stamps

Event_Detection_Enable

Profile_Name

*Writable when out of service; otherwise read-only.
*PROPRIETARY PROPERTIES*
None.

![New Entrostar PICS image 26](./images/new-entrostar-pics_26.png)

## 2.5.8 ‘ANALOG VALUE’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Present_Value

Description

Status_Flags

Event_State

Reliability

Out_Of_Service

Units

Priority_Array

Relinquish_Default

COV_Increment

Time_Delay

Notification_Class

High_Limit

Low_Limit

Deadband

Limit_Enable

Event_Enable

Acked_Transitions

Notify_Type

Event_Time_Stamps


![New Entrostar PICS image 27](./images/new-entrostar-pics_27.png)

Event_Detection_Enable

Profile_Name

*PROPRIETARY PROPERTIES*
Active_Command_Priority:
**ID**
8163

## Meaning

Priority of the currently active command

## Data Type

Unsigned

## Writeable



![New Entrostar PICS image 28](./images/new-entrostar-pics_28.png)

## 2.5.9 ‘BINARY INPUT’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Present_Value
*
Description

Device_Type

Status_Flags

Event_State

Reliability
*
Out_Of_Service

Polarity

Inactive_Text

Active_Text

Change_Of_State_Time

Change_Of_State_Count

Time_Of_State_Count_Reset

Elapsed_Active_Time

Time_Of_Active_Time_Reset

Time_Delay

Notification_Class

Alarm_Value

Event_Enable


![New Entrostar PICS image 29](./images/new-entrostar-pics_29.png)

Acked_Transitions

Notify_Type

Event_Time_Stamps

Event_Detection_Enable

Profile_Name

*Writable when out of service; otherwise read-only.
*PROPRIETARY PROPERTIES*
Debounce_Period:
**ID**
8140
Timeperiod in milliseconds during which debouncing is applied to
**Meaning**
the binary input, following a state change
**Data Type**
Unsigned

## Writeable



![New Entrostar PICS image 30](./images/new-entrostar-pics_30.png)

## 2.5.10 ‘BINARY OUTPUT’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Present_Value

Description

Device_Type

Status_Flags

Event_State

Reliability
*
Out_Of_Service

Polarity

Inactive_Text

Active_Text

Change_Of_State_Time

Change_Of_State_Count

Time_Of_State_Count_Reset

Elapsed_Active_Time

Time_Of_Active_Time_Reset

Minimum_Off_Time

Minimum_On_Time

Priority_Array

Relinquish_Default


![New Entrostar PICS image 31](./images/new-entrostar-pics_31.png)

Time_Delay

Notification_Class

Feedback_Value

Event_Enable

Acked_Transitions

Notify_Type

Event_Time_Stamps

Event_Detection_Enable

Profile_Name

*Writable when out of service; otherwise read-only.
*PROPRIETARY PROPERTIES*
Active_Command_Priority:
**ID**
8163

## Meaning

Priority of the currently active command

## Data Type

Unsigned

## Writeable


Feedback_Reference:
**ID**
8134
Reference to a Binary Input object. This proprietary property
**Meaning**
represents the feedback value for the controlled state of the
binary output.
**Data Type**
BACnetObjectIdentifier

## Writeable



![New Entrostar PICS image 32](./images/new-entrostar-pics_32.png)

## 2.5.11 ‘BINARY VALUE’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Present_Value

Description

Status_Flags

Event_State

Reliability

Out_Of_Service

Inactive_Text

Active_Text

Change_Of_State_Time

Change_Of_State_Count

Time_Of_State_Count_Reset

Elapsed_Active_Time

Time_Of_Active_Time_Reset

Minimum_Off_Time

Minimum_On_Time

Priority_Array

Relinquish_Default

Time_Delay

Notification_Class

Alarm_Value

Event_Enable

Acked_Transitions


![New Entrostar PICS image 33](./images/new-entrostar-pics_33.png)

Notify_Type

Event_Time_Stamps

Event_Detection_Enable

Profile_Name

*PROPRIETARY PROPERTIES*
Active_Command_Priority:
**ID**
8163

## Meaning

Priority of the currently active command

## Data Type

Unsigned

## Writeable



![New Entrostar PICS image 34](./images/new-entrostar-pics_34.png)

## 2.5.12 ‘CALENDAR’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Description

Present_Value

Date_List

Profile_Name

*PROPRIETARY PROPERTIES*
None.

![New Entrostar PICS image 35](./images/new-entrostar-pics_35.png)

## 2.5.13 ‘COMMAND’

*GENERAL*
  Creatable (for Object_Identifier > 4)
  Deletable (for Object_Identifier > 4)
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Description

Present_Value

In_Process

All_Writes_Successful

Action

Action_Text

Profile_Name

*PROPRIETARY PROPERTIES*
Command_Time_Range:
**ID**
8155
Reference to a BACnetObjectPropertyReference object. This
**Meaning**
proprietary property represents any time constraints for executing
a command in an automatic or scheduled action.
**Data Type**
ObjectPropertyReference

## Writeable



![New Entrostar PICS image 36](./images/new-entrostar-pics_36.png)

Command_Trigger:
**ID**
8156
Reference to a BACnetDevObjRef object. This proprietary
**Meaning**
property represents the binary input used as the 'trigger'
equipment item for executing a command in an automatic action.
**Data Type**
DeviceObjectPropertyReference

## Writeable


Command_Trigger_Value:
**ID**
8157
For automated actions and their just-mentioned binary input
triggers, this proprietary property is the triggering state for the
**Meaning**
binary input. If the binary input enters this state, then the
command executes.
**Data Type**
Boolean

## Writeable



![New Entrostar PICS image 37](./images/new-entrostar-pics_37.png)

## 2.5.14 ‘CREDENTIAL DATA INPUT’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Present_Value
*
Description

Status_Flags

Reliability
*
Out_Of_Service

Supported_Formats

Supported_Format_Classes

Update_Time

Profile_Name

*Writable when out of service; otherwise read-only.

![New Entrostar PICS image 38](./images/new-entrostar-pics_38.png)

*PROPRIETARY PROPERTIES*
Custom_Decoding_String:
**ID**
8039

## Meaning

Configuration string containing custom card decoding instructions

## Data Type

CharacterString

## Writeable


Duress_Code:
**ID**
8037

## Meaning

Value associated with a duress setting

## Data Type

BACnetAuthenticationFactor

## Writeable


Duress_Style:
**ID**
8036

## Meaning

Way in which duress codes are handled at a reader

## Data Type

ReaderDuressStyle (see Section 2.7.4)

## Writeable


Presentation_Retries_Allowed:
**ID**
8136
Number of unsuccessful attempts to present a card at a reader
**Meaning**
before an alarm is generated
**Data Type**
Unsigned

## Writeable



![New Entrostar PICS image 39](./images/new-entrostar-pics_39.png)

Rolling_Pin:
**ID**
8135
Whether or not a reader accepts rolling PINs (that is, the typing in
**Meaning**
of a correct PIN at the end of a sequence of incorrect type-ins)
**Data Type**
Boolean

## Writeable


User_Access_Functions:
**ID**
8038
User access function codes operating at a Credential Data Input
**Meaning**
object
**Data Type**
List of AuthenticationIdentification (see Section 2.7.1)

## Writeable



![New Entrostar PICS image 40](./images/new-entrostar-pics_40.png)

## 2.5.15 ‘DEVICE’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

System_Status

Vendor_Name

Vendor_Identifier

Model_Name

Firmware_Revision

Application_Software_Version

Location

Description

Protocol_Version

Protocol_Revision

Protocol_Services_Supported

Protocol_Object_Types_Supported

Object_List

Max_APDU_Length_Accepted

Segmentation_Supported

Max_Segments_Accepted

VT_Classes_Supported

Active_VT_Sessions

Local_Time


![New Entrostar PICS image 41](./images/new-entrostar-pics_41.png)

Local_Date

UTC_Offset

Daylight_Savings_Status

APDU_Segment_Timeout

APDU_Timeout

Number_Of_APDU_Retries

Max_Master

Max_Info_Frames

Device_Address_Binding

Database_Revision

Active_COV_Subscriptions

Last_Restart_Reason

Time_Of_Device_Restart

Restart_Notification_Recipients

Serial_Number

Profile_Name

*PROPRIETARY PROPERTIES*
Event_Delivery_Status:
**ID**
8147

## Meaning

Current status of event deliveries within the EntroStar

## Data Type

EventDeliveryStatus (see Section 2.7.3)

## Writeable


Event_Retention_Period:
**ID**
8170
How long the database is willing to hold on to undeliverable
**Meaning**
events while the intended recipient is unavailable. [For EntroStar,
the recipients are Data Acquisition Units, known as DAUs.]
See also 'Max_Events_Recorded', later in this set of proprietary
**Data Type**
properties.
**Writeable**


![New Entrostar PICS image 42](./images/new-entrostar-pics_42.png)

First_Discovered:
**ID**
8154

## Meaning

When the EntroStar was first discovered on the network

## Data Type

CharacterString

## Writeable


Max_Events_Recorded:
**ID**
8171
How many undeliverable events the database is willing to hold on
**Meaning**
to while the intended recipient is unavailable. [For EntroStar, the
recipients are Data Acquisition Units, known as DAUs.]
See also 'Events_Retention_Period', earlier in this set of
**Data Type**
proprietary properties.
**Writeable**

Registration_Date:
**ID**
8153

## Meaning

Date when the EntroStar was first registered

## Data Type

CharacterString

## Writeable


Suite_Version:
**ID**
8148

## Meaning

Software suite version installed on the EntroStar

## Data Type

CharacterString

## Writeable


System_Authors_ID:
**ID**
8149

## Meaning

Assigned to the EntroStar by the master station

## Data Type

CharacterString

## Writeable



![New Entrostar PICS image 43](./images/new-entrostar-pics_43.png)

Timezone:
**ID**
8151

## Meaning

Timezone in which EntroStar operates
CharacterString (formatted as per the 'TZ' environment variable in
**Data Type**
the 'POSIX.1' standard)
**Writeable**


![New Entrostar PICS image 44](./images/new-entrostar-pics_44.png)

## 2.5.16 ‘FILE’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Description

File_Type

File_Size

Modification_Date

Archive

Read_Only

File_Access_Method

Record_Count

Profile_Name

*PROPRIETARY PROPERTIES*
None.

![New Entrostar PICS image 45](./images/new-entrostar-pics_45.png)

## 2.5.17 ‘MULTI_STATE INPUT’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Present_Value
*
Description

Device_Type

Status_Flags

Event_State

Reliability
*
Out_Of_Service

Number_Of_States

State_Text

Time_Delay

Notification_Class

Alarm_Values

Fault_Values

Event_Enable

Acked_Transitions

Notify_Type

Event_Time_Stamps

Event_Detection_Enable

Profile_Name


![New Entrostar PICS image 46](./images/new-entrostar-pics_46.png)

*Writable when out of service; otherwise read-only.
*PROPRIETARY PROPERTIES*
None.

![New Entrostar PICS image 47](./images/new-entrostar-pics_47.png)

## 2.5.18 ‘MULTI_STATE OUTPUT’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Present_Value

Description

Device_Type

Status_Flags

Event_State

Reliability
*
Out_Of_Service

Number_Of_States

State_Text

Priority_Array

Relinquish_Default

Time_Delay

Notification_Class

Feedback_Value

Event_Enable

Acked_Transitions

Notify_Type

Event_Time_Stamps

Event_Detection_Enable


![New Entrostar PICS image 48](./images/new-entrostar-pics_48.png)

Profile_Name

*Writable when out of service; otherwise read-only.
*PROPRIETARY PROPERTIES*
Active_Command_Priority:
**ID**
8163

## Meaning

Priority of the currently active command

## Data Type

Unsigned

## Writeable



![New Entrostar PICS image 49](./images/new-entrostar-pics_49.png)

## 2.5.19 ‘MULTI-STATE VALUE’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable

Object_Identifier

Object_Name

Object_Type

Present_Value

Description

Status_Flags

Event_State

Reliability
*
Out_Of_Service

Number_Of_States

State_Text

Priority_Array

Relinquish_Default

Time_Delay

Notification_Class

Alarm_Values

Fault_Values

Event_Enable

Acked_Transitions

Notify_Type

Event_Time_Stamps

Event_Detection_Enable


![New Entrostar PICS image 50](./images/new-entrostar-pics_50.png)

Profile_Name

*Writable when out of service; otherwise read-only.
*PROPRIETARY PROPERTIES*
Active_Command_Priority:
**ID**
8163

## Meaning

Priority of the currently active command

## Data Type

Unsigned

## Writeable



![New Entrostar PICS image 51](./images/new-entrostar-pics_51.png)

## 2.5.20 ‘NETWORK SECURITY’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable


Object_Identifier

Object_Name

Object_Type

Description

Base_Device_Security_Policy

Network_Access_Security_Policies

Security_Time_Window

Packet_Reorder_Time

Distribution_Key_Revision

Key_Sets

Last_Key_Server

Security_PDU_Timeout

Update_Key_Set_Timeout

Supported_Security_Algorithms

Do_Not_Hide

Profile_Name
*PROPRIETARY PROPERTIES*
None.

![New Entrostar PICS image 52](./images/new-entrostar-pics_52.png)

## 2.5.21 ‘NOTIFICATION CLASS’

*GENERAL*
  Creatable (for Object_Identifier > 4)
  Deletable (for Object_Identifier > 4)
*STANDARD PROPERTIES*

## Property

## Writable


Object_Identifier

Object_Name

Object_Type

Description

Notification_Class

Priority

Ack_Required

Recipient_List

Profile_Name
*PROPRIETARY PROPERTIES*
None.

![New Entrostar PICS image 53](./images/new-entrostar-pics_53.png)

## 2.5.22 ‘SCHEDULE’

*GENERAL*
  Creatable
  Deletable
*STANDARD PROPERTIES*

## Property

## Writable


Object_Identifier

Object_Name

Object_Type
Present_Value
*

Description

Effective_Period

Weekly_Schedule

Exception_Schedule

Schedule_Default

List_Of_Object_Property_References

Priority_For_Writing

Status_Flags

Reliability

Out_Of_Service

Profile_Name
*Writable when out of service; otherwise read-only.
*PROPRIETARY PROPERTIES*
None.

![New Entrostar PICS image 54](./images/new-entrostar-pics_54.png)

## 2.6 PROPRIETARY OBJECT TYPES

None.

## 2.7 PROPRIETARY DATA TYPES

## 2.7.1 AuthenticationIdentification

**AuthenticationIdentification** :: = SEQUENCE {
Style
[0] ENUMERATED {
fixed-authentication-factor
(0),
added-to-factor
(1),
subtracted-from-factor
(2),
not-used
(3)
},
AuthenticationFactor
[1] BACnetAuthenticationFactor
}
**2.7.2 DropPulseUnlock**
**DropPulseUnlock** :: = ENUMERATED {
drop-on-closing
(0),
drop-on-opening
(1),
drop-at-strike-end
(2),
}

## 2.7.3 EventDeliveryStatus

**EventDeliveryStatus** :: = ENUMERATED {
event-delivered-normally
(0),
some-destinations-failed
(1),
all-destinations-failed
(2),
}

![New Entrostar PICS image 55](./images/new-entrostar-pics_55.png)

## 2.7.4 ReaderDuressStyle

**ReaderDuressStyle** :: = ENUMERATED {
fixed-authentication-factor
(0),
number-added-to-factor
(1),
number-subtracted-from-factor (2),
not-used
(3)
}

![New Entrostar PICS image 56](./images/new-entrostar-pics_56.png)

## 2.8 DATA LINK LAYER OPTIONS

 BACnet IP, (Annex J)
 BACnet IP, (Annex J), Foreign Device
 ISO 8802-3, Ethernet (Clause 7)
 ATA 878.1, 2.5 Mb. ARCNET (Clause 8)
 ATA 878.1, EIA-485 ARCNET (Clause 8), baud rate(s): ____________
 MS/TP master (Clause 9), baud rate(s):   Max 115.2K
 MS/TP slave (Clause 9), baud rate(s):   Max 115.2K
 Point-To-Point, EIA 232 (Clause 10), baud rate(s):   Max 115.2K
 Point-To-Point, modem, (Clause 10), baud rate(s):   Max 115.2K
 LonTalk, (Clause 11), medium: __________
 BACnet/ZigBee (Annex O): __________
 Other

## 2.9 DEVICE ADDRESS BINDING

 Static device binding (currently necessary for two-way communications with MS/TP slaves and
certain other devices)

## 2.10 NETWORKING OPTIONS

 Router, Clause 6 routing between the following data-links: B/IP, MS/TP, PTP Direct, PTP Switched
Circuit.
  Annex H, BACnet Tunnelling Router over IP
  BACnet/IP Broadcast Management Device (BBMD)
  BBMD supports registrations by Foreign Devices
  BBMD supports network address translation

![New Entrostar PICS image 57](./images/new-entrostar-pics_57.png)

## 2.11 CHARACTER SETS

Indicated support for multiple character sets does not imply that they can all be supported
simultaneously.
 ISO 10646 (UTF-8)
 IBM/Microsoft DBCS
 ISO 8859-1
 ISO 10646 (UCS-2)
 ISO 10646 (UCS-4)
 JIS X 0208
If this product is a communications gateway, then describe the types of non-BACnet
equipment/networks(s) that the gateway supports: (Not applicable)

## 2.12 NETWORK SECURITY OPTIONS

  Non-Secure Device — is capable of operating without BACnet Network Security
  Secure Device — is capable of using BACnet Network Security (NS-SD BIBB)
  Multiple Application-Specific Keys
  Supports encryption (NS-ED BIBB)
  Key Server (NS-KS BIBB)

---

*© DAQ Electronics, LLC*
