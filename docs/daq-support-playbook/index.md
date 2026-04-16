---
layout: default
title: DAQ Support Playbook
nav_order: 30
---

# DAQ Support Playbook

Best Practices for the Most Common Customer Issues

*Derived from 404 support tickets (HESK export) submitted between January 4, 2023 and April 13, 2026.*

Compiled from DAQ Electronics help-desk ticket history — April 16, 2026.


## About this playbook


This guide distills recurring customer issues from roughly three and a
quarter years of DAQ Electronics help-desk tickets into a short set of
runbooks. Each runbook captures the symptoms a customer typically
describes, the likely causes, the checks worth running before
escalation, and the resolution pattern that most often applies. The goal
is to shorten the path from first-touch to resolution for the issues
that appear again and again.

Every example and pattern in this document is derived directly from the
original ticket bodies and from staff replies captured in the HESK
export. Nothing here is invented from general IT knowledge. Ticket IDs
cited at the end of each runbook are the HESK numeric ids visible to DAQ
staff and can be used to pull the original thread for context.


## How to use it


  - Skim the Typical symptoms section for each runbook to find the one
    that matches the customer’s wording.

  - Run the Diagnostic checklist before changing anything. Several
    high-severity tickets in the source data escalated because a tech
    made changes before capturing state.

  - Apply Resolution steps in the order shown; later steps assume
    earlier ones did not resolve the issue.

  - If nothing in a runbook matches, use the Related ticket IDs to pull
    the original tickets and compare wording — the runbooks are
    summaries, not transcripts.


## Ticket landscape at a glance


Across 404 tickets from January 4, 2023 through April 13, 2026, customer
issues cluster into about twenty recurring categories. The table below
shows how often each category’s keywords appeared in ticket threads;
tickets frequently touch more than one category, so the totals are
greater than the ticket count. SCIF / ICIDS issues dominate by volume;
Site Planner / map work and comms-fail triage are the next two largest
categories; backup, licensing, and launch failures are less frequent but
generate the highest-severity tickets.

|                                             |                  |
| ------------------------------------------- | ---------------- |
| **Category**                                | **Ticket count** |
| SCIF / ICIDS-specific                       | 131              |
| Site Planner / Map / Widget issues          | 100              |
| Panel / zone in comms fail                  | 71               |
| Firmware / controller / RPI / IAC           | 66               |
| Database backup & restore                   | 65               |
| Install / upgrade / server migration        | 53               |
| Licensing / activation / Viewing Mode       | 43               |
| Card / credential programming & migration   | 41               |
| Orbit.Net / SMS service launch              | 40               |
| Performance / crash / BSOD                  | 27               |
| Card reader / strike / door hardware        | 25               |
| Starwatch / Operator login & initialization | 23               |
| Camera / video / audio integration          | 20               |
| EntroStar discovery & credential sync       | 16               |
| Time / clock / schedule                     | 14               |
| Reports / export / import                   | 14               |
| Alarms / events / history                   | 13               |
| Workstation / domain / Windows login        | 7                |
| Notifications / email / SMTP                | 1                |

*Note: tickets can touch more than one category; the table above shows
primary classification by first matching keyword and is intended for
orientation, not precise reporting.*


## Runbooks for the most common issues


Fourteen runbooks follow. They are ordered by a combination of
frequency, severity, and how often the same issue reappears on tickets
from multiple sites — not strictly by category count. Each runbook is
self-contained; you do not need to read them in order.


## 1. Starwatch / Orbit.Net fails to launch or initialize


Launch and initialization failures show up on new server installs, new
workstations, and existing machines after a reimage, patch, drive swap,
or SCIF transfer. In the 2023–2026 dataset this surfaces in forty-plus
Orbit.Net and Starwatch-login tickets. The pattern is usually a
dependency (DLL or SQL Compact runtime), a service-start ordering issue,
or a version skew between client and server.


### Typical symptoms


  - “SMS Orbit.NET refuses to start” after a fresh SMS install on a new
    server.

  - “Unable to load DLL 'PassDBClient.dll': The specified module could
    not be found. (HRESULT: 0x8007007E).”

  - Starwatch login hangs, then a Select Server window opens with
    “Notification engine ping fails. The application disconnected from
    the server and must be closed.”

  - Operator / Starwatch gets stuck on the loading screen after the user
    enters credentials.

  - TCP error 10061: “No connection could be made because target machine
    actively refused it 127.0.0.1:6543” when launching Site Planner or
    Starwatch.

  - Starwatch prompts “unable to connect, see admin for software update”
    when the client and server versions are out of sync.

  - “Failed to register new workstation. The workstation name is already
    registered” after importing a database into a new test machine.

  - “Cannot start Orbit Service. It says it cannot find related files
    and will not start” on a fresh install.


### Likely causes


  - Missing or mis-registered Orbit.Net dependencies (PassDBClient.dll,
    32-bit and 64-bit SQL Server Compact runtimes).

  - Windows services (SQL Server, SMS Server, SMS Orbit.Net) not running
    or started in the wrong order.

  - Installer package incomplete or not run to completion — files are
    missing rather than corrupt.

  - Client/server version mismatch — workstation installer newer or
    older than the server build.

  - Imported database already lists the current machine under a stale
    workstation name.

  - Local dispatcher port (default 6543) blocked by firewall or
    endpoint-AV, or Orbit.Net never finished starting.


### Diagnostic checklist


1.  Confirm the server’s exact SMS version and build date, then confirm
    the workstation’s installer matches before anything else.

2.  In Windows Services verify SQL Server, SMS Server, and SMS Orbit.Net
    are all Running. Start them in that order if stopped.

3.  Open the Orbit trace log and search for DLL load failures or
    TSM\_TIMEOUT entries.

4.  Verify PassDBClient.dll and its SQL Compact runtime dependencies
    exist and are registered — a DLL present on disk but not registered
    still yields HRESULT 0x8007007E.

5.  From the workstation, Test-NetConnection to the server on the SMS
    dispatcher port (6543) to rule out a firewall drop.

6.  If you see “workstation name already registered,” open Workstations
    in the imported database and remove/rename the stale entry before
    re-registering.


### Resolution steps


1.  Re-run both the 32-bit and 64-bit SQL Server Compact installers on
    the affected server, then reboot.

2.  Restart SMS services in Management Console (stop all, then start
    all) — tickets consistently show a clean stop/start clears minor
    hiccups.

3.  For installs where Orbit “cannot find related files”: assume the
    install did not complete; fully uninstall, re-run the
    StarWatchSMS-Redist package, then the client exe, and point the
    client to the server by name or IP on first launch (\#734 flow).

4.  For “already registered” errors: delete the conflicting Workstations
    record from the imported database or rename the local machine before
    first login.

5.  If the Notification Engine ping fails, stop/restart the Notification
    Engine service and confirm the server name in the client profile
    resolves to the correct IP.

6.  If Starwatch or Operator stays stuck on the loading screen, run a
    Repair install of the client; if that does not clear it, fully
    uninstall and reinstall exactly matching the server version.


### Related ticket IDs


*\#758, \#846, \#904, \#910, \#914, \#918, \#922, \#927, \#951, \#968,
\#975, \#994, \#1003, \#1026, \#1043, \#1047, \#1052, \#1079, \#1086,
\#1108*


## 2. Database backup failures and problematic restores


Backup problems are one of the highest-stakes categories in the dataset.
They come in two flavors: routine failures (backup will not run, drive
missing, log file out of control, disk full) and painful recoveries
(restore will not apply, prior backup was overwritten, system comes back
with reduced rights or in Viewing Mode). Many escalate because there was
no clean earlier backup to fall back to.


### Typical symptoms


  - Scheduled or manual backup fails in Management Console; SQL
    transaction log file balloons (values over 100 GB observed).

  - “The configured backup drive isn’t available on the server,” or the
    backup path points to a drive that no longer exists.

  - Daily backups failing while a weekly manual backup still works —
    almost always disk full from unbounded retention.

  - Only the most recent .BAK exists because the scheduled job is set to
    Replace — no rollback window when a problem is noticed later.

  - Restore from backup fails after a drive swap or hardware
    replacement; the associated log file shows errors.

  - After recovering from an image and restoring the DB: new PICs do not
    authenticate, Administrator rights look reduced, Starwatch comes up
    in “Viewing mode.”


### Likely causes


  - Backup destination drive or share unreachable or full — observed
    repeatedly when retention is unlimited and old .BAKs are never
    purged.

  - SQL transaction log never truncated because the recovery model was
    never set to match the backup schedule.

  - Scheduled backup configured to overwrite rather than retain history,
    leaving no pre-incident copy.

  - Database logical name in SQL does not match the expected machine /
    application-server name after a C: drive swap.

  - License / activation state changed during the hardware swap, leaving
    the restored DB unable to come fully online.


### Diagnostic checklist


1.  In Management Console run a manual backup and capture the error
    immediately (do not close the dialog).

2.  Check the configured backup destination: does the drive letter exist
    on this host, is it online, and how much free space remains?

3.  In SQL Management Studio check the size of the transaction log; if
    it is tens of GB or more the log has never been truncated.

4.  List all existing .BAK files on disk and confirm at least one
    pre-incident backup exists before touching anything else.

5.  After a hardware swap, compare the SQL database instance name
    against the expected machine/application-server name. If they do not
    match, the restore will behave oddly.


### Resolution steps


1.  Fix the destination first — remap the backup drive or point the
    schedule at a valid local path — before rerunning.

2.  If the disk is full from prior .BAKs, delete old backups, set a
    retention limit (at minimum seven dailies), then fully uninstall and
    reinstall Starwatch if the install state has been corrupted by the
    full-disk condition (\#723 flow).

3.  Shrink the transaction log via the standard SQL Management Studio
    procedure, then adjust the recovery model / scheduled job so it
    truncates regularly.

4.  Change the scheduled backup from Replace to Retain N copies so a bad
    DB state is not immediately overwritten on the next run.

5.  For a failing restore after a drive swap: obtain a new
    license/activation key first (required when the hardware fingerprint
    changed), then rename the SQL database to match the current server
    name, then retry the restore.

6.  If the restored system comes up in Viewing Mode or with reduced
    Administrator rights, see Runbook 5 — this almost always traces to a
    license or role-rights issue that survived the restore.


### Related ticket IDs


*\#723, \#928, \#1002, \#1008, \#1014, \#1018, \#1019, \#1024, \#1032,
\#1041, \#1043, \#1044, \#1045, \#1053, \#1068, \#1077, \#1079, \#1091,
\#1095, \#1105, \#1107, \#1108*


## 3. Zones and panels in communication failure (“comms fail”)


Comms-fail tickets are the single largest operational pattern in the
data. They come in three distinct flavors that are fixed in different
places: individual panels intermittently dropping, mass failures after a
site-wide event (power outage, broadcast storm, NEC change, firmware
push), and mysterious failures that only clear after Orbit.Net is
restarted. Treat them as three different problems.


### Typical symptoms


  - Individual Stargate 3 / E-RADC / EntroStar panels cycling offline
    and back within minutes.

  - Zones show Status = Online, Sync Status = Good, but Enable = False,
    and Enable/Disable commands return “Operation failed.”

  - MCU shows the server polling and the RADC replying, yet Starwatch
    still shows comms fail.

  - Zones stay online for \~10 minutes after an Orbit.Net restart, then
    fall back into comms fail.

  - Mux Cards going in and out of comm fail after a server swap,
    sometimes with the entire bend following a specific slot offline.

  - Mass comms fail after a power outage, broadcast storm, NEC path
    change, or firmware push.

  - “Intermittent comm fails since the 5.5.604 update” — failures that
    started exactly after a software upgrade.


### Likely causes


  - Site-side infrastructure (fiber link degraded, NEC rerouted a path,
    failed switch, broadcast storm).

  - Encryption or transceiver hardware at the far end (SEL-3025 Serial
    Shield is end-of-life; Digi Connect EZ Mini; Gold-X / USB hub)
    failing or mis-configured.

  - Audio-mux card or backplane hardware fault; the offending slot can
    produce mux chirping with no useful link.

  - Panel not actually Enabled in Site Browser even though Status shows
    Online.

  - Orbit.Net service stuck in a state that only a restart clears — a
    recurring workaround, not a fix.

  - Firmware version mismatch after an update (EntroStar 1.4.41J vs
    1.4.45f changed behavior site-wide).


### Diagnostic checklist


1.  Check Status / Sync Status / Enable flags in Site Browser. If Enable
    = False, that is the root cause, not a symptom — you must re-enable.

2.  Open MCU on both sides (SCIF / remote and application server).
    Confirm bidirectional polling and replies, not just one direction.

3.  For Mux bend / card problems, isolate a single card at a time (see
    \#733): add only Card 1, capture an MCU trace, then try a different
    card in slot 1, then the same card in a known-good slot, then a
    different comm port, then a different cable, then a different MCU
    converter.

4.  Compare LED patterns on the MSTR set to a known-good bend: you
    should see RX, GD MSG, GD STA, RTS, TX in a continuous pattern.

5.  If Orbit.Net is running, ping the panel IP with Orbit stopped and
    with Orbit running. Drops only under Orbit = Orbit-side port /
    service issue, not physical network.

6.  For mass recent failures, correlate with site events in the last 30
    days: power outage, NEC change, software or firmware update.

7.  Bypass any encryption device (DES, Digi Connect) to prove or rule
    out the transceiver.


### Resolution steps


1.  If Enable = False in Site Browser, right-click the panel and Enable.
    If that pop-up returns “Enable failed,” stop and restart SMS
    services first, then retry.

2.  For comms fails that clear with an Orbit.Net restart: treat it as a
    workaround, not a fix. Capture Orbit trace logs the next occurrence
    and escalate with those logs attached.

3.  Power-outage failures: confirm UPS health and generator behavior
    before panel-level troubleshooting. Multiple tickets traced mass
    failures to the UPS or generator not kicking in.

4.  Broadcast-storm or NEC-caused failures: verify with the base NEC
    that the path is clean before continuing.

5.  Firmware-regression comms fails: note the exact firmware build that
    introduced the regression, attach before/after comm-fail
    spreadsheets, and ask about rolling firmware back until root cause
    is found.

6.  If a specific transceiver is the common factor (for example the
    end-of-life SEL-3025 Serial Shield), replace with the current
    supported equivalent rather than continuing to troubleshoot the old
    part.

7.  For Mux-bend failures traced to a master comm board by the isolation
    procedure above, swap the master comm board; a Gold-X serial
    fallback has resolved cases where the root cause was never fully
    isolated (\#733).


### Related ticket IDs


*\#733, \#945, \#961, \#963, \#976, \#1019, \#1023, \#1024, \#1033,
\#1042, \#1046, \#1050, \#1055, \#1056, \#1057, \#1066, \#1068, \#1075,
\#1086, \#1089, \#1090, \#1099, \#1108*


## 4. Card reader reads badge but door strike does not fire


Sites repeatedly report readers appearing to grant access (LED turns
green, event logs “Valid Access”) while the strike does not actually
release, or the opposite — the door stays unlocked when it should not. A
large fraction of these tickets involve 75-bit PIV / FIPS-201 / CAC
credentials on HID Signo, IAC, or EntroStar hardware. BACnet Browser is
the diagnostic tool of choice for this class.


### Typical symptoms


  - Reader LED flashes green (or yellow then green) on a PIV / 75-bit
    card, but the strike never fires.

  - “Valid Access” reported at the front end, but no physical strike
    actuation.

  - Prox cards work correctly on the same reader; only PIV / CAC /
    75-bit fails.

  - Door command in Starwatch: selecting Normal goes straight to
    Unlocked; Lock sets the door to Unlocked.

  - REX button does not change the mag-lock state.

  - New cards do not work anywhere even though previously enrolled cards
    still do.

  - Card shows “Unregistered ID” at the reader despite being enrolled,
    or no event is logged at all.

  - New FIPS-201 200-bit readers report “unrecognized card” on CAC
    credentials while the same reader works on HID stock.


### Likely causes


  - Wrong card format assigned in Starwatch (the reader is configured
    for Wiegand 26 but the card is FIPS-201 200-bit / PIV CAC).

  - Card format or facility code changed on-site and old/new no longer
    align; or multiple card formats share a facility code and the RPI
    driver cannot bind card data to a person (\#720).

  - New credentials never reached the panel — BACnet Browser shows old
    credentials list but no new ones.

  - Panel at credential capacity (one site had \~21,687 profiles).

  - Portal / door wiring confusion — strike wired to the wrong output,
    or REX wired in reverse.

  - Firmware-regression behavior after an EntroStar update (Left-Open
    false alarms after 1.4.41J → 1.4.45f).


### Diagnostic checklist


1.  In Starwatch, open the credential and confirm the Card Type exactly
    matches the reader’s configured format (26-bit vs 75-bit vs 200-bit
    PIV CAC).

2.  Use BACnet Browser to walk from the person to the panel (\#721):
    note the person’s BACnet ID, open Access Credential \<ID\> on the
    panel, inspect Authentication Factors, then compare present-value on
    Credential\_Data\_Input after a card swipe. CDI mapping: Door 1
    entry = CDI 1, Door 1 exit = CDI 4, Door 2 entry = CDI 7, Door 2
    exit = CDI 10.

3.  If Credential\_Data\_Input Present-Value stays “undefined 0” on
    swipe, the reader never handed card data to the panel — reader
    config or wiring problem.

4.  Compare a working and non-working portal side-by-side in Site
    Planner; duplicate the working portal’s config before changing
    anything else.

5.  Check reader LED sequence against that reader’s valid-access
    pattern; some HID Signo + IAC combinations flash green but never
    strobe the strike relay when the card format is wrong.

6.  Confirm the door is not stuck in an override (Unlocked, NoAccess)
    that overrides access grants.


### Resolution steps


1.  Reassign the correct card format and republish the credential to the
    panel. For PIV/CAC pick FIPS-201 75-bit or 200-bit PIV CAC
    explicitly, not generic Wiegand (\#837).

2.  Remove duplicate card formats that share a facility code — keep one
    per facility code with a consistent string format (for example
    “00-”). Re-register affected cards and restart Orbit.Net
    manually so PASSDB resyncs (\#720).

3.  When credentials stop reaching the panel, factory-reset the panel
    (BACnet Browser → reset) and re-link. Multiple tickets resolved this
    way.

4.  If the panel is at capacity, purge unused/expired credentials before
    adding new ones.

5.  For inverted door states (Normal → Unlocked, Lock → Unlocked):
    re-check output mapping in Site Planner and verify strike / mag-lock
    wiring matches the polarity the panel expects (fail-secure vs
    fail-safe).

6.  For intermittent Left-Open / tailgating alarms after a firmware
    update, document the exact firmware build and consider rolling back
    until a fix is available.


### Related ticket IDs


*\#720, \#721, \#816, \#837, \#842, \#867, \#883, \#895, \#930, \#934,
\#948, \#949, \#955, \#966, \#967, \#972, \#973, \#985, \#999, \#1001,
\#1003, \#1007, \#1015, \#1036, \#1071, \#1078, \#1117*


## 5. Licensing, activation, and “Viewing Mode”


Licensing issues are a disproportionate source of High-priority tickets
because they take down the ability to make any changes. Three patterns
dominate: license renewal needed on a working system, license lost after
a hardware replacement / reimage, and unexplained drops into “Viewing
Mode.” The standard hand-off to license@daq.net should be pre-staged to
avoid a round trip.


### Typical symptoms


  - Red “Viewing Mode” banner in Starwatch; user can view maps and edit
    graphics but cannot manage people, credentials, or rights.

  - “License must be renewed on this product” after activating on a
    replacement server.

  - RSM / workstation shows Offline with a prompt to restart services,
    but restarting services does not clear the state.

  - Support key or product key needed urgently for a new install or
    reimage.

  - Installer / support password unknown when trying to renew a license
    from Management Console.

  - Trial version keeps dropping into comm fail and the customer has an
    imminent deadline.


### Likely causes


  - License tied to the original hardware fingerprint and not yet
    re-issued after a drive swap or new server.

  - Administrator role permissions reduced (intentionally or
    accidentally), producing behavior that looks identical to Viewing
    Mode.

  - Licensed workstation count exceeded — an additional or replacement
    OPWS counts against the limit.

  - License renewal email to license@daq.net not yet actioned.

  - Default installer / support password was changed on-site and not
    documented.


### Diagnostic checklist


1.  Check System → License in Management Console. Capture the exact
    error text and product key.

2.  Check the Administrator role’s Person Management and Site Management
    rights — if reduced, Viewing Mode is actually a role problem, not a
    license problem.

3.  Confirm the server hostname and, if the server was replaced, the
    hardware ID. The license may have been issued against the old
    fingerprint.

4.  Verify whether licenses were emailed to license@daq.net and exactly
    which .lic attachment was sent; several tickets delayed because the
    attached file was wrong.

5.  Count workstations (RSM/OPWS) actually registered against the
    current license; if over the limit, adding another puts the system
    into Viewing Mode.


### Resolution steps


1.  For Viewing Mode caused by role reduction: log in as a user whose
    role still has Role Management rights, re-grant Person Management
    and Site Management to Administrator, save, and have the affected
    user restart Starwatch. If no such user exists, a DB restore to
    before the rights change is required.

2.  For license renewal on replacement hardware: email license@daq.net
    with server hostname, product key, exact error text, and the .lic
    file; do not run repeated activation attempts in the meantime
    because each attempt can consume state.

3.  For workstation-count-exceeded Viewing Mode: remove retired
    workstations from the Workstations list before registering the new
    one.

4.  For trial systems dropping into comm fail before a deadline:
    prioritize the license email; communicate to the customer that the
    trial is time-limited.

5.  For lost installer / support passwords: escalate to DAQ rather than
    guessing. One ticket shows an installer trying to guess and needing
    DAQ to reset.


### Related ticket IDs


*\#714, \#834, \#884, \#968, \#969, \#979, \#989, \#991, \#997, \#1007,
\#1018, \#1022, \#1023, \#1024, \#1042, \#1043, \#1049, \#1051, \#1086,
\#1090, \#1091, \#1092, \#1107, \#1115*


## 6. Workstation / OPWS can’t log in (domain / trust / registration)


Windows-side problems knock workstations out of service regularly. Two
distinct failure modes surface as “can’t log in”: the machine is no
longer accepted on the ICIDS / site domain, and the Starwatch
workstation record is stale after a database action. They are fixed in
different places.


### Typical symptoms


  - Windows login fails with “the security database on the server does
    not have a computer account for this workstation trust
    relationship.”

  - “We can’t sign you in with this credential because your domain is
    not available.”

  - “Unable to log onto logon servers” on an ICIDS PMC workstation —
    computer looks like it fell off the domain.

  - Starwatch login fails with “Failed to register new workstation. The
    workstation name is already registered.”

  - On a device server newly joined to the domain, Management Console /
    Task Manager / Services / Device Manager report “This app has been
    blocked by your system administrator.”

  - icidsadmin account locked after repeated wrong-password attempts.


### Likely causes


  - Machine left the domain (trust relationship broken) after extended
    downtime, a reimage, or password-age mismatch.

  - Imported database still lists a different workstation under the
    current machine name.

  - Group Policy from the newly joined domain is blocking admin tools on
    the device server.

  - BIOS / account lock on RMA hardware (one OPWS RMA came back with
    BIOS password locked).

  - Account lockout policy triggered on icidsadmin after troubleshooting
    attempts.


### Diagnostic checklist


1.  Try logging in as a local administrator first. If local works but
    domain fails, the issue is domain trust, not Starwatch.

2.  From another workstation check the computer account in Active
    Directory for the affected hostname.

3.  If the error mentions “workstation name already registered,” open
    Workstations in the SMS database; the current hostname is already
    recorded against a different record.

4.  On a device server where admin tools are blocked, run gpresult /
    rsop to identify which policy is blocking.

5.  For a locked icidsadmin: check the lockout counter and the site’s
    account-lockout policy length.


### Resolution steps


1.  For a broken trust relationship: remove the machine from the domain,
    reboot, rejoin, reboot — the canonical fix.

2.  For the “already registered” Starwatch error: delete the stale
    workstation record from the database, or rename the local machine
    before first launch.

3.  For a device server blocked by admin policy after joining:
    coordinate with base NEC / IT. Do not try to override by editing the
    registry — this is a policy issue, not a product issue.

4.  For an RMA unit locked at BIOS: return to DAQ for unlock rather than
    attempting BIOS resets on hardened hardware.

5.  For a locked icidsadmin account: have the customer’s domain admin
    unlock and reset the password; document the new password
    immediately.


### Related ticket IDs


*\#795, \#859, \#939, \#942, \#994, \#1026, \#1027, \#1052, \#1070,
\#1081, \#1104*


## 7. EntroStar panels not discoverable or not accepting new credentials


EntroStar-specific issues show up across a significant fraction of
hardware tickets. Symptoms fall into two groups: brand-new units that do
not appear in Site Planner’s Find Panel, and previously working units
that stop accepting new credentials or new configuration. There is one
DAQ-specific recovery trick every tech should know (USB factory reset
via entrostar.cmd) that resolves units that are otherwise unreachable.


### Typical symptoms


  - Out of a batch, a handful of EntroStar units never appear under Find
    Panel in Site Planner — powered but not discoverable.

  - “An attempt was made to access a socket in a way forbidden by its
    access permissions.”

  - “Network not available, no network adapters were found” when opening
    Find Panel.

  - Update Firmware option is greyed out even when the panel is online.

  - Panel’s Ethernet port locked up after an IP change; panel no longer
    responds on old or new IP (\#712 pattern).

  - New cards / profiles work on some panels but not a specific one;
    BACnet shows user sync stopping at a certain profile.

  - Door state inversions on a specific EntroStar (Normal → Unlocked,
    Unlock → Lock), with REX not affecting mag-lock state.


### Likely causes


  - Windows network / socket permission issue on the Site Planner
    workstation (not the panel itself).

  - Missing network adapter binding, or the workstation NIC is in a
    state that blocks UDP discovery.

  - Bad IP / subnet pushed to the panel leaves its Ethernet port locked
    out to the discovery tool.

  - Panel at credential capacity or sync stuck on a malformed profile.

  - PoE power insufficient when door strikes energize, causing the panel
    to reboot (documented with two portals on PoE-only).

  - Configuration duplicated from a working panel but a subtle field
    (for example output polarity) still differs.


### Diagnostic checklist


1.  Run Find Panel from a different workstation. If other workstations
    see the panels, the issue is the first workstation’s NIC / socket
    state, not the panels.

2.  Check the workstation’s firewall / AV — Site Planner uses UDP
    discovery that some enterprise AV blocks silently.

3.  For panels that power but never discover after 30–60 minutes, swap
    the Ethernet cable and port before assuming the unit is DOA.

4.  For sync stuck on a specific profile, identify that profile in
    BACnet Browser and export it — a specific credential often contains
    invalid data that blocks the rest of the batch.

5.  For EntroStar reboots on valid access, watch the switch’s port power
    draw at strike actuation. PoE budget shortages cause reboots only
    under load.


### Resolution steps


1.  For an EntroStar whose Ethernet is locked after a bad IP change, use
    the USB factory-reset procedure (\#712): create a file named
    entrostar.cmd on a USB flash drive containing a single line
    factory,reset (note the comma between factory and reset, and make
    sure the file is saved with extension .cmd not .cmd.txt). Insert
    into the panel’s USB A socket, power-cycle the panel, and on startup
    the panel executes the file, creates an entrostar.log, renames the
    .cmd to .bak, and resets IP to auto-IP / DHCP so it becomes
    discoverable again.

2.  For socket / no-adapter errors in Site Planner, restart the Site
    Planner workstation; if that fails, reinstall Site Planner on that
    workstation.

3.  For panels stuck undiscovered after cable and port swaps, RMA the
    specific unit rather than spending more time — the pattern held
    across multi-unit batches.

4.  For sync stopped on a profile, delete and re-create that specific
    profile, then clear the EntroStar and let it resync.

5.  For PoE-induced reboots, move the strike/mag-lock load off PoE onto
    a dedicated supply; keep PoE for the panel and reader only.

6.  For door-state inversions, compare Site Planner outputs and polarity
    fields against a known-good panel at the same site, not a panel from
    a different site.


### Related ticket IDs


*\#712, \#740, \#760, \#819, \#850, \#856, \#908, \#934, \#969, \#973,
\#987, \#1003, \#1014, \#1025, \#1064, \#1089, \#1097, \#1104, \#1110,
\#1117*


## 8. Zone / widget / map issues in Site Planner and Starwatch


Map and widget problems became more common after the ICIDS IV → ICIDS V
/ Starwatch 5.5.60x upgrades and now represent the second-largest
category in the dataset. Zones appear but are not interactable, widgets
do not render, or the wrong map calls up on alarm.


### Typical symptoms


  - A zone appears only in the Navigator pane in Site Planner with a
    yellow icon (not associated with any map), and all right-click
    options are greyed out except Properties; Properties fields are also
    greyed.

  - Operators cannot see a commissioned zone on the site map — the zone
    is blacked out even after rights are re-granted and Starwatch is
    restarted.

  - Summary status map pops up on alarm instead of the zone-specific map
    (ICIDS V widget auto-assignment).

  - New zone added to the RPI does not appear when trying to place it on
    a map.

  - After making a device-widget change in Site Planner and saving,
    Starwatch stops displaying any devices.

  - SCIF / PC missing widget files for sensor mapping.


### Likely causes


  - Zone was created but never associated with a map; without the
    association Site Planner treats it as an orphan and greys out most
    commands.

  - ICIDS V widget auto-assignment locks a widget to the first zone it
    is placed with, and that assignment cannot currently be overridden
    in Device Manager.

  - Widget files (.widget) not deployed to the workstation / SCIF PC —
    Site Planner can reference them but cannot render them.

  - Rights cache on the Operator workstation not fully cleared even
    after a Starwatch restart.


### Diagnostic checklist


1.  For a greyed-out zone: check whether it has a parent map in Site
    Planner’s tree. An orphan (no parent) is the expected cause of
    greyed commands.

2.  For a blacked-out zone at the operator station: confirm the zone
    exists in both the server’s Site Planner and the remote
    workstation’s local cache — sometimes the workstation has a stale
    copy.

3.  For missing widgets: compare the widgets folder on the affected
    workstation against a working workstation.

4.  For alarm call-up landing on the wrong map: open the zone’s widget
    binding in the map editor and confirm it is pointing to the correct
    zone, not an auto-assigned summary widget.


### Resolution steps


1.  Assign the orphan zone to a map (drag onto a parent in Site
    Planner), save to the database, and its commands become active
    again.

2.  For blacked-out zones at operators: remove the operator’s rights to
    that zone, save, re-grant rights, save, and restart Starwatch on
    that specific workstation (not just the server).

3.  For wrong-map alarm call-up after ICIDS V upgrade: remove the
    summary-status widget from the map being incorrectly called up, or
    accept the current behavior until DAQ exposes a Device Manager
    override.

4.  For missing widget files: copy the widget set from a working SCIF PC
    and restart Starwatch / Operator.


### Related ticket IDs


*\#959, \#978, \#998, \#1004, \#1039, \#1041, \#1042, \#1044, \#1047,
\#1055, \#1057, \#1058, \#1059, \#1060, \#1064, \#1066, \#1068, \#1076,
\#1077, \#1083, \#1088, \#1093, \#1097, \#1104, \#1114, \#1116*


## 9. Time, clock, and schedule problems


Time drift on controllers and keypads shows up as wrong clocks,
automations that do not fire at the scheduled time, and events
timestamped incorrectly. Most of these are resolved by confirming the
authoritative time source and pushing a time-sync after any DST
transition, install, or firmware update.


### Typical symptoms


  - Controller time off by exactly one hour (daylight-saving-time
    pattern).

  - Remote / StarPad keypad displays the wrong time.

  - Scheduled door-unlock automation does not execute at the specified
    time, but the same command works fine when manually executed.

  - Event reports show incorrect time stamps.


### Likely causes


  - Controller not syncing with the server’s time source, or the
    server’s DST rules differ from the controller’s.

  - Time zone configured differently on the controller vs the server.

  - Remote keypad did not receive a time push after the last site
    update.

  - Automations evaluated against controller clock, not server clock, so
    automations miss a drifted window.


### Diagnostic checklist


1.  Compare time on the server, application server, controller, and
    keypad at the same instant. A one-hour delta usually means DST.

2.  Confirm which device is the authoritative time source for this site.

3.  In Site Planner check the automation’s schedule and the controller’s
    local clock at the scheduled time.


### Resolution steps


1.  Push a time-sync command from Management Console / Site Planner to
    all controllers after any DST transition, new install, or firmware
    update.

2.  Set the controller’s time zone explicitly; do not rely on inheriting
    it from the server.

3.  For a remote keypad displaying wrong time: reboot the keypad, then
    issue a time-sync to the parent panel.

4.  For automations that do not fire: once clocks agree, re-test. If
    they still do not fire, check that the target device is online at
    the trigger time and not in an override state.


### Related ticket IDs


*\#731, \#758, \#766, \#796, \#891, \#897, \#930, \#987, \#988, \#1009,
\#1016, \#1017, \#1027, \#1043, \#1109*


## 10. SCIF PIC / PIN and new-CAC enrollment failures


SCIF sites surface their own class of enrollment problems, especially
after a database restore, drive swap, or reimage. New PICs / PINs and
newly registered CAC cards look enrolled in Starwatch but do not
authenticate at the keypad or reader. This is the largest single
category in the dataset at 131 tickets.


### Typical symptoms


  - All CAC cards registered after a given date return Unregistered ID
    at any reader; CAC cards registered earlier still work, and prox
    cards are unaffected.

  - New persons can be created and PICs issued in Starwatch, but the
    PICs do not work at the SCIF.

  - SCIF “not accepting new PICs / PINs” — forcing an update moves Sync
    Status from Busy to Good but the new codes still fail.

  - RADC in a SCIF keeps rebooting every 45 seconds.

  - SCIF WS reconfigured / DB transferred, after which new PIC users no
    longer authenticate.


### Likely causes


  - Database restored from a point before the last card-format or SMS
    update, leaving new credentials invisible to the panel.

  - Card format silently changed at a specific date and new enrollments
    now use a format the reader is not configured for.

  - Disk-level change during upgrade (BitLocker, etc.) prevented
    credentials from propagating to the panel firmware.

  - After an outage, SCIF panels need an explicit PIC push — not just a
    Sync (\#738 pattern).

  - Rebooting RADC: power, PoE, firmware regression, or grounding in the
    SCIF rack.


### Diagnostic checklist


1.  Pick one CAC card that used to work and one newly enrolled card.
    Present both. If old works and new fails at every reader, the
    problem is a format / sync issue, not a panel problem.

2.  In BACnet Browser confirm the new credential actually exists on the
    panel — not just in the server database.

3.  Compare the Card Format on the reader config against the format used
    when the new card was enrolled.

4.  For a looping RADC: swap power supply, then swap RADC, then check
    the USB / fiber path. The exactly \~45-second reboot pattern usually
    points to a watchdog timeout rather than a pure power issue.


### Resolution steps


1.  If new credentials are not on the panel, factory-reset the panel
    from BACnet and re-link (\#837 procedure): first disable the panel
    on the system to prevent the factory mode from being re-asserted,
    then use BACnet Browser to read CREDENTIAL\_DATA\_INPUT 1 to verify
    supported card formats and the present value after a card swipe.

2.  If a card-format cutover date exists, revert the reader / panel
    configuration to the prior format, or reconfigure the reader to the
    new format depending on what the site standard is going forward.

3.  After a DB transfer to a new SCIF machine, run a full re-sync from
    Management Console and push an explicit credential reload to each
    affected RADC before declaring the transfer complete.

4.  After an outage, send a PIC download to the SCIF panels explicitly;
    a Sync alone has repeatedly failed to restore PIC authentication
    (\#738).

5.  For a RADC rebooting every 45 seconds, escalate with photos, serial
    number, and firmware build — multiple tickets ended with an RMA on
    the affected board.


### Related ticket IDs


*\#738, \#795, \#859, \#966, \#979, \#994, \#1002, \#1068, \#1070,
\#1074, \#1075, \#1077, \#1079, \#1080, \#1083, \#1085, \#1086, \#1089,
\#1090, \#1094, \#1104, \#1108, \#1112*


## 11. Firmware, controller, RPI, and IAC updates


Firmware-related tickets hit sixty-six times across the period and mix
three kinds of work: planned updates (MachCheckPoint, EntroStar 1.4.4x
series, IAC-3, CallistoView), unplanned regressions introduced by an
update, and recovery work on units that went sideways during an update.
Treat every firmware push as a change-control event.


### Typical symptoms


  - MachCheckPoint firmware mismatch — some panels accept new
    credentials, some do not, same site.

  - Update Firmware option greyed out in Site Planner.

  - EntroStar Ethernet locked up after pushing an IP change (\#712).

  - Mux-bend comm fail after a master comm board or firmware change
    (\#733).

  - IAC-3 not responding after an update; RPI driver throwing errors in
    the trace log.

  - CallistoView keypad resets or goes blank after a version step (\#731
    → 5.5.38B fix).


### Likely causes


  - Firmware build mismatch across units in the same bend / site.

  - Update script aborted mid-way (Ethernet change applied before the
    discovery settings, or panel power-cycled during flash).

  - Hardware-specific regression between otherwise compatible firmware
    versions (1.4.41J → 1.4.45f left-open pattern).

  - RPI driver version not refreshed after a controller update.

  - CallistoView version older than the fix for a known keypad-reset
    issue.


### Diagnostic checklist


1.  List firmware version per unit for the bend / site and flag outliers
    before troubleshooting.

2.  If Update Firmware is greyed out, the panel is reporting a state
    that excludes the update (offline, busy, credential sync in
    progress). Resolve the upstream state first.

3.  For a post-update regression, capture the before/after behavior and
    attach an MCU or Orbit trace log to the ticket.

4.  For CallistoView keypad issues, note the current version;
    CallistoView 5.5.38B is the baseline that fixed the keypad-reset
    issue for StarPad (\#731).


### Resolution steps


1.  Recover locked-out EntroStars with the USB factory-reset procedure
    in Runbook 7 (entrostar.cmd / “factory,reset” / .cmd not .cmd.txt).

2.  Align firmware across a bend before declaring an update done; never
    leave a site with mixed versions in the same master.

3.  For an IAC-3 that does not respond after an update, power-cycle,
    check RPI driver logs, and if unresponsive reflash using the
    documented recovery path. Escalate with trace logs if the unit does
    not come back.

4.  For a known-regression firmware build, roll back if the customer’s
    risk posture allows it; otherwise document the regression on the
    ticket and keep the ticket open until DAQ releases a fixed build.

5.  For CallistoView-linked keypad issues, step to 5.5.38B or later
    before replacing hardware.

6.  Mux-bend recovery after a firmware or hardware change follows the
    single-card isolation procedure documented in Runbook 3.


### Related ticket IDs


*\#712, \#720, \#731, \#733, \#1017, \#1027, \#1029, \#1034, \#1036,
\#1042, \#1047, \#1056, \#1057, \#1058, \#1067, \#1080, \#1085, \#1088,
\#1089, \#1099, \#1102, \#1103, \#1106, \#1117*


## 12. Install, upgrade, and server migration


Install/upgrade/migration is fifty-three tickets in this window and
drives a disproportionate share of follow-on problems (licensing, backup
failures, credential sync gaps). Most failures here are about mismatched
versions, skipped prerequisite installers, or a migration that moved the
DB without re-syncing credentials.


### Typical symptoms


  - Fresh client install cannot connect to server — “unable to connect,
    see admin for software update.”

  - Post-install Starwatch comes up but cannot find Crystal Reports /
    reports fail (\#751).

  - After a server swap or upgrade, panels show comm fail where none
    existed before.

  - Migration completed but new PIC users added post-migration do not
    authenticate (Runbook 10 overlap).

  - Assure ID signature pad error “Object reference not set to an
    instance of an object” after a fresh SCIF install (\#753).

  - Upgrade to Starwatch 5.5.60x leaves some widgets unrendered (Runbook
    8 overlap).


### Likely causes


  - Installer prerequisites skipped — in particular the 32-bit and
    64-bit variants of a dependency (Crystal Reports, SQL Server
    Compact).

  - Client installer does not match the server build.

  - Post-migration DB points at a logical name that no longer matches
    the new machine.

  - Upgrade advanced a SCIF from an older Starwatch line without the
    corresponding Orbit / firmware prerequisites.

  - Install left behind stale workstation records in the DB that collide
    with the new hosts.


### Diagnostic checklist


1.  Pre-flight checklist: server exact version, backup retention,
    license state, prerequisite runtimes, .NET level, SQL level,
    firewall state on 6543.

2.  Confirm the StarWatchSMS-Redist package was actually run (separate
    from the main client exe). Ticket \#734 shows the minimum install
    sequence — Redist, then client exe, then point to server.

3.  For Crystal / reporting errors after a workstation move, confirm
    both 32-bit and 64-bit Crystal runtimes were installed (\#751).

4.  After a migration, explicitly exercise: a new person + PIC, a new
    credential push, one representative portal per RADC, and one
    automation.


### Resolution steps


1.  Match the workstation SMS build to the server’s build exactly before
    closing out an install.

2.  After a server migration, push an explicit credential reload to each
    RADC and verify a newly created PIC on one representative portal per
    panel before leaving the site.

3.  For the Crystal error, install both the 32-bit and 64-bit Crystal
    runtimes and restart Starwatch (\#751).

4.  For Assure ID integration, confirm the database connection works
    with Assure ID launched standalone before wiring it into Starwatch,
    then re-check the SCIF vs RSM topology because the Assure ID
    connection string differs on a SCIF (which hosts the SQL instance)
    vs an RSM (which points across the network).

5.  For stale-workstation collisions after migration, clean up
    Workstations in the DB before first launch on each new host.

6.  Pair every new install with Runbook 2’s backup-retention settings on
    day one — the Firelake investigation, the Rock Island SCIF
    retrieval, and the Fort Carson SCIF transfer all escalated because
    the site left default Replace-on-backup in place.


### Related ticket IDs


*\#723, \#734, \#747, \#751, \#753, \#1018, \#1024, \#1030, \#1036,
\#1037, \#1040, \#1042, \#1049, \#1058, \#1059, \#1060, \#1074, \#1083,
\#1091, \#1092, \#1106, \#1107, \#1108, \#1111, \#1112*


## 13. Performance, crashes, and BSOD


Performance tickets are smaller in count than hardware or map problems
but tend to be noisy on the customer side (users perceive it as
instability). Patterns cluster around aging hardware (10-year-old
workstations), overloaded databases (hundreds of thousands of events),
and specific component regressions.


### Typical symptoms


  - Starwatch hangs or freezes after \~20 minutes of use.

  - BSOD / memory-management errors on an aging workstation.

  - 100% disk utilization with Starwatch as the biggest contributor.

  - StarPad keypad resets itself / comes up blank (\#731).

  - Mux card chirping or cycling under load (Runbook 3 overlap).

  - Reports take minutes to run and sometimes time out.


### Likely causes


  - End-of-life workstation hardware (spinning disk, low RAM).

  - Database overgrown with expired credentials and raw event history
    (hundreds of thousands of events observed at Detrick).

  - SQL transaction log not truncated (Runbook 2 overlap).

  - Specific component regression (older CallistoView builds have the
    known keypad-reset issue).

  - Background AV scanning Starwatch working directories in real time.


### Diagnostic checklist


1.  Task Manager → sort by disk and memory for five minutes of typical
    use; capture the top three processes.

2.  Open Event Viewer for the window around the freeze / BSOD; look for
    the exact bugcheck code.

3.  SQL Management Studio: check event / history table size and
    transaction log size.

4.  Confirm whether Starwatch working directories are excluded from
    real-time AV scans.

5.  Check the workstation’s hardware age and disk health (SMART).


### Resolution steps


1.  For aging workstations, plan a replacement rather than chasing
    transient fixes; communicate lifecycle to the customer.

2.  For overgrown databases, schedule a maintenance pass: purge expired
    credentials, archive old events, truncate the transaction log.

3.  For CallistoView keypad resets, step to 5.5.38B or later (\#731).

4.  Add Starwatch working folders to the AV exclusion list.

5.  For BSOD / memory-management on a specific host, run the hardware
    vendor’s diagnostic before replacing anything; multiple tickets here
    resolved by swapping a failing RAM DIMM.


### Related ticket IDs


*\#731, \#733, \#841, \#855, \#857, \#897, \#910, \#911, \#933, \#948,
\#949, \#958, \#960, \#984, \#996, \#1017, \#1042, \#1057, \#1074,
\#1095, \#1102, \#1107*


## 14. Reports, exports, and imports


Reports / export / import is small in count (fourteen tickets) but
recurs because the same operations are needed on every new site:
exporting a portal list, producing audit reports, importing a CSV of
personnel, bringing Assure ID into a Starwatch install. Most failures
here are either missing runtime prerequisites or a mismatch between
import file columns and Starwatch’s person-type model.


### Typical symptoms


  - “Cannot find Crystal Reports” after moving Starwatch to a new
    workstation.

  - CSV import runs but persons land with wrong card type or wrong
    person group.

  - Need to export a portal list with names / types / associated panels
    and there is no obvious way in Site Builder.

  - Assure ID launches but cannot see SMS fields.

  - Custom report times or counts look wrong after a DST change (Runbook
    9 overlap).


### Likely causes


  - Missing 32-bit or 64-bit Crystal Reports runtime (\#751).

  - Single CSV import used for multiple person types — the import
    applies one person-type, one card-type, one person-group per run.

  - Unaware of the Operator → Devices → Print → Excel export path
    (\#744).

  - Assure ID not pointed at the correct SMS database instance, or the
    SCIF vs RSM connection-string difference was missed (\#854).


### Diagnostic checklist


1.  For Crystal errors, confirm both 32-bit and 64-bit runtimes are
    installed.

2.  For CSV imports, split the file into one CSV per person-type before
    importing.

3.  For Assure ID field visibility, confirm Assure ID connects to the
    same SQL instance Starwatch uses, and confirm you are running it
    from a machine where that instance is reachable.


### Resolution steps


1.  Install both the 32-bit and 64-bit Crystal Reports runtimes and
    restart Starwatch (\#751).

2.  Split CSV imports per person type, map column headings to SMS fields
    (names do not need to match), and run one import per type (\#809).

3.  For a portal inventory export, use Operator → Devices, sort by
    Category, Print, and choose Export to Excel (\#744).

4.  For Assure ID on a new install, verify standalone Assure ID can
    create and edit templates before wiring it into Starwatch; then
    configure the DB connection string using the machine name and
    /SQLEXPRESS of the SCIF or server that hosts the DB (\#854, \#747).


### Related ticket IDs


*\#744, \#747, \#751, \#809, \#837, \#854, \#870, \#897, \#973, \#996,
\#1014, \#1030, \#1040, \#1049, \#1050*


## Cross-cutting best practices


These practices are not tied to a specific runbook. They are patterns
observed across categories that, if applied consistently, would have
reduced the severity of several incidents in the source data.


### Before touching anything, capture state


Every high-severity ticket that went sideways shared one trait: the
on-site tech started making changes before grabbing logs or a backup.
For any non-trivial issue, collect the Starwatch logs folder, the
Windows Event Viewer log, the Orbit trace log, and a database backup
before starting. If the problem is already a restore-from-backup, also
grab the .BAK you are about to restore from.


### Keep multiple backups, not one


The Firelake investigation, the Rock Island SCIF database retrieval, and
the Fort Carson SCIF transfer all traced back to the same root cause:
the scheduled backup was set to Replace rather than Retain, so the last
known-good database was gone by the time anyone noticed a problem.
Default every new install to retain at least seven daily backups on a
drive that will still exist after a reimage. Cap total retention so the
disk-full condition in \#723 does not repeat.


### Confirm version parity before onsite work


Multiple login, Orbit, and comm-fail tickets resolved once the customer
matched the workstation SMS build to the server’s build. Before
dispatching or coaching onsite, ask the customer for the server’s exact
SMS version and build date and confirm their installer matches. Do the
same for CallistoView and EntroStar firmware.


### Document what Orbit.Net and Services restart fixes mean


Restarting Orbit.Net or SMS services temporarily clears a large share of
comms-fail tickets. Treat this as diagnostic information, not a
resolution. If a site needs an Orbit restart to stay online, the ticket
should escalate with Orbit trace logs from the window around the drop,
not close as “restart fixed it.”


### Track firmware changes as a change-control event


Several unrelated problems (EntroStar left-open alarms after 1.4.41J →
1.4.45f, the post-594 comm-fail spike, the post-604 Index Out Of Range
at Fort Polk, the StarPad keypad reset pre-5.5.38B) all traced to a
specific firmware or SMS build. Maintain a site-by-site record of
installed firmware and SMS build so that when a new issue appears, the
first question can be “what changed on this site in the last thirty
days.”


### Standardize the license-renewal hand-off


Licensing tickets routinely hit High priority because systems are
effectively down. Pre-stage a short form for installers that captures
server hostname, product key, exact error text, the current workstation
count, and what hardware was replaced, and include it in the first email
to license@daq.net so the license team does not need a round trip.
Attach the .lic file rather than pasting its contents into the email
body.


### Know the EntroStar USB factory-reset trick


When an EntroStar’s Ethernet is locked out and it is no longer
discoverable from Site Planner, create a file named entrostar.cmd on a
USB flash drive whose only content is the single line factory,reset
(comma between factory and reset; save as .cmd not .cmd.txt). Insert the
drive into the panel’s USB A socket and power-cycle the panel. On
successful execution the panel writes an entrostar.log, renames the .cmd
to .bak, and returns to auto-IP / DHCP so it is discoverable again. This
is the canonical recovery path on ticket \#712 and has resurfaced
repeatedly.


### Treat ICIDS V widget auto-assignment as a known quirk


ICIDS V auto-binds widgets to the first zone placed on a map and
currently does not allow override in Device Manager. Put that in
onboarding notes so new techs stop retrying the override and instead
remove / re-place the widget correctly the first time.


### Do not let one card format per facility code slip


The Fort Detrick investigation (\#720) took 720,000 unattributed events
to untangle because multiple card formats shared facility code 102 with
different string formats. Enforce one card format per facility code at
setup, with a consistent string format (for example “00-” for FC 102).
When cleaning up after the fact, delete unused formats (they delete
cleanly if nothing is using them), re-register the affected cards, and
restart Orbit manually so PASSDB resyncs properly.


## Appendix: source data


Source file: hesk\_tickets-055804b2.csv (HESK SQL export joining
hesk\_tickets and hesk\_replies, semicolon-delimited).

Total tickets in scope: 404.

Date range: January 4, 2023 – April 13, 2026.

Status distribution: 390 Resolved, 7 Waiting Reply, 7 Replied. Category
distribution at ingestion is uniform (all tickets tagged “General”); the
category table earlier in this document is a derived classification
based on full-thread keyword matching against subject, initial message,
and staff replies.

Priority distribution: 234 Low, 99 High, 71 Medium. 387 of the 404
tickets (96%) had at least one staff reply, which is what made it
possible to capture the resolution patterns documented in the runbooks.

Most-active customer organizations by email domain: Security 2000 /
security2k.com (134), army.mil (35), Evergreen Fire & Security (31),
Firelake Construction (19), Minuteman Security Solutions / mmss.one
(18), ES2 Built (17), Minuteman Security Solutions /
minutemansecuritysolutions.com (14), ICIDS-V (13), Core Controls (10).

---

*© DAQ Electronics, LLC*

