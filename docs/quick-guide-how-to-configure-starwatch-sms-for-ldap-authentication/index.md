---
layout: default
title: How to Configure StarWatch SMS for LDAP Authentication
nav_order: 140
---

# How to Configure StarWatch SMS for LDAP Authentication

![How to Configure StarWatch SMS for LDAP Authentication image 01](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_01.png)

![How to Configure StarWatch SMS for LDAP Authentication image 02](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_02.png)

## Introduction

The *StarWatch SMS* suite allows for the use of LDAP communication to store and extract objects such as
usernames and passwords in/from Active Directory. This object data can then be shared throughout the
network. This framework enables enriched development and distribution of identity control, security,
and web applications.
Integration of this framework within *StarWatch SMS* involves several parameters set during installation
and then subsequent modifications made within the system *Administration* panel, as outlined in this
document.

![How to Configure StarWatch SMS for LDAP Authentication image 03](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_03.png)

## Installation Settings

During the initial *StarWatch SMS* software installation process, the *SMS LDAP Server* must be directly
selected for installation on your local hard drive.
1. As you progress through the series of options screens provided by the installation wizard, you
will eventually arrive at the *Specific Setup* screen. In the features window, click on the *Server*
drop-down menu icon
.

![How to Configure StarWatch SMS for LDAP Authentication image 04](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_04.png)

![How to Configure StarWatch SMS for LDAP Authentication image 05](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_05.png)

2. From the *Server* options, select the menu icon
for *SMS LDAP Server*.
3. Next, select the *Entire feature will be installed on local hard drive* option.
4. No other changes need to be made related to LDAP communication. Once this feature has been
selected and you have made any other required changes on the *Specific Setup* screen, click the
*Next* button.
5. Continue through the remaining options screens to complete *StarWatch SMS* setup/installation.

![How to Configure StarWatch SMS for LDAP Authentication image 06](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_06.png)

## Updating the Administration Panel

After *StarWatch SMS* has been fully installed, the *Administration* panel must be modified to enable the
importing of groups and roles from LDAP.
1. After launching the *StarWatch SMS* application, open the *Administration* panel by clicking the
*Admin* icon on the top menu ribbon.

![How to Configure StarWatch SMS for LDAP Authentication image 07](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_07.png)

2. Next, select the *Roles* tab from the *Admin* side menu.

![How to Configure StarWatch SMS for LDAP Authentication image 08](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_08.png)

![How to Configure StarWatch SMS for LDAP Authentication image 09](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_09.png)

![How to Configure StarWatch SMS for LDAP Authentication image 10](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_10.png)

3. In the *Global Rights* window, click on the *Person Management* drop-down menu icon
.

![How to Configure StarWatch SMS for LDAP Authentication image 11](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_11.png)

![How to Configure StarWatch SMS for LDAP Authentication image 12](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_12.png)

4. Next, from the *Person Management* list, enable both the *Import LDAP Groups* and *Import LDAP*
*Roles* options. The top menu ribbon will change to include the *Import LDAP Groups* and *Import*
*LDAP Roles* icons in the *Personnel* area.

![How to Configure StarWatch SMS for LDAP Authentication image 13](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_13.png)

![How to Configure StarWatch SMS for LDAP Authentication image 14](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_14.png)

To proceed with importing a group from the *LDAP Server*, complete the following steps.
1. Launch the *Import Person Group* dialog box by clicking the *Import LDAP Groups* icon.

![How to Configure StarWatch SMS for LDAP Authentication image 15](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_15.png)

Several options for connecting to the *LDAP Server* are provided.
2. In the *Host* field, enter the IP address for the *SMS LDAP Server*.
3. Be sure that the *Windows Authentication* option has been enabled.
4. Click the *Connect* button.
5. Click the *Next* button at the bottom of the screen to call up the *Create New Person Group*
area.

![How to Configure StarWatch SMS for LDAP Authentication image 16](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_16.png)

![How to Configure StarWatch SMS for LDAP Authentication image 17](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_17.png)

Here you can create new *Person* groups in *StarWatch SMS* and associate them with groups
created in the domain controller/server.
6. In the *Create new SMS Group* field, assign a name for the group.
7. Next, assign a *Person Type* to the group using the provided drop-down menu.
8. Click on the *Browse LDAP* button. The *LDAP Group Browser* window will appear.

![How to Configure StarWatch SMS for LDAP Authentication image 18](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_18.png)

![How to Configure StarWatch SMS for LDAP Authentication image 19](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_19.png)

9. From the *LDAP Groups* list, select the groups that you want to import and click the *OK* button.

![How to Configure StarWatch SMS for LDAP Authentication image 20](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_20.png)

Back in the *Create New Person Group* area, the system must be set to import the desired
strings from LDAP using the *Property Mapping* fields.

![How to Configure StarWatch SMS for LDAP Authentication image 21](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_21.png)

10. In the *First Name* field, click on the small icon

![How to Configure StarWatch SMS for LDAP Authentication image 22](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_22.png)

to the right of the *LDAP Attribute* section
and set the string to *Given Name*.

![How to Configure StarWatch SMS for LDAP Authentication image 23](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_23.png)

11. Repeat this action in the *Last Name* field and set the string to *Surname*.

![How to Configure StarWatch SMS for LDAP Authentication image 24](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_24.png)

These are the only mandatory properties for importation into *StarWatch SMS*. You can add
other properties to import as needed.
12. Click the *Next* button. The newly created *Person Group* will be imported. Access rights can be
assigned to the new group using normal *StarWatch SMS* functionality.

![How to Configure StarWatch SMS for LDAP Authentication image 25](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_25.png)

## Settings in Management Console

In *Management Console*, settings for LDAP configuration can be found by clicking on *SMS LDAP Server* in
the *Service* list and then clicking the *Settings* button in the top right.

![How to Configure StarWatch SMS for LDAP Authentication image 26](./images/quick-guide-how-to-configure-starwatch-sms-for-ldap-authentication_26.png)

## Workgroup settings

Auto retire removed – if checked, removing a person from a group in the domain will retire a
•
person in *StarWatch SMS*.
Auto restore added – if checked, adding a role back to a person in LDAP will unretire them.
•

## Login access settings

Enables/disables user login to *StarWatch SMS* if that person belongs to a certain group on LDAP.
•

## Card access settings

Enables/disables person cards in the event they are removed or moved from an LDAP group.
•

---

*© DAQ Electronics, LLC*
