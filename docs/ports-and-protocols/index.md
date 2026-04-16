---
layout: default
title: StarWatch SMS Ports and Protocols
nav_order: 20
---

# StarWatch SMS Ports and Protocols

Technical reference listing the network ports, transports, encryption, session types, applications, usage, wire protocols, and proprietors involved in a StarWatch SMS deployment.

*Rev. 001*

| Port  | Transport | Encryption                    | Session          | Application                 | Usage                                                                    | Protocol      | Proprietary |
|-------|-----------|-------------------------------|------------------|-----------------------------|--------------------------------------------------------------------------|---------------|-------------|
| 6543  | TCP       | FIPS 102-3                    | WCF              | SMS Client/Server           | Viewing and modifying SMS database data                                  | Private       | DAQ         |
| 6123  | TCP       | FIPS 102-3                    | WCF              | SMS Notifications           | Receiving database change notifications                                  | Private       | DAQ         |
| 7101  | TCP       | FIPS 102-3                    | WCF              | SMS Messaging               | Distributing real-time data                                              | Orbit.NET     | DAQ         |
| 4662  | TCP       | FIPS 102-3                    | WCF              | Site Browser                | Diagnostic real-time network browsing                                    | Orbit.NET     | DAQ         |
| 47808 | UDP       | BACnet Security (optional)    | UDP Socket       | BACnet Browser              | Diagnostic real-time BACnet browsing                                     | BACnet/IP     | ASHRAE      |
| 47809 | UDP       | BACnet Security (optional)    | UDP Socket       | EntroStar Driver            | Communication with EntroStar panels                                      | BACnet/IP     | ASHRAE      |
| 47810 | UDP       | BACnet Security               | UDP Socket       | Site Planner / Builder      | Discovery via BACnet of EntroStar panels                                 | BACnet/IP     | ASHRAE      |
| 48700 | UDP       | Class-B                       | UDP Socket       | RPI Driver                  | Communication with ICIDS panels                                          | RPI/IP        | DAQ         |
| 50231 | UDP       | RSA 512-bit                   | Multicast Groups | DAQ Panel Net Config        | Discovery and network configuration of all DAQ panels                    | DAQ Discovery | DAQ         |
| 1433  | TCP       | TLS 1.2–1.2 with Certificates | TCP              | SQL Server / Clients        | Asure ID badging on workstations                                         | Private       | Microsoft   |
| 1434  | UDP       | None                          | UDP Socket       | SQL Server Browser/Clients  | Remote browsing and connection to SQL Server (may be needed for Asure ID)| Private       | Microsoft   |

## Notes

- **FIPS 102-3** denotes DAQ's internal FIPS-compliant encryption profile used across the SMS WCF channels (ports 6543, 6123, 7101, 4662).
- **BACnet Security** on ports 47808 and 47809 is optional and typically enabled only when the deployment requires it; port 47810 always uses BACnet Security for discovery.
- **Asure ID** workstations require outbound access to SQL (port 1433) and, for remote browsing, port 1434.
- DAQ-proprietary ports (6543, 6123, 7101, 4662, 48700, 50231) should be opened only on the segments carrying StarWatch SMS traffic.

---

*© DAQ Electronics, LLC*
