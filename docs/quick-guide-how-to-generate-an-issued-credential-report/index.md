---
layout: default
title: How to Generate an Issued Credential Report
nav_order: 190
---

# How to Generate an Issued Credential Report

![How to Generate an Issued Credential Report image 01](./images/quick-guide-how-to-generate-an-issued-credential-report_01.png)

![How to Generate an Issued Credential Report image 02](./images/quick-guide-how-to-generate-an-issued-credential-report_02.png)

Within *StarWatch SMS*, there are three ways to generate reports detailing the credentials/cards that
have been issued during a specific time period:

Using the *Credentials Management* function

Using the system *Event Log*

Using the *Crystal Reports* application

## Credentials Management

Using the column editing tools provided in the *Credentials Management* window, users can create
custom reports that are organized by set parameters. This is accomplished by adding a new view,
selecting the required columns, and setting up date/time filters. Reports created in this manner can be
saved for future use.

![How to Generate an Issued Credential Report image 03](./images/quick-guide-how-to-generate-an-issued-credential-report_03.png)

Here is an example of a report called “Issued Report”. Note that the range of dates can be changed
easily from the *Issued* column filter.

![How to Generate an Issued Credential Report image 04](./images/quick-guide-how-to-generate-an-issued-credential-report_04.png)

Here is how the printed version of the report will appear:

![How to Generate an Issued Credential Report image 05](./images/quick-guide-how-to-generate-an-issued-credential-report_05.png)

![How to Generate an Issued Credential Report image 06](./images/quick-guide-how-to-generate-an-issued-credential-report_06.png)

## Event Log

You can also create and save reports using the system *Event Log*.
In the following example, the created report has been named “Issued Report” and contains all events
of the type *Audit* that are linked to the *Card Issued* parameter within the *Access Control* sub-category:

![How to Generate an Issued Credential Report image 07](./images/quick-guide-how-to-generate-an-issued-credential-report_07.png)

![How to Generate an Issued Credential Report image 08](./images/quick-guide-how-to-generate-an-issued-credential-report_08.png)

As shown, the event view displays the time, operator name, and the person that the card was issued to
including the card type and card number.

![How to Generate an Issued Credential Report image 09](./images/quick-guide-how-to-generate-an-issued-credential-report_09.png)

Note that it is highly desirable to create reports that can be re-used. Each report can be saved
including columns selected, layout, and widths.
This type of data can easily be exported and reformatted if needed.

![How to Generate an Issued Credential Report image 10](./images/quick-guide-how-to-generate-an-issued-credential-report_10.png)

## Crystal Reports

The *Crystal Reports* application includes a report called “Issued Credential Report”. Using the
parameters provided, users can filter reports to include specific types of cards and/or persons:

![How to Generate an Issued Credential Report image 11](./images/quick-guide-how-to-generate-an-issued-credential-report_11.png)

![How to Generate an Issued Credential Report image 12](./images/quick-guide-how-to-generate-an-issued-credential-report_12.png)

Here is how the output version of the report will appear:

![How to Generate an Issued Credential Report image 13](./images/quick-guide-how-to-generate-an-issued-credential-report_13.png)

![How to Generate an Issued Credential Report image 14](./images/quick-guide-how-to-generate-an-issued-credential-report_14.png)

Note that all Crystal reports can be output to Crystal format and browser or to XtraGrid format:

![How to Generate an Issued Credential Report image 15](./images/quick-guide-how-to-generate-an-issued-credential-report_15.png)

---

*© DAQ Electronics, LLC*
