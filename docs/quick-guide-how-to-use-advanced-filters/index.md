---
layout: default
title: How to Use Advanced Filters
nav_order: 330
---

# How to Use Advanced Filters

![How to Use Advanced Filters image 01](./images/quick-guide-how-to-use-advanced-filters_01.png)

## Step 1 – Start new filter

Choose an item to filter on – in this example, the *Card Type*.

![How to Use Advanced Filters image 02](./images/quick-guide-how-to-use-advanced-filters_02.png)

We now have the filter *NewProxCard* as the card type filter.

![How to Use Advanced Filters image 03](./images/quick-guide-how-to-use-advanced-filters_03.png)

![How to Use Advanced Filters image 04](./images/quick-guide-how-to-use-advanced-filters_04.png)

## Step 2 – Edit filter

Click on the *Edit Filter* button at the bottom right of the view.

![How to Use Advanced Filters image 05](./images/quick-guide-how-to-use-advanced-filters_05.png)

![How to Use Advanced Filters image 06](./images/quick-guide-how-to-use-advanced-filters_06.png)

Click on the *And* condition (root node of the filter) to call up the following menu.

![How to Use Advanced Filters image 07](./images/quick-guide-how-to-use-advanced-filters_07.png)

Select the menu item *Add Group*.

![How to Use Advanced Filters image 08](./images/quick-guide-how-to-use-advanced-filters_08.png)

You should now see two conditions: the main node condition *And* and a sub-node condition *And*
(group).

![How to Use Advanced Filters image 09](./images/quick-guide-how-to-use-advanced-filters_09.png)

## Step 3 – Customize the filter as needed

Most conditions involving multiple columns and multiple values require groups of conditions. For
example:
*Card = ‘My card’ AND (Area = ‘Floor 1’ OR Area = ‘Floor 2’)*
Note that in this filter the brackets include multiple values of the item *Area*.  Multiple values of the
same item must always be grouped by *OR* and different items are always grouped by *AND* with each
group of item values.
First, change the sub-group condition to *Or*, as shown, by clicking on the sub *And* item and selecting *Or*
from the menu.

![How to Use Advanced Filters image 10](./images/quick-guide-how-to-use-advanced-filters_10.png)

Next, add another comparison to this group by clicking on the “*+*” sign to the right of the *Or* group.

![How to Use Advanced Filters image 11](./images/quick-guide-how-to-use-advanced-filters_11.png)

![How to Use Advanced Filters image 12](./images/quick-guide-how-to-use-advanced-filters_12.png)

Next, change all the items and values as needed.
If we want all cards except one type of card *And* located in two different areas, change the first item
called *[Card]* and modify the *Equals* to *Does not equal*.

![How to Use Advanced Filters image 13](./images/quick-guide-how-to-use-advanced-filters_13.png)

Next, change both the items labeled as *[Access Permission]* to *Area*.

![How to Use Advanced Filters image 14](./images/quick-guide-how-to-use-advanced-filters_14.png)

![How to Use Advanced Filters image 15](./images/quick-guide-how-to-use-advanced-filters_15.png)

Enter the value required (this is a manual operation, so care must be taken to enter the exact value
needed).

![How to Use Advanced Filters image 16](./images/quick-guide-how-to-use-advanced-filters_16.png)

Note that the filtered results are as required.

![How to Use Advanced Filters image 17](./images/quick-guide-how-to-use-advanced-filters_17.png)

IMPORTANT: click *Update* to save the filter to the required view and *Share* if this view is to be used by
all operators.

---

*© DAQ Electronics, LLC*
