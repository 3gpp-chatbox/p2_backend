|  |
|---|
| 3GPPPostal address3GPP support office address650 Route des Lucioles - Sophia AntipolisValbonne - FRANCETel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16Internethttp://www.3gpp.org |
| Copyright NotificationNo part may be reproduced except as authorized by written permission.The copyright and the foregoing restriction extend to reproduction in all media.©2024, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC).All rights reserved.UMTS™ is a Trade Mark of ETSI registered for the benefit of its members3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersLTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational PartnersGSM® and the GSM logo are registered and owned by the GSM Association |

# Foreword

This Technical Specification has been produced by the 3rd Generation Partnership Project (3GPP).

The contents of the present document are subject to continuing work within the TSG and may change following formal TSG approval. Should the TSG modify the contents of the present document, it will be re-released by the TSG with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

x the first digit:

1 presented to TSG for information;

2 presented to TSG for approval;

3 or greater indicates TSG approved document under change control.

y the second digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been incorporated in the document.

# 1 Scope

The present document specifies the non-access stratum (NAS) procedures in the 5G system (5GS) used by the protocols for:

- mobility management between the user equipment (UE) and the access and mobility management function (AMF) for both 3GPP access and non-3GPP access; and

- session management between the user equipment (UE) and the session management function (SMF) for both 3GPP access and non-3GPP access.

The 5GS mobility management (5GMM) protocol defined in the present document provides procedures for the control of mobility when the user equipment (UE) is using the NG radio access network (NG-RAN), non-3GPP access network, or both. The 5GMM protocol also provides control of security for the NAS protocols.

The 5GS session management (5GSM) protocol defined in the present document provides procedures for the handling of 5GS PDU sessions. Together with the bearer control provided by the access stratum, this protocol is used for the control of user-plane resources.

For both NAS protocols the present document specifies procedures for the support of inter-system mobility between the NG-RAN and the evolved universal terrestrial radio access (E-UTRAN), between the NG-RAN and the non-3GPP access network connected to the EPC, and between the non-3GPP access network connected to the 5G core network (5GCN) and the E-UTRAN.

For both NAS protocols the present document specifies procedures for the support of mobility between the NG-RAN and the non-3GPP access network connected to the 5GCN.

In addition, the present document specifies the procedures in the 5GS for UE policy delivery service between the UE and the policy control function (PCF) for both 3GPP access and non-3GPP access.

The present document is applicable to the UE, the access and mobility management function (AMF), the session management function (SMF), and the PCF in the 5GS.

The clauses and subclauses in the present document are common for both 3GPP access and non-3GPP access unless it is explicitly stated that they apply to 3GPP access only or non-3GPP access only.

# 2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.

- For a specific reference, subsequent revisions do not apply.

- For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same Release as the present document.

[1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications".

[1A] 3GPP TS 22.011: "Service accessibility".

[2] 3GPP TS 22.101: "Service aspects; Service principles".

[3] 3GPP TS 22.261: "Service requirements for the 5G system; Stage 1".

[4] 3GPP TS 23.003: "Numbering, addressing and identification".

[4A] 3GPP TS 23.040: "Technical realization of Short Message Service (SMS)".

[4B] 3GPP TS 23.032: "Universal Geographical Area Description (GAD)".

[5] 3GPP TS 23.122: "Non-Access-Stratum functions related to Mobile Station (MS) in idle mode".

[6] 3GPP TS 23.167: "IP Multimedia Subsystem (IMS) emergency sessions".

[6A] 3GPP TS 23.216: "Single Radio Voice Call Continuity (SRVCC); Stage 2".

[6AB] 3GPP TS 23.256: "Support of Uncrewed Aerial Systems (UAS) connectivity, identification and tracking; Stage 2".

[6B] 3GPP TS 23.273: "5G System (5GS) Location Services (LCS); Stage 2".

[6C] 3GPP TS 23.287: "Architecture enhancements for 5G System (5GS) to support Vehicle-to-Everything (V2X) services".

[6D] 3GPP TS 23.316: "Wireless and wireline convergence access support for the 5G System (5GS)".

[6E] 3GPP TS 23.304: "Proximity based Services (ProSe) in the 5G System (5GS)".

[7] 3GPP TS 23.401: "GPRS enhancements for E-UTRAN access".

[8] 3GPP TS 23.501: "System Architecture for the 5G System; Stage 2".

[9] 3GPP TS 23.502: "Procedures for the 5G System; Stage 2".

[10] 3GPP TS 23.503: "Policy and Charging Control Framework for the 5G System; Stage 2".

[10A] 3GPP TS 23.548: "5G System Enhancements for Edge Computing; Stage 2".

[11] 3GPP TS 24.007: "Mobile radio interface signalling layer 3; General aspects".

[12] 3GPP TS 24.008: "Mobile Radio Interface Layer 3 specification; Core Network Protocols; Stage 3".

[13] 3GPP TS 24.011: "Point-to-Point Short Message Service (SMS) support on mobile radio interface".

[13A] 3GPP TS 24.080: "Mobile radio interface layer 3 Supplementary services specification; Formats and coding".

[13B] 3GPP TS 24.193: "Access Traffic Steering, Switching and Splitting; Stage 3".

[13C] 3GPP TS 24.173: "IMS Multimedia telephony communication service and supplementary services; Stage 3".

[13D] 3GPP TS 24.174: "Support of multi-device and multi-identity in the IP Multimedia Subsystem (IMS); Stage 3".

[14] 3GPP TS 24.229: "IP multimedia call control protocol based on Session Initiation Protocol (SIP) and Session Description Protocol (SDP); Stage 3".

[14AA] 3GPP TS 24.237: "IP Multimedia (IM) Core Network (CN) subsystem IP Multimedia Subsystem (IMS) service continuity; Stage 3".

[14A] 3GPP TS 24.250: "Protocol for Reliable Data Service; Stage 3".

[15] 3GPP TS 24.301: "Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS); Stage 3".

[16] 3GPP TS 24.302: "Access to the 3GPP Evolved Packet Core (EPC) via non-3GPP access networks; Stage 3"

[17] 3GPP TS 24.368: "Non-Access Stratum (NAS) configuration Management Object (MO)".

[18] 3GPP TS 24.502: "Access to the 3GPP 5G System (5GS) via non-3GPP access networks; Stage 3".

[19] 3GPP TS 24.526: "UE policies for 5G System (5GS); Stage 3".

[19BA] 3GPP TS 24.539: "5G System (5GS); Network to TSN translator (TT) protocol aspects; Stage 3".

[19A] 3GPP TS 24.535: "Device-Side Time-Sensitive Networking (TSN) Translator (DS-TT) to Network-Side TSN Translator (NW-TT) protocol aspects; Stage 3".

[19B] 3GPP TS 24.587: "Vehicle-to-Everything (V2X) services in 5G System (5GS); Protocol aspects; Stage 3"

[19C] 3GPP TS 24.588: "Vehicle-to-Everything (V2X) services in 5G System (5GS); User Equipment (UE) policies; Stage 3"

[19D] Void.

[19E] 3GPP TS 24.554: "Proximity-service (ProSe) in 5G System (5GS) protocol aspects; Stage 3".

[19F] 3GPP TS 24.555: "Proximity-services (ProSe) in 5G System (5GS); User Equipment (UE) policies; Stage 3".

[20] 3GPP TS 24.623: "Extensive Markup Language (XML) Configuration Access Protocol (XCAP) over the Ut interface for Manipulating Supplementary Services".

[20AA] 3GPP TS 29.500: "5G System; Technical Realization of Service Based Architecture; Stage 3".

[20A] 3GPP TS 29.502: "5G System; Session Management Services; Stage 3".

[20AB] 3GPP TS 29.503: "5G System; Unified Data Management Services; Stage 3".

[20B] 3GPP TS 29.518: "5G System; Access and Mobility Management Services; Stage 3".

[21] 3GPP TS 29.525: "5G System; UE Policy Control Service; Stage 3".

[21A] 3GPP TS 29.526: "5G System; Network Slice-Specific Authentication and Authorization (NSSAA) services; Stage 3".

[21B] 3GPP TS 29.256: "5G System; Uncrewed Aerial Systems Network Function (UAS-NF); Aerial Management Services; Stage 3.

[22] 3GPP TS 31.102: "Characteristics of the Universal Subscriber Identity Module (USIM) application".

[22A] 3GPP TS 31.111: "USIM Application Toolkit (USAT)".

[22B] 3GPP TS 31.115: "Secured packet structure for (Universal) Subscriber Identity Module (U)SIM Toolkit applications".

[23] 3GPP TS 33.102: "3G security; Security architecture".

[23A] 3GPP TS 33.401: "3GPP System Architecture Evolution; Security architecture".

[24] 3GPP TS 33.501: "Security architecture and procedures for 5G System".

[24A] 3GPP TS 33.535: "Authentication and Key Management for Applications (AKMA) based on 3GPP credentials in the 5G System (5GS)".

[24B] 3GPP TS 33.256: "Security aspects of Uncrewed Aerial Systems (UAS)".

[25] 3GPP TS 36.323: "NR; Packet Data Convergence Protocol (PDCP) specification".

[25A] 3GPP TS 36.331: "Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC) protocol specification".

[25B] 3GPP TS 36.300: "Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall description".

[25C] 3GPP TS 36.304: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) procedures in idle mode".

[25D] 3GPP TS 36.306: "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) radio access capabilities".

[25E] 3GPP TS 36.321: "Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification".

[26] 3GPP TS 37.355: "LTE Positioning Protocol (LPP)".

[26A] 3GPP TS 38.355: "Sidelink Positioning Protocol (SLPP); Protocol specification".

[27] 3GPP TS 38.300: "NR; NR and NG-RAN Overall Description; Stage 2".

[28] 3GPP TS 38.304: "New Generation Radio Access Network; User Equipment (UE) procedures in Idle mode".

[28A] 3GPP TS 38.306: "New Generation Radio Access Network; User Equipment (UE) radio access capabilities".

[29] 3GPP TS 38.323: "Evolved Universal Terrestrial Radio Access (E-UTRA); Packet Data Convergence Protocol (PDCP) specification".

[30] 3GPP TS 38.331: "NR; Radio Resource Control (RRC); Protocol Specification".

[31] 3GPP TS 38.413: "NG Radio Access Network (NG-RAN); NG Application Protocol (NGAP)".

[31A] IEEE Std 802.3™-2022: "Ethernet".

[31AA] 3GPP TS 38.509: "Special conformance testing functions for User Equipment (UE)".

[32] IETF RFC 768: "User Datagram Protocol".

[33] IETF RFC 793: "Transmission Control Protocol."

[33A] IETF RFC 3095: "RObust Header Compression (ROHC): Framework and four profiles: RTP, UDP, ESP and uncompressed".

[33B] Void.

[33C] Void.

[33D] IETF RFC 8415: "Dynamic Host Configuration Protocol for IPv6 (DHCPv6)".

[33E] IETF RFC 2131: "Dynamic Host Configuration Protocol".

[33F] IETF RFC 2132: "DHCP Options and BOOTP Vendor Extensions".

[34] IETF RFC 3748: "Extensible Authentication Protocol (EAP)".

[34A] IETF RFC 3843: "RObust Header Compression (ROHC): A Compression Profile for IP".

[35] Void.

[35A] IETF RFC 4122: "A Universally Unique IDentifier (UUID) URN Namespace".

[36] IETF RFC 4191: "Default Router Preferences and More-Specific Routes".

[36A] IETF RFC 5905: "Network Time Protocol Version 4: Protocol and Algorithms Specification".

[37] IETF RFC 7542: "The Network Access Identifier".

[38] IETF RFC 4303: "IP Encapsulating Security Payload (ESP)".

[38A] IETF RFC 4815: "RObust Header Compression (ROHC): Corrections and Clarifications to RFC 3095".

[38B] IETF RFC 4861: "Neighbor Discovery for IP version 6 (IPv6)".

[39] IETF RFC 4862: "IPv6 Stateless Address Autoconfiguration".

[39A] IETF RFC 5225: "RObust Header Compression (ROHC) Version 2: Profiles for RTP, UDP, IP, ESP and UDP Lite".

[39B] IETF RFC 5795: "The RObust Header Compression (ROHC) Framework".

[40] IETF RFC 5448: "Improved Extensible Authentication Protocol Method for 3rd Generation Authentication and Key Agreement (EAP-AKA')".

[40A] IETF RFC 6603: "Prefix Exclude Option for DHCPv6-based Prefix Delegation".

[40B] IETF RFC 6846: "RObust Header Compression (ROHC): A Profile for TCP/IP (ROHC-TCP)".

[41] IETF RFC 7296: "Internet Key Exchange Protocol Version 2 (IKEv2)".

[42] ITU-T Recommendation E.212: "The international identification plan for public networks and subscriptions", 2016-09-23.

[43] IEEE Std 802-2014: "IEEE Standard for Local and Metropolitan Area Networks: Overview and Architecture" (30 June 2014).

[43A] Void

[43B] IEEE Std 1588™-2019: "IEEE Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems".

[43C] Void.

[43D] Void.

[43E] Void.

[44] Void.

[45] Void.

[46] Void.

[47] Void.

[48] IEEE: "Guidelines for Use of Extended Unique Identifier (EUI), Organizationally Unique Identifier (OUI), and Company ID (CID)".

[49] BBF TR-069: "CPE WAN Management Protocol".

[50] BBF TR-369: "User Services Platform (USP)".

[51] 3GPP TS 37.340: "Evolved Universal Terrestrial Radio Access (E-UTRA) and NR; Multi-connectivity; Stage 2".

[52] IETF RFC 8106:"IPv6 Router Advertisement Options for DNS Configuration".

[53] 3GPP TS 23.247: "Architectural enhancements for 5G multicast-broadcast services; Stage 2".

[54] 3GPP TS 23.380: "IMS Restoration Procedures".

[55] IETF RFC 3948: "UDP Encapsulation of IPsec ESP Packets".

[56] 3GPP TS 33.503: "Security Aspects of Proximity based Services (ProSe) in the 5G System (5GS)".

[57] 3GPP TS 33.246: "Security of Multimedia Broadcast/Multicast Service (MBMS)".

[58] 3GPP TS 38.321: "NR; Medium Access Control (MAC); Protocol specification".

[59] IEEE Std 802.11™-2020: "Information Technology- Telecommunications and information exchange between systems-Local and metropolitan area networks-Specific requirements-Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications".

[60] 3GPP TS 24.577: "Aircraft-to-Everything (A2X) services in 5G System (5GS) protocol aspects; Stage 3".

[61] 3GPP TS 24.578: "Aircraft-to-Everything (A2X) services in 5G System (5GS); UE policies".

[62] 3GPP TS 24.514: "Ranging based services and sidelink positioning in 5G system (5GS); Stage 3".

[63] 3GPP TS 23.586: "Architectural Enhancements to support Ranging based services and Sidelink Positioning".

[64] 3GPP TS 24.572: "User Plane Location Services (LCS) Protocols And Procedures; Stage 3".

[65] 3GPP TS 24.575: "5G System; Multicast/Broadcast UE pre-configuration Management Object (MO)".

[66] IETF RFC 4291:" IP Version 6 Addressing Architecture".

[67] 3GPP TS 38.305: "Stage 2 functional specification of User Equipment (UE) positioning in NG-RAN".

[68] 3GPP TS 23.271: "Functional stage 2 description of Location Services (LCS)".

[69] 3GPP TS 26.522: "5G Real-time Media Transport Protocol Configurations".

[70] IETF RFC 8285: "A General Mechanism for RTP Header Extensions".

[71] IETF RFC 3550: "RTP: A Transport Protocol for Real-Time Applications".

# 3 Definitions and abbreviations

## 3.1 Definitions

For the purposes of the present document, the terms and definitions given in 3GPP TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in 3GPP TR 21.905 [1].

4G-GUTI: A GUTI defined in 3GPP TS 24.301 [15].

5GMM-IDLE mode: In this specification, if the term is used standalone, a UE in 5GMM-IDLE mode means the UE can be either in 5GMM-IDLE mode over 3GPP access or in 5GMM-IDLE mode over non-3GPP access.

5GMM-CONNECTED mode: In this specification, if the term is used standalone, a UE in 5GMM-CONNECTED mode means the UE can be either in 5GMM-CONNECTED mode over 3GPP access or in 5GMM-CONNECTED mode over non-3GPP access.

5GMM-IDLE mode over 3GPP access: A UE is in 5GMM-IDLE mode over 3GPP access when no N1 NAS signalling connection between the UE and network over 3GPP access exists. The term 5GMM-IDLE mode over 3GPP access used in the present document corresponds to the term CM-IDLE state for 3GPP access used in 3GPP TS 23.501 [8].

5GMM-CONNECTED mode over 3GPP access: A UE is in 5GMM-CONNECTED mode over 3GPP access when an N1 NAS signalling connection between the UE and network over 3GPP access exists. The term 5GMM-CONNECTED mode over 3GPP access used in the present document corresponds to the term CM-CONNECTED state for 3GPP access used in 3GPP TS 23.501 [8].

5GMM-IDLE mode over non-3GPP access: A UE is in 5GMM-IDLE mode over non-3GPP access when no N1 NAS signalling connection between the UE and network over non-3GPP access exists. The term 5GMM-IDLE mode over non-3GPP access used in the present document corresponds to the term CM-IDLE state for non-3GPP access used in 3GPP TS 23.501 [8].

5GMM-CONNECTED mode over non-3GPP access: A UE is in 5GMM-CONNECTED mode over non-3GPP access when an N1 NAS signalling connection between the UE and network over non-3GPP access exists. The term 5GMM-CONNECTED mode over non-3GPP access used in the present document corresponds to the term CM-CONNECTED state for non-3GPP access used in 3GPP TS 23.501 [8].

5GS services: Services provided by PS domain. Within the context of this specification, 5GS services is used as a synonym for EPS services.

5G-EA: 5GS encryption algorithms. The term 5G-EA, 5G-EA0, 128-5G-EA1, 128-5G-EA2, 128-5G-EA3, 5G-EA4, 5G-EA5, 5G-EA6 and 5G-EA7 used in the present document corresponds to the term NEA, NEA0, 128-NEA1, 128-NEA2, 128-NEA3, NEA4, NEA5, NEA6 and NEA7 defined in 3GPP TS 33.501 [24].

5G-IA: 5GS integrity algorithms. The term 5G-IA, 5G-IA0, 128-5G-IA1, 128-5G-IA2, 128-5G-IA3, 5G-IA4, 5G-IA5, 5G-IA6 and 5G-IA7 used in the present document corresponds to the term NIA, NIA0, 128-NIA1, 128-NIA2, 128-NIA3, NIA4, NIA5, NIA6 and NIA7 defined in 3GPP TS 33.501 [24].

Access stratum connection: A peer to peer access stratum connection:

- between the UE and the NG-RAN for 3GPP access;

- between the UE and the N3IWF for untrusted non-3GPP access;

- between the UE and the TNGF for trusted non-3GPP access used by the UE;

- within the TWIF acting on behalf of the N5CW device for trusted non-3GPP access used by the N5CW device;

- between the 5G-RG and the W-AGF for wireline access used by the 5G-RG;

- within the W-AGF acting on behalf of the FN-RG for wireline access used by the FN-RG; or

- within the W-AGF acting on behalf of the N5GC device for wireline access used by the N5GC device.

The access stratum connection for 3GPP access corresponds to an RRC connection via the Uu reference point. The creation of the access stratum connection for untrusted non-3GPP access corresponds to the completion of the IKE_SA_INIT exchange (see IETF RFC 7296 [41]) via the NWu reference point. The creation of the access stratum connection for trusted non-3GPP access used by the UE corresponds to the UE reception of an EAP-request/5G-start via NWt reference point (see 3GPP TS 23.502 [9]). The creation of the access stratum connection for trusted non-3GPP access used by the N5CW device corresponds to the TWIF's start of acting on behalf of the N5CW device. The creation of the access stratum connection for wireline access used by the 5G-RG corresponds to establishment of signalling connection using W-CP protocol stack via the Y4 reference point (see 3GPP TS 23.316 [6D]). The creation of the access stratum connection for wireline access used by the FN-RG corresponds to the W-AGF's start of acting on behalf of the FN-RG. The creation of the access stratum connection for wireline access used by the N5GC device corresponds to the W-AGF's start of acting on behalf of the N5GC device.

Access to SNPN services via a PLMN/To access SNPN services via a PLMN: A UE is accessing SNPN services via a PLMN when the UE is connecting to the 5GCN of the SNPN using the 3GPP access of the PLMN.

Aggregate maximum bit rate: The maximum bit rate that limits the aggregate bit rate of a set of non-GBR bearers of a UE. Definition derived from 3GPP TS 23.501 [8].

Alternative NSSAI: A list of mapping information between the S-NSSAI to be replaced and the alternative S-NSSAI.

Always-on PDU session: A PDU session for which user-plane resources have to be established during every transition from 5GMM-IDLE mode to 5GMM-CONNECTED mode. A UE requests a PDU session to be established as an always-on PDU session based on indication from upper layers and the network decides whether a PDU session is established as an always-on PDU session.

NOTE 1: How the upper layers in the UE are configured to provide an indication is outside the scope of the present document.

Applicable UE radio capability ID for the current UE radio configuration in the selected network: The UE has an applicable UE radio capability ID for the current UE radio configuration in the selected network if:

a) the UE supports RACS; and

b) the UE has:

1) a stored network-assigned UE radio capability ID which is associated with the PLMN ID or SNPN identity of the serving network and which maps to the set of radio capabilities currently enabled at the UE; or

2) a manufacturer-assigned UE radio capability ID which maps to the set of radio capabilities currently enabled at the UE.

Backhaul PLMN or backhaul SNPN (BH PLMN or BH SNPN): The term backhaul PLMN or backhaul SNPN (BH PLMN or BH SNPN) used in the present document corresponds to the term backhaul PLMN/SNPN (BH PLMN/SNPN) used in 3GPP TS 23.501 [8].

CAG cell: A cell in which only members of the CAG can get normal service. Depending on local regulation, the CAG cell can provide emergency services and emergency services fallback also to subscribers who are not members of the CAG.

CAG-ID: A CAG-ID is a unique identifier within the scope of one PLMN defined in 3GPP TS 23.003 [4] which identifies a Closed Access Group (CAG) in the PLMN associated with a cell or group of cells to which access is restricted to members of the CAG.

CAG restrictions: Restrictions applied to a UE in accessing a PLMN's 5GCN via:

a) a non-CAG cell if the entry for the PLMN in the UE's "CAG information list" includes an "indication that the UE is only allowed to access 5GS via CAG cells"; or

b) a CAG cell if none of the CAG-ID(s) supported by the CAG cell is authorized based on the "allowed CAG list" for the PLMN in the UE's "CAG information list".

The CAG restrictions are not applied in a PLMN when a UE accesses the PLMN due to emergency services or emergency services fallback.

Cleartext IEs: Information elements that can be sent without confidentiality protection in initial NAS messages as specified in subclause 4.4.6.

Configuration of SNPN subscription parameters in PLMN via the user plane: Configuration of a UE in a PLMN with one or more entries of the "list of subscriber data” via the user plane.

Control plane CIoT 5GS optimization: Signalling optimizations to enable efficient transport of user data (IP, Ethernet, Unstructured or SMS) over control plane via the AMF including optional header compression of IP data and Ethernet data.

Current TAI: A TAI of a selected PLMN broadcast in the cell on which the UE is camping. If the cell is a satellite NG-RAN cell broadcasting multiple TACs of the selected PLMN, the UE NAS layer selects the current TAI from these multiple TACs of the selected PLMN as specified in subclause 4.23.5.

NOTE 2: For the purpose of this definition, the selected PLMN can either be the registered PLMN or a PLMN selected according to PLMN selection rules as specified in 3GPP TS 23.122 [5].

DNN based congestion control: Type of congestion control at session management level that is applied to reject session management requests from UEs or release PDU sessions when the associated DNN is congested. DNN based congestion control can be activated at the SMF over session management level and also activated at the AMF over mobility management level.

DNN determined by the AMF: If no DNN requested by the UE is provided, a DNN determined by the AMF based subscription information or local policy. Otherwise DNN determined by the AMF is the DNN requested by the UE.

DNN requested by the UE: A DNN explicitly requested by the UE and included in a NAS request message.

DNN selected by the network: If DNN replacement applies, a DNN selected and indicated to the AMF by PCF. Otherwise DNN selected by the network is the DNN determined by the AMF.

Default S-NSSAI: An S-NSSAI in the subscribed S-NSSAIs marked as default.

Emergency PDU session: A PDU session established with the request type "initial emergency request" or "existing emergency PDU session".

General NAS level congestion control: Type of congestion control at mobility management level that is applied at a general overload or congestion situation in the network, e.g. lack of processing resources.

Globally-unique SNPN identity: An SNPN identity with an NID whose assignment mode is not set to 1 (see 3GPP TS 23.003 [4]).

Home country: The country of the HPLMN (see 3GPP TS 23.122 [5] for the definition of country).

HPLMN S-NSSAI: An S-NSSAI applicable in the HPLMN without any further mapping by the network. If the UE has an EHPLMN list which is not empty, then the HPLMN S-NSSAIs are applicable without any further mapping in the PLMN whose PLMN code is derived from the IMSI, regardless of whether or not this PLMN is included in the EHPLMN list.

The UE considers as HPLMN S-NSSAIs at least the following S-NSSAIs:

a) any S-NSSAI included in the configured NSSAI or allowed NSSAI for a PLMN or SNPN if it is provided by

1) the PLMN whose PLMN code is derived from the IMSI; or

2) the subscribed SNPN;

b) any S-NSSAI provided as mapped S-NSSAI for the configured NSSAI or allowed NSSAI or partially allowed NSSAI for a PLMN or SNPN;

c) any S-NSSAI associated with a PDU session if there is no mapped S-NSSAI associated with the PDU session and the UE is

1) in the PLMN whose PLMN code is derived from the IMSI; or

2) in the subscribed SNPN; and

d) any mapped S-NSSAI associated with a PDU session.

NOTE 3: The above list is not intended to be complete. E.g., also in case of PLMN the S-NSSAIs included in URSP rules or in the signalling messages for network slice-specific authentication and authorization are HPLMN S-NSSAIs.

In NB-N1 mode: Indicates this paragraph applies only to a system which operates in NB-N1 mode. For a multi-access system this case applies if the current serving radio access network provides access to network services via E-UTRA connected to 5GCN by NB-IoT (see 3GPP TS 36.300 [25B], 3GPP TS 36.331 [25A], 3GPP TS 36.306 [25D]).

In WB-N1 mode: Indicates this paragraph applies only to a system which operates in WB-N1 mode. For a multi-access system this case applies if the system operates in N1 mode with E-UTRA connected to 5GCN, but not in NB-N1 mode.

In WB-N1/CE mode: Indicates this paragraph applies only when a UE, which is a CE mode B capable UE (see 3GPP TS 36.306 [25D]), is operating in CE mode A or B in WB-N1 mode.Initial NAS message: A NAS message is considered as an initial NAS message, if this NAS message can trigger the establishment of an N1 NAS signalling connection. For instance, the REGISTRATION REQUEST message is an initial NAS message.

Initial registration for emergency services: A registration performed with 5GS registration type "emergency registration" in the REGISTRATION REQUEST message.

Initial registration for onboarding services in SNPN: A registration performed with 5GS registration type "SNPN onboarding registration" in the REGISTRATION REQUEST message.

Initial registration for disaster roaming services: A registration performed with 5GS registration type "disaster roaming initial registration" in the REGISTRATION REQUEST message.

Initial small data rate control parameters: Parameters that, if received by the UE during the establishment of a PDU session, are used as initial parameters to limit the allowed data for the PDU session according to small data rate control after establishment of a PDU session as described in subclause 6.2.13. At expiry of the associated validity period, the initial small data rate control parameters are no longer valid and the small data rate control parameters apply.

Initial small data rate control parameters for exception data: Parameters corresponding to initial small data rate control parameters for small data rate control of exception data.

Last visited registered TAI: A TAI which is contained in the registration area that the UE registered to the network and which identifies the tracking area last visited by the UE. If the cell is a satellite NG-RAN cell broadcasting multiple TAIs, a TAI which is contained in the registration area that the UE registered to the network and last selected by the UE as the current TAI.

Local release: Release of a PDU session without peer-to-peer signalling between the network and the UE.

NOTE 3A: Local release can include communication among network entities.

Mapped 5G-GUTI: A 5G-GUTI which is mapped from a 4G-GUTI previously allocated by an MME. Mapping rules are defined in 3GPP TS 23.003 [4].

Mapped S-NSSAI: An S-NSSAI in the subscribed S-NSSAIs for the HPLMN or the subscribed SNPN, to which an S-NSSAI of the registered PLMN (in case of a roaming scenario) or the registered non-subscribed SNPN is mapped.

MBSR-UE: a UE that is operating as a MBSR and supporting UE NAS functionalities specified in this specification.

Mobility registration for disaster roaming services: A registration performed with 5GS registration type "disaster roaming mobility registration updating" in the REGISTRATION REQUEST message.

MUSIM UE: A UE with multiple valid USIMs, capable of initiating and maintaining simultaneous separate registration states over 3GPP access with PLMN(s) using identities and credentials associated with those USIMs and supporting one or more of the N1 NAS signalling connection release, the paging indication for voice services, the reject paging request, the paging restriction and the paging timing collision control (see 3GPP TS 23.501 [8]).

MWAB broadcasted PLMN or MWAB broadcasted SNPN: The term MWAB broadcasted PLMN or MWAB broadcasted SNPN used in the present document corresponds to the term MWAB broadcasted PLMN/SNPN used in 3GPP TS 23.501 [8].

MWAB-UE: a UE that is operating as part of MWAB and supporting UE NAS functionalities specified in this specification.

N1 mode: A mode of a UE allowing access to the 5G core network via the 5G access network.

Native 4G-GUTI: A native GUTI defined in 3GPP TS 24.301 [15].

Native 5G-GUTI: A 5G-GUTI previously allocated by an AMF.

Non 5G capable over WLAN (N5CW) device: A device that is not capable to operate as a UE supporting NAS signalling with the 5GCN over a WLAN access network. However, this device may be capable to operate as a UE supporting NAS signalling with 5GCN using the N1 reference point as specified in this specification over 3GPP access. An N5CW device may be allowed to access the 5GCN via trusted WLAN access network (TWAN) that supports a trusted WLAN interworking function (TWIF) as specified in 3GPP TS 24.502 [18].

Non-CAG Cell: An NR cell which does not broadcast any Closed Access Group identity or an E-UTRA cell connected to 5GCN.

Non-equivalent PLMN: A PLMN which is not an equivalent PLMN.

Non-equivalent SNPN: An SNPN which is not an equivalent SNPN.

Non-globally-unique SNPN identity: An SNPN identity with an NID whose assignment mode is set to 1 (see 3GPP TS 23.003 [4]).

N1 NAS signalling connection: A peer to peer N1 mode connection between UE and AMF. An N1 NAS signalling connection is either the concatenation of an RRC connection via the Uu reference point and an NG connection via the N2 reference point for 3GPP access, or the concatenation of an IPsec tunnel via the NWu reference point and an NG connection via the N2 reference point for non-3GPP access.

N5CW device supporting 3GPP access: An N5CW device which supports acting as a UE in 3GPP access (i.e. which supports NAS over 3GPP access).

N6 PDU session: A PDU session established between the UE and the User Plane Function (UPF) for transmitting the UE's IP data, Ethernet data or Unstructured data related to a specific application.

NEF PDU session: A PDU session established between the UE and the Network Exposure Function (NEF) for transmitting the UE's Unstructured data related to a specific application.

Network slicing information: information stored at the UE consisting of one or more of the following:

a) default configured NSSAI for PLMN or SNPN;

b) configured NSSAI for a PLMN or an SNPN;

b1) NSSRG information for the configured NSSAI for a PLMN or an SNPN;

b2) S-NSSAI location validity information for the configured NSSAI for a PLMN or an SNPN;

b3) S-NSSAI time validity information for the configured NSSAI for a PLMN or an SNPN;

c) mapped S-NSSAI(s) for the configured NSSAI for a PLMN or an SNPN;

d) pending NSSAI for a PLMN or an SNPN;

e) mapped S-NSSAI(s) for the pending NSSAI for a PLMN or an SNPN;

f) rejected NSSAI for the current PLMN or SNPN;

g) mapped S-NSSAI(s) for the rejected NSSAI for the current PLMN or an SNPN;

h) rejected NSSAI for the failed or revoked NSSAA;

i) for each access type:

1) allowed NSSAI for a PLMN or an SNPN;

2) mapped S-NSSAI(s) for the allowed NSSAI for a PLMN;

3) rejected NSSAI for the current registration area;

4) mapped S-NSSAI(s) for the rejected NSSAI for the current registration area;

5) rejected NSSAI for the maximum number of UEs reached;

6) mapped S-NSSAI(s) for the rejected NSSAI for the maximum number of UEs reached;

7) alternative NSSAI for a PLMN or an SNPN; and

8) on-demand NSSAI for a PLMN or an SNPN; and

j) for 3GPP access type:

1) NSAG information for the configured NSSAI for a PLMN or an SNPN;

2) partially allowed NSSAI for a PLMN or an SNPN;

3) mapped S-NSSAI(s) for the partially allowed NSSAI for a PLMN or an SNPN;

4) partially rejected NSSAI for a PLMN or an SNPN; and

5) mapped S-NSSAI(s) for the partially rejected NSSAI for a PLMN or an SNPN;

NG-RAN cell: A cell with NG-RAN access technology or satellite NG-RAN access technology.

NITZ information: Network Identity and Time Zone (NITZ) information includes full name for network, short name for network, local time zone, universal time and local time zone, network daylight saving time.

Non-cleartext IEs: Information elements that are not cleartext IEs.

Non-emergency PDU session: Any PDU session which is not an emergency PDU session.

Non-satellite NG-RAN cell: A cell with NG-RAN access technology.

Onboarding SUCI: SUCI derived from onboarding SUPI.

Onboarding SUPI: SUPI with the SUPI format "network specific identifier" containing a network specific identifier or with the SUPI format "IMSI" containing an IMSI, derived by a UE in SNPN access operation mode, from default UE credentials for primary authentication and used to identify the UE during initial registration for onboarding services in SNPN and while registered for onboarding services in SNPN.

On-demand NSSAI: A list of on-demand S-NSSAI(s) and optionally slice deregistration inactivity timer per on-demand S-NSSAI.

On-demand S-NSSAI: An S-NSSAI included in the configured NSSAI that the UE supporting network slice usage control is allowed to request only when this S-NSSAI is used by the UE to establish a PDU session for user data transmission.

Partially rejected NSSAI: Indicating the S-NSSAI(s) is rejected by the network in some TA(s) but not all TAs of the registration area. Each S-NSSAI in the partially rejected NSSAI is associated with a list of TAs where the S-NSSAI is rejected.

PDU address: An IP address assigned to the UE by the packet data network.

PDU session for LADN: A PDU session with a DNN associated with an LADN or a PDU session with a DNN and an S-NSSAI associated with an LADN.

PDU session with suspended user-plane resources: A PDU session for which user-plane resources were established or re-established, and for which data radio bearers were suspended when transition to 5GMM-CONNECTED mode with RRC inactive indication.

Persistent PDU session: Either a non-emergency PDU session contains a GBR QoS flow with QoS equivalent to QoS of teleservice 11 and where there is a radio bearer associated with that PDU session over 3GPP access, or an emergency PDU session where there is a radio bearer associated with that PDU session over 3GPP access.

NOTE 4: An example of a persistent PDU session is a non-emergency PDU session which includes 5QI set to 5QI 1 where there is a radio bearer associated with that context.

PLMN ID representing the participating operator: A PLMN ID broadcasted in the area of indirect network sharing deployment to enable the UE of the participating operator to select it based on the existing PLMN selection procedures as specified in 3GPP TS 23.122 [5]. PLMN ID representing the participating operator can be:

a) PLMN ID of the HPLMN of UE of the participating operator;

b) PLMN ID of the EHPLMN of UE of the participating operator; or

c) PLMN ID included in the list of equivalent PLMNs, when the UE of participating operator registers in the HPLMN (i.e. PLMN ID different from the PLMN ID of case a and case b above).

Procedure transaction identity: An identity which is dynamically allocated by the UE for the UE-requested 5GSM procedures or allocated by the UE or the PCF for the UE policy delivery procedures. The procedure transaction identity is released when the procedure is completed but it should not be released immediately.

RAT frequency selection priority index: A parameter provided by the AMF to the NG-RAN via the N2 reference point. The AMF selects an RFSP index for a particular UE based on the subscribed RFSP index, the locally configured operator's policies, the allowed NSSAI, the partially allowed NSSAI, the partially rejected NSSAI, the rejected NSSAI for the current registration area, the pending NSSAI and the UE context information, including the UE's usage setting, if received during the registration procedure. Definition derived from 3GPP TS 23.501 [8].

Registered for 5GS services with CIoT 5GS optimization: A UE is registered for 5GS services with control plane CIoT 5GS optimization or registered for 5GS services with user plane CIoT 5GS optimization.

Registered for 5GS services with control plane CIoT 5GS optimization: A UE supporting CIoT 5GS optimizations is registered for 5GS services, and control plane CIoT 5GS optimization along with one or more other CIoT 5GS optimizations have been accepted by the network.

Registered for 5GS services with user plane CIoT 5GS optimization: A UE supporting CIoT 5GS optimizations is registered for 5GS services, and user plane CIoT 5GS optimization along with one or more other CIoT 5GS optimizations have been accepted by the network.

Registered for disaster roaming services: A UE is considered as "registered for disaster roaming services" when it has successfully completed initial registration or mobility registration for disaster roaming services.

Registered for emergency services: A UE is considered as "registered for emergency services" when it has successfully completed initial registration for emergency services.

Registered for onboarding services in SNPN: A UE is considered as "registered for onboarding services in SNPN" when it has successfully completed initial registration for onboarding services in SNPN. While registered for onboarding services in SNPN, services other than the onboarding services are not available.

Registered PLMN: The PLMN on which the UE performed the last successful registration. The identity of the registered PLMN (MCC and MNC) is provided to the UE within the GUAMI field of the 5G-GUTI.

Rejected NSSAI: Rejected NSSAI for the current PLMN or SNPN, rejected NSSAI for the current registration area, rejected NSSAI for the failed or revoked NSSAA or rejected NSSAI for the maximum number of UEs reached.

NOTE 5: Rejected NSSAI for the current PLMN or SNPN, rejected NSSAI for the current registration area or rejected NSSAI for the maximum number of UEs reached contains a set of S-NSSAI(s) associated with a PLMN identity or SNPN identity for the current PLMN or SNPN and in roaming scenarios also contains a set of mapped S-NSSAI(s) if available. Rejected NSSAI for the failed or revoked NSSAA only contains a set of S-NSSAI(s) associated with a PLMN identity or SNPN identity for the HPLMN or RSNPN.

Rejected NSSAI for the current PLMN or SNPN: A set of S-NSSAI(s) which was included in the requested NSSAI by the UE and is sent by the AMF with the rejection cause "S-NSSAI not available in the current PLMN or SNPN".

Rejected NSSAI for the current registration area: A set of S-NSSAI(s) which was included in the requested NSSAI by the UE and is sent by the AMF with the rejection cause "S-NSSAI not available in the current registration area".

Rejected NSSAI for the failed or revoked NSSAA: A set of S-NSSAI(s) which is sent by the AMF with the rejection cause "S-NSSAI not available due to the failed or revoked network slice-specific authentication and authorization".

Rejected NSSAI for the maximum number of UEs reached: A set of S-NSSAI(s) which was included in the requested NSSAI by the UE and is sent by the AMF with the rejection cause "S-NSSAI not available due to maximum number of UEs reached".

Removal of eCall only mode restriction: All the limitations as described in 3GPP TS 22.101 [2] for the eCall only mode do not apply any more.

Satellite NG-RAN cell: A cell with satellite NG-RAN access technology.

Satellite NG-RAN RAT type: In case of satellite NG-RAN access, RAT types are used to distinguish different types of satellite NG-RAN access, as defined in 3GPP TS 38.413 [31]. In this version of the specification, the defined satellite NG-RAN RAT types are "NR(LEO)", "NR(MEO)" and "NR(GEO)".

Selected core network type information: A type of core network (EPC or 5GCN) selected by the UE NAS layer in case of an E-UTRA cell connected to both EPC and 5GCN.

SNPN access operation mode: A UE operating in SNPN access operation mode only selects SNPNs. This includes the case when the UE is accessing an SNPN over 3GPP access, the case when the UE is accessing an SNPN over non-3GPP access and the case where the UE is accessing SNPN services via a PLMN

NOTE 7: In this release of specification, the term "SNPN access operation mode" is the same as the term "SNPN access mode" used in 3GPP TS 23.501 [8].

S-NSSAI based congestion control: Type of congestion control at session management level that is applied to reject session management requests from UEs or release PDU sessions when the associated S-NSSAI and optionally the associated DNN are congested. S-NSSAI based congestion control can be activated at the SMF over session management level and also activated at the AMF over mobility management level.

UE configured for high priority access in selected PLMN: A UE configured with one or more access identities equal to 1, 2, or 11-15 applicable in the selected PLMN as specified in subclause 4.5.2. Definition derived from 3GPP TS 22.261 [3].

UE configured for high priority access in selected SNPN: A UE configured with one or more access identities equal to 1, 2, or 11-15 applicable in the selected SNPN as specified in subclause 4.5.2A.

UE operating in single-registration mode in a network supporting N26 interface: A UE, supporting both N1 mode and S1 mode. During the last attach, tracking area update (see 3GPP TS 24.301 [15]) or registration procedures, the UE has received either a 5GS network feature support IE with IWK N26 bit set to "interworking without N26 interface not supported" or an EPS network feature support IE with IWK N26 bit set to "interworking without N26 interface not supported".

UE supporting CIoT 5GS optimizations: A UE that supports control plane CIoT 5GS optimization or user plane CIoT 5GS optimization and one or more other CIoT 5GS optimizations when the UE is in N1 mode.

UE supporting UAS services: A UE which supports an aerial vehicle, such as a drone, with an onboard or built-in USIM and is able to perform UE NAS functionalities specified in this specification. Upper layers of the UE supporting UAS services are responsible for UAS related procedures, such as UUAA and C2 authorization, for which the NAS layer of the UE supporting UAS services performs the necessary NAS procedures.

UE using 5GS services with control plane CIoT 5GS optimization: A UE that is registered for 5GS services with the control plane CIOT 5GS optimization accepted by the network.

User plane CIoT 5GS optimization: Signalling optimizations to enable efficient transport of user data (IP, Ethernet or Unstructured) over the user plane.

User Plane Positioning Connection Management Information (UPP-CMI): The messages defined in clause 6 of 3GPP TS 24.572 [64] that are utilized to manage the user plane connection between the UE and the LMF for LCS-UPP.

User-plane resources: Resources established between the UE and the UPF. The user-plane resources consist of one of the following:

- user plane radio bearers via the Uu reference point, a tunnel via the N3 reference point and a tunnel via the N9 reference point (if any) for 3GPP access;

- IPsec tunnels via the NWu reference point, a tunnel via the N3 reference point and a tunnel via the N9 reference point (if any) for untrusted non-3GPP access;

- IPsec tunnels via the NWt reference point, a tunnel via the N3 reference point and a tunnel via the N9 reference point (if any) for trusted non-3GPP access used by the UE;

- a layer-2 connection via the Yt reference point, a layer-2 or layer-3 connection via the Yw reference point, a tunnel via the N3 reference point and a tunnel via the N9 reference point (if any) for trusted non-3GPP access used by the N5CW device;

- W-UP resources via Y4 reference point, a tunnel via the N3 reference point and a tunnel via the N9 reference point (if any) for wireline access used by the 5G-RG; and

- L-W-UP resources via Y5 reference point, a tunnel via the N3 reference point and a tunnel via the N9 reference point (if any) for wireline access used by the FN-RG.

UE policy section identifier: A UE policy section identifier (UPSI) is an identifier of a UE policy section, which is composed of the MCC and MNC of:

- the PLMN ID of a PLMN of the PCF which provides the UE policy section, and a UE policy section code (UPSC), assigned by the PCF in that PLMN; or

- the PLMN ID part of an SNPN of the PCF which provides the UE policy section, and a UPSC, assigned by the PCF in that SNPN.

W-AGF acting on behalf of the N5GC device: A W-AGF that enables an N5GC device behind a 5G-CRG or an FN-CRG to connect to the 5G Core.

For the purposes of the present document, the following terms and definitions given in 3GPP TS 22.261 [3] apply:

Disaster Roaming

Non-public network

satellite NG-RAN

For the purposes of the present document, the following terms and definitions given in 3GPP TS 23.003 [4] apply:

5G-GUTI

5G-S-TMSI

5G-TMSI

Global Line Identifier (GLI)

Global Cable Identifier (GCI)

GUAMI

IMEI

IMEISV

IMSI

PEI

SUPI

SUCI

For the purposes of the present document, the following terms and definitions given in 3GPP TS 23.122 [5] apply:

Access Technology

CAG selection

CAG-ID authorized based on "Allowed CAG list"

Country

EHPLMN

HPLMN

Onboarding services in SNPN

Registered SNPN

Selected PLMN

Selected SNPN

Shared network

SNPN identity

Steering of roaming SNPN selection information (SOR-SNPN-SI)

Steering of roaming SNPN selection information for localized services in SNPN (SOR-SNPN-SI-LS)

Steering of Roaming (SOR)

Steering of roaming connected mode control information (SOR-CMCI)

Steering of Roaming information

Subscribed SNPN

Suitable cell

UE determined PLMN with disaster condition

VPLMN

For the purposes of the present document, the following terms and definitions given in 3GPP TS 23.167 [6] apply:

eCall over IMS

For the purposes of the present document, the following terms and definitions given in 3GPP TS 23.216 [6A] apply:

SRVCC

For the purposes of the present document, the following terms and definitions given in 3GPP TS 23.401 [7] apply:

eCall only mode

For the purposes of the present document, the following terms and definitions given in 3GPP TS 23.501 [8] apply:

5G access network

5G core network

5G QoS flow

5G QoS identifier

5G-RG

5G-BRG

5G-CRG

5G System

5G VN Group

Allowed area

Allowed NSSAI

Alternative S-NSSAI

AMF region

AMF set

Closed access group

Configured NSSAI

Credentials Holder (CH)

Default Credentials Server (DCS)

Group ID for Network Selection (GIN)

Hosting operator

IAB-node

Indirect network sharing

Local area data network

Mobile Base Station Relay

Mobile gNB with Wireless Access Backhauling (MWAB)

N3QAI

Network identifier (NID)

Network slice

Network slice area of service

NG-RAN

Non-allowed area

Onboarding Standalone Non-Public Network

Partially allowed NSSAI

Participating operator

PDU connectivity service

PDU session

PDU session type

PDU set

PEGC

PEMC

Pending NSSAI

PIN

PIN direct communication

PIN indirect communication

PIN-DN communication

PINE

Requested NSSAI

Routing Indicator

Service data flow

Service Gap Control

Serving PLMN rate control

Small data rate control status

SNPN-enabled UE

(S)RTP multiplexed media information

Stand-alone Non-Public Network

Time Sensitive Communication

Time Sensitive Communication and Time Synchronization Function

UE-DS-TT residence time

UE-Slice-MBR

UE presence in LADN service area

For the purposes of the present document, the following terms and definitions given in 3GPP TS 23.503 [10] apply:

UE local configuration

VPLMN specific (VPS) URSP

For the purposes of the present document, the following terms and definitions given in 3GPP TS 24.008 [12] apply:

A/Gb mode

GMM

GPRS

Iu mode

MM

Non-GPRS

For the purposes of the present document, the following terms and definitions given in 3GPP TS 24.301 [15] apply:

CIoT EPS optimization

Control plane CIoT EPS optimization

EENLV

EMM

EMM-DEREGISTERED

EMM-DEREGISTERED-INITIATED

EMM-IDLE mode

EMM-NULL

EMM-REGISTERED

EMM-REGISTERED-INITIATED

EMM-SERVICE-REQUEST-INITIATED

EMM-TRACKING-AREA-UPDATING-INITIATED

EPS

EPS security context

EPS services

Lower layer failure

Megabit

Message header

NAS signalling connection recovery

NB-S1 mode

Non-EPS services

S1 mode

User plane CIoT EPS optimization

WB-S1 mode

For the purposes of the present document, the following terms and definitions given in 3GPP TS 33.501 [24] apply:

5G security context

5G NAS security context

ABBA

Current 5G NAS security context

Default UE credentials for primary authentication

Default UE credentials for secondary authentication

Full native 5G NAS security context

K'AME

KAMF

KASME

Mapped 5G NAS security context

Mapped security context

Native 5G NAS security context

NCC

Non-current 5G NAS security context

Partial native 5G NAS security context

RES*

For the purposes of the present document, the following terms and definitions given in 3GPP TS 38.413 [31] apply:

NG connection

User Location Information

For the purposes of the present document, the following terms and definitions given in 3GPP TS 24.587 [19B] apply:

E-UTRA-PC5

NR-PC5

V2X

For the purposes of the present document, the following terms and its definitions given in 3GPP TS 23.256 [6AB] apply:

3GPP UAV ID

CAA (Civil Aviation Administration)-Level UAV Identity

Command and Control (C2) Communication

Direct C2 communication

No-transmit zone (NTZ)

UAV controller (UAV-C)

UAS Services

UAS Service Supplier (USS)

Uncrewed Aerial System (UAS)

USS communication

UUAA

UUAA-MM

UUAA-SM

For the purposes of the present document, the following terms and definitions given in 3GPP TS 24.554 [19E] apply:

5G ProSe

For the purposes of the present document, the following terms and definitions given in 3GPP TS 23.548 [10A] apply:

Edge Application Server

Edge DNS Client

For the purposes of the present document, the following terms and definitions given in 3GPP TS 24.526 [19] apply:

Non-subscribed SNPN signalled URSP

PLMN generic (PG) URSP

VPLMN specific (VPS) URSP of the RPLMN

VPLMN specific (VPS) URSP of the equivalent PLMN of the RPLMN

For the purposes of the present document, the following terms and definitions given in 3GPP TS 24.577 [60] apply:

A2X

For the purposes of the present document, the following terms and definitions given in 3GPP TS 24.514 [62] apply:

A2XP

RSLPP

For the purposes of the present document, the following terms and definitions given in 3GPP TS 23.316 [6D] apply:

Authenticable Non-3GPP (AUN3) device

Non-Authenticable Non-3GPP (NAUN3) device

For the purposes of the present document, the following terms and definitions given in 3GPP TS 23.586 [63] apply:

SL Positioning Server UE

For the purposes of the present document, the following terms and definitions given in 3GPP TS 38.300 [27] apply:

NCR-MT

For the purposes of the present document, the following terms and definitions given in 3GPP TS 24.572 [64] apply:

LCS-UPP

## 3.2 Abbreviations

For the purposes of the present document, the abbreviations given in 3GPP TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in 3GPP TR 21.905 [1].

4G-GUTI 4G-Globally Unique Temporary Identifier

5GCN 5G Core Network

5G-GUTI 5G-Globally Unique Temporary Identifier

5GMM 5GS Mobility Management

5G-RG 5G Residential Gateway

5G-BRG 5G Broadband Residential Gateway

5G-CRG 5G Cable Residential Gateway

5GS 5G System

5GSM 5GS Session Management

5G-S-TMSI 5G S-Temporary Mobile Subscription Identifier

5G-TMSI 5G Temporary Mobile Subscription Identifier

5QI 5G QoS Identifier

ABBA Anti-Bidding down Between Architectures

ACS Auto-Configuration Server

AKA Authentication and Key Agreement

AKMA Authentication and Key Management for Applications

A-KID AKMA Key Identifier

A-TID AKMA Temporary Identifier

AMBR Aggregate Maximum Bit Rate

AMF Access and Mobility Management Function

ANDSP Access Network Discovery and Selection Policy

APN Access Point Name

AS Access stratum

ATSSS Access Traffic Steering, Switching and Splitting

AUN3 Authenticable Non-3GPP

AUSF Authentication Server Function

AVC Advanced Video Coding

BH BackHaul

CAG Closed access group

CGI Cell Global Identity

CHAP Challenge Handshake Authentication Protocol

DDX Downlink Data Expected

DEI Drop Eligible Indicator

DL Downlink

DN Data Network

DNN Data Network Name

DNS Domain Name System

DS-TT Device-Side TSN Translator

eDRX Extended DRX cycle

ePDG Evolved Packet Data Gateway

EUI Extended Unique Identifier

E-UTRAN Evolved Universal Terrestrial Radio Access Network

EAC Early Admission Control

EAP-AKA' Improved Extensible Authentication Protocol method for 3rd generation Authentication and Key Agreement

EAS Edge Application Server

EASDF Edge Application Server Discovery Function

ECIES Elliptic Curve Integrated Encryption Scheme

ECN Explicit Congestion Notification

ECS Edge Configuration Server

ECSP Edge Computing Service Provider

EDC Edge DNS Client

EEC Edge Enabler Client

EPD Extended Protocol Discriminator

EMM EPS Mobility Management

EPC Evolved Packet Core Network

EPS Evolved Packet System

EPS-UPIP User-plane integrity protection in EPS

ESM EPS Session Management

FN-RG Fixed Network RG

FN-BRG Fixed Network Broadband RG

FN-CRG Fixed Network Cable RG

FQDN Fully Qualified Domain Name

Gbps Gigabits per second

GEO Geostationary Orbit

GFBR Guaranteed Flow Bit Rate

GUAMI Globally Unique AMF Identifier

HEVC High Efficiency Video Coding

IAB Integrated access and backhaul

IMEI International Mobile station Equipment Identity

IMEISV International Mobile station Equipment Identity and Software Version number

IMSI International Mobile Subscriber Identity

IP-CAN IP-Connectivity Access Network

KSI Key Set Identifier

L4S Low Latency, Low Loss and Scalable Throughput

LADN Local Area Data Network

LCS LoCation Services

LCS-UPP Location Services User Plane Protocol

LEO Low Earth Orbit

LMF Location Management Function

LPP LTE Positioning Protocol

MAC Message Authentication Code

MA PDU Multi-Access PDU

MBS Multicast/Broadcast Services

MBSR Mobile Base Station Relay

Mbps Megabits per second

MCS Mission Critical Service

MEO Medium Earth Orbit

MFBR Maximum Flow Bit Rate

MICO Mobile Initiated Connection Only

MINT Minimization of Service Interruption

MPS Multimedia Priority Service

MSK MBS Service Key

MTK MBS Traffic Key

MUSIM Multi-USIM

MWAB Mobile gNB with Wireless Access Backhauling

N3IWF Non-3GPP Inter-Working Function

N3QAI Non-3GPP QoS Assistance Information

N5CW Non-5G-Capable over WLAN

N5GC Non-5G Capable

NAI Network Access Identifier

NAUN3 Non-Authenticable Non-3GPP

NITZ Network Identity and Time Zone

ngKSI Key Set Identifier for Next Generation Radio Access Network

NPN Non-public network

NR New Radio

NSAC Network Slice Admission Control

NSACF Network Slice Admission Control Function

NSAG Network slice AS group

NS-AoS Network slice area of service

NSSAA Network slice-specific authentication and authorization

NSSAAF Network Slice-Specific and SNPN authentication and authorization Function

NSSAI Network Slice Selection Assistance Information

NSSRG Network Slice Simultaneous Registration Group

NTZ No-Transmit Zone

ON-SNPN Onboarding Standalone Non-Public Network

OS Operating System

OS Id OS Identity

PAP Password Authentication Protocol

PCO Protocol Configuration Option

PCP Priority Code Point

PEI Permanent Equipment Identifier

PEIPS Paging Early Indication with Paging Subgrouping

PEGC PIN Element with Gateway Capability

PEMC PIN Element with Management Capability

PIN Personal IoT Network

PINE PIN Element

PMF Performance Measurement Function

PNI-NPN Public Network Integrated Non-Public Network

ProSe Proximity based Services

ProSeP 5G ProSe policy

PG PLMN Generic

PTI Procedure Transaction Identity

PTP Precision Time Protocol

PVS Provisioning Server

QFI QoS Flow Identifier

QoS Quality of Service

QRI QoS Rule Identifier

RACS Radio Capability Signalling Optimisation

(R)AN (Radio) Access Network

RFSP RAT Frequency Selection Priority

RG Residential Gateway

RPLMN Registered PLMN

RQA Reflective QoS Attribute

RQI Reflective QoS Indication

RSC Relay Service Code

RSN Redundancy Sequence Number

RSNPN Registered SNPN

RTT Round Trip Time

S-NSSAI Single NSSAI

SA Security Association

SDF Service Data Flow

SDNAEPC Secondary DN authentication and authorization over EPC

SDT Small Data Transmission

SMF Session Management Function

SGC Service Gap Control

SLPP SideLink Positioning Protocol

SNN Serving Network Name

SNPN Stand-alone Non-Public Network

SOR Steering of Roaming

SOR-CMCI Steering of Roaming Connected Mode Control Information

SRTP Secure Real-time Transport Protocol

SUCI Subscription Concealed Identifier

SUPI Subscription Permanent Identifier

TA Tracking Area

TAC Tracking Area Code

TAI Tracking Area Identity

Tbps Terabits per second

TMGI Temporary Mobile Group Identity

TNAN Trusted Non-3GPP Access Network

TNGF Trusted Non-3GPP Gateway Function

TSC Time Sensitive Communication

TSCTSF Time Sensitive Communication and Time Synchronization Function

TWIF Trusted WLAN Interworking Function

TSN Time-Sensitive Networking

UAS Uncrewed Aerial System

UAV Uncrewed Aerial Vehicle

UAV-C Uncrewed Aerial Vehicle-Controller

UDM Unified Data Management

UL Uplink

UPDS UE policy delivery service

UPF User Plane Function

UP-PRUK User Plane ProSe Remote User Key

UPP-CMI User Plane Positioning Connection Management Information

UPSC UE Policy Section Code

UPSI UE Policy Section Identifier

URN Uniform Resource Name

URSP UE Route Selection Policy

USS UAS Service Supplier

UUAA USS UAV Authorization/Authentication

V2X Vehicle-to-Everything

V2XP V2X policy

VID VLAN Identifier

VPS VPLMN Specific

W-AGF Wireline Access Gateway Function

WLAN Wireless Local Area Network

WUS Wake-up signal

### 4.15.2 Void

#### 4.15.2.1 Void

#### 4.15.2.2 Void

#### 4.15.2.3 Void

### 4.22.4 Void

#### 8.2.1.4 Void

#### 8.2.6.31 Void

##### 8.2.7.54.4 Void

#### 8.2.20.2 Void

#### 8.2.25.3 Void

#### 8.3.1.6 Void

#### 8.3.2.13 Void

#### 8.3.4.3 Void

#### 8.3.5.3 Void

#### 8.3.9.10 Void

#### 8.3.20.2 Void

#### 8.3.20.3 Void

#### 8.3.20.4 Void

#### 9.11.2.16 Void

#### 9.11.3.11 Void

#### 9.11.3.21 Void

#### 9.11.3.22 Void

#### 9.11.3.27 Void

#### 9.11.3.58 Void

#### 9.11.3.59 Void

#### 9.11.3.60 Void

#### 9.11.3.61 Void

#### 9.11.3.62 Void

#### 9.11.3.63 Void

#### 9.11.3.64 Void

#### 9.11.3.65 Void

#### 9.11.3.66 Void

#### 9.11.3.67 Void

#### 9.11.3.78 Void

#### 9.11.4.19 Void

#### 9.11.4.35 Void

## 10.4 Void

######## Annex A (informative): Cause values for 5GS mobility management

######## Annex B (informative): Cause values for 5GS session management

######## Annex C (normative): Storage of 5GMM information

######## Annex D (normative): UE policy delivery service

######## Annex E (informative): Void

######## Annex F (informative): Change history

| Change history |
|---|
| Date | Meeting | Tdoc | CR | Rev | Cat | Subject/Comment | New version |
| 2017-10 | CT1#106 | C1-174182 |  |  |  | Draft skeleton provided by the rapporteur. | 0.0.0 |
| 2017-11 | CT1#106 |  |  |  |  | Implementing the following p-CRs agreed by CT1:C1-174183, C1-174184, C1-174185. | 0.1.0 |
| 2017-12 | CT1#107 |  |  |  |  | Implementing the following p-CRs agreed by CT1:C1-175098, C1-175313.Corrections done by the rapporteur. | 0.2.0 |
| 2017-12 | CT1 e-mail review |  |  |  |  | Editorial corrections. | 0.2.1 |
| 2017-12 | CT1 e-mail review |  |  |  |  | Re-introduction of table in subclause8.2.23.1 | 0.2.2 |
| 2018-02 | CT1#108 |  |  |  |  | Implementing the following p-CRs agreed by CT1:C1-180663, C1-180224, C1-180046, C1-180437, C1-180438, C1-180448, C1-180307, C1-180211, C1-180316, C1-180221, C1-180281, C1-180339, C1-180361, C1-180148, C1-180415, C1-180451, C1-180453, C1-180455, C1-180459, C1-180482, C1-180483, C1-180484, C1-180619, C1-180620, C1-180623, C1-180624, C1-180627, C1-180628, C1-180664, C1-180665, C1-180668, C1-180672, C1-180673, C1-180679, C1-180680, C1-180684, C1-180707, C1-180721, C1-180725, C1-180736, C1-180737, C1-180738, C1-180739, C1-180740, C1-180741, C1-180750, C1-180751, C1-180013, C1-180311, C1-180312, C1-180197, C1-180313, C1-180283, C1-180037, C1-180041, C1-180464, C1-180465, C1-180466, C1-180469, C1-180645, C1-180646, C1-180648, C1-180688, C1-180689, C1-180690, C1-180473, C1-180720, C1-180226, C1-180632, C1-180633, C1-180635, C1-180640, C1-180669, C1-180731, C1-180732, C1-180734, C1-180735, C1-180746, C1-180209, C1-180040, C1-180015, C1-180035, C1-180198, C1-180421, C1-180487, C1-180488, C1-180490, C1-180621, C1-180622, C1-180701, C1-180162, C1-180190, C1-180604, C1-180605, C1-180606, C1-180611, C1-180614, C1-180616, C1-180704, C1-180719, C1-180722, C1-180747, C1-180755, C1-180756Corrections done by the rapporteur. | 0.3.0 |
| 2018-02 | CT1 e-mail review |  |  |  |  | Resolution of collision among C1-180679, C1-180721 and C1-180740.Resolution of collision among C1-180605, C1-180616 and C1-180704.Re-implementation ofparts ofC1-180035,C1-180488,C1-180605, C1-180606,C1-180729and C1-180734as someof the proposedchanges were not implemented correctlyin the previous version.Implementation of C1-180646 which was missed.Editorial corrections.Corrections done by the rapporteur. | 0.3.1 |
| 2018-03 | CT1#109 |  |  |  |  | Implementing the following p-CRs agreed by CT1:C1-181362, C1-181377, C1-181456, C1-181457, C1-181703, C1-181748, C1-181462, C1-181786, C1-181168, C1-181269, C1-181278,C1-181307,C1-181180, C1-181279, C1-181280, C1-181281, C1-181354, C1-181283, C1-181284, C1-181287, C1-181305, C1-181352, C1-181364, C1-181365, C1-181366, C1-181399, C1-181466, C1-181467, C1-181468, C1-181470, C1-181471, C1-181473, C1-181474, C1-181477, C1-181628, C1-181629, C1-181633, C1-181661, C1-181663, C1-181666, C1-181668, C1-181670, C1-181681, C1-181682, C1-181683, C1-181684, C1-181695, C1-181696, C1-181707, C1-181713, C1-181715, C1-181716, C1-181717, C1-181718, C1-181733, C1-181734, C1-181735, C1-181736, C1-181737, C1-181738, C1-181739, C1-181740, C1-181741, C1-181747, C1-181752, C1-181764, C1-181770, C1-181771, C1-181781, C1-181782, C1-181785, C1-181182, C1-181120, C1-181121, C1-181395, C1-181480, C1-181482, C1-181484, C1-181485, C1-181486, C1-181487, C1-181488, C1-181650, C1-181651, C1-181652, C1-181678, C1-181726, C1-181751, C1-181273, C1-181274, C1-181276, C1-181277, C1-181496, C1-181784, C1-181312, C1-181357, C1-181605, C1-181606, C1-181609, C1-181645, C1-181674, C1-181675, C1-181677, C1-181679, C1-181708, C1-181710, C1-181728, C1-181613, C1-181615, C1-181680, C1-181750, C1-181618, C1-181619, C1-181779, C1-181360, C1-181636, C1-181640, C1-181643, C1-181729, C1-181730, C1-181731, C1-181732Corrections done by the rapporteur. | 0.4.0 |
| 2018-03 | CT1 e-mail review |  |  |  |  | Re-implementation of C1-181168 and C1-181307.Re-implementation of C1-181656 and C1-181606 so that C1-181656 is implemented first.Reverting to the old title.Editorial correctionsof some of the implemented p-CRs as well asaddingsome missing parts.Corrections done by the rapporteur. | 0.4.1 |
| 2018-03 | CT#79 | CP-180101 |  |  |  | Version 1.0.0 created for presentation to TSG CT#79 for information. | 1.0.0 |
| 2018-05 | CT1#110 |  |  |  |  | Implementing the following p-CRs agreed by CT1:C1-182219, C1-182493, C1-182496, C1-182202, C1-182497, C1-182053, C1-182311, C1-182019, C1-182359, C1-182360, C1-182361, C1-182358, C1-182305, C1-182306, C1-182354, C1-182117, C1-182182, C1-182455, C1-182459, C1-182491, C1-182600, C1-182601, C1-182605, C1-182606, C1-182607, C1-182608, C1-182609, C1-182610, C1-182614, C1-182615, C1-182621, C1-182662, C1-182664, C1-182665, C1-182708, C1-182728, C1-182730, C1-182733, C1-182724, C1-182757, C1-182759, C1-182760, C1-182768, C1-182772, C1-182775, C1-182786, C1-182787, C1-182791, C1-182831, C1-182832, C1-182833, C1-182834, C1-182835, C1-183836, C1-182838, C1-182840, C1-182844, C1-182067, C1-182073, C1-182303, C1-182321, C1-182352, C1-182385, C1-182645, C1-182646, C1-182647, C1-182648, C1-182650, C1-182651, C1-182657, C1-182659, C1-182660, C1-182741, C1-182742, C1-182761, C1-182762, C1-182763, C1-182764, C1-182765, C1-182774, C1-182789, C1-182789, C1-182815, C1-182845, C1-182797, C1-182232, C1-182230, C1-182666, C1-182667, C1-182671, C1-182673, C1-182677, C1-182800, C1-182824, C1-182710, C1-182072, C1-182078, C1-182174, C1-182190, C1-182456, C1-182636, C1-182637, C1-182638, C1-182639, C1-182726, C1-182729, C1-182747, C1-182749, C1-182766, C1-182767, C1-182841, C1-182847, C1-182043, C1-182057, C1-182260, C1-182044, C1-182617, C1-182618, C1-182619, C1-182620, C1-182622, C1-182623, C1-182624, C1-182627, C1-182628, C1-182629, C1-182802, C1-182808, C1-182345, C1-182461, C1-182630Corrections done by the rapporteur. | 1.1.0 |
| 2018-05 | CT1 e-mail review |  |  |  |  | Re-implementation ofC1-182768, C1-182841,C1-182841, C1-182619, C1-182665, C1-182497, C1-182067 and C1-182078 to correct some editorials as well as adding some missing parts.Corrections done by the rapporteur. | 1.1.1 |
| 2018-06 | CT1#111 |  |  |  |  | Implementing the following p-CRs agreed by CT1:C1-183268, C1-183109, C1-183281, C1-183517, C1-183518, C1-183519, C1-183791, C1-183115, C1-183527, C1-183812, C1-183813, C1-183141, C1-183148, C1-183406, C1-183070, C1-183207, C1-183273, C1-183276, C1-183277, C1-183415, C1-183143, C1-183146, C1-183197, C1-183260, C1-183142, C1-183151, C1-183154, C1-183225, C1-183205, C1-183223, C1-183314, C1-183278, C1-183367, C1-183279, C1-183381, C1-183399, C1-183413, C1-183467, C1-183530, C1-183532, C1-183533, C1-183534, C1-183535, C1-183538, C1-183539, C1-183715, C1-183716, C1-183717, C1-183718, C1-183720, C1-183721, C1-183737, C1-183739, C1-183741, C1-183744, C1-183745, C1-183748, C1-183749, C1-183750, C1-183751, C1-183774, C1-183775, C1-183779, C1-183780, C1-183781, C1-183809, C1-183822, C1-183824, C1-183825, C1-183826, C1-183845, C1-183858, C1-183761, C1-183147, C1-183237, C1-183329, C1-183353, C1-183378, C1-183387, C1-183401, C1-183408, C1-183499, C1-183541, C1-183542, C1-183543, C1-183545, C1-183726, C1-183756, C1-183757, C1-183758, C1-183759, C1-183762, C1-183795, C1-183796, C1-183802, C1-183827, C1-183846, C1-183847, C1-183848, C1-183211, C1-183731, C1-183784, C1-183578, C1-183585, C1-183831, C1-183861, C1-183247, C1-183562, C1-183563, C1-183798, C1-183194, C1-183238, C1-183256, C1-183528, C1-183427, C1-183706, C1-183707, C1-183709, C1-183763, C1-183766, C1-183767, C1-183768, C1-183769, C1-183770, C1-183771, C1-183772, C1-183773, C1-183785, C1-183787, C1-183788, C1-183789, C1-183799, C1-183805, C1-183816, C1-183832, C1-183834, C1-183849, C1-183850, C1-183114, C1-183457, C1-183458, C1-183510, C1-183511, C1-183512, C1-183513, C1-183515, C1-183800, C1-183806, C1-183470Corrections done by the rapporteur. | 1.2.0 |
| 2018-06 | CT1 e-mail review |  |  |  |  | Re-implementation ofC1-183535,C1-183813, C1-183408, C1-183766and C1-183831.Implementation ofC1-183816which was missed.Editorial corrections of some of the implemented p-CRs.Corrections done by the rapporteur. | 1.2.1 |
| 2018-06 | CT#80 | CP-181094 |  |  |  | Version 2.0.0 created for presentation to TSG CT#80 for approval. | 2.0.0 |
| 2018-06 | CT#80 |  |  |  |  | Version 15.0.0 created after approval | 15.0.0 |
| 2018-09 | CT#81 | CP-182139 | 0001 |  | F | Replace unknown "registration update accept" | 15.1.0 |
| 2018-09 | CT#81 | CP-182142 | 0003 | 2 | F | Pass (Extended) Emergency Number List to upper layers | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0004 |  | F | Correcting access selection for SMS over NAS | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0006 | 1 | F | Referring to the correct bits for SMS over NAS during the registration procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0007 | 1 | F | Setting and checking 5GS update status | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0008 | 1 | F | Clarifications on MICO indication | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0009 | 1 | F | Timer T3540 clarifications | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0010 | 3 | F | Network Slicing Subscription Change Indication | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0012 |  | F | Correction for PDU session context | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0013 | 1 | F | Correction for establishment of user-plane resources | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0014 | 1 | F | Correction for establishment cause | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0016 | 4 | F | Correction for maximum data rate per UE for integrity protection for DRBs | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0018 | 3 | F | Invalid DNN | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0020 | 1 | F | Correction for 5GMM cause #90 in subclause A.3 | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0021 |  | F | Editor's notes in UPDP | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0023 | 2 | F | Exchange of extended protocol configuration options | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0024 | 1 | F | 5G QoS - restructuring QoS rules IE | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0025 | 1 | F | Correction for editor's note on further 5GSM causes and further minor issues | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0026 |  | F | Correction and alignment of cause code values | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0027 | 2 | F | UAC information and establishment cause when uplink user data packet is to be sent for a PDU session with suspended user-plane resources | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0028 | 2 | F | Corrections for operator-defined access categories | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0030 | 1 | F | AMF Region ID (8 bits), AMF Set ID (10 bits), and AMF Pointer (6 bits) | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0031 | 1 | F | Correcting message definition of message including EENL | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0032 | 2 | F | SMF knowledge that a UE is configured for high priority access | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0035 | 2 | F | Authentication for normal services not accepted by network | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0036 | 4 | C | Addition of ABBA in 5G based primary authentication procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0037 | 2 | C | Alignment and correction of mapped security context creation at S1 to N1 mode HO | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0038 | 1 | C | Addition of NAS container IE for N1 mode HO | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0039 | 1 | F | Correction and update of S1 mode to N1 mode NAS transparent container | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0040 | 1 | C | Removal of MAC editor´s note | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0041 | 1 | F | Removal of transparent container at N1 mode to S1 mode HO | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0042 |  | F | Correction of 5GS TAC LSB | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0043 | 1 | B | Handling of Emergency PDU sessions and null algorithms | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0044 | 2 | B | Request for Kamf re-derivation | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0045 | 1 | F | Mobility Registration when T3346 running | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0046 |  | F | DL NAS Transport message | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0047 | 1 | F | Single-registration mode | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0048 |  | F | Authentication Response | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0049 | 2 | F | Parameters for PDU session establishment due to change of SSC mode 3 or 2 PSA | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0054 | 2 | F | Equivalent PLMNs | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0055 | 2 | F | Remove the remaining instance of SUPI paging | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0056 | 2 | F | PDU session status | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0058 | 1 | F | Clarification on NAS level MM congestion Control | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0060 | 3 | B | SM cause for out of LADN service area | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0064 | 1 | F | Removal of redundant MICO statement | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0065 | 4 | C | LADN indication from UE at registration | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0066 |  | F | Mapping to configured NSSAI for HPLM shall be included if available | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0069 | 2 | F | Abnormal Cases in the UE for mobilty and periodic Registration Update Procedures | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0070 | 1 | D | Correction to 5GMM Substate | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0071 | 1 | F | Definition of emergency and non-emergency PDU sessions | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0074 | 2 | F | PDU session establish criteria for emergency PDU sessions | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0075 | 3 | F | Service request allowed for PDU release outside LADN | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0076 | 2 | F | Handling of Transmission failure for Service request message. | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0077 | 4 | B | How to determine the maximum number of established PDU sessions | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0079 | 2 | F | UAC and setting of the Uplink data status IE | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0080 | 1 | C | Non-3GPP access to 5GCN not allowed | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0082 | 2 | B | Including S-NSSAI received in EPS in Requested NSSAI and in PDU session establishment request upon inter-system change from S1 mode to N1 mode | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0083 |  | B | UE configuration for AC 11-15 and MCS (access identity 2) | 15.1.0 |
| 2018-09 | CT#81 | CP-182142 | 0084 |  | B | UE configuration for NAS signalling low priority via OMA-DM or USIM not applicable in 5GS | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0085 | 2 | F | Miscellaneous corrections | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0086 | 2 | F | Clarifications on ATTEMPTING-REGISTRATION-UPDATE | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0087 | 2 | F | UE behaviour in substate ATTEMPTING-REGISTRATION-UPDATE | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0090 |  | F | Service area list IE | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0091 | 1 | F | Handling of forbidden tracking area list | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0092 | 2 | F | Corrections for authentication | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0094 | 4 | F | Trigger for mobility and periodic registration update | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0095 |  | F | Abnormal cases in the UE for network-initiated de-registration procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0096 | 4 | F | Add attempt counter to Service Request procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0097 | 1 | F | Authentication procedure during registration procedure for mobility and periodic registration update | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0098 | 4 | F | Registration procedure for mobility and periodic registration update | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0099 | 3 | F | Release of the N1 NAS signalling connection | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0100 | 2 | F | Resetting of registration attempt counter | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0101 | 4 | F | On #27 N1 mode not allowed | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0102 | 3 | F | Adding EPLMN list related descriptions | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0104 | 2 | F | Provision of IWK N26 indication in registration update procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0105 |  | F | Corrections for interworking with EPS | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0106 | 4 | F | Emergency Services Support indicator for non-3GPP access | 15.1.0 |
| 2018-09 | CT#81 | CP-182219 | 0107 | 7 | C | Network control for always-on PDU sessions | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0108 |  | F | Corrections on inconsistent descriptions for 5GSM and 5GMM | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0110 |  | F | Corrections on the timers of 5GMM | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0112 | 1 | F | No operation code for UE policy management | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0113 | 1 | F | Correction on UE behaviour for 5GSM congestion control | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0114 |  | F | Correction on UE security capability IE | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0115 | 5 | F | Including SD when Mapped configured SD is included in S-NSSAI | 15.1.0 |
| 2018-09 | CT#81 | CP-182142 | 0116 | 3 | F | Updates to deleting a derived QoS rule in the UE | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0117 |  | F | Provisioning of ANDSP for non-3GPP access | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0118 |  | D | Fix incorrect references | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0120 | 2 | F | Addition of ngKSI in DEREGISTRATION REQUEST | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0123 | 2 | F | Storing of MPS indicator in non-volatile memory of mobile | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0124 | 4 | C | NW slicing and delayed re-registration due to emergency services | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0125 | 1 | F | Addtion of cause values for service request reject | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0126 | 3 | F | UE actions when other causes received at SERVICE REJECT | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0128 |  | F | Missing general description on sub-clause 9.10 | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0130 |  | F | Correction to general message format | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0131 |  | F | Plain 5GS NAS message | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0134 | 1 | F | Correction to the 5GMM capability IE | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0135 |  | F | Correction to the 5GS identity type IE | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0136 | 1 | F | Correction to the 5GS network feature support IE | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0137 | 1 | F | Editorials and minor corrections | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0138 |  | F | Security procedures and handling after inter-system change | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0140 |  | F | 5GMM aspects of NAS over non-3GPP access | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0141 | 2 | F | Resolution of editor's note on equivalent PLMN list | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0142 |  | F | Resolution of editor's notes on 5GMM sub-layer design | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0143 |  | F | Resolution of editor's note on UE behaviour in substate 5GMM-DEREGISTERED.ATTEMPTING-REGISTRATION | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0144 |  | F | Resolution of editor's note on other sub-states of state 5GMM-DEREGISTERED | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0145 | 3 | F | Resolution of editor's note on sub-states of state 5GMM-REGISTERED | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0146 | 1 | F | Resolution of editor's note on the key derivation function field | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0147 |  | F | Resolution of editor's note on security context coordination | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0148 |  | F | Removal of unnecesary editor's notes FFS | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0151 |  | F | Resolution of editor's note on handling of unknown, unforeseen, and erroneous protocol data | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0153 | 2 | C | AMF taking both EMC and EMC BS availability into account in setting EMF | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0154 | 1 | F | Clarification on SM congestion control specific to PLMN | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0155 | 1 | F | Aligning T35cd handling upon NW initiated SM request with T3396 and T35ef | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0156 | 2 | F | Clarification on stopping back-off timers upon reception of NW initiated SM request | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0157 | 1 | F | Clarification for registration attempt counter handling and introduction of lower layer failure | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0158 | 2 | B | Introduction of 5GMM cause #15 | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0159 | 1 | F | Timer for re-enabling N1 mode capability | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0160 |  | F | Lists of 5GS forbidden tracking areas | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0162 | 1 | F | Local release of a persistent PDU session | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0163 | 1 | F | Correction on retry of PDU session establishment procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0164 |  | F | Correction to 5GSM/ESM coordination | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0165 |  | F | Correction on PDU address IE | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0166 | 1 | F | 5GSM congestion control over AMF on PDU session modification procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0167 | 3 | F | Exception handling in QoS operation | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0168 | 1 | F | Correction on PTI mismatch | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0169 | 1 | B | Establishment of N1 NAS signalling connection due to change in the network slicing information | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0170 | 2 | F | Release of N1 NAS signalling connection due to change in the network slicing information | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0171 | 3 | F | Multiple S-NSSAIs in PDU session establishment | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0173 | 3 | F | Clarifications on UE 5GSM capabilities and procedures during inter-working with EPS | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0174 | 1 | B | Interworking between ePDG/EPC and NG-RAN/5GCN | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0176 | 1 | B | Interworking between E-UTRAN/EPC and N3IWF/5GCN | 15.1.0 |
| 2018-09 | CT#81 | CP-182142 | 0178 | 2 | F | UE re-registration when the AMF cannot determine an Allowed NSSAI | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0180 | 2 | F | Local release of a PDU session due to 5GSM cause #43: Invalid PDU session identity | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0182 | 2 | C | Common NAS security transparent container IE for intra-5G HO and S1 to N1 inter-system HO | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0184 | 1 | F | Handling of PDU session type after intersystem change from N1 mode to S1 mode | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0185 | 2 | F | Allowed NSSAI of a single-registration mode UE within a network with N26 | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0187 | 1 | F | SMF selection based on DNN for transfer a PDN connection from EPS to 5GS | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0188 | 1 | F | UE behaviour for determination of the UE presence in LADN service area | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0189 | 3 | F | Correction on emergency PDU session handling | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0190 | 1 | F | No EMM parameters handling for DR mode UEs due to rejected service request | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0192 | 3 | F | Clarification on activation of UP resources of PDU session | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0194 | 1 | B | Access attempt barred for the UE-initiated NAS transport procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182142 | 0195 | 5 | F | UE configured for EAB and access category 1 | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0197 | 1 | F | No bearer for N1 NAS | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0198 | 4 | F | Correction of S-NSSAI based congestion control | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0199 | 1 | F | Clean-up in definitions | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0200 | 4 | F | Clarify abnormal cases in the UE for independency of 5GMM procedures between accesses | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0203 | 2 | B | Storing Configured NSSAI when the PLMN is changed | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0206 |  | F | Incorrect statement for handling of security context at IWK | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0207 | 2 | F | Correction to SSC mode selection | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0208 | 2 | F | Corrections to terms and references | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0209 | 1 | C | Revision on AMF transport behaviour of 5GSM message | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0210 | 2 | F | Differences between NAS over 3GPP access and NAS over non-3GPP access | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0212 | 6 | B | Preferred list terminating at ME or USIM | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0213 | 4 | F | Clarification on network-initiated de-registration procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0214 |  | F | Correction of detach terminology | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0215 |  | F | Clarification on S-NSSAI based congestion control for PDU session modification procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0216 | 4 | B | SOR acknowledge message coding | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0232 | 1 | F | SMS over NAS re-transmission upon delivery failure on one Access Type | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0233 | 2 | F | Corrections in EAP based primary authentication procedure (alternative 2) | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0234 |  | F | Correction for multi-homed IPv6 PDU session | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0235 | 1 | F | Correction for transfer of a PDN connection from untrusted non-3GPP access connected to EPC | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0237 | 1 | F | Correction for generation of QoS rules | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0239 |  | F | Interworking for multi-homed IPv6 PDU session | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0241 | 1 | F | Clarification of N1 NAS signalling connection release in AMF on generic UE configuration update completion | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0242 | 1 | F | Requests for emergency services fallback from upper layers | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0245 |  | F | Corrections to the Identification and Registration procedures | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0246 |  | F | Correct abnormal procedures reference when handling CC #22 (Congestion) | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0247 | 1 | F | Non-IP PDN connection type for S1 to N1 interworking | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0248 | 1 | F | Non-3GPP de-registration timer | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0250 | 3 | F | Substates for registration result | 15.1.0 |
| 2018-09 | CT#81 | CP-182142 | 0251 | 1 | F | Updating NS Configuration via registration procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0254 | 4 | B | SUCI encoding format and protection scheme | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0255 | 1 | C | Clarify the method of configuring the UE to use Access Identity 1 | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0256 | 1 | B | Handling of error case when UE gets URSP from VPLMN | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0258 | 2 | F | Correction for abnormal cases in the UE of service request procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0259 | 1 | F | Setting of RRC establishment cause for operator-defined access categories | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0262 |  | F | Alignment with terminology"emergency PDU session"throughout TS 24.501 | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0263 | 1 | F | TAI removed from list of Servie area lists after reject from network | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0264 | 1 | F | EAP message IE mandatory in PDU SESSION AUTHENTICATION messages | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0269 | 1 | F | Corrections related to the authentication procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0271 | 2 | F | Security parameter carrying DL NAS COUNT during N1 to S1 mode HO | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0272 | 2 | F | Adding procedures for updating local emergency numbers in other modes | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0275 |  | F | Authentication response parameter IE to be of fixed length (24.501) | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0276 |  | F | Correction to the PDU Session ID value in Allowed PDU session status IE | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0277 | 2 | F | Reactivation result indicating insufficient resources during service request procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0278 | 1 | C | Registration procedure triggered by a change of UE Radio Capability | 15.1.0 |
| 2018-09 | CT#81 | CP-182142 | 0280 | 2 | F | Updates to RRC fallback indication while in 5GMM-CONNECTED mode, or while in 5GMM-CONNECTED mode with RRC inactive indication | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0281 | 2 | C | PDU Session Release due to Semantic or Syntactical Errors | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0282 | 3 | F | Removal of 5GSM cause from ePCO for PDU Session Release Complete | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0283 |  | F | Correction on PTI definition | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0284 | 1 | F | Resolving EN on fatal causes in 5GMM/5GSM state machine | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0285 | 1 | F | Uplink data handling for MT notification | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0286 | 1 | F | Fallback handling for RRC inactive | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0287 | 1 | F | Correction on PDU session modification procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0289 | 1 | F | RRC establishment cause for EAB | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0290 | 2 | C | NW slicing and delayed registration due to emergency services, reject PDU session request | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0291 | 1 | F | Correction to the UE security capability IE encoding | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0292 | 3 | F | Additions to UE configuration update completion clause | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0293 | 2 | F | Removal of local PDU session relase statement in UCU procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0294 |  | F | Resolution of editor's notes in D.3 and D.6.2 | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0295 |  | F | Resolution of the editor's note on value of the non-3GPP de-registration timer value | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0296 |  | F | Resolution of editor's note on the format of the authentication parameters | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0297 | 2 | F | Resolution of editor's note on unknown or unforeseen PDU session identity | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0298 |  | F | Resolution of editor's note on other types of payload for the NAS transport procedure(s) | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0300 | 2 | F | Serving network name format for primary authentication | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0301 | 1 | B | Initial registration not accepted due to serving network not authorized | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0303 | 1 | F | 5GSM cause #xx –out of LADN service area | 15.1.0 |
| 2018-09 | CT#81 | CP-182142 | 0304 | 1 | F | UE policy delivery protocol in the scope | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0305 | 1 | F | AMF pointer pointing one or more AMFs | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0306 |  | F | Corrections in the conditions for SMS via non-3GPP access | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0308 |  | F | 5GMM STATUS message sent by the AMF when certain error conditions are detected upon receipt of 5GMM protocol data in the AMF | 15.1.0 |
| 2018-09 | CT#81 | CP-182137 | 0311 | 1 | F | Interworking with E-UTRAN connected to EPC of a UE registered to 5GC via non-3GPP access | 15.1.0 |
| 2018-09 | CT#81 | CP-182142 | 0313 | 2 | F | Use of S-NSSAI and session-AMBR provided during the EPS bearer context modification procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0314 | 1 | F | Handling of inter-access handover of a PDU session whose S-NSSAI is not allowed for the target access | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0319 | 1 | F | 5GSM sublayer states for PDU session inactive | 15.1.0 |
| 2018-09 | CT#81 | CP-182139 | 0321 | 1 | F | Rename of T3584 and T3585 | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0322 |  | F | Correction on acknowledgement handling of UE configuration update | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0323 | 1 | F | Correction on NW initiated de-registration procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0326 | 1 | F | Service area restrictions | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0327 | 3 | F | Disabling and re-enabling N1 mode capability | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0328 | 1 | F | Clarification on packet filters | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0329 | 1 | F | Correction on 5G-GUTI type encoding | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0330 | 1 | F | Correction on EAP-AKA' based primary authentication | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0331 |  | F | Correction on 5GSM state mapping when interworking | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0333 | 1 | F | Removal of Default EPS Bearer (DEB) indication | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0334 | 1 | F | Correction on interaction with upper layers | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0337 | 2 | F | Security Context | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0339 | 3 | B | Emergency call in limited service state | 15.1.0 |
| 2018-09 | CT#81 | CP-182201 | 0340 | 3 | C | Emergency call error handling | 15.1.0 |
| 2018-09 | CT#81 | CP-182138 | 0341 | 2 | F | PDU session status in notification response message | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0342 | 1 | F | Clarifications on inclusion of S-NSSAI in 5GSM request | 15.1.0 |
| 2018-09 | CT#81 | CP-182133 | 0344 |  | F | Correction for LADN | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0345 | 1 | F | Definition of user-plane resources | 15.1.0 |
| 2018-09 | CT#81 | CP-182136 | 0346 | 1 | F | Handling of PDU session(s) not supporting interworking with EPS | 15.1.0 |
| 2018-09 | CT#81 | CP-182141 | 0350 |  | D | Terminology correction | 15.1.0 |
| 2018-09 | CT#81 | CP-182131 | 0351 | 3 | F | Clarification on MICO indication and LADN information via generic UE configuration update procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0352 | 1 | F | Clarification on the temporary identity in the service request procedure | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0353 |  | F | Abbreviation update for NITZ | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0355 |  | D | Duplicated subclause for registration request message | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0356 | 1 | D | Editorial corrections | 15.1.0 |
| 2018-09 | CT#81 | CP-182135 | 0357 | 2 | B | DL and UL NAS Transport procedure updates for SOR | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0358 | 1 | F | Conditions to send registration complete message. | 15.1.0 |
| 2018-09 | CT#81 | CP-182132 | 0359 | 1 | F | Condition for starting timer T3540 | 15.1.0 |
| 2018-09 | CT#81 | CP-182140 | 0361 | 2 | F | Security context mapping at 5GS to EPS HO | 15.1.0 |
| 2018-09 | CT#81 | CP-182134 | 0363 | 2 | F | Correction to reset registration attempt counter | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0365 | 3 | F | Adding the reference to T3346 | 15.1.0 |
| 2018-09 | CT#81 | CP-182130 | 0367 | 1 | F | Access attempt due to delivery of LPP message/transparent container/UE policy container | 15.1.0 |
| 2018-12 | CT#82 | CP-183032 | 0103 | 6 | F | Clarification on coordination between 5GMM and 5GSM | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0121 | 10 | F | Clarification to VoPS indicator | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0274 | 4 | F | Correct Extended Local Emergency Numbers List deletion upon PLMN change | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0315 | 4 | F | Operator-controlled inclusion of NSSAI in access stratum connection establishment | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0371 | 2 | F | Correction for maximum data rate per UE for integrity protection for DRBs for PDU sessions in non-3GPP access which are transferable to 3GPP access | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0372 | 1 | F | Correction for 3GPP PS data off and non-IP user data packets | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0373 | 2 | F | Corrections for determination of RRC establishment cause and establishment cause for non-3GPP access | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0374 |  | F | Corrections for MTU PCO parameters handling | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0376 | 2 | F | Correction for SM PDU DN request container coding | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0379 | 1 | F | UAC: Correction for SMSoIP sent over DNN other that "IMS" | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0380 | 2 | F | UAC: Correction for operator-defined access categories | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0381 | 1 | F | DRX parameters IE definition | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0383 | 1 | F | Removal of UE security capability from Intra N1 mode NAS container | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0385 |  | F | Correct procedure for determining registered PLMN | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0392 | 1 | F | Definition of emergency registration | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0393 | 1 | F | Correction for EAP based primary authentication and AUTHENTICATION REJECT | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0394 |  | F | Correction for LADN information encoding | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0395 | 3 | B | Dynamic Routing indicator update description | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0398 | 1 | F | ABBA handling for 5G-AKA based authentication procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0399 | 2 | F | ABBA handling when initiating EAP procedures | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0401 | 3 | F | Clarification on NAS message field format and mapping | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0402 | 1 | F | Correction to home country definition | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0403 | 1 | F | Signalling Default Configured NSSAI indication in the registration procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0404 | 1 | F | Rename "configured NSSAI not associated with a PLMN" to align to new stage 2 terminology | 15.2.0 |
| 2018-12 | CT#82 | CP-183032 | 0405 | 1 | F | "SMS subscribed indication" in CONFIGURATION UPDATE COMMAND | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0406 | 1 | F | S-NSSAI not allowed by AMF | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0407 |  | F | Continued need to align with terminology"emergency PDU session"throughout TS 24.501 | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0408 | 1 | F | Ambiguity in the use of the terms "no other parameter" and "no parameters" | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0409 |  | F | Change EMCW to EMCN3 | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0410 | 2 | F | Miscellaneous wording, terminology and reference corrections | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0411 |  | F | Rejected NSSAI clarifications | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0413 | 1 | F | Rejected NSSAI sent in CONFIGURATION UPDATE COMMAND – Alt 2 | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0415 |  | F | UAC – meaning of "the broadcast of categories a, b or c" | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0416 | 2 | F | Clarification of "registration requested" in CONFIGURATION UPDATE COMMAND | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0417 | 5 | F | Updates on steering of roaming handling and information coding | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0419 | 3 | F | Securitycontextusage during NAS security mode control procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0420 | 1 | F | Corrections on GFBR parameter for QoS flow | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0421 | 1 | F | Correction to UE behavior when disabling N1 mode for non-3GPP access | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0423 | 1 | F | Mapped QoS information validation (Solution 1) | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0424 | 4 | B | Protection of initial NAS messages – overall description | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0425 | 4 | B | Support for protection of initial NAS messages | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0426 | 2 | B | Update to 5GS registration type IE and introduction of a new 5GS update type IE | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0427 | 1 | F | S-NSSAI received in Notify payload during PDN connection establishment over ePDG/EPC | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0428 |  | F | No interworking to ePDG/EPC for Ethernet and unstructured PDU sessions | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0429 |  | F | Addition of UE capability for LPP in 5GMM capability IE | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0430 | 1 | F | Correct superfluous test for N1 mode and S1 mode capability | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0431 | 1 | F | Change UE policy classmark as mandatory IE | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0432 | 2 | F | Forward compatibility for UE security capability IE and a few other IEs | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0433 | 1 | F | Introduction of Replayed S1 UE security capabilities | 15.2.0 |
| 2018-12 | CT#82 | CP-183033 | 0434 | 1 | F | Applicability of UAC for other cases of NAS message transport | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0435 | 5 | F | Emergency registered | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0436 | 3 | F | Correction to domain selection rules for EPS/RAT Fallback | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0438 |  | F | UL data status upon fallback indication from lower layers | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0440 | 1 | F | Misc. corrections to 24.501 | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0441 | 2 | F | Clarification on handling of PDU session for LADN | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0442 | 2 | F | Correction to determination method of LADN DNN | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0443 | 1 | F | Correction to trigger of the mobility and periodic registration update procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0444 | 1 | F | Abnormal cases in the network side for Configuration update prcedure. | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0445 | 1 | F | Correction in emergency reg cause name | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0446 |  | F | UE behavior on NW initiated deregistration procedure with #22 | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0447 | 1 | F | Miscellaneous corrections | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0448 | 3 | F | Resetting service request attempt counter upon receipt of the REGISTRATION ACCEPT message | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0450 |  | F | Correction in determining sytactic errors for PDU session establishment accept | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0451 |  | F | T3540 started by the UEon getting 5GMM cause #27 – N1 mode not allowed | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0452 | 2 | F | Clarification on UE identities used for registration | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0454 | 1 | F | Transition from 5GMM-CONNECTED mode with RRC inactive indication to 5GMM-IDLE mode triggered by radio capability update | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0455 | 1 | F | Finalizing 5GSM timers on the UE and SMF side | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0458 | 1 | F | Local PDU session release upon receipt of PDU Session Release Reject with 5GSM cause #34 (service option temporarily out of order) or #35 (PTI already in use) | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0460 | 3 | F | Clarifications on the EAP based AKA procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0461 | 1 | F | Applicability of the Service area list IE indicating all TAIs to equivalent PLMNs | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0464 | 1 | F | Clarification on PDU session transfer from non-3GPP to 3GPP access when 3GPP PS data off UE status is activated | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0465 | 1 | F | EAP-Identification in EAP-AKA' primary authentication and key agreement procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0467 | 1 | F | Excluding mobility procedures from ODAC access control checks | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0470 | 3 | F | Alignment of 5G-GUTI assignment with SA3 | 15.2.0 |
| 2018-12 | CT#82 | CP-183034 | 0471 | 1 | F | Network initiated de-registration in case of emergency PDU session | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0472 |  | F | Resolution of editor's note on always-on PDU session | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0473 |  | F | Addition of 5GSM cause values | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0474 |  | F | Resolution of editor's note on operator-defined access category | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0476 | 6 | C | Support for Traffic Segregation | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0479 |  | F | Correct reference to Mapped EPS bearer contexts | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0480 |  | F | Aborted UE-initiated NAS transport procedure for delivery of SMS/LPP message/UE policy container | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0484 | 3 | F | Clarification on back-off timer upon PLMN change | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0485 | 2 | F | Emergency call in limited service state | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0490 | 2 | F | Correction on Network slicing indication | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0491 |  | F | Correction on De-registration procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0492 | 1 | F | Correction on dual-registration mode | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0494 | 1 | F | Correction to Configured NSSAI for the HPLMN | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0499 |  | F | Updates to 5GS mobility management aspects subclause | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0500 | 5 | F | Editorials and minor corrections | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0501 | 3 | F | Adding necessary term defintions | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0502 | 1 | F | Resolution of editor's notes on abnormal case handling when rejection with "Extended wait time" received from lower layers | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0503 | 1 | F | Resolution of editor's note on maximum length of the 5GS mobile identity IE | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0505 | 1 | F | Resolution of editor's note in sub-clause 4.8.3 | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0506 | 1 | F | Correct unified access control applicability in 5GMM-REGISTERED.UPDATE-NEEDED | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0507 | 3 | F | Correct non-3GPP registration accept procedure when local emergency numbers are received from a different country | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0509 | 1 | F | Remove editor's note for MT LCS | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0510 | 1 | F | Reusing T3519 for Initial Registration procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0511 | 2 | F | Abnormal cases for Registration procedure for mobility and periodic registration update | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0516 | 1 | F | Correction on handling of mandatory IE errors | 15.2.0 |
| 2018-12 | CT#82 | CP-183035 | 0517 | 1 | F | Correction on handling of invalid PSI | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0518 | 2 | F | Clarification on PLMN's maximum number of PDU sessions | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0519 | 1 | F | Handling on collision of PDU session establishment and release procedures | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0521 |  | F | Correction on QoS rules IE | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0522 | 2 | F | Correction on QoS flow description IE | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0523 | 1 | F | Correction of storage of operator-defined access categories | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0525 | 2 | F | Clarification on coordination between 5GMM and EMM for a UEin DRM | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0526 |  | F | The UE behavior in non-3GPP access and in stateATTEMPTING-REGISTRATION | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0528 | 1 | F | Enabling use of and disabling use of MICO mode | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0529 | 2 | F | Apply service area restrictions in NAS procedures | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0530 | 1 | F | Abnormal cases in 5GSM procedures | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0532 |  | F | Clarifications on UE behaviour upon receiving RRC fallback indication | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0533 | 2 | F | Corrections for interworking with EPS | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0534 | 1 | F | Release of the N1 NAS signalling connection upon Service Accept message | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0535 | 1 | F | QoS rules verification during PDU session establishment procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0536 | 1 | F | Clarifications on UE and network state | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0537 | 1 | F | T3517 handling and emergency services fallback | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0540 | 2 | F | Revisions on N1 NAS signaling connection establishment and release | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0541 | 1 | F | Disabling N1 mode capability for 3GPP access and impacts to PLMN selection | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0543 | 1 | F | UE's homogeneous support of emergency services fallback per RAT | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0544 |  | F | Context management for 3GPP access and non-3GPP access due to SR rejection | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0545 | 2 | F | Clarification on setting a service type of a SERVICE REQUEST message | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0546 | 1 | F | UL NAS TRNAPORT message pending due to network slicing information update | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0547 |  | F | Distinction in AMF-side abnormal cases for generic UE configuration update procedure with respect to 5G-GUTI update | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0548 | 1 | F | Handling of security contexts by a UE operating in dual-registration mode | 15.2.0 |
| 2018-12 | CT#82 | CP-183036 | 0549 | 2 | F | Establishment of secure exchange of NAS messages during inter-system change between N1 mode and S1 mode | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0550 | 2 | D | Terminology alignment regarding support for interworking without N26 | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0551 | 3 | F | Correction on reporting change of 3GPP PS data off UE status | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0553 | 1 | F | Correction on Uplink data status handling | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0557 | 2 | F | Correction of LADN information for generic UE configuration update procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0559 |  | F | Management of the registration attempt counter and the attach attempt counter during inter-system change | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0560 | 1 | F | No direct security protection to 5GSM | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0562 | 1 | F | No S-NSSAI for emergency PDU sessions | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0563 | 1 | F | S-NSSAI selection for S-NSSAI based congestion control | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0565 | 2 | F | UE in registered state without registration complete | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0569 | 1 | F | Abnormal Cases in the UE for initial registration | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0571 | 2 | F | Addition of 24.501 overview | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0572 | 2 | F | Service area restrictions applicable for PLMNs in registration area | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0573 | 1 | F | Periodically erase of service area restriction list | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0574 | 1 | F | Completion of mobile identity IE definition in messages | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0575 |  | F | Correction of erroneously encoded IE | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0576 | 2 | F | Correction for local release | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0577 | 3 | F | UAC - providing access identities for barring checks of AS triggered access attempts | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0578 | 2 | F | Correction for indicating 3GPP PS data off status | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0580 | 1 | F | UPSIs in UE STATE INDICATION | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0582 | 1 | F | Initial registration for emergency PDU session | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0583 | 2 | F | Multiple 5G-GUTIs | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0584 |  | F | Correction on Maximum number of supported packet filters | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0585 |  | F | T3584 and T3585 update in Timer table | 15.2.0 |
| 2018-12 | CT#82 | CP-183037 | 0586 | 1 | F | Abnormal case for T3550 | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0590 | 1 | F | No UPF Resources at PDU Session Establishment | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0591 | 2 | F | Clarifications on NAS level mobility management congestion control | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0592 | 1 | F | SOR over control plane in non-3GPP access | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0593 | 1 | F | Handling of target CN type by NAS upon redirection to E-UTRA cell | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0594 | 3 | C | Procedure for UDM-triggered UE parameters update | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0595 | 1 | F | Sending of 5GSM capability IE and Maximum number of supported packet filters IE in in PDU SESSION ESTABLISHMENT REQUEST with request type"existing PDU session" | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0597 | 3 | F | Correction of reference | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0598 | 2 | C | Clarification on 5GSM cause_#46 out of LADN service area | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0604 | 2 | C | Clarification on congestion control upon intersystem change | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0605 |  | F | Editorial correction related to LADN | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0606 | 1 | F | Correcting the structure of LADN related description | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0607 | 2 | F | N3GPP de-registration timers handling at long MM back-off time | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0608 | 1 | F | Abnormal cases in the network side for Configuration update prcedure. | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0609 | 1 | F | Abnormal cases in the UE side for Configuration update prcedure. | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0610 | 1 | F | Handling of 5GSM reject causes #50 and #51 for PDU types IPv4v6. | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0611 | 1 | F | Correction to QoS rules verification during PDU session establishment. | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0612 | 1 | F | QoS rules verification during PDU session modification. | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0613 | 1 | F | QoS flow descriptions IE to be set by SMF mandatory in PDU establishment accept for initial request. | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0614 | 1 | B | MCS Indicator and Access Identity 2 | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0615 | 3 | F | SUCI encoding and support of NAI format | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0617 | 1 | F | UAC for simultaneous access attempt triggers | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0618 | 1 | F | Reset of registration attempt counter | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0619 |  | F | Reset of service request attempt counter | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0622 |  | F | CN paging handling in RRC inactive | 15.2.0 |
| 2018-12 | CT#82 | CP-183038 | 0623 | 2 | F | Procedure collision handling in paging and notification procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0624 |  | F | Resolution of editor's note on different TAI for 4G and for 5G | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0625 |  | F | Correction on 'E' bit for deleting QoS flow description | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0626 |  | F | EMM parameters handling for EPC interworking | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0627 | 1 | F | Registration rejected because of non-3GPP access to 5GCN is not allowed | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0628 | 2 | F | Correction to SUPI definition due to NAI format | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0629 |  | F | Correct secured packet procedures | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0630 | 2 | F | Abnormal cases for EAP-based AKA | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0631 | 1 | F | CONFIGURATION UPDATE COMMAND with no parameters other than registraion requested. | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0633 | 1 | F | Correction of the UE-initiated de-registration procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183039t | 0634 | 1 | F | Definition of a 5GMM cause for DNN subscription check failure | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0635 | 1 | F | Stopping T3511 after transitioning to 5GMM-CONNECTED mode | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0636 | 2 | F | Clarification on storage of UE policy sections of multiple PLMNs | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0637 | 1 | F | Corrections to UE handling of reject with cause #13 | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0639 | 1 | F | Clarification on the Selected EPS NAS security algorithms | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0641 | 3 | F | Handling errors due to missing QoS flow descriptions parameters for GBR QoS flows | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0642 | 2 | F | Clarification on inclusion of Requested NSSAI during periodic registration updating | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0643 | 1 | F | The release of the existing N1 NAS signalling connection after UCU | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0646 | 1 | F | Always-on PDU sessions and associated access | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0647 | 1 | F | Clarification on the applicability of NSSAI to the EPLMNs | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0648 | 1 | F | Clarification on the applicability of service area restrictions to the EPLMNs | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0649 | 1 | F | QFI and QRI values in 5GSM messages | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0650 | 2 | F | Corrections on operation mode selection | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0651 | 1 | F | Clarification on handling of PDU sessions associated with 3GPP access and non-3GPP access for interworking | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0652 |  | F | Clarifications on Configuration Update procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183039 | 0653 |  | F | Correction on timer T3511 | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0654 | 2 | F | Clarification on Notification procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0655 | 1 | F | Clarification on handling of invalid LADN DNN in registration procedure – Alt 1 | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0657 | 1 | F | Correction for LADN information IE | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0659 |  | F | Editorial correction for the generic UE configuration update procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0660 | 1 | F | UE behavior in ATTEMPTING-REGISTRATION state | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0661 | 1 | F | UE-AMF selected PLMN ID mismatch in INACTIVE state | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0662 |  | F | UL NAS Transport behavior due to transmission failure | 15.2.0 |
| 2018-12 | CT#82 | CP-183029 | 0663 | 1 | F | UAC: Correction for operator-defined access categories of acknowledgement | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0664 | 2 | F | Lower layer indication on the establishment/release of user plane resources | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0665 | 3 | F | Setting the Uplink data status and Service type IEs after receiving a fallback indication from the lower layers | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0666 | 2 | F | Indication of a reason for failure in reactivating a PDU session | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0667 | 1 | F | Adding the case that UE initiates the registration procedure for mobility and periodic registration | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0668 | 1 | F | Handling of network rejection with 5GSM cause values #50, #51, and #54 | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0669 | 2 | F | Mobility and periodic registration update triggered by indications from lower layers | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0673 | 1 | F | UE STATE INDICATION message delivered in a REGISTRATION REQUEST message | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0674 | 1 | F | Correction to operator-defined access category criteria type values | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0677 | 1 | F | Exceptions for UEs configured for high priority access in handling T3396, T3584, and T3585 | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0678 |  | D | Removal of non-seamless non-3GPP offload from definitions | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0679 | 4 | F | UE identifier provided during an initial registration procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0680 | 1 | F | Revisons on PDU Session Eestablishment procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0682 | 1 | F | UE registered for emergency services upon authentication failure | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0683 |  | F | Update the trigger of mobility registration update initiation | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0684 | 2 | F | Clarification on T3346 for registration procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0686 | 2 | F | Support sending multiple payloads via Payload container | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0687 | 1 | F | Correction on LADN information handling | 15.2.0 |
| 2018-12 | CT#82 | CP-183040 | 0688 | 2 | F | Mapping of a NOTIFICATION message to an access category | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0690 | 2 | F | Transmission of SUCI in DEREGISTRATION REQUEST | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0691 |  | F | Clarification on missing subclause | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0692 |  | F | Stop T3516 when authentication reject received | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0693 | 1 | F | Limited service and no SUPI states in 5GMM instance for non-3GPP accesst | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0695 | 1 | F | QoS flow and mapped EPS bearer context | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0696 | 1 | F | Corrections on 5GSM IEs | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0697 | 1 | F | Correction on 5GSM congestion control | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0698 |  | F | Correction on PTI value release | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0699 | 1 | F | Corrections on QoS rules IE | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0700 | 1 | F | UE handling for semantic error in the QoS operation | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0701 |  | F | Resolution of editor's note on abnormal case handling for the UE-initiated UE state indication procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0702 | 1 | F | Resolution of editor's note on abnormal case handling for the network-requested UE policy management procedure | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0703 |  | F | Resolution of editor's note on the information the N3IWF maintains for a registered UE | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0709 | 2 | F | Congestion control | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0711 | 1 | F | Correction to authentication abnormal cases | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0712 | 1 | F | Corrections for non-3GPP access idle mode | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0715 | 1 | F | Integrity protection maximum data rate for UL and DL | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0717 | 1 | F | General section for limited service state over non-3GPP access | 15.2.0 |
| 2018-12 | CT#82 | CP-183041 | 0718 |  | F | T35xx in Annex D | 15.2.0 |
| 2019-01 | CT#82 |  |  |  |  | Change of IEI values from 7E to 74 and from 7F to 75 | 15.2.1 |
| 2019-03 | CT#83 | CP-190084 | 0382 | 9 | F | Correct Extended Local Emergency Numbers List use involving WLAN | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0638 | 3 | F | Clarification for abnormal case handling of registration procedure after inter-system change from S1 mode to N1 mode | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0706 | 6 | F | Resolution on the editor's note on abnormal cases in the UE for the PDU EAP message reliable transport procedure | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0721 | 2 | F | Clarification on inclusion of the Uplink data status IE in the SERVICE REQUEST message after an RRC fallback indication | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0724 | 4 | F | Corrections to Annex D | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0725 | 2 | F | Update reference for UE policy control service | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0728 | 1 | F | Completion of correction for local release | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0729 | 2 | F | UAC - access attempt matching criteria of operator-defined access categoryt | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0731 | 2 | F | Correcting the name of ITU-T Recommendation E.212 | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0732 | 2 | F | 5GSM - request type not included in PDU SESSION ESTABLISHMENT REQUEST | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0734 | 2 | F | AMF rejecting PDU session establishment when the DNN is not subscribed | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0735 | 1 | F | Correction for acknowledgement of extended emergency number list | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0741 | 3 | F | Mobility between 5GS over non-3GPP access and EPS over 3GPP access | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0743 | 1 | F | PDU session status for IWK without N26 | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0744 | 2 | F | EPS GUTI provided to lower layer | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0745 | 1 | F | Length of 5G-S-TMSI | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0746 | 3 | F | S1 UE security capability | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0747 | 2 | F | Clarification on creating new QoS flowst | 15.3.0 |
| 2019-03 | CT#83 | CP-190084 | 0750 | 1 | F | Correction to handling of #50 and #51t | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0752 | 1 | F | PDU session modification for emergency PDU sessions. | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0753 | 1 | F | Removal of unncessary text. | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0754 | 1 | F | QoS flow description to be added in PDU session modification command | 15.3.0 |
| 2019-03 | CT#83 | CP-190100 | 0758 |  | F | Correction of the erroneous length of EAP messageIE | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0759 | 2 | F | Update of SUCI encoding | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0762 |  | F | Minor corrections to TS 24.501 | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0763 | 2 | F | Cleanup on support of multiple payloads for NAS transport | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0765 | 1 | F | Correction on initial NAS message protection | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0766 | 2 | F | Correction on 5GS mobile identity IE name | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0767 | 1 | F | Addition of the 5GSM cause IE in the PDU SESSION MODIFICATION COMPLETE message | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0768 | 2 | D | Minor corrections for interworking | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0769 | 1 | F | Change of "a wildcard DNN" to "the wildcard DNN" | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0771 | 2 | F | Adding missing abnormal cases for initial registration (UE side) | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0772 | 2 | F | Clarification for the use of the default value for T3512 | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0773 | 3 | F | Removal of UE security capabilities from the S1 mode to N1 mode NAS transparent container | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0774 | 2 | F | Clarification on NSSAI inclusion mode after an inter-system change from S1 mode to N1 mode | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0780 | 1 | F | Corrections to UE policy section management result | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0785 | 1 | F | Removal of abnormal case handling for collision between initial registration and paging or notification | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0788 |  | D | DNN as a common IE | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0791 | 2 | F | Generic UE configuration update procedure during registration procedure | 15.3.0 |
| 2019-03 | CT#83 | CP-190085 | 0792 |  | D | References for NAS signalling connection recovery and a fallback indication from the lower layers | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0796 | 1 | F | Corrections on fallback indication from lower layers | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0798 | 2 | F | Correction to the notification procedure | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0801 | 1 | D | Correction on sub-clause numbering | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0802 | 3 | F | Handling of QoS flow description without valid EPS bearer contextt | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0803 |  | F | Correction on the lengths of 5GSM procedures | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0804 | 2 | F | Corrections on Mapped EPS bearer context IE | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0805 | 2 | F | Handling of missing QoS flow description and QoS rule | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0806 | 3 | F | UE re-registration following UE parameters update | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0807 | 1 | F | Clarification on providing NSSAI to the lower layer | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0808 | 1 | F | Adjustment of relevent timers when T3346 is included in the 5GMM message | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0809 | 1 | F | Clarification on PDU Session Modification procedure | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0810 | 1 | F | Clarification on the behaviors of UE and SMF during the inter-system change | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0812 | 2 | F | Several corrections to messages and IEs | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0814 | 2 | F | Correction to IEI values | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0815 | 2 | F | Resolution on editor's notes on whether explicit start and stop indications for SMS over NAS is needed | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0817 |  | F | Correction to the definition of UE STATE INDICATION message content | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0819 | 1 | F | Reference corrections on UE's state change due to congestion control | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0820 | 3 | F | Correction to behaviour upon receipt of 5GMM reject cause for a UE in single-registration mode | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0821 | 1 | F | Informing the UE about the integrity protection failure at S1 to N1 mode change | 15.3.0 |
| 2019-03 | CT#83 | CP-190086 | 0823 | 1 | F | Handling of abnormal case when UE gets UE policies with incorrect PLMN ID | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0824 |  | F | Abnormal case handling for cause#72 | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0829 | 3 | F | Correction on handling of invalid PSI | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0831 |  | F | Correction for missing 5QIs | 15.3.0 |
| 2019-03 | CT#83 | CP-190174 | 0833 | 4 | F | Possible criterion for the selection of the requested NSSAI | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0834 | 2 | F | Skip barring checks during fallback handling | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0835 | 1 | F | Correct missing Non-3GPP NW policies IE | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0836 | 1 | F | 5G-GUTI provided to lower layer | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0838 | 1 | F | Handling of abnormal authentication errors | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0839 | 1 | F | Update the conditions on the AMF to provide the configured NSSAI to the UE | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0844 | 1 | F | Rejected NSSAI for current registration area | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0845 | 1 | F | Removal of Editor's note on home network public key and home network public key identifier update and removal of protection scheme identifier | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0846 | 1 | F | Update of PDU session authentication and authorization messages | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0847 | 2 | F | Update of error handling for Mapped EPS bearer contexts IE | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0849 | 1 | F | Correction for Cause code #7 | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0854 | 1 | F | 3GPP PS Data Off UE status change and congestion control in AMF - alternative 2 | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0855 | 1 | F | Retransmission of PDU SESSION ESTABLISHMENT REQUEST | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0856 | 1 | F | Retransmission of PDU SESSION MODIFICATION REQUEST | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0857 | 1 | F | Retransmission of PDU SESSION RELEASE REQUEST | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0859 | 1 | F | Correction in EAP handling | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0860 |  | F | Issue in SNN | 15.3.0 |
| 2019-03 | CT#83 | CP-190087 | 0862 | 2 | F | Temporary identity allocation | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0863 |  | F | Initial maximum number of packet filters for associated PDU session | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0864 | 1 | F | SUCI to be used for the registration for emergency services | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0867 |  | F | Correction to the inclusion of requested QoS rule and requested QoS flow descripstion in PDU session modification request. | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0868 | 1 | F | Wrong message name | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0870 | 2 | F | SUCI applicability | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0873 | 1 | F | Transmission failure at UE side for UE policy delivery procedure | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0875 | 2 | F | Upper layer request while T3540 is running | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0876 | 1 | F | Encoding of Routing indicator set to default value 0 | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0877 | 2 | F | OS Id information element | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0878 | 1 | F | Clarification on deregistration procedure. | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0880 | 1 | D | Correction of the use of word "wants" | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0883 | 1 | F | Handling on errors of QoS flow description operations | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0885 | 1 | F | Addressing missing scenarios and providing other clarifications related to fallback indication | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0888 | 2 | F | Handling when the UE indicated security capabilities are invalid or unacceptable | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0889 | 1 | F | Correction in UE-initiated de-registration procedure initiation | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0891 | 1 | F | Reporting QoS error when a delete or modify operation is received for a non-existent QoS rule | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0892 | 1 | F | Presence of the precedence and QFI fields in QoS rules | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0894 | 2 | F | Mandating UE sending registration complete for SOR | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0895 | 1 | F | Improvement on 5G-GUTI allocation after network triggered service request | 15.3.0 |
| 2019-03 | CT#83 | CP-190088 | 0899 | 2 | F | Clarification on the authorized QoS rule modification | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0901 | 1 | F | Clarification on congestion control upon intersystem change | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0902 | 4 | F | Default EPS bearer associates with the default QoS rule | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0907 | 2 | F | NSSAI inclusion mode, EPLMNs, and registration area | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0910 | 2 | F | 5GSM messages for a PDU session associated with non-3GPP access exchanged via 3GPP access | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0911 | 1 | F | Mobility and periodic registration update initiation by a UE in inactive mode reselecting an EPLMN cell | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0912 | 1 | F | Change of N1 mode capability on UE mode change or on IMS availability change | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0914 | 1 | F | Inclusion of a 5G-GUTI mapped from the valid 4G-GUTI in the REGISTRATION REQUEST message during an initial registration is not available in Rel-15 | 15.3.0 |
| 2019-03 | CT#83 | CP-190209 | 0915 | 3 | F | Correction to the REGISTRATION REQUEST msg when the Payload container IE is included | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0917 | 1 | F | Correction to the length of the IMEISV | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0918 | 1 | F | Correcton on handing of downlink signalling and data for non-3GPP PDU session | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0919 |  | F | Correction to the Payload container IE | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0920 |  | F | Correction to several 5GMM IEs | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0921 | 1 | F | Mapped configured S-NSSAI from the S-NSSAI(s) of the HPLMN | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0922 |  | F | Use of stored NSSAI inclusion mode during initial registrationt | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0923 |  | F | Correction to the Operator-defined access category definitions IEt | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0925 | 1 | F | Non-delivery of PDU SESSION ESTABLISHMENT ACCEPT | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0926 | 1 | F | Correction to Service area list IE Type of list "11" | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0927 | 1 | F | Setting of 5GSM cause value#36 regular deactivation | 15.3.0 |
| 2019-03 | CT#83 | CP-190092 | 0929 | 3 | F | Local release | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0930 | 1 | F | Adding the UE local configuration option in 24.501 | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0933 |  | F | Handling of Replayed S1 UE security capabilities IE in Security Mode Command message | 15.3.0 |
| 2019-03 | CT#83 | CP-190089 | 0934 | 2 | F | Clarifications on use of PCF-provided PTI for UE policies delivery | 15.3.0 |
| 2019-03 | CT#83 | CP-190101 | 0720 | 1 | F | Initiation of Service Request after reception of Notification over non-3GPP while the UE is in 5GMM-CONNECTED mode with RRC inactive indication in the 3GPP access | 16.0.0 |
| 2019-03 | CT#83 | CP-190106 | 0730 | 4 | B | SINE_5G: Back-off control and retry restriction mechanisms in 5GS | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0733 | 1 | F | Transfer of a PDU session among 5G-ANs and DNN | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0739 | 5 | F | Handling for QoS Flow status synchronization failure | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0775 | 5 | F | Clarification on rejected NSSAI for the PLMN | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0782 | 1 | F | 5G-GUTI as additional guti in initial registration and UE holds 4G-GUTI | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0786 | 1 | D | Consistent description on release of N1 NAS signalling connection | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0787 | 1 | F | Correction to TFT check | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0789 | 4 | F | Handling of indication to the 5GSM sublayer in case of 5GSM message not forwarded to SMF due to service area restrictions | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0797 | 3 | F | Alignment for the notification procedure | 16.0.0 |
| 2019-03 | CT#83 | CP-190108 | 0830 |  | B | New 5QIs for Enhanced Framework for Uplink Streaming | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0840 |  | F | Update the conditions on the AMF to provide an allowed NSSAI based upon the default S-NSSAI(s) | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0841 | 1 | F | Alignment of terms of configured NSSAI and allowed NSSAI | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0842 | 1 | F | Provision of NSSAI information to the lower layers | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0843 | 1 | F | Correction for the UE configuration update procedure | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0848 | 1 | F | Clarification to definition of"ongoing service" | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0851 | 1 | F | Update of validity conditions for access identities 1 and 2 | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0852 |  | F | SR procedure for emergency services fallback when T3525 timer running | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0865 | 2 | F | Clarfication on allowed NSSAI storage in Non Volatile Memory | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0866 | 1 | F | UE state at lower layer failure on the NW side at initial registration | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0869 |  | F | Content of SMS payload container | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0872 | 1 | F | Correct mistake in case (i) in service request procedure | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0881 |  | D | Correction of wrong reference | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0886 | 2 | F | Clarifications related to fallback indication | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0896 |  | F | Correction on deriving mapped EPS security context for EPC interworking in connected mode | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0897 | 1 | F | Correction on abnormal case handlng at AMF for registration | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0904 | 2 | F | Clarification on MICO mode | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0905 |  | F | Correction on 5GMM cause #65 | 16.0.0 |
| 2019-03 | CT#83 | CP-190101 | 0924 |  | F | Correction to N1 NAS signalling connection establishment | 16.0.0 |
| 2019-03 | CT#83 |  |  |  |  | De-implementation of CR468 | 16.0.1 |
| 2019-03 | CT#83 |  |  |  |  | Completion of de-implementation of CR468 | 16.0.2 |
| 2019-06 | CT#84 | CP-191147 | 0936 |  | B | Interworking of Ethernet PDU session to Ethernet PDN connection | 16.1.0 |
| 2019-06 | CT#84 | CP-191137 | 0937 | 2 | B | PEI for 5G-CRG and FN-CRG | 16.1.0 |
| 2019-06 | CT#84 | CP-191137 | 0938 |  | B | Usage of ACS information PCO parameter | 16.1.0 |
| 2019-06 | CT#84 | CP-191137 | 0939 |  | B | Session-TMBR for PDU session in W-5GAN | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0944 | 5 | F | Handling of 5G NAS security contexts | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0946 | 1 | F | Handling of PDU session type | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 0948 | 2 | A | Precedence between access identities for derivation of RRC establishment cause and for derivation of establishment cause for non-3GPP access | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0949 |  | F | Clarifications on the validity of access identities | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0950 |  | F | Corrections to the length of the SOR transparent container and UE parameters update transparent container | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 0953 | 1 | A | Correction on T3396 | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0955 | 1 | F | Correction on the descriptions of 5GSM parameters and capabilities | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 0957 | 2 | A | Handling of PS Data Off status update | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 0959 | 1 | A | SR procedure for emergency services fallback when T3346 timer running | 16.1.0 |
| 2019-06 | CT#84 | CP-191148 | 0963 | 3 | B | Adding support for SNPNs (Stand-alone Non-Public Networks) | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0964 |  | F | Clarification on LADN information for the registered and equivalent PLMNs | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0965 | 3 | F | Clarification on the stop of T3540 | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0966 | 1 | F | Clarification on the creation of a single QoS flow during a PDU session modification procedure | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0968 | 2 | F | Correction to the checks on QoS rule operations - R16 | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0969 | 1 | B | Introduction of extended DRX for 5G CIoT | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0970 | 1 | B | Small data rate control, general description | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0971 | 1 | B | Small data rate control, activation | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0972 | 4 | B | Serving PLMN rate control, general description | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0973 | 4 | B | Serving PLMN rate control, activation | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0974 | 1 | B | Service Gap control in 5GS, general description | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0975 | 3 | B | Service Gap control in 5GS, activation with IE and indication flag | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0977 | 3 | B | Service Gap control in 5GS, enforcement in UE | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0978 | 3 | B | Service Gap control in 5GS, enforcement in AMF | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0979 | 1 | B | Service Gap control in 5GS, new time value via UCU procedure | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0980 | 1 | B | General Description for Restriction on use of enhanced coverage | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0981 | 1 | B | Updates to Registration procedure for Restriction on use of enhanced coverage | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0982 | 2 | B | Support for Reliable Data Service in 5GS | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0983 | 1 | F | Handling 5GMM cause #5 "PEI not accepted" | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0984 |  | F | Correcting UE state when disabling and re-enabling N1 mode | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0985 | 2 | F | Terminology definition for 5G_CIoT | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0986 | 3 | B | General introduction on CIoT 5GS optimizations | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0987 | 5 | B | CIoT capability negotiation between UE and network | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0988 | 3 | B | CIoT optimisations redirection betwee EPC and 5GC | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0989 | 2 | B | Inter-RAT mobility to and from NB-IoT in 5GS | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 0990 | 3 | B | Congestion control for CP data transport in 5GS | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 0992 | 2 | A | Correction on the 5GSM S-NSSAI congestion control | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0993 | 2 | F | Network slicing indication | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 0995 | 1 | A | Correction on the SMS over NAS | 16.1.0 |
| 2019-06 | CT#84 | CP-191148 | 0997 | 2 | B | Providing CAG ID to the lower layer | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 0998 | 5 | B | UE behaviour upon receiving non-integrity protected NAS reject messages in 5GS | 16.1.0 |
| 2019-06 | CT#84 | CP-191217 | 1000 | 5 | A | Multiple NAS connections and 5G NAS security context change handling | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1002 | 1 | A | EPS bearer synchronization when moving from EPC to 5GC | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 1018 | 6 | F | UE-requested PDU session modification procedure and exemption indication | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 1019 | 1 | B | Active Time for MICO mode | 16.1.0 |
| 2019-06 | CT#84 | CP-191138 | 1020 | 5 | B | MA PDU request in UL NAS TRANSPORT message | 16.1.0 |
| 2019-06 | CT#84 | CP-191138 | 1021 | 4 | B | Update PDU session establishment procedure to support MA PDU session | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 1022 |  | F | Correction to Mico mode activation in the UE | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 1023 | 4 | F | Correction to rejected NSSAI deletion. | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 1025 |  | A | Correction of timer table | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 1027 | 2 | F | Coordination between GMM and 5GMM | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 1029 | 2 | F | Correction of requirements for the handling of access barring | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 1030 | 2 | B | Strictly periodic registration timer indication for MICO mode | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 1037 | 2 | A | Network initiated deregistration update for cause #3 and #6 | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 1038 |  | F | Correction of typos in octet numbering for AMF Set ID | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 1039 |  | F | Stopping T3519 and deleting SUCI when receiving authentication reject | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 1041 | 1 | A | Correct UE parameters update data type | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 1043 | 2 | F | Clarifications to the Routing indicator encoding | 16.1.0 |
| 2019-06 | CT#84 | CP-191132 | 1045 | 1 | F | Correction on Payload container type information element | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 1046 | 2 | B | Introduction to UE selection of CN for 5G CIoT (for 24.501) | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1047 |  | F | Exception in suspension of 5GSM procedures in case of ongoing 5GMM procedures: Service request procedure initiated during connected mode | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 1050 | 1 | A | PDU SESSION ESTABLISHMENT message sent via target access in case of handover of an existing PDU session between 3GPP access and non-3GPP access | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1052 | 2 | F | Retreival of an SMF ID during transfer of a PDN connection in EPS to 5GS | 16.1.0 |
| 2019-06 | CT#84 | CP-191146 | 1053 | 3 | F | Clarification of 5GSM cause values for which network may include a back-off timer or a re-attempt indicator | 16.1.0 |
| 2019-06 | CT#84 | CP-191148 | 1054 | 4 | B | Introduction of non-public network | 16.1.0 |
| 2019-06 | CT#84 | CP-191148 | 1055 | 1 | B | PLMN ID and NID provided to the lower layers | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1058 |  | F | Extensible Authentication Protocol specified in IETF RFC 3748 | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1059 |  | F | Corrections on security context terminologies | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1060 | 2 | F | Correction on UE handling for network initiated de-registration with #22 | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1061 | 1 | F | T3540 handling for re-registration triggered by UCU | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1062 | 2 | F | Correction on coding of "all other values are spare" | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 1064 | 2 | A | Indication of resume failure from the lower layer | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1066 | 1 | F | Integrity protection failure | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1067 | 1 | F | Clarification related to dual registration mode | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1070 |  | F | Including the other cases in [S-NSSAI, DNN] combination back-off timer | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1071 | 4 | A | Correction to the Payload container IE | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 1073 | 3 | A | Correction because of wrong implementation of CR0763 and CR0919 | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 1075 | 2 | A | Resolution of editor's notes on handling at emergency registration and emergency PDU sessions | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 1077 | 2 | A | Resolution of editor's notes on handling at non-existing 5G NAS security context indicated by the UE when an emergency PDU session exists | 16.1.0 |
| 2019-06 | CT#84 | CP-191137 | 1078 | 3 | B | Introduction of general aspects of wireline access | 16.1.0 |
| 2019-06 | CT#84 | CP-191137 | 1082 | 1 | B | Introduction of references, definitions and abbreviations for 5WWC | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1088 | 1 | F | Correction on PTI error handling of the UE | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1090 | 1 | F | Correction on PTI error handling of the network | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1092 | 1 | F | Correction on QoS rule operation | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 1094 | 1 | A | Correction on handling of mapped EPS bearer contexts IE | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1096 | 2 | F | Correction on associating default EPS bearer with the default QoS rule | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1098 | 1 | F | Feature support after inter-system change from 5GS to EPS | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1100 | 3 | F | Correction on 5GSM IE handling when an error is detected | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1105 | 1 | F | Security Mode Command procedure when S1 mode supported | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1107 | 1 | F | Correction of term"user preference"to"UE local configuration"for inter-system change without N26 | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 1109 | 1 | A | Addition of missing codepoints for 5GSM causes | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1114 | 2 | F | Modification of the maximum number of supported packet filters | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1115 | 1 | F | 5GS-EPS interworking for Multi-homed IPv6 PDU Session not supported without N26 | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1118 | 3 | F | UE-requested PDU session modification for emergency PDU session | 16.1.0 |
| 2019-06 | CT#84 | CP-191133 | 1119 |  | F | Clarification of emergency support indications | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 1121 | 3 | A | Access control and indication that access barring is applicable for all access categories except categories '0' and '2' | 16.1.0 |
| 2019-06 | CT#84 | CP-191138 | 1122 | 2 | B | Multiple Access PDU Session | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 1124 | 1 | A | 5GSM cause value #29 semantic extension | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 1128 | 4 | A | NSSAI inclusion mode in ePLMN | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 1129 | 1 | F | Interaction between active time for MICO mode and eDRX | 16.1.0 |
| 2019-06 | CT#84 | CP-191224 | 1130 | 4 | B | User plane CIoT 5GS optimization | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 1131 | 3 | B | CP only indication | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1133 | 1 | A | Handling of PDU session modification while a back-off timer is running | 16.1.0 |
| 2019-06 | CT#84 | CP-191148 | 1134 | 1 | B | Adding support for unified access control in SNPNs (Stand-alone Non-Public Networks) | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1135 | 1 | D | The phrase"outside the scope of the present document"is not used consistently | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1137 | 3 | F | Clarification regarding replayed UE security capabilities | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 1140 | 1 | A | UE policy length mismatch | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1142 | 2 | F | Conditions for congestion control in AMF | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1146 | 3 | F | Correction of inconsistent requirements for the use of SUCI | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1147 | 1 | F | Disabling of N1 mode capability after emergency services fallback | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1149 | 1 | F | Clarification on disabling N1 mode capability when there is persistent PDU session | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1151 | 1 | A | Indicating PS data off status report for the UE in the Non-allowed Area | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1156 | 1 | F | Clarification of "registration requested" with no other parameters | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1157 |  | F | Updates to Network slicing indication | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1160 |  | F | Clarification on the length of the key stream for initial NAS message protection | 16.1.0 |
| 2019-06 | CT#84 | CP-191207 | 1162 | 4 | F | Applicability of the allowed NSSAI in an equivalent PLMN outside the UE's registration area | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1164 | 3 | A | Handling of the ABBA parameter with a non-zero value and a length of more than 2 octets | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1165 | 1 | F | Clarifications to service area restrictions | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1168 | 1 | A | IEI for the Non-3GPP NW provided policies IE | 16.1.0 |
| 2019-06 | CT#84 | CP-191136 | 1169 |  | F | Reference to IEEE 802.3 | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1171 | 2 | A | Correction to serving network name (SNN) reference | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1173 | 1 | A | IEI for the UE OS Id IE | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1174 | 2 | F | Correction for PDU session modification with QFI change. | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1175 | 2 | F | Correction to PDU session release reject handling | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1176 | 1 | F | Correction to PDU session authentication result transport procedure. | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1177 | 1 | F | Clarification for transfter of PDU session for LADN to EPS. | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1178 | 1 | F | Correction to De-registration and registration procedure collision | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1179 |  | F | Clarification for 5GMM cause #3 and #6 in the SERVICE REJECT message | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1180 | 2 | F | Added detailed description for substates INITIAL-REGISTRATION-NEEDED and UPDATE-NEEDED | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1182 |  | D | Minor editorial corrections | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 1185 | 1 | A | Always-on PDU session | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1186 | 1 | F | S-NSSAI association for PDU session established in S1 mode | 16.1.0 |
| 2019-06 | CT#84 | CP-191130 | 1187 | 1 | B | 5GMM capability for SRVCC from NG-RAN to UTRAN | 16.1.0 |
| 2019-06 | CT#84 | CP-191130 | 1188 | 1 | B | MS classmark 2 and supported codec | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1191 | 2 | F | Handling of 5GSM parameters | 16.1.0 |
| 2019-06 | CT#84 | CP-191134 | 1193 | 2 | F | Handling of SM back-off timer | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1195 | 1 | A | DNN based congestion control for PDU session for LADN | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1197 |  | F | Terminology correction about PDU session type | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1199 | 1 | F | Definition of EMM-IDLE mode in TS 24.501 | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 1200 |  | F | No CIoT 5GS optimizations for non-3GPP access | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 1203 | 2 | A | Network initiated EPS bearer synchronization when moving from EPC to 5GC | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1204 | 1 | F | Correction on follow-on request indicator | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1205 |  | F | Correction on UE behaviour in 5GMM-REGISTERED.PLMN-SEARCH | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1206 | 1 | A | Deletion of the 5GSM cause IE in the PDU SESSION MODIFICATION COMPLETE message | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1207 | 1 | F | Correction on the abnormal cases for registration procedure | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 1210 |  | F | Alignment of the Abnormal cases for eDRX between 5GS and EPS | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1211 | 1 | F | Collision handling | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1212 | 2 | F | Authenticate before deleting UE context | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 1213 | 3 | B | Uplink NAS message transmission and CIoT data transfer | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1214 | 1 | F | Correction on T3346 and EPLMN handling | 16.1.0 |
| 2019-06 | CT#84 | CP-191122 | 1219 | 2 | A | Alignment of the 5G ciphering and integrity algorithm identifiers | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1220 | 2 | F | Conditions to apply the "null-scheme" to generate the SUCI | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1221 |  | F | Correction on the description of code point for 128-5G-EA3 | 16.1.0 |
| 2019-06 | CT#84 | CP-191129 | 1222 | 1 | B | Service Gap control in 5GS, reject of UL NAS Transport message | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1227 | 2 | F | Transmission failure of Registration Request during Initial Reg proc | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1228 | 3 | F | Handling of Radio Link failure during service Req proc | 16.1.0 |
| 2019-06 | CT#84 | CP-191148 | 1229 | 1 | B | Abnormal case handling for receipt of 5GMM cause value #11 from a PLMN | 16.1.0 |
| 2019-06 | CT#84 | CP-191148 | 1231 | 2 | B | Packet filters based on N3IWF IP address and SPI for IPsec SA | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 1238 | 1 | A | QoS flow for SIP signalling after inter-system change | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1239 | 1 | F | Handling of multiple QoS rule/flow parameters included in one PCO/ePCO | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1240 | 1 | F | Error handling of optional IEs in a payload container entry of the Payload container IE | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1241 |  | F | Add codings of 5GSM causes #41 and #42 | 16.1.0 |
| 2019-06 | CT#84 | CP-191124 | 1245 | 1 | A | Indication of syntactical or semantic errors related to SM policy association to UE | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1246 | 3 | F | Clean-up of general section for 5GMM aspects of network slicing | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1247 |  | F | Request from the upper layers to perform emergency service fallback | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1248 |  | F | Non-overlapping tracking areas | 16.1.0 |
| 2019-06 | CT#84 | CP-191146 | 1249 | 1 | C | 5GSM cause values #27, #50, #51 and #70 for SINE_5G | 16.1.0 |
| 2019-06 | CT#84 | CP-191123 | 1251 | 1 | A | Correction to handling of cause #72 | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1254 | 2 | F | Originating MMTEL voice due to upper layers request while T3346 is running | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1257 |  | F | Shared or valid 5G NAS security context | 16.1.0 |
| 2019-06 | CT#84 | CP-191135 | 1264 | 1 | F | EAP-success of EAP-TLS received in SECURITY MODE COMMAND | 16.1.0 |
| 2019-09 | CT#85 | CP-192073 | 1056 | 5 | B | Provisioning of an allowed CAG list and a CAG access only indication | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1057 | 8 | B | 5GMM cause value for CAG | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1189 | 3 | F | PDU session modication command not forwarded to 5G AN | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1236 | 3 | B | Storage for CAG information | 16.2.0 |
| 2019-09 | CT#85 | CP-192060 | 1269 | 2 | B | Procedure for Multiple Access upgrade of PDU Session | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1270 | 1 | F | Handling the non-current 5G NAS security context after inter-system change from N1 mode to S1 mode | 16.2.0 |
| 2019-09 | CT#85 | CP-192060 | 1271 | 2 | B | NSSAI not allowed for MA PDU session establishment | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1273 |  | F | Updates to new stage-2 requirements of CAG information structure | 16.2.0 |
| 2019-09 | CT#85 | CP-192059 | 1274 | 2 | F | Wireline access is a type of non-3GPP access | 16.2.0 |
| 2019-09 | CT#85 | CP-192059 | 1276 | 2 | F | Management of service area restrictions in wireline access | 16.2.0 |
| 2019-09 | CT#85 | CP-192059 | 1277 | 2 | F | IP address allocation for 5G-RG | 16.2.0 |
| 2019-09 | CT#85 | CP-192059 | 1278 | 2 | B | Security for W-AGF acting on behalf of an FN-RGt | 16.2.0 |
| 2019-09 | CT#85 | CP-192059 | 1279 | 1 | C | Alignment with stage-2 on PEI for 5G-RG and FN-RG | 16.2.0 |
| 2019-09 | CT#85 | CP-192063 | 1280 | 2 | B | V2X capability and V2X PC5 capability | 16.2.0 |
| 2019-09 | CT#85 | CP-192063 | 1281 | 1 | B | USPS extension for V2X policy | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1282 |  | F | Incorrect security algorithm | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1283 |  | F | Registration attempt counter correction | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1286 | 2 | C | 5GMM cause values applicable in an SNPN | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1287 | 1 | F | Clarification for UE selecting a suitable cell that supports CIoT optimisation | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1288 | 1 | F | Core network type restriction determined by operator policy | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1290 | 1 | F | Disabling the N1 mode capability for 3GPP access in Idle mode | 16.2.0 |
| 2019-09 | CT#85 | CP-192060 | 1293 | 1 | C | PDU Session release for MA PDU Session | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1295 | 1 | F | Clarification on error check for QoS rules | 16.2.0 |
| 2019-09 | CT#85 | CP-192060 | 1297 | 1 | B | MA PDU session establishment reject due to unstructured PDU Session type | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1298 |  | F | Clarification for T3580 Stop condition | 16.2.0 |
| 2019-09 | CT#85 | CP-192060 | 1300 | 1 | B | MA PDU session modification for ATSSS parameters | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1302 | 3 | F | Staying in inactive upon resume failure with RRC staying in RRC_INACTIVE | 16.2.0 |
| 2019-09 | CT#85 | CP-192045 | 1306 | 1 | A | Maintaining the UL and DL NAS COUNTs after a handover from 5GS to EPS | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1308 | 2 | BV | PDU sessions and QoS flows for NB-IoT UEs | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1311 | 3 | B | Idle mode optimizations for 5G Control plane CIoT small data transfer t | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1315 | 1 | F | Performing registration update upon resume failure for reasons other than barring | 16.2.0 |
| 2019-09 | CT#85 | CP-192062 | 1316 | 2 | B | 5GMM capability update for eNS | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1318 | 1 | B | Header compression for control plane user datat | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1322 | 1 | B | UE behavior when RRC connection resume failst | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1323 | 1 | F | Correction on service gap timer | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1324 | 1 | F | Correction on T3448 value IE | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1325 | 1 | F | Alleviation of SM congestion | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1326 |  | F | Correction wrt EPS attempt counter to be used for Single Registration Failure use cases | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1328 |  | F | Correction on terminology regarding EPS bearer contextst | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1330 | 1 | F | Correction to SM procedures for back off timer not forwarded from 5GMM case. | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1332 |  | F | Deletion of RAND and RES on receiving Service Accept message | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1333 |  | F | Clarification for emergency call when T3396 or T3585 is running | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1334 | 1 | F | Removal of Editors Note for active timers in the NW | 16.2.0 |
| 2019-09 | CT#85 | CP-192083 | 1335 | 1 | B | Addition of LCS indication in 5GMM capability and 5GS NW capability | 16.2.0 |
| 2019-09 | CT#85 | CP-192083 | 1336 | 1 | B | Addition of location service message condition to Additional informaton IE | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1337 |  | F | Minor miscellaneous corrections | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1340 |  | F | Clarify encoding of EPS bearer identity | 16.2.0 |
| 2019-09 | CT#85 | CP-192071 | 1341 |  | F | Keep equivalent PLMNs list for Deregistration Request message with 5GMM cause #7 | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1344 |  | F | Correction to handling of operator-defined access category missing a standardized access category | 16.2.0 |
| 2019-09 | CT#85 | CP-192056 | 1345 | 1 | F | ODAC IEI correction | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1346 |  | F | Removal of eDRX support with RRC_INACTIVE for NB-IoT | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1348 | 1 | F | IMEI not required for non-3GPP only UEs | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1351 | 1 | F | Emergency services fallback from non-3GPP access or ePDG/EPC | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1353 | 1 | F | Re-ordering of text on the applicability of access identities | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1354 | 1 | F | Trigger for NAS procedure retry in case NAS is put back in RRC inactivet | 16.2.0 |
| 2019-09 | CT#85 | CP-192069 | 1355 |  | B | Adding general description of RACS | 16.2.0 |
| 2019-09 | CT#85 | CP-192069 | 1356 | 1 | B | Signalling of UE support for RACS and of UE radio capability ID | 16.2.0 |
| 2019-09 | CT#85 | CP-192069 | 1357 | 2 | B | UE radio capability ID assignment by the network | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1358 | 1 | B | Signalling of UE support for transfer of port management information containers, MAC address and DS-TT residence time | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1359 | 2 | B | Adding support for transfer of Ethernet port management information containers | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1360 | 1 | F | Removal of Editor's note on adding unified access control configuration to "list of subscriber data" for access to SNPNs | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1361 | 2 | F | Resolution of Editor's notes on abnormal case handling for UE-initiated de-registration procedure in an SNPN | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1363 | 1 | F | Resolution of Editor's notes on the applicability of MPS, MCS and delay tolerant in SNPNs | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1364 | 1 | F | Update of requirements on UE to construct packet filters based on the N3IWF destination IP address and the SPI for the IPsec SA | 16.2.0 |
| 2019-09 | CT#85 | CP-192083 | 1365 | 2 | B | NAS transport of supplementary services messages for a deferred 5GC-MT-LR | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1366 |  | F | Resolve Editor's note on support indication for Small Data Rate Control | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1367 | 1 | B | Small data rate control parameters received in EPS | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1369 | 1 | F | Including EPS Preferred Network Behaviour to 5GCN | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1370 | 1 | F | General description on redirection of the UE by the core network | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1371 |  | F | No RRC inactive for NB-IoT | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1372 |  | F | Removal of Editor's Note for the T3348 | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1380 |  | F | T3540 for 5GMM cause #31 or #73 | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1384 | 1 | F | Service gap control timer and MICO mode | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1385 | 2 | F | Service gap control, stop of timer via configuration update command | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1386 |  | F | Service gap control, MO service request when connected and timer running | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1387 | 2 | C | Service gap control, follow-on request indicator at mobility update registration | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1388 | 2 | 2 | Service gap control, follow-on request indicator at initial registration | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1391 |  | F | MICO mode and stop of active timer in AMF when UE enters 5GMM-CONNECTED | 16.2.0 |
| 2019-09 | CT#85 | CP-192062 | 1395 | 3 | C | Registration reject due to no available allowed S-NSSAI(s) | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1396 | 1 | F | Service gap control, MO SMS or LPP payload not allowed when connected | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1398 | 1 | F | Consistent use of PLMN ID for AKA | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1399 |  | F | Service reject without integrity protection | 16.2.0 |
| 2019-09 | CT#85 | CP-192052 | 1405 |  | F | Strictly periodic handling due to emergency service. | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1406 | 2 | F | Emergency call handling for a CAG only UE | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1408 |  | F | Collision of deregistration and other NAS procedure | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1410 |  | D | Missing inactive term. | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1411 | 1 | F | Handling of an emergency call in SNPN access mode. | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1412 | 1 | F | Initial NAS message protection | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1413 | 1 | F | Stopping conditions for Timer T3565. | 16.2.0 |
| 2019-09 | CT#85 | CP-192062 | 1421 | 4 | BV | Update of existing subclause for network slice specific authentication and authorizationt | 16.2.0 |
| 2019-09 | CT#85 | CP-192060 | 1425 | 1 | F | Updates to UE-requested PDU session procedures for converting to MA PDU session | 16.2.0 |
| 2019-09 | CT#85 | CP-192059 | 1427 | 2 | F | Applicability of unified access control for wireline 5G access network | 16.2.0 |
| 2019-09 | CT#85 | CP-192070 | 1434 | 2 | F | Correction of handling of 5GSM causes #27 and #70 for SINE_5G | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1435 | 1 | F | Corrections to the disabling and re-enabling of N1 mode | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1436 | 1 | F | FPLMN list for 3GPP and non-3GPP access types | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1438 | 1 | F | Resolve ENs in clause 5.3.20 | 16.2.0 |
| 2019-09 | CT#85 | CP-192083 | 1440 | 1 | B | Access control on MO-LR | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1442 |  | F | Barred MO SMSoNAS | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1448 |  | F | Correction of the QoS rule operation name | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1453 | 2 | B | Handling of non-integrity protected messages in an SNPN | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1454 | 1 | C | Support of network slicing in an SNPN | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1456 | 1 | F | Lists of forbidden networks in an SNPN | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1457 | 1 | F | Lists of forbidden TAIs in an SNPN | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1458 | 1 | F | 5G-GUTI not globally unique in an SNPN | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1460 | 2 | C | Shared network broadcasting PLMN identity(ies) or SNPN identity(ies) | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1461 | 2 | F | Alignment on the implication description of type of list ="11"in service area list IE | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1466 | 1 | B | Support of time sensitive communication | 16.2.0 |
| 2019-09 | CT#85 | CP-192073 | 1470 | 2 | B | Port management information container: Delivery via the NAS protocol and coding | 16.2.0 |
| 2019-09 | CT#85 | CP-192054 | 1474 | 2 | F | Update the UE-requested PDU session establishment procedure regarding always-on PDU session for URLLC service | 16.2.0 |
| 2019-09 | CT#85 | CP-192054 | 1476 | 2 | F | Update the network-requested PDU session modification procedure regarding always-on PDU session for URLLC service | 16.2.0 |
| 2019-09 | CT#85 | CP-192057 | 1482 | 1 | F | Periodic update is allowed also in non-allowed area | 16.2.0 |
| 2019-12 | CT#86 | CP-193094 | 1233 | 4 | F | QoS operation upon activation of dedicated EPS bearer | 16.3.0 |
| 2019-12 | CT#86 | CP-193100 | 1275 | 3 | F | Management of forbidden area in wireline access | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1284 | 2 | F | Handling of unknown, unforeseen, and erroneous UPDS data in UE policy delivery service | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1327 | 4 | F | Handing of 5GMM parameters during certain mobility registration failurest | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1339 | 2 | F | Consistent back off timer handling for EPC interworking | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1342 | 2 | F | Local release when receiving REFRESH command for routing indicator in RRC inactive | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1349 | 3 | F | UAC check for services started in WLAN and being transferred to 3GPP access | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1352 | 2 | F | Addition of abnormal case handling for T3346 running in NAS transport procedure | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1373 | 4 | F | Maintenance of forbidden TA lists for non-integrity protected NAS reject | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1374 | 2 | F | EMM parameters handling for 5G ony causes | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1375 | 5 | F | Covering 5GMM cuase #31 for DoS attack | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1376 | 3 | F | UE checking the active EPS bearer ID for mapped QoS flows | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1378 | 3 | F | 5G NAS security context for interworking | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1397 | 2 | F | Clarification on handling of MP-REG | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1400 | 3 | F | Correction on handling and coding of Mapped EPS bearer contexts | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1401 | 4 | F | QoS rule and QoS flow error handling | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1402 | 2 | F | QoS error operation during interworking | 16.3.0 |
| 2019-12 | CT#86 | CP-193115 | 1403 | 1 | F | Correction on the condition for handling reattempt for PDU session type related rejection | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1404 | 1 | F | Additional 5GS PDU session rejection cause values | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1409 | 4 | F | Emergency registered state handling. | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1416 | 2 | F | Correction for N1 signalling connection release | 16.3.0 |
| 2019-12 | CT#86 | CP-193094 | 1418 | 3 | F | Emergency PDU session establishment upon expiry of timer T3580 | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1426 | 1 | F | Correction to the storage of 5GMM information; SOR counter and a UE parameter update counter | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1431 | 8 | B | Transmission of the UE CAG capability to the network | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1432 | 3 | F | Correction of 5GMM state for cause #27 "N1 mode not allowed" | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1433 | 3 | F | Correction and clarification of interworking with ePDG connected to EPC | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1449 | 1 | F | No requirement for network to store a back-off timer per UE and other criteria | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1450 | 5 | B | Slice-specific authentication and authorization procedure | 16.3.0 |
| 2019-12 | CT#86 | CP-193115 | 1452 | 3 | B | Back-off control in case of routing failure | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1469 | 3 | C | PDU session used for TSC established as an always-on PDU session | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1480 | 7 | F | Correction to delivery of mapped S-NSSAI(s) | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1489 |  | F | Correction of statement related to K'AMF derivation during S1 to N1 handover | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1490 | 1 | C | Condition to avoid redundant registration procedures during inter system change from S1 to N1 mode | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1493 | 1 | F | Removal of update status dependency for sub-state selection | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1494 | 2 | F | Handling of pending NAS messages during resume of the N1 NAS signalling connection | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1495 | 1 | F | Apply UAC during resume of the N1 NAS signalling connection | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1496 | 2 | F | Receiving deregistration with cause #72 when registered for both 3GPP and Non-3GPP accesst | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1497 | 2 | F | Correcting DDX description | 16.3.0 |
| 2019-12 | CT#86 | CP-193113 | 1499 |  | F | Correct UE radio capability ID reference | 16.3.0 |
| 2019-12 | CT#86 | CP-193101 | 1500 | 2 | B | MA PDU session release | 16.3.0 |
| 2019-12 | CT#86 | CP-193101 | 1501 |  | F | Addthemissing MAPDUrequest | 16.3.0 |
| 2019-12 | CT#86 | CP-193101 | 1504 | 2 | F | MA PDU session rejection due to operator policy and subscription policy | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1505 | 6 | C | Introduction of pending NSSAI for network slice-specific authentication and authorization | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1506 | 1 | F | Resolving Editor's Note for need of new EPD in CPSR message | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1507 | 1 | F | Resolving Editor's Note on whether CIoT small data container IE can be TV format in CPSR message | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1509 | 2 | F | Corrections of service gap controlt | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1510 | 3 | B | Primary authentication using EAP methods other than EAP-AKA' and EAP-TLS | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1511 | 1 | B | Serving network name in SNPN | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1512 | 2 | B | Extensions of EAP-TLS usage in primary authentication | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1513 |  | B | Extensions of EAP-AKA' usage in primary authentication | 16.3.0 |
| 2019-12 | CT#86 | CP-193100 | 1514 | 1 | F | Further alignment with stage-2 on PEI for 5G-RG and FN-RG | 16.3.0 |
| 2019-12 | CT#86 | CP-193100 | 1515 | 1 | F | Corrections for wireline access service area restrictions | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1516 | 2 | F | Corrections related to Service Gap timer | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1517 | 1 | F | 5GS Control plane CIoT data transfer for UE in connected mode | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1518 | 2 | F | NAS message container for Control plane service request | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1519 | 4 | F | Abnormal case handling for uplink NAS transport for non-supporting UEs | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1520 | 2 | F | Applicability of existing emergency PDU session request type | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1523 |  | F | Corrections on the Port management information container IE | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1526 | 6 | F | Deregistration due to the failed network Slice-Specific Authentication and Authorization | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1527 | 1 | F | Correction of the misuse of T3525 | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1529 |  | F | Inclusion of the T3324 IE in REGISTRATION ACCEPT | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1532 | 1 | C | Control plane service request message and abnornal cases on the network side | 16.3.0 |
| 2019-12 | CT#86 | CP-193113 | 1535 | 1 | B | RACS support at EPS to 5GS IWK | 16.3.0 |
| 2019-12 | CT#86 | CP-193113 | 1539 | 1 | F | UE storage of RACS parameters in non-volatile memory | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1541 | 1 | B | Initial Small Data rate control parameters | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1542 |  | F | Reset of registration attempt counter at registration reject with cause #62 | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1543 |  | F | Incorrect reference in Authentication subclause | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1544 |  | F | IE inclusion criteria style alignment | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1545 | 1 | C | CP CIoT header compression, UE initiated re-configuration | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1546 | 1 | F | Corrrection to the notification procedure and collision with UE initiated de-registration | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1547 | 1 | F | Request of IMEISV via the security mode control procedure | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1548 | 1 | F | Service gap control, simultaneous registration over N3GPP access in same PLMN | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1549 | 3 | F | Registration reject due to no allowed slices and NW slice specific authentication and authorization | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1551 | 2 | F | Clarification to forbidden TAI lists for SNPN | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1552 | 1 | F | Clarification to PLMN-SEARCH substate. | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1553 | 1 | F | Correction to SNPN enabled terminology. | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1555 | 2 | F | 5GMM cause value #74 and requirements for non-integrity protected reject messages | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1556 | 1 | F | Discarding the REGISTRATION REJECT message with 5GMM cause #76 received without integrity protection | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1558 |  | F | Handling of the DEREGISTRATION REQUEST message with 5GMM cause value #74 or #75 in a PLMN | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1559 |  | F | Reset of the registration attempt counter upon receipt of NPN-based cause values | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1560 |  | F | Handling of T3510, T3517, and the service request attempt counter in an SNPN | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1561 | 4 | F | Missing requirement on UE policies for SNPN | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1562 | 1 | F | Corrections of RRC requirements specified in NAS specs | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1563 | 5 | F | Handling of maximum number of allowed active DRBs | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1565 |  | F | Correction to name of IE carrying residence time for TSN | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1569 |  | F | Stop conditions for timers T3580 and T3581 | 16.3.0 |
| 2019-12 | CT#86 | CP-193115 | 1570 | 1 | F | Correction to re-attempt indicator IE description | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1571 | 2 | F | 5GMM Cause #62 | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1574 |  | F | SMC message trigger | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1575 | 1 | F | Congestion control for UL NAS TRANSPORT message | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1577 | 1 | F | Applying small data rate control at inter-system change | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1578 | 1 | F | Counter events handling for SNPN | 16.3.0 |
| 2019-12 | CT#86 | CP-193118 | 1579 | 1 | F | 5GMM cause handling for SNPN | 16.3.0 |
| 2019-12 | CT#86 | CP-193101 | 1580 | 1 | F | Provision of MA PDU session information during the UE-initiated NAS transport procedure initiation | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1583 |  | F | Octet alignment for 5G-GUTI in 5GS mobile identity IE | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1584 | 1 | F | Clarification on handling of 5G NAS security context | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1585 | 1 | C | Resolving Editor's notes on the Data Type field for the Control Plane Service Request message | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1586 | 1 | F | Registration upon change of UE radio capability during 5GMM-CONNECTED mode | 16.3.0 |
| 2019-12 | CT#86 | CP-193095 | 1589 |  | F | Handling of 5GSM cause #54 PDU session does not exist | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1590 | 1 | F | Correction to the indication upon receipt of 5GMM cause #91 | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1592 | 2 | F | Handling of errors in mapped EPS bearer contexts | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1593 | 1 | F | Cleanups and editorials | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1598 | 4 | B | "S-NSSAI not available in the current PLMN" when non NSSAA supported UE requesting the S-NSSAI subjects to NSSAA | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1602 | 6 | B | NSSAI storage impact with NSSAA | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1603 |  | F | EHPLMN and Dual registration | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1604 | 7 | F | CAG only UE and emergency procedure. | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1605 | 3 | F | SGC timer and handling during intersystem change | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1608 |  | F | Abbreviation of AUSF and UDM | 16.3.0 |
| 2019-12 | CT#86 | CP-193106 | 1619 | 1 | B | Release of NAS signalling connection for the UE authorized for V2X communication over PC5 | 16.3.0 |
| 2019-12 | CT#86 | CP-193113 | 1622 | 3 | F | Identification procedure for RACS | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1623 | 2 | F | Control plane service request, correction regarding service accept message applicability | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1625 | 2 | F | Precedence for segregation flow | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1628 | 4 | F | Unified Access Control for IMS registration related signalling | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1633 | 1 | B | Handling of non-integrity protected rejects when registered | 16.3.0 |
| 2019-12 | CT#86 | CP-193101 | 1636 |  | D | Editorial on PDU session establisment request upgraded to MA PDU session | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1640 | 1 | C | Handling of MT paging for CP-CIoT | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1647 | 2 | B | 5GS NAS extended timers for NB-N1 mode and WB-N1/CE mode devices | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1648 | 1 | C | Serving PLMN rate control at PDU session modification | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1649 | 1 | F | Clarification on the Mapped EPS bearer context | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1650 |  | D | Editorial corrections to text related to the status of PDU sessions during SR procedure | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1651 | 1 | F | Short MAC and ngKSI in Control plane service request NAS message | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1657 | 2 | B | Introduction of NSSAI efficient signalling for IoT devices | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1658 | 1 | C | Removal of Editor's note on conditions of accepting registration | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1660 | 2 | F | UE behaviour when T3448 timer running | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1661 |  | F | AMF behaviour for mobility registration when SGC timer running | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1662 |  | F | Clarification on the UE policy container | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1663 | 1 | F | DNN Replacement | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1664 | 1 | F | Faulty and missing reference | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1665 | 1 | F | Correction of handling of de-registration procedure in ATTEMPTING-REGISTRATION-UPDATE | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1666 | 1 | F | Corrections and enhancements for T3540 | 16.3.0 |
| 2019-12 | CT#86 | CP-193084 | 1668 | 2 | A | Handling of UE NAS Count during handover from N1 mode to S1 mode | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1669 | 2 | F | Handling multiple QoS errors during a PDU session modification procedure – Option 1 | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1674 | 1 | F | No info on S-NSSAI subject to NSSAA in UE | 16.3.0 |
| 2019-12 | CT#86 | CP-193169 | 1676 | 2 | F | Equivalent SNPNs not supported for stand-alone non-public networks | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1680 |  | F | 5GMM state in non-3GPP access not impacting EMM state of single-registered UE | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1681 | 1 | F | Registration attempt counter reset by single-registered UE | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1682 |  | F | Correction for 5GMM and inter-system change | 16.3.0 |
| 2019-12 | CT#86 | CP-193096 | 1683 |  | F | Correction for 5GSM and inter-system change with N26 | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1684 | 1 | F | Clarification to forbidden PLMN list | 16.3.0 |
| 2019-12 | CT#86 | CP-193100 | 1685 |  | C | Access stratum connection and user-plane resources for trusted non-3GPP access and wireline access | 16.3.0 |
| 2019-12 | CT#86 | CP-193100 | 1686 | 1 | B | Usage of PDU session identity for the PDU sessions requested by the TWIF | 16.3.0 |
| 2019-12 | CT#86 | CP-193100 | 1687 |  | C | Removal of Session-TMBRt | 16.3.0 |
| 2019-12 | CT#86 | CP-193100 | 1688 |  | C | 5G-RG and W-AGF acting on behalf of FN-RG performing UE requirements | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1690 |  | F | Correction for 5GS network feature support IE | 16.3.0 |
| 2019-12 | CT#86 | CP-193106 | 1692 | 1 | B | UPDS updates enabling UE-requested V2X policy provisioning procedure | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1693 | 1 | B | Exchange of port management capabilities during PDU session establishment | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1694 | 1 | C | Additional abnormal cases in SNPN | 16.3.0 |
| 2019-12 | CT#86 | CP-193106 | 1697 | 1 | B | 5QI 86 introduction | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1698 | 1 | F | Deletion of UE radio capability in the network | 16.3.0 |
| 2019-12 | CT#86 | CP-193115 | 1699 | 1 | C | Retry restriction on non-3GPP access | 16.3.0 |
| 2019-12 | CT#86 | CP-193115 | 1700 | 1 | F | No retry restriction for 5GSM cause value #39 | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1702 | 3 | C | Support of UE specific DRX for NB-IoT | 16.3.0 |
| 2019-12 | CT#86 | CP-193090 | 1705 | 1 | B | Transfer of Ciphering Key Information for Broadcast Location Assistance Data | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1707 |  | F | Timer T3448 | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1709 | 1 | F | Rejected NSSAI | 16.3.0 |
| 2019-12 | CT#86 | CP-193090 | 1710 | 1 | F | Sending location services data from 5GMM-IDLE mode using the Control Plane Service Request message | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1711 | 1 | F | Correction of the format of CIoT small data container | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1712 | 3 | F | Removal of a Code-Point in Control Plane Service Type | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1715 | 1 | F | Correction to EPLMN list deletion for 5GMM cause #7 | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1716 |  | F | Correction to UE OS ID encoding | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1717 | 3 | F | Removal of CAG suscription while emergency PDU session is established. | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1718 | 1 | F | Defenition of CAG cell, CAG ID and CAG selection | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1719 | 2 | F | Handling of Service request message in a non-subscribed CAG cell | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1720 | 1 | F | Updation of LIMITED SERVICE state for CAG | 16.3.0 |
| 2019-12 | CT#86 | CP-193116 | 1722 | 2 | F | Handling of parameters stored in the ME memory | 16.3.0 |
| 2019-12 | CT#86 | CP-193104 | 1723 | 2 | F | Network slice authentication and emergency procedure | 16.3.0 |
| 2019-12 | CT#86 | CP-193115 | 1728 |  | F | Excluding 5GSM causes for congestion control from SINE | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1730 | 1 | F | ngKSI for CONTROL PLANE SERVICE REQUEST message | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1731 |  | F | Inclusion of PDU session reactivation result error cause IE | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1732 | 1 | F | IMEI and IMEISV formats support | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1733 | 1 | F | PEI format for non-3GPP access only UE | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1737 | 1 | F | Correction to the coding of EPS bearer identity | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1740 | 1 | F | UE handling upon receipt of 5GSM #46 out of LADN service area | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1742 | 1 | C | CIoT user data container in UL NAS transport message not routable | 16.3.0 |
| 2019-12 | CT#86 | CP-193089 | 1744 | 1 | C | Service gap control, supporting UE sends MO user data when connected when timer running | 16.3.0 |
| 2019-12 | CT#86 | CP-193088 | 1749 | 2 | F | Correction on the condition for including CP only indication | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1752 |  | F | T3540 in Service Accept Case | 16.3.0 |
| 2019-12 | CT#86 | CP-193106 | 1753 | 1 | C | Access control for UE triggered V2X policy provisioning procedure | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1754 | 2 | F | Abnormal cases for 5GMM cause values #74 and #75 | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1755 | 1 | C | Rejected NSSAI in SNPNs | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1756 | 2 | C | Introduction of SNPN-specific attempt counter for non-3GPP access and counter for "the entry for the current SNPN considered invalid for non-3GPP access" events | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1758 | 1 | F | Maintenance of forbidden TA lists for non-integrity protected NAS reject in an SNPN | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1759 | 1 | F | Handling of UAC for an MO IMS registration related signalling | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1760 |  | D | Correction of the definition of Network slicing information | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1766 | 2 | F | Moving Annex E to TS 24.5xy | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1767 | 1 | F | Follow on request codepoint value | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1770 | 1 | F | No CAG access control for emergency services | 16.3.0 |
| 2019-12 | CT#86 | CP-193119 | 1772 | 2 | F | Coding of the CAG-ID | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1773 | 1 | D | Timer order in timer tables | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1774 | 1 | F | Mobility registration accept with NSSAIs | 16.3.0 |
| 2019-12 | CT#86 | CP-193097 | 1775 | 2 | F | Correction to PLMN change with 5G-EA0 | 16.3.0 |
| 2019-12 | CT#86 | CP-193101 | 1778 | 1 | D | Editorial on PDU session establisment request upgraded to MA PDU session | 16.3.0 |
| 2020-03 | CT#87e | CP-200117 | 1533 | 6 | C | NW slice specific authentication and authorization failure and revocation | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1567 | 2 | B | CAG information towards the lower layers for paging | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1641 | 5 | B | PDU session handling for N5CW device | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1672 | 4 | C | Handling of user-plane resources for NB-IoT UEs having at least two PDU sessions | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1689 | 2 | C | Secondary authentication and W-AGF acting on behalf of FN-RG | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1781 | 3 | F | Correcting unimplementable condition regarding N26 interworking support detection | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1784 | 2 | F | Maintain Selected EPS NAS security algorithms during N1 mode to N1 mode handover | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1785 |  | F | Correction for AUTHENTICATION REJECT handling | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1786 | 1 | D | Editorial correction of an input parameter for 5G NAS message integrity protection | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1789 | 1 | F | Correction to sending of EPS NAS message container in Registration Request message | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1793 |  | D | Correct"ANSDP" | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1794 | 2 | F | Handling of unsupported SSC mode | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1797 | 1 | F | Abnormal case for service request procedure | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1798 | 2 | F | Mapped EPS bearer contexts deletion | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1799 | 1 | F | Service Request for PS Data Off | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1800 | 1 | F | Abnormal case for UL NAS TRANSPORT | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1804 |  | F | Declare syntactical error when both MFBR uplink and MFBR downlink equal zero | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1805 | 1 | D | Editorial correction to T3447 timer behavior | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1807 | 1 | F | Handling multiple QoS errors during a PDU session establishment procedure | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1810 | 1 | F | Inclusion of PDU session reactivation result error cause IE | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1811 |  | F | Correction on NAS transparent container for 5G-4G interworking | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1812 | 2 | F | Deletion of the rejected NSSAI for the current registration area | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1813 |  | F | Trigger for stopping timer T3511 | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1814 |  | F | Correction on T3502 for deactivated value | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1815 | 1 | F | 5GMM cause #22 for resetting registration attempt counter | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1816 |  | F | Consistent use of additional 5G security information IE | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1817 |  | F | Correction on N26 interface indicator | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1818 |  | F | Correction on reference of TS 36.304 | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1819 | 1 | F | Inclusion of 5GSM cause in PDU session modification request | 16.4.0 |
| 2020-03 | CT#87e | CP-200111 | 1820 |  | F | Inclusion of 5GSM cause in PDU session release request | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1821 |  | F | PDU session establishment reject with 5GSM #29 | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1822 | 1 | F | Correction on QoS rule/QoS flow synchronization | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1824 | 1 | F | Correction on NAS COUNT handling for intra-N1 handover | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1825 | 1 | F | Correction on Uplink data status IE coding | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1826 |  | F | Acknowledgement of UCU procedure | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1827 | 1 | F | Update bullet index to include all NAS transport cases | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1828 | 1 | D | Editorial correction on payload container | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1829 | 2 | F | Corrections on UE-initiated NAS transport procedure initiation | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1834 | 2 | D | Corrections in specifying reasons for errors | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1835 | 1 | F | UE handling of invalid QoS flow description | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1836 | 2 | F | S-NSSAI as a mandatory parameter to support interworking with 5GS | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1837 | 1 | F | Optional IE description for release assistance indication IE | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1838 | 1 | F | UE handling of multiple QoS errors in EPS | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1839 | 1 | F | S-NSSAI value associated with the BO timer applied for all PLMNs | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1840 | 1 | F | Abnormal case handling for 5GMM cause value #90 along with a PDU SESSION MODIFICATION REQUEST message | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1842 |  | F | Correction in handling of persistent PDU session during the mobility registration update | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1843 |  | D | NAS signalling spelling correction | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1845 | 2 | F | Reject non-emergency PDU session request attempt while UE registered for emergency services in the network | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1846 |  | F | Correction to IEI values | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1847 | 1 | F | Correction to 5GMM cause IE | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1848 |  | F | Correction to UCU procedure abnormal cases on NW side for a new TAI list | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1853 | 3 | F | Service area restrictions, case missing for when UE is out of allowed tracking area list and RA | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1854 |  | F | Correction to the Mapped NSSAI IE | 16.4.0 |
| 2020-03 | CT#87e | CP-200112 | 1858 |  | D | Correcting reference to 5GSM procedures | 16.4.0 |
| 2020-03 | CT#87e | CP-200114 | 1860 | 2 | F | 5GSM capabilities for MA PDU session | 16.4.0 |
| 2020-03 | CT#87e | CP-200114 | 1862 | 4 | B | MA PDU session is not supported | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1869 | 2 | F | Cleanups on introduction of pending NSSAI | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1870 |  | F | SUCI used by W-AGF acting on behalf of FN-RG | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1871 |  | F | Resolving editor's note on W-AGF acting on behalf of FN-RG not using the "null integrity protection algorithm" 5G-IA0 | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1872 |  | F | Resolving editor's note on service area restrictions in case of FN-BRG | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1873 |  | F | Resolving editor's note in forbidden wireline access area | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1874 |  | F | Wireline 5G access network and wireline 5G access clean up | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1875 | 1 | F | PEI clean up | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1876 |  | F | Alignment for stop of enforcement of mobility restrictions in 5G-RG and W-AGF acting on behalf of FN-CRG | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1877 | 1 | F | Introduction of GCI and GLI | 16.4.0 |
| 2020-03 | CT#87e | CP-200109 | 1878 | 1 | F | Always-On PDU session and URLLC | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1879 | 1 | F | CAG information list storage | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1881 | 2 | F | Abnormal case for cause #31 | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1882 |  | F | Removal of Editor's note on the use of the NOTIFICATION message in SNPNs | 16.4.0 |
| 2020-03 | CT#87e | CP-200135 | 1884 | 3 | B | Including CAG information list in REGISTRATION ACCEPT message | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1885 |  | F | Update of text on time synchronization | 16.4.0 |
| 2020-03 | CT#87e | CP-200125 | 1886 |  | F | Removal of Editor's note on applicability of RACS to SNPNs | 16.4.0 |
| 2020-03 | CT#87e | CP-200125 | 1887 |  | C | Finalizing the encoding of the UE radio capability ID | 16.4.0 |
| 2020-03 | CT#87e | CP-200125 | 1888 | 1 | B | UE radio capability ID deletion upon Version ID change | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1889 | 2 | B | Handling of S-NSSAIs in the pending NSSAI | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1891 |  | F | Resolve Editor´s Notes on NB-N1 mode extended NAS timers for CE | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1892 |  | F | Resolve Editor´s Notes on WB-N1 mode extended NAS timers for CE | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1893 | 1 | F | Clarification on HPLMN S-NSSAI | 16.4.0 |
| 2020-03 | CT#87e | CP-200114 | 1896 | 1 | F | MA PDU session and one set of QoS parameters | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1899 | 1 | F | Update to registration procedure due to eNS | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1900 | 1 | F | Stop T3565 upon connection resumption | 16.4.0 |
| 2020-03 | CT#87e | CP-200125 | 1902 | 1 | F | RACS not apply for non-3GPP access | 16.4.0 |
| 2020-03 | CT#87e | CP-200114 | 1903 |  | F | Minor Correction to ATSSS container IE desciption | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1907 | 3 | B | Support for the signalling of the capability for receiving WUS assistance information | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1910 | 3 | F | Enabling mobility with (emergency) sessions/connections between the (trusted) non-3GPP access network connected to the 5GCN and the E-UTRANt | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1913 | 1 | F | UE behaviour for other causes in the rejected NSSAI during deregistration procedure | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1914 | 1 | F | Pending NSSAI update for the configured NSSAI in the CUC message | 16.4.0 |
| 2020-03 | CT#87e | CP-200139 | 1915 | 2 | F | Cleanup for NSSAA message and coding | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1916 | 1 | F | Rejected NSSAI during the initial registration procedure | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1917 | 1 | F | UE behaviour when T3447 running | 16.4.0 |
| 2020-03 | CT#87e | CP-200108 | 1918 | 1 | C | PDU session release | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 1919 |  | B | ACS information via DHCP | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1921 | 1 | D | Name of the rejected NSSAI cause values | 16.4.0 |
| 2020-03 | CT#87e | CP-200125 | 1922 |  | F | Clarification of the cause of start of T3550 | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1923 | 1 | F | Clarification of forbidden TAI lists for SNPN | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1924 |  | F | Deletion of all CAG-IDs of a CAG cell 5GMM cause for #76 | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1926 |  | F | Clarification of the rejected NSSAI cause value | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1927 |  | F | Removal of term CAG access control | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1928 |  | F | Definition alignment for UE-DS-TT residence time | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1930 |  | F | Ciphering and deciphering handling of CPSR message | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1932 | 1 | C | Truncated 5G-S-TMSI over NAS | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1933 |  | F | AMF behavior on stop T3448 | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1934 | 1 | F | Correction on SMS in payload container IE in CPSR message | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1935 | 1 | F | Correction on 5GMM cause #74/#75 for no touching non-3GPP access | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1937 |  | F | Correction on term "non-3GPP access" used in SNPN | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1938 |  | F | Reset the registration attempt counter for #76 in service reject | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1941 | 1 | F | ENs resolution for revoked or failed NSSAA | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1942 |  | D | Consistent name for NSSAA | 16.4.0 |
| 2020-03 | CT#87e | CP-200127 | 1943 |  | F | No retry in 4G for PDU session type related 5GSM causes | 16.4.0 |
| 2020-03 | CT#87e | CP-200127 | 1944 |  | F | Correction on UE retry restriction on EPLMN | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1945 | 1 | F | Clarification on Public Network Integrated NPN in TS 24.501 | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1946 | 1 | F | UE receives CAG information in SNPN access mode | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1947 | 2 | F | Establish PDU session to transfer port management information containers | 16.4.0 |
| 2020-03 | CT#87e | CP-200114 | 1948 | 2 | F | ATSSS Non-MPTCP traffic support | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1949 | 1 | F | Correction for the wrongly implemented CR1693r1 | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1953 |  | F | NSSAA revocation function | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1956 | 1 | F | Stopping of T3513 after connection resume for user plane CIoT 5GS optimization | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1958 |  | F | Correction UE behaviour when the UE recives the pending NSSAI | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1961 | 1 | F | Adding an editor's note for suspend indication due to user plane CIoT 5GS optimization | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1966 | 1 | C | Recovery from fallback for UEs using CP CIoT optimization | 16.4.0 |
| 2020-03 | CT#87e | CP-200119 | 1968 |  | B | Triggering service request procedure for V2X communication over PC5 interface | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1971 | 1 | C | Removal of the use of Service area list IE during NSSAAt | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1973 |  | F | Additional triggers for deletion of pending S-NSSAI | 16.4.0 |
| 2020-03 | CT#87e | CP-200114 | 1976 | 1 | B | Considering allowed NSSAI when establishing MA PDU session | 16.4.0 |
| 2020-03 | CT#87e | CP-200114 | 1977 | 1 | B | UE Handling upon receipt of PDU session release command | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1978 | 1 | F | Correction to UL CIoT user data container not routable or not allowed to be routed | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1979 | 1 | F | Single downlink data only indication and release of N1 NAS signalling connection | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1980 | 2 | F | PDU session status with control plane service request message | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1981 | 1 | F | Service gap control, correction when to start service gap control timer in UE and NW | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1982 | 1 | F | Clarification of control plane service request message options | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1983 | 1 | C | UAC updates for NB-IoT to include "MO exception data" | 16.4.0 |
| 2020-03 | CT#87e | CP-200107 | 1984 | 1 | B | Clarification on the use of exception data reporting | 16.4.0 |
| 2020-03 | CT#87e | CP-200286 | 1985 | 5 | F | Update SNPN key differences | 16.4.0 |
| 2020-03 | CT#87e | CP-200109 | 1987 | 1 | F | Setting the Always-on PDU session indication IE in the PDU SESSION ESTABLISHMENT ACCEPT message | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1991 |  | F | AMF updates the UE NSSAI storage after network slice-specific authentication and authorization is completed | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1995 |  | F | Clarification on the S-NSSAI not subject to NSSAA included in allowed NSSAI | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1996 | 2 | F | Subscribed S-NSSAI marked as default and NSSAA | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 1997 |  | F | Additional conditions to the presence in the subscribed S-NSSAIs | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 1998 | 1 | F | Triggering mobility registration update due to manual CAG selection | 16.4.0 |
| 2020-03 | CT#87e | CP-200117 | 2000 | 1 | F | Emergency PDU session handling after NSSAA failure | 16.4.0 |
| 2020-03 | CT#87e | CP-200125 | 2002 |  | F | UE behaviour upon receipt of a UE radio capability ID deletion indication | 16.4.0 |
| 2020-03 | CT#87e | CP-200125 | 2005 | 1 | F | Additional condition to change UE radio capability ID during mobility registration update | 16.4.0 |
| 2020-03 | CT#87e | CP-200125 | 2006 | 1 | F | UE radio capability information storage not needed for RACS | 16.4.0 |
| 2020-03 | CT#87e | CP-200097 | 2008 | 3 | F | Handling of a UE with an emergency PDU session in terms of CAG | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 2012 | 2 | F | N1 mode capability disabling and re-enabling for SNPN | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 2013 | 1 | F | #31 not applicable in an SNPN | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 2015 | 1 | F | Validity of the USIM for an SNPN and for a specific access type | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 2016 |  | F | Handling of 5GMM cause values #62 in an SNPN | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 2017 | 1 | F | No mandate to support default configured NSSAI or network slicing indication | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 2018 | 2 | F | SNN coding | 16.4.0 |
| 2020-03 | CT#87e | CP-200130 | 2019 | 1 | F | 5GMM cause value #74 in an SNPN with a globally-unique SNPN identity | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 2020 | 1 | B | Registration of N5GC devices via wireline access | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 2021 | 1 | F | Correction on EUI-64 as PEI | 16.4.0 |
| 2020-03 | CT#87e | CP-200113 | 2022 |  | F | Corrections on N5CW support | 16.4.0 |
| 2020-03 | CT#87e |  |  |  |  | Addition of IEI values, editorial corrections, implementation of missing CR1985 | 16.4.1 |
| 2020-06 | CT#88e | CP-201102 | 0793 | 9 | F | Inclusion of ATTACH REQUEST message in REGISTRATION REQUEST message during initial registration when 5G-GUTI mapped from 4G-GUTI is used | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 1379 | 6 | F | Corrections on the abnormal cases of registration procedure for initial registration | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 1415 | 12 | F | Handling of MCS data in various 5GMM states. | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 1701 | 5 | C | Enhancement on CPSR for CIoT CP data transport | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 1734 | 2 | F | S-NSSAI in rejected NSSAI for the failed or revoked NSSAA not to be requested | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 1782 | 5 | F | Correcting transfer of connections/sessions if there is an emergency call | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 1792 | 2 | F | Restricting handling of cause #9 to the access on which it was received | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 1795 | 3 | F | Clarification on use of operator-defined access categories | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 1803 | 3 | F | Add handling for UE configured to use timer T3245 in 5GS via 3GPP access | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 1823 | 4 | F | Correction on UE behaviour for service area restriction | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 1841 | 4 | F | Paging with two valid 5G-GUTIs | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 1880 | 2 | C | CAG-ID not provided to lower layers during NAS signalling connection establishment | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 1912 | 5 | C | Deleting Editors note regarding indefinite wait at the UE for NSSAA completion | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 1974 | 1 | F | Dual-registration requirements for EHPLMNs | 16.5.0 |
| 2020-06 | CT#88e |  |  |  |  |  | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2010 | 2 | C | Correction in UE behavior upon receipt of 5GMM cause value #74 or #75 via a non-integrity protected NAS message | 16.5.0 |
| 2020-06 | CT#88e | CP-201109 | 2027 |  | B | EPS interworking of MA PDU session of 5G-RG when N26 is not supported | 16.5.0 |
| 2020-06 | CT#88e | CP-201108 | 2028 | 1 | F | Secondary authentication and W-AGF acting on behalf of N5GC device | 16.5.0 |
| 2020-06 | CT#88e | CP-201109 | 2029 | 2 | B | EPS interworking of MA PDU session of 5G-RG when N26 is supported | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2030 | 2 | F | Indication of change in the use of enhanced coverage | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2031 |  | F | Integrity protection data rate for UEs that don't support N3 data transfer | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2032 |  | F | Addition of Control Plane Service Request in the abnormal cases for service request procedure | 16.5.0 |
| 2020-06 | CT#88e | CP-201132 | 2033 |  | F | Correction of certain erroneous Information Element Identifiers | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2034 | 5 | F | DRX parameters for NB-IoT | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2035 |  | F | Correcting a wrong reference | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2037 |  | F | Clarification on DL only match-all packet filer | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2038 | 1 | F | Clarification S-NSSAI status in AMF for NSSAA | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2039 | 2 | F | Update description on UE indicate supporting NSSAA | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2040 | 1 | F | Pending NSSAI update for the configured NSSAI in the UCU message | 16.5.0 |
| 2020-06 | CT#88e | CP-201109 | 2042 | 1 | F | Applicability of PS data off to MA PDU session | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2043 | 1 | F | Missing condition for inclusion of"NSSAA to be performed"indicator | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2044 | 1 | F | AMF triggers PDU session release | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2047 |  | F | Correction of the handling of 5GMM cause #27 | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2049 |  | F | Stopping of T3346 after receiving the NSSA Command message | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2050 | 2 | F | Additional condition to start T3540 | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2051 | 1 | F | Specify UE behaviour for NOTIFICATION message for additional state/sub-states | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2053 | 1 | F | Clarification on the rejected S-NSSAI included in requested NSSAI inregistration procedure. | 16.5.0 |
| 2020-06 | CT#88e | CP-201108 | 2055 |  | F | ANDSP is not supported by 5G-RG and W-AGF | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2056 | 3 | C | Addinganew abnormal case on the network side for CPSR | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2058 | 3 | F | Clarifying the description for Network Slice-Specific Authorization Revocation | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2059 | 3 | C | Updating requirements of NSSAA for roaming scenarios | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2060 | 1 | F | Definition of registered SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2062 |  | F | Correction of SGC | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2063 | 1 | F | Emergency PDU sesseion established after WUS negotiation | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2064 |  | F | update of the counter for SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2065 |  | F | temporarily and permanently forbidden SNPNs lists per access type | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2066 | 3 | F | storage of counters for UE in SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2067 | 1 | F | 5G GUTI of SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2068 |  | F | 5GMM cause value #74 in an SNPN with a globally-unique SNPN identity | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2069 | 2 | F | 5GMM cause value #13 not supporting roaming for SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2070 |  | F | Clarification of the cause of start of T3550 | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2071 | 2 | F | storage of counters for UE in PLMN | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2072 |  | F | Clarification of the figure of registration procedure | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2074 | 1 | D | Editorial corrections | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2075 |  | F | T3540 is not started if the Registration Accept includes a pending NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2077 | 1 | C | Generic UE configuration update trigger for registration and EC Restriction change | 16.5.0 |
| 2020-06 | CT#88e | CP-201127 | 2078 | 1 | F | RACS parameters in generic UE configuration procedure | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2079 | 1 | F | Clarify that NSSAA can occur during periodic registration or mobility updating for NB-N1 mode UEs | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2080 |  | F | Fixing typo related to eNS | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2084 | 1 | F | Alignment of UE actions of rejected NSSAI for the failed or revoked NSSAA | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2087 | 1 | C | Addition of CAG information list in registration reject message. | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2089 | 1 | F | Exception to initiate the service request procedure during NSSAA when there is no allowed NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2091 | 1 | F | Missing condition at registration reject due to no available slices | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2093 | 1 | F | Add handling for parameter set to"value is not used"in 5GS | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2094 | 1 | F | Correct UE behavior for receiving 5GMM cause #31 in 5GS | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2095 |  | F | Correct parameters included by AMF during inter-system change from S1 mode to N1 mode in 5GMM-CONNECTED mode | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2096 |  | F | Remove invalid cases in error handling for QoS rule operation and TFT operation | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2098 | 2 | F | Applicable URSP is not optional for a UE | 16.5.0 |
| 2020-06 | CT#88e | CP-201144 | 2100 | 2 | F | Inclusion of NSSAI in AN Parameters for non-3GPP access | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2101 | 1 | F | Additional QoS error handling related to mapped EBI | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2102 | 1 | F | PS Data Off status report for non-3GPP access | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2103 | 1 | D | Unify terms network-initiated and network-requested | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2104 | 1 | F | Network triggered service request procedure over non-3GPP access | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2106 | 3 | F | Avoid repeated redirection for CIoT | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2107 | 2 | F | PDU session release due to CP only revocation | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2108 | 3 | C | Updating Rejected NSSAI IE for failed NSSAA case in roaming scenerios | 16.5.0 |
| 2020-06 | CT#88e | CP-201102 | 2110 |  | F | Consider PDU session type IE set by UE in IP address allocation | 16.5.0 |
| 2020-06 | CT#88e | CP-201116 | 2111 | 1 | F | T3540 for service request for V2X communications | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2112 | 1 | F | Clarification on the UE behaviour when receiving T3448 | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2113 | 2 | F | Connection Resumption for Notification | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2114 | 1 | F | CIoT user or small data container in CPSR message not forwarded | 16.5.0 |
| 2020-06 | CT#88e | CP-201099 | 2115 | 2 | F | Initial Registration after 5G-SRVCC | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2118 |  | F | Fixing a reference in the service request procedure | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2120 | 1 | F | Add MFBR as mandatory parameter in GBR QoS flow | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2121 | 2 | F | Initial registration for initiating emergency PDU session | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2122 | 3 | F | Missing QoS flow description parameters for GBR QoS flows in 5GSM and ESM coordination | 16.5.0 |
| 2020-06 | CT#88e | CP-201196 | 2128 | 4 | F | Sending CAG information list | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2130 | 1 | F | Correction on terminology for the Control plane CIoT 5GS optimization | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2132 | 1 | F | Handling of PDU session and PDN connection associated with Control plane only indication in case of N26 based interworking procedures | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2134 | 1 | F | Non-integrity protected REGISTRATION REJECT message including 5GMM cause #76 | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2135 | 2 | F | NSSAA in an SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201139 | 2140 | 3 | F | Correction in the UE behaviour upon failure of the procedures initiated for ESFB | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2141 |  | F | No emergency session transfer after ESFB | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2142 | 2 | F | Indication that the emergency services fallback attempt failed | 16.5.0 |
| 2020-06 | CT#88e | CP-201113 | 2144 | 1 | F | Handling of Pending S-NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2145 | 1 | F | QoS error checks for UEs in NB-N1 mode | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2149 | 2 | F | NB-IoT not applicable for SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2150 | 1 | F | Retransmission of a CPSR message after integrity check failure at the AMF | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2152 | 1 | F | Miscellaneous clean-up for SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2153 | 2 | F | Service area restrictions in an SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2154 | 1 | D | Corrections on MICO | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2156 | 3 | F | 5GSM back-off mechanisms in an SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2157 | 1 | F | UE in the 5GMM-REGISTERED.ATTEMPTING-REGISTRATION-UPDATE substate operating in SNPN access mode | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2158 | 2 | F | Routing indicator update in an SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2159 | 1 | F | 3GPP PS data off in an SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2161 | 1 | F | Correction to conditions for including the S-NSSAI(s) from default NSSAI in the requested NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2162 |  | F | Corrections to CR#1907 | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2164 | 1 | B | Signalling of EPS APN rate control parameters during PDU session establishment | 16.5.0 |
| 2020-06 | CT#88e | CP-201283 | 2165 | 3 | B | Ethernet header compression for CP CIoT – 5GMM aspects | 16.5.0 |
| 2020-06 | CT#88e | CP-201109 | 2169 | 1 | F | Editorial fix in 9.11.4 | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2173 |  | F | Acknowledgement of truncated 5G-S-TMSI configuration | 16.5.0 |
| 2020-06 | CT#88e | CP-201096 | 2174 |  | F | NAS-MAC calculation for RRC connection reestablishment for NB-IoT CP optimisation | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2175 |  | F | Removal of Editor's Note for CP congestion control | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2176 | 1 | F | Correction on WUS assistance | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2177 | 1 | F | Non-3GPP access for PLMN and SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2178 |  | F | No CAG in non-3GPP access | 16.5.0 |
| 2020-06 | CT#88e | CP-201136 | 2179 |  | F | Correction on 5GMM #27 for CAG | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2180 | 2 | F | Clarification on handling of pending NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2181 |  | F | Term on rejected NSSAI for the failed or revoked NSSAA | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2182 | 1 | F | Single-registration mode without N26 | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2183 | 1 | F | Handling of unallowed SSC mode | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2184 | 1 | F | UAC exception for emergency | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2185 | 3 | F | MRU after SR for ESFB aborted | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2187 | 1 | F | Correction to criteria to enter 5GMM-REGISTERED.UPDATE-NEEDED substate after resumption failure | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2192 |  | F | Correcting that 5G NAS integrity key is one of the input parameters for integrity protection algorithm | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2193 | 2 | F | Correction to Handling of T3521 timer | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2194 |  | F | Correction to Handling of #31 | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2195 | 1 | F | Correction to handling of T3447 timer | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2196 |  | D | Correct "theregistration" | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2197 |  | F | De-registration before initial registration for Emergency Services | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2198 | 2 | F | Handling of allowed NSSAI when the RA includes the TAI belonging to EPLMN | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2200 |  | F | Corrections on NSSAI storage | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2202 | 1 | F | UE behaviour when the UE receives the rejected NSSAI for the current RA and does not have a valid RA | 16.5.0 |
| 2020-06 | CT#88e | CP-201109 | 2203 | 1 | B | Handlings of MA PDU session when deregistration from an access | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2204 |  | F | Indicate support of ePCO length of two octets parameter when establishing the PDU session – Alt#2 | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2205 | 2 | F | Addition of 5GSM cause #59 | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2214 | 1 | F | Handling of mapped EPS bearer contexts | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2215 | 1 | F | Integrity check interworking in 5GMM-CONNECTED mode | 16.5.0 |
| 2020-06 | CT#88e | CP-201103 | 2216 | 1 | F | Correction on LADN DNN based congestion control | 16.5.0 |
| 2020-06 | CT#88e | CP-201108 | 2218 | 1 | B | Primary authentication of an N5GC device | 16.5.0 |
| 2020-06 | CT#88e | CP-201108 | 2219 |  | F | Stop of enforcement of wireline access service area restrictions and forbidden wireline access area | 16.5.0 |
| 2020-06 | CT#88e |  |  |  |  |  | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2221 |  | F | Incorrect set up of PDN type in inter-system change from S1 mode to N1 mode | 16.5.0 |
| 2020-06 | CT#88e | CP-201109 | 2222 |  | F | Session-AMBR and MA PDU session | 16.5.0 |
| 2020-06 | CT#88e | CP-201109 | 2223 | 1 | F | Introduction of ATSSS | 16.5.0 |
| 2020-06 | CT#88e | CP-201109 | 2224 |  | F | "MA PDU request" when the UE has an MA PDU session established over one access and requests establishment of user plane resources over the other access | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2227 | 1 | F | Mobile Terminated Voice Gap for MPS | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2228 | 1 | F | Adding AAA-S via NSSAAF to support NSSAA | 16.5.0 |
| 2020-06 | CT#88e | CP-201311 | 2229 | 2 | F | Resolve EN for Ciphering Key data IE regarding positioning SIBs | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2230 | 1 | F | MICO indication needs to be included without Network Slicing Subscription Change Indication in UCU. | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2231 | 2 | F | Conditions for use of S-NSSAIs after receiving Rejected NSSAI Conditions for use of S-NSSAIs after receiving Rejected NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2232 | 2 | F | Default S-NSSAI not subject to network slice-specific authentication and authorization | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2233 | 3 | F | Performing network slice-specific re-authentication and re-authorisation | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2234 | 2 | F | Storage of pending NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2235 | 1 | F | UE stopping back-off timer when receiving PDU SESSION AUTHENTICATION COMMAND | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2236 | 4 | F | Pending NSSAI and equivalent PLMNs | 16.5.0 |
| 2020-06 | CT#88e | CP-201132 | 2237 |  | F | Correcting the incorrect mode of the UE | 16.5.0 |
| 2020-06 | CT#88e | CP-201127 | 2241 | 1 | F | Avoiding too frequent registration procedures due to signalling of UE radio capability ID | 16.5.0 |
| 2020-06 | CT#88e | CP-201119 | 2242 | 1 | F | Unified access control is not applicable to a UE operating as IAB-node | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2247 | 1 | F | Revert CR 0820t | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2249 | 1 | F | Change of E-UTRAN UE Capability | 16.5.0 |
| 2020-06 | CT#88e | CP-201106 | 2250 |  | F | Store the received S-NSSAI via ePDG in the configured NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2254 |  | F | Re-initiation of NSSAA – Reactive solution | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2255 | 1 | F | Clarification of the forbidden PLMN list used for non-3GPP access | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2256 |  | F | Re-enabling the N1 mode capability upon request from the upper layers | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2257 |  | F | Correction of re-enabling E-UTRA capability | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2258 | 1 | F | Native 5G-GUTI in Additional GUTI IE | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2259 | 1 | F | Correction of IEI | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2260 |  | F | Maintenance of T3517 | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2261 |  | F | Operation of UE in SNPN access mode when timer T3247 expires | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2262 |  | F | Reference correction for SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2264 | 1 | D | Stop T3346 before sending NAS message | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2265 | 1 | F | Condition under which the UE shall enter 5GMM-IDLE mode when user plane CIoT 5GS optimization is used | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2267 | 1 | F | Correction to handling of 5GSM timers in abnormal cases | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2269 | 1 | F | Clarification for de-registration procedure initiation | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2270 |  | F | Clarification in state transition of 5GMM-DEREGISTERED from another 5GMM state | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2271 |  | F | Clarification of SMS over NAS supported bit in initial registration | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2272 |  | F | Clarification on missing subclause in 5GMM-DEREGISTERED.ATTEMPTING-REGISTRATION | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2273 |  | F | Clarification on missing subclause in 5GMM-REGISTERED.ATTEMPTING-REGISTRATION-UPDATE | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2274 |  | F | Clarification regarding update status in NR RAT | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2275 | 1 | F | Correction to paging timer stop in case of integrity check failure | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2277 | 1 | D | Correction to spelling mistakes | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2278 | 2 | F | UE shall use the GUTI assigned by thesame SNPN during registration | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2279 |  | F | Correct PLMN to SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2281 | 1 | F | Clarification on S-NSSAI deletion based on the rejected NSSAI due to NSSAA in the roaming case | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2282 | 1 | F | Correction on allowed NSSAI for UE not supporting NSSAA | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2283 |  | B | Indicate 5GSM cause when initiating 5GSM procedure for error handling | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2284 | 1 | F | PDU session release upon receipt of PDU session status IE | 16.5.0 |
| 2020-06 | CT#88e | CP-201130 | 2286 | 1 | F | Correction to the handling for 5GSM #27 | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2287 |  | F | Stop back-off timer upon receipt of 5GSM #39 | 16.5.0 |
| 2020-06 | CT#88e | CP-201104 | 2289 |  | D | Removal of duplicate words | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2290 | 1 | F | Correction to 5GMM-REGISTERED.NORMAL-SERVICE | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2292 |  | F | Correction to handling of #3/#6/#7 | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2294 | 1 | F | Correction to 5GMM-DEREGISTERED.NORMAL-SERVICE | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2296 |  | F | Correction to subclause in Requested NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2297 |  | F | Clarification in usage of SIM terminology in 5GS services | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2299 | 2 | F | Support for continuity of emergency session upon registration failure | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2303 |  | F | Updating Port management information container IE | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2304 |  | F | De-registration request and CPSR collision case in the NW | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2305 |  | F | Additional stop condition for timer T3580 | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2306 | 1 | F | Abonormal cases on UE side and the CPSR message | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2307 | 1 | F | Service gap control: Alignment of NW and UE behaviour for timer T3447 | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2308 | 1 | F | Service gap control: Exceptions to start of timer T3447 | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2309 | 1 | F | UE behaviour when more than 16 S-NSSAIs received in pending NSSAI IE | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2313 | 1 | F | Handling of CAG information list in REGISTRATION ACCEPT messages | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2314 |  | F | Provision of CAG information list in SERVICE REJECT message. | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2315 | 1 | F | Size of pending NSSAI in REGISTRATION ACCEPT message | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2316 |  | F | Corrections for Enhanced Coverage in 5GS for CIoT | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2317 |  | F | Not including NSSAI for emergency session for interworking without N26 interface | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2318 |  | F | AMF not using 5GMM registration status in UE status IE | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2319 | 1 | F | CPBO timer handling when AMF is congested for CP data. | 16.5.0 |
| 2020-06 | CT#88e | CP-201108 | 2321 |  | D | Removal of TMBR | 16.5.0 |
| 2020-06 | CT#88e | CP-201284 | 2323 | 2 | B | Ethernet header compression for CP CIoT – 5GSM aspects | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2326 | 1 | C | Associating S-NSSAI-based congestion backoff timers with S-NSSAI when S-NSSAI is provided during PDU session establishment | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2327 | 2 | C | Updates to non-allowed area restrictions | 16.5.0 |
| 2020-06 | CT#88e | CP-201127 | 2328 | 1 | F | Correction of RACS ID deletion via UCU | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2330 | 1 | F | Correction related the pending NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2332 | 1 | F | Clarification on handling of rejected NSSAI for the current registration area | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2333 | 1 | F | Clarification on S-NSSAI(s) in URSP(NSSP) be added into the request NSSAI | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2336 | 1 | F | Multiple DRB support for UEs in NB-N1 mode | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2337 | 1 | F | Establishment of UP resources for NB-IoT based on number of supported DRBs | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2339 | 1 | F | A default S-NSSAI not subject to NSSAA | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2340 | 1 | F | Clarification on the non-supported functions and procedures for SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2341 |  | D | Correction on unclear texts regarding the CONFIGURATION UPDATE COMMAND message | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2342 | 1 | F | IP header compression after inter-system change from S1 mode to N1 mode | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2344 | 1 | F | Trigger SR over non-3GPP access after T3346 expiry. | 16.5.0 |
| 2020-06 | CT#88e | CP-201322 | 2345 | 2 | B | Provisioning of DNS server security information to the UE | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2346 | 1 | F | Adding a missing case on the UE side for CPSR | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2347 |  | F | Condition for setting the Selected EPS NAS algorithm IE to NULL | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2348 | 2 | F | Connected mode mobility from N1 mode to S1 mode and DL NAS COUNT handling | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2350 | 1 | F | Correction in the AMF behaviour upon LADN information update | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2352 | 1 | F | Unify terminology for default S-NSSAIs and subscribed S-NSSAIs marked as default | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2356 |  | F | Correction to Service Reject with cause #28 | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2357 | 1 | F | UE behaviour when receiving allowed NSSAI in CUC | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2358 |  | F | Ciphering initial registration message with NULL algorithm | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2362 |  | F | Clean up description of Cause #34 in TS 24.501 | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2364 | 1 | F | Semantic error check for duplicate QRI or QFI | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2366 |  | D | Editorial change to SNPN | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2368 | 1 | F | No CAG ID in de-registration request | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2369 | 1 | F | No dedicated EPS bearer for interworking from WB-N1 to NB-S1 mode | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2371 | 1 | F | Management for SNPN access mode per access type | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2372 | 2 | F | Redirection of UE from N1 mode to S1 mode | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2375 | 1 | F | NAS message transmission failure indication with delayed TAI change | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2376 | 1 | F | PDU session transfer between 3GPP and non-3GPP when CP CIoT 5GS optimization is being used | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2377 | 1 | F | PDU session transfer between 3GPP and non-3GPP when UP CIoT 5GS optimization is being used | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2379 |  | F | Correction on CIoT small data container IE | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2380 |  | F | Maximum length of Unstructured data via the control plane | 16.5.0 |
| 2020-06 | CT#88e | CP-201097 | 2381 |  | F | Missing LCS/LPP container content in Payload container IE | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2382 |  | F | Handling of multiple QoS flow descriptions | 16.5.0 |
| 2020-06 | CT#88e | CP-201105 | 2384 | 1 | F | Clarification of NAS COUNT handling in 5G | 16.5.0 |
| 2020-06 | CT#88e | CP-201114 | 2386 | 1 | F | Providing complete pending NSSAI for NSSAA | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2388 | 1 | F | SNPN services via a PLMN over 3GPP access | 16.5.0 |
| 2020-06 | CT#88e | CP-201108 | 2390 | 1 | B | N5GC NAS aspects | 16.5.0 |
| 2020-06 | CT#88e | CP-201108 | 2391 | 1 | B | N5GC service area restrictions | 16.5.0 |
| 2020-06 | CT#88e | CP-201137 | 2394 | 2 | F | Prevention of loop for 5GMM cause #62 | 16.5.0 |
| 2020-06 | CT#88e | CP-201108 | 2398 |  | F | N5CW device registration and IP assignment | 16.5.0 |
| 2020-07 | CT#88e |  |  |  |  | Editorial corrections by rapporteur and MCC. Addition of IEI values | 16.5.1 |
| 2020-09 | CT#89e | CP-202171 | 1970 | 2 | F | Handling of LADN information when the UE is operating in SNPN access mode | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2086 | 5 | F | S-NSSAIs always selected by AMF from allowed NSSAI | 16.6.0 |
| 2020-09 | CT#89e | CP-202166 | 2092 | 5 | F | TA change during Authentication procedure in 5GMM-CONNECTED mode | 16.6.0 |
| 2020-09 | CT#89e | CP-202152 | 2220 | 2 | F | IPv6 configuration for W-AGF acting on behalf of FN-RG | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2244 | 4 | F | Disabling of N1 capabilities when all requested S-NSSAIs subjected to NSSAA are rejected due to failure of NSSAA or when no slice is available for UE | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2251 | 2 | F | Alternative 2: UE behaviour regarding N1 mode capability upon T3247 expiry | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2252 | 1 | B | Alternative 2: Handling of a UE not allowed to access SNPN services via a PLMN by subscription with 5GMM cause value #72 | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2397 | 4 | F | Transfer of PDN connection from untrusted non-3GPP access connected to EPC to 5GS | 16.6.0 |
| 2020-09 | CT#89e | CP-202146 | 2401 |  | F | Correction to PDU session ID inclusion in UL and DL NAS transport | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2403 | 1 | F | Clarification on the condition when the allowed NSSAI IE shall be included in the REGISTRATION ACCEPT message | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2405 | 1 | F | Consistency of the term on rejected NSSAI for the failed or revoked NSSAA | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2409 | 1 | F | Correction to clarify S-NSSAI(s) in allowed NSSAI doesn't require NSSAA | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2410 | 1 | F | Clarification on the"NSSAA to be performed"indicator | 16.6.0 |
| 2020-09 | CT#89e | CP-202166 | 2411 | 1 | F | Support of User Plane Integrity Protection for any data rates | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2418 | 1 | F | URSP evaluation after rejection with the same URSP rule | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2419 | 1 | F | Remove #43 in PDU session modification command not accepted by UE | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2420 | 1 | F | NSSAA Slice handling for 1-to-many mapping in roaming scenario | 16.6.0 |
| 2020-09 | CT#89e | CP-202153 | 2422 | 1 | F | Correcting partial implementation of CR#2029 | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2423 |  | F | Correcting partial implementation of CR#2221 | 16.6.0 |
| 2020-09 | CT#89e | CP-202153 | 2424 | 1 | F | "MA PDU request" when the 5G-RG performs inter-system change from S1 mode to N1 mode with an MA PDU session with a PDN connection as a user-plane resource | 16.6.0 |
| 2020-09 | CT#89e | CP-202152 | 2430 |  | F | W-CP connection | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2433 |  | F | SIM not applicable for 5GS cases | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2434 | 1 | F | NAS MAC terminology | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2436 | 1 | F | Congestion handling of initial registration for emergency | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2437 | 1 | F | Corrections to the QoS parameter checks for "unstructured" data and for QoS flow deletion | 16.6.0 |
| 2020-09 | CT#89e | CP-202168 | 2441 |  | F | Removal of Editor's note on inter PLMN mobility under same AMF | 16.6.0 |
| 2020-09 | CT#89e | CP-202159 | 2442 |  | F | Removal of Editor's note on UAC for IAB | 16.6.0 |
| 2020-09 | CT#89e | CP-202146 | 2443 |  | F | Avoiding double barring for CPSR following NAS connection recovery from fallback | 16.6.0 |
| 2020-09 | CT#89e | CP-202146 | 2445 |  | F | Correction to the 5GS network feature support IE | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2459 |  | F | Correction of counters in an SNPN | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2460 |  | F | Provisioning of a CAG information list in Service Request procedure | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2462 | 1 | F | NSSAA during PDU session modification procedure | 16.6.0 |
| 2020-09 | CT#89e | CP-202153 | 2464 | 1 | F | Clarification on the applicability of Allowed PDU session status IE to MA PDU | 16.6.0 |
| 2020-09 | CT#89e | CP-202153 | 2465 | 1 | F | Correction on unnecessary restriction for modifying/upgrading a PDU session to an MA PDU session | 16.6.0 |
| 2020-09 | CT#89e | CP-202153 | 2466 | 1 | F | Correction on PDU session status IE handling for MA PDU sessions | 16.6.0 |
| 2020-09 | CT#89e | CP-202153 | 2467 | 1 | F | local release of an MA PDU session having user plane resources established on both 3GPP access and non-3GPP access | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2468 | 1 | F | Clarification for SR attempt count reset | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2469 | 1 | F | Handling for SR in 5U2 state | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2470 | 1 | F | Clairification of Rejected NSSAI | 16.6.0 |
| 2020-09 | CT#89e | CP-202146 | 2473 |  | F | CP data allowed in connected mode in Non-allowed area | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2474 | 1 | F | Deleting Editors note regarding to network slice-specific re-authorization and re-authorization | 16.6.0 |
| 2020-09 | CT#89e | CP-202152 | 2476 |  | F | IPv6 prefix not allocated | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2480 |  | F | Minimum length of port management information container in SM messages | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2481 | 1 | F | Mapped dedicated EPS bearer without default EPS bearer | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2482 |  | F | Calculation of MAC in NAS transparent containers | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2483 | 1 | F | Provisioning of DNS server security information to the UE-25.401 | 16.6.0 |
| 2020-09 | CT#89e | CP-202168 | 2484 | 1 | F | Use existing NAS signalling connection to send mobility reg due to receipt of URC delete indication IE. | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2488 | 1 | F | Clarification of Rejected NSSAI associated with 5GMM cause #62 | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2491 |  | F | CAG information list in Registration reject message. | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2492 | 1 | F | CR#2299 clean up: continuity of emergency session upon registration failure | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2497 | 2 | F | Correction on UE behavior for the rejected NSSAI for the failed or revoked NSSAA and the pending NSSAI when the Allowed NSSAI is received | 16.6.0 |
| 2020-09 | CT#89e | CP-202146 | 2499 | 1 | F | Adding the handling of AMF for case k in the service request procedure | 16.6.0 |
| 2020-09 | CT#89e | CP-202146 | 2502 | 1 | F | UE behavior when the timer T3447 is stopped | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2503 |  | F | UE behavior on SNPN access mode when accessing to PLMN services via a SNPN | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2506 | 2 | F | Mobility Registration for Inter-RAT movement | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2507 | 1 | F | #76 cause handling in case of reception of Registration Reject in roaming scenarios | 16.6.0 |
| 2020-09 | CT#89e | CP-202150 | 2509 | 1 | F | Corrections on the error check of QoS rules | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2512 | 1 | F | Add definition of"allowed CAG list" | 16.6.0 |
| 2020-09 | CT#89e | CP-202032 | 2514 | 1 | F | Paging not initiated for PDU session transfer from non-3GPP access when CP CIoT 5GS optimization is being used | 16.6.0 |
| 2020-09 | CT#89e | CP-202146 | 2515 |  | F | UE specific DRX value for NB-IoT | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2521 | 1 | F | Rejection of PDU session establishment associated with an S-NSSAI for which NSSAA is re-initiated | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2525 | 1 | F | Removal of the"failed or revoked NSSAA"definition | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2526 |  | F | Finding a suitable cell in a PLMN where a UE is allowed to access a non-CAG cell | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2527 | 1 | F | 5GMM cause value #76 mapped to a different 5GMM cause value | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2528 | 1 | F | EAB not applicable for a UE operating in SNPN access mode | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2530 | 1 | F | T3245 for a UE operating in SNPN access mode | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2531 | 1 | F | Handling of back-off due to 5GSM cause value #27 "missing or unknown DNN" by a UE operating in SNPN access mode | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2534 | 1 | F | Handing of QoS errors in ESM procedures | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2535 |  | F | Delete unimplementable QoS operations in ESM procedure | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2536 |  | F | Packet filter identifier setting when requesting new packet filters | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2537 | 1 | F | Update of the timers table for 5GS session management | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2539 | 1 | F | Infinite De-registration attempt | 16.6.0 |
| 2020-09 | CT#89e | CP-202146 | 2540 | 1 | F | Define"emergency services"for Control plane service type in CPSR | 16.6.0 |
| 2020-09 | CT#89e | CP-202122 | 2552 | 4 | F | Type of the N5GC indication information element | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2555 |  | F | Clarification of conditions which the rejected NSSAI for the failed or revoked NSSAA is deleted | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2561 | 1 | F | T3525 clarification for UE configured with high priority access | 16.6.0 |
| 2020-09 | CT#89e | CP-202171 | 2562 | 1 | F | Clarification to the usage of last visited registered TAI in SNPN registration | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2564 | 1 | F | Minimum length of "Plain 5GS NAS message" | 16.6.0 |
| 2020-09 | CT#89e | CP-202203 | 2568 | 2 | F | Resolution of editor's notes on the handling of timers T3484 and T3585 when the UE provided no S-NSSAI during PDU session establishment. | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2570 | 1 | F | Handling of timers T3484 and T3585 received with 5GSM cause value #39 | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2572 | 1 | C | Allowed NSSAI assignment based on default subscribed NSSAI | 16.6.0 |
| 2020-09 | CT#89e | CP-202146 | 2575 |  | F | Retry restriction for NB-IoT UEs due to out of tariff package | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2577 | 1 | F | Default subcribed S-NSSAIs for re-NSSAA or revoked NSSAA | 16.6.0 |
| 2020-09 | CT#89e | CP-202156 | 2578 | 1 | F | Deleting pending NSSAI when moving to 4G | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2582 | 1 | F | Correction on QoS parameter"value is not used"in 5GS | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2587 |  | F | Handling of T3520 in AUTH REJ | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2589 | 1 | F | Correction that service reject is received not service request | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2590 |  | F | Correction to implementation of CR2297 | 16.6.0 |
| 2020-09 | CT#89e | CP-202151 | 2591 |  | F | Correction to the implementation of CR0988 | 16.6.0 |
| 2020-09 | CT#89e | CP-202146 | 2598 | 1 | F | Fix of Timer T3448 encoding | 16.6.0 |
| 2020-09 | CT#89e | CP-202152 | 2602 |  | F | Clarification on TWIF acting on behalf of N5CW device | 16.6.0 |
| 2020-09 | CT#89e | CP-202141 | 2606 |  | F | AMF including CAG information list in rejection messages | 16.6.0 |
| 2020-09 | CT#89e | CP-202228 | 2608 |  | F | Correction of the IEI of UE radio capability ID deletion indication | 16.6.0 |
| 2020-09 | CT#89e | CP-202173 | 2248 | 3 | F | Update of emergency number list using Configuration Update Command | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2383 | 3 | F | Single-registration mode without N26 for EPS NAS message container IE | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2404 | 1 | F | Clarification on the applicable access type for persistent PDU session | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2406 | 1 | D | Clarification on protection of initial NAS messages | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2408 | 1 | F | Fixing several typos and adding full form of abbreviation W-AGF | 17.0.0 |
| 2020-09 | CT#89e | CP-202184 | 2416 | 1 | D | Editorial changes – red text corrected to black text | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2425 |  | D | Not capitalized 5GSM IE names | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2426 |  | F | Incorrect IE names | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2427 |  | F | Selected PDU session type | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2429 |  | F | Overlapping requirements in 5.3.23 | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2432 |  | F | Minor corrections | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2435 |  | F | Dual-registration mode list correction | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2448 | 2 | F | QoS error checks for unstructured PDU session type | 17.0.0 |
| 2020-09 | CT#89e | CP-202024 | 2452 | 2 | F | The requirement of AMF to provide CAG information list for the current PLMN | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2454 | 1 | D | Abbreviations correction | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2456 | 1 | F | Definition of Routing Indicator | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2457 |  | F | Service Request procedure over non-3GPP access | 17.0.0 |
| 2020-09 | CT#89e | CP-202173 | 2458 |  | D | Several editorial changes | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2471 | 1 | F | Clarification of paging response | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2477 |  | F | Misleading definition of 5G-IA and 5G-EA | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2479 |  | D | Restructure the statement on establishment cause for non-3GPP access | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2489 | 1 | F | Correction to the octet number in 5GS network feature support | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2490 | 1 | F | Correction to Configred NSSAI updation based on Rejected NSSAI. | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2505 | 1 | F | Handling of 5GSM procedures when fallback is triggered | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2511 |  | F | Include NAS message container in security mode complete message | 17.0.0 |
| 2020-09 | CT#89e | CP-202113 | 2513 | 1 | F | High priority access before pass the NSSAA | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2516 | 1 | F | Exceptions in providing NSSAI to lower layers | 17.0.0 |
| 2020-09 | CT#89e | CP-202033 | 2517 | 1 | F | No VPLMN S-NSSAI change via the generic UE configuration update | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2519 | 1 | F | Correction in the session transfer | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2532 |  | F | UE behaviour for service reject with #15 | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2541 |  | F | Mapped 5G security context deletion upon IDLE mode mobility from 5GS to EPS over N26 interface | 17.0.0 |
| 2020-09 | CT#89e | CP-202227 | 2547 | 2 | F | Clarification to emergency registration procedure | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2573 | 2 | C | Rejected NSSAI due to subscription | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2579 | 1 | D | Deleting 5G NAS security context when 5G-EA0 used and PLMN changed | 17.0.0 |
| 2020-09 | CT#89e | CP-202184 | 2580 | 1 | F | De-registration in ATTEMPTING-REGISTRATION-UPDATE | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2581 | 1 | F | Correction on Payload container IE | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2583 | 1 | F | EMM parameters handling for 5G only causes | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2584 | 2 | F | Clarification on Operator-defined access category definitions IE | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2585 | 1 | F | The suggestion on back-off timer for 5GSM #29 | 17.0.0 |
| 2020-09 | CT#89e | CP-202174 | 2597 | 1 | F | Fix of encoding errors in 5GS mobile identity IE | 17.0.0 |
| 2020-09 | CT#89e | CP-202249 | 2609 |  | F | Avoid unnecessary signalling for CP only PDU sessions after inter-system change from S1 mode to N1 mode | 17.0.0 |
| 2020-12 | CT#90e | CP-203169 | 2524 | 2 | F | Clarification on HPLMN S-NSSAI | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2610 | 1 | F | Clarification for CP only PDU session | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2611 | 1 | F | Clarification for reflective QoS | 17.1.0 |
| 2020-12 | CT#90e | CP-203213 | 2615 | 1 | A | Alignment of User Plane Integrity Protection description | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2617 |  | F | Consistency of the term on rejection cause"S-NSSAI not available due to the failed or revoked network slice-specific authentication and authorization" | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2618 | 1 | F | Clarification on the condition when registration request is rejected for no network slices available | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2619 |  | F | Correction on UE behaviour after receiving"Network slicing subscription changed"indication | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2620 | 1 | F | Clarification on the S-NSSAI(s) included in the pending NSSAI | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2621 | 1 | F | Consistency of NETWORK SLICE-SPECIFIC AUTHENTICATION COMPLETE message | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2623 | 1 | F | AMF behavior upon receipt of NETWORK SLICE-SPECIFIC AUTHENTICATION COMPLETE message | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2624 |  | F | Addition of used definitions and abbreviations | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2625 |  | D | Editorial corrections in 24.501 | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2626 |  | F | Clarification on the 5GMM procedures which can be initiated by the UE in substate 5GMM-REGISTERED.ATTEMPTING-REGISTRATION-UPDATE | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2627 |  | F | Removal of bullet irrelevant to tracking area concept | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2628 | 1 | F | Merge of two bullets with the same handling for different Request type IE | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2631 | 1 | D | Phrase that the abbreviation PCO represents | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2632 | 1 | F | Protection of NAS IEs | 17.1.0 |
| 2020-12 | CT#90e | CP-203167 | 2635 | 2 | A | QoS parameter handling for the PDU session transfer between 3GPP and non-3GPP access | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2637 | 1 | F | Handling of QoS flow description without associated QoS rule | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2640 |  | F | RFCs related to DHCPv6 are obsoleted by RFC 8415 | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2642 |  | F | Inclusion of requested NSSAI in the REGISTRATION REQUEST message | 17.1.0 |
| 2020-12 | CT#90e | CP-203169 | 2643 |  | F | Clarification on the SPRTI bit of the MICO indication IE | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2644 |  | F | UE behavior after receiving the rejected NSSAI with rejection cause"S-NSSAI not available in the current PLMN or SNPN" | 17.1.0 |
| 2020-12 | CT#90e | CP-203166 | 2645 | 1 | A | 5G-GUTI reallocation after resume from 5GMM-IDLE mode with suspend indication due to paging | 17.1.0 |
| 2020-12 | CT#90e | CP-203186 | 2647 | 1 | A | Adding a missing "modification request" for the Request type IE during NSSAA | 17.1.0 |
| 2020-12 | CT#90e | CP-203218 | 2657 | 1 | A | NAS signalling connection release upon CAG information update via UCU | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2659 |  | F | Missing lower layer indications of barring and alleviation of barring | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2662 | 2 | F | Uplink data status IE in CPSR after integrity check failure | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2664 | 1 | F | Missing Allowed PDU Session Status IE in CPSR | 17.1.0 |
| 2020-12 | CT#90e | CP-203179 | 2667 | 2 | A | Clarification on 2nd Leg PDU SESSION ESTABLISHMENT ACCEPT handling for MA PDU Sessions | 17.1.0 |
| 2020-12 | CT#90e | CP-203179 | 2669 | 2 | A | Clarifications on Necessity of ATSSS Container IE | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2670 | 1 | F | Prohibit UE from setting "Follow-on request pending" in the REGISTRATION REQUEST when UE is in non-allowed area | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2675 |  | F | Clarifications on indicating subscribed MFBR/GFBR uplink/downlink | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2676 | 1 | F | Update cases where whether ER-NSSAI IE is used | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2677 | 1 | F | Extended rejected NSSAI storage | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2679 | 1 | F | Update definition of Network slicing information | 17.1.0 |
| 2020-12 | CT#90e | CP-203186 | 2681 | 2 | A | Excluding the S-NSSAI(s) in the pending NSSAI from the requested NSSAI | 17.1.0 |
| 2020-12 | CT#90e | CP-203186 | 2683 | 1 | A | Update the allowed/rejected NSSAI based on the result of NSSAA over 3GPP access and N3GPP access separately | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2687 | 2 | F | Add some missing ESM causes on the network side | 17.1.0 |
| 2020-12 | CT#90e | CP-203166 | 2688 | 1 | A | Timer value of active timer | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2689 | 1 | F | Paging collision with 5GMM specific procedure or service request procedure | 17.1.0 |
| 2020-12 | CT#90e | CP-203211 | 2690 | 1 | A | Correction to S-NSSAI based retry restriction | 17.1.0 |
| 2020-12 | CT#90e | CP-203167 | 2692 | 1 | A | EN resolution on 5QI as criteria type for ODAC | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2694 |  | F | Correction on slice based congestion control | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2696 | 1 | F | Rejected NSSAI handling for 1-to-many mapping in roaming scenario | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2697 |  | F | Set T3517 to smaller value for emergency services fallback | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2700 | 1 | F | Service request procedure and abnormal cases in the UE for CPSR and emergency fallback | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2701 | 1 | F | IEEE Std reference updates | 17.1.0 |
| 2020-12 | CT#90e | CP-203186 | 2703 | 1 | A | Correct pending NSSAI handling | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2707 | 1 | F | Correction to NAS transport procedure | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2708 | 1 | F | Correction to 5GMM cause #62 and allowed NSSAI | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2712 | 1 | D | Improve"Emergency PDU session"definition | 17.1.0 |
| 2020-12 | CT#90e | CP-203186 | 2717 | 1 | A | Correction in allowed NSSAI and pending NSSAI handling upon receipt of rejected NSSAI | 17.1.0 |
| 2020-12 | CT#90e | CP-203170 | 2719 |  | F | Clarification the condition that the Extended NSSAI IE is included in the CONFIGURATION UPDATE COMMAND message | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2722 | 1 | F | Correction on inclusion criteria for IP header compression configuration IE | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2724 | 1 | F | Correction on inclusion criteria for Ethernet header compression configuration IE | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2725 | 1 | F | Correction on the rejected NSSAI in the registration reject message | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2727 | 1 | F | SNPN access mode over 3GPP access when accessing SNPN services via a PLMN | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2729 | 3 | F | Handling of pending NSSAI and allowed NSSAI during periodic registration update | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2730 |  | F | Cell search in NG-RAN | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2731 |  | F | Correction in the N1 mode capability handling | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2733 | 4 | F | UE operation in case of routing failure | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2734 |  | F | Paging a UE using eDRX | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2735 | 1 | F | Correction in the AUSF operation in terms of checking the presence of the AT_RESULT_IND attribute in the EAP-response/AKA'-challenge message | 17.1.0 |
| 2020-12 | CT#90e | CP-203218 | 2739 | 2 | A | CAG information list in SR reject message | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2742 | 1 | F | Provision CAG information list through de-registration procedure | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2742 | 3 | F | Mobility Registration after back to coverage | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2744 |  | F | Delete 5G NAS security context due to invalid key | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2745 |  | F | Lack of ID for inter-system change from S1 mode to N1 mode | 17.1.0 |
| 2020-12 | CT#90e | CP-203166 | 2748 | 1 | A | PDU session release in CP-SR | 17.1.0 |
| 2020-12 | CT#90e | CP-203218 | 2750 | 2 | A | Update IEI of Port management information container | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2751 |  | F | Correct location of ABO field | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2752 |  | F | Correct reference of SM timer | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2754 |  | F | Only CAG supported UE process CAG information list | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2757 | 1 | F | Correction of EPS bearer context being activated | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2758 | 3 | F | Clarification on LADN Information update | 17.1.0 |
| 2020-12 | CT#90e | CP-203171 | 2759 | 1 | F | Absence of timer T3448 | 17.1.0 |
| 2020-12 | CT#90e | CP-203186 | 2761 | 1 | A | NSSAA for roaming UEs | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2764 | 1 | D | IE length style in message definition | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2765 |  | D | Minor corrections | 17.1.0 |
| 2020-12 | CT#90e | CP-203218 | 2771 | 1 | A | Reception of CAG information list without serving PLMN's entry in roaming | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2772 |  | F | N5CW device clean up | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2773 |  | F | Correction in paging procedure | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2774 | 3 | B | Usage of initial CAG information list | 17.1.0 |
| 2020-12 | CT#90e | CP-203218 | 2776 |  | A | 5GMM cause value #76 mapped to a different 5GMM cause value in network-initiated de-registration procedure | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2779 | 4 | F | Handling of radio link failure during NSSAA procedure | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2780 | 4 | F | AMF behavior in case of NSSAA failure due to temporal network failure | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2782 | 1 | F | Addition of 5GSM cause #37 | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2783 | 2 | F | Handing of QoS flow description errors | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2785 | 1 | F | Clarification on stopping back-off timers | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2786 |  | F | Delete EBI in the QoS flow description when the corresponding mapped EPS bearer context is deleted | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2787 |  | F | Update of the timers table for PDU session authentication command | 17.1.0 |
| 2020-12 | CT#90e | CP-203178 | 2794 | 2 | B | The impact on UE due to the introduction of Authentication and Key Management for Applications (AKMA) | 17.1.0 |
| 2020-12 | CT#90e | CP-203186 | 2796 | 2 | A | PLMN selection condition upon reception Registration Reject with cause #62 | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2807 | 1 | F | Avoiding repeated inter-system re-directions | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2809 | 3 | F | UE procedures when a request for emergency services fallback not accepted | 17.1.0 |
| 2020-12 | CT#90e | CP-203215 | 2811 | 2 | B | Notification to upper layer upper layer for MMTEL video call when T3346 or T3525 running | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2812 |  | F | Correct UE behaviour for cause #31 in SR | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2813 | 1 | F | Correction to T3502 for MRU | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2814 | 1 | F | Deregistration before initial registration in SNPN selection | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2815 | 1 | F | Clarification on description of triggering UE to enter 5GMM-DEREGISTERED state | 17.1.0 |
| 2020-12 | CT#90e | CP-203218 | 2817 | 2 | A | Correction in 5GMM cause value #72 | 17.1.0 |
| 2020-12 | CT#90e | CP-203166 | 2818 |  | A | Rapporteur cleanup of editor's notes for 5G_CIoT | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2819 | 2 | F | MO-SMS in non-3GPP access | 17.1.0 |
| 2020-12 | CT#90e | CP-203172 | 2824 | 1 | F | Clarification on default configured NSSAI update will initiate a registration procedure by UE when "re-registration requested" indicated | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2826 |  | F | Addition of used abbreviations | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2827 | 1 | D | Editorial corrections in 24.501 | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2828 | 1 | F | Consistency of terms"5GMM-IDLE mode over non-3GPP access"and"5GMM-CONNECTED mode over non-3GPP access" | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2829 | 1 | D | Consistent usage of acronym UE | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2832 | 1 | F | Set the Follow-on request indicator to"Follow-on request pending" | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2833 |  | F | requested NSSAI is Requested NSSAI IE or Requested mapped NSSAI IE | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2834 |  | F | Mobility and periodic registration update when the UE receives"RRC Connection failure"indication | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2835 |  | F | Condition when the UE shall include or not include the NAS message container IE | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2836 |  | F | S-NSSAI(s) contained in the pending NSSAI | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2839 | 1 | F | Default configured NSSAI storage after update by UE Parameters Update via UDM Control Plane Procedure | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2841 | 1 | F | Correcting the SERVICE ACCEPT message into SERVICE REQUEST message. | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2842 |  | D | REGISTRATION ACCCEPT message | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2845 | 1 | F | Correction on the condition of filling allowed NSSAI in registration accept message | 17.1.0 |
| 2020-12 | CT#90e | CP-203186 | 2847 | 2 | A | Add a missing case for registration reject | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2848 |  | F | Limit the guidance only for UE not supporting ER-NSSAI | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2851 | 1 | F | The handling of a CAG information list with no entry | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2853 |  | F | Correction to incrementing the registration attempt counter during abnormal cases for Mobility and periodic registration update for initiating an emergency PDU session | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2854 |  | F | Correction to the reference to service request abnormal cases | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2855 |  | F | Clarify PDU session modification command reject due to QoS-related errors | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2858 | 1 | F | Addition of missing requirements for storing KAUSF, KSEAF, SOR counter and UE parameter update counter | 17.1.0 |
| 2020-12 | CT#90e | CP-203173 | 2859 | 1 | F | Correction of UE-requested PDU session modification | 17.1.0 |
| 2020-12 | CT#90e | CP-203205 | 2860 | 2 | B | DNN setting in the 5GSM sublayer | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2861 | 1 | F | Buffered T3512 handling in non allowed service area | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2863 | 1 | F | Handling of Emergency Service Fallback procedure in NON-ALLOWED area | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2866 | 1 | F | NAS signalling connection release when SAR list is received | 17.1.0 |
| 2020-12 | CT#90e | CP-203166 | 2868 |  | A | 5G-GUTI reallocation after MT service request but before connection suspend | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2869 | 1 | F | Completion of service request procedure following CPSR for emergency fallback | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2870 | 1 | F | Clarification on Selected EPS NAS security algorithms IE | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2872 |  | F | SNPN access mode over 3GPP access when accessing PLMN services via a SNPN | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2876 | 1 | F | Adding the definition of non-CAG cell | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2877 | 1 | F | Protection of 5GSM message | 17.1.0 |
| 2020-12 | CT#90e | CP-203167 | 2879 |  | A | Shared 5G NAS security context | 17.1.0 |
| 2020-12 | CT#90e | CP-203205 | 2882 | 1 | F | Adding the abbreviations of PAP/CHAP in TS 24.501 and fixing a minor grammatical error in the NOTE on PAP/CHAP | 17.1.0 |
| 2020-12 | CT#90e | CP-203218 | 2884 | 1 | A | AN Release triggered by CAG information Update | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2885 | 1 | F | Miss local de-registration procedure before entering DEREGISTERED state | 17.1.0 |
| 2020-12 | CT#90e | CP-203270 | 2889 | 5 | F | N1 mode disable when neither emergency services nor emergency services fallback works | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2890 | 1 | F | Provide different UE IDs for trusted and untrusted non-3GPP access | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2895 | 1 | F | Delay enabling N1 mode until NAS signalling connection or RR connection is released | 17.1.0 |
| 2020-12 | CT#90e | CP-203179 | 2900 | 1 | A | Release MA PDU session when connecting to an ATSSS unsupported AMF | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2901 |  | F | Correction of UE handlings on 5GSM cause #50 and #51 | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2905 | 1 | F | UE behavior when the UE receives the rejected NSSAI | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2907 | 1 | F | S-NSSAI not available due to the failed or revoked NSSAA | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2908 | 1 | F | PDU session ID in CPSR message | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2910 | 1 | F | No available S-NSSAIs and emergency PDU session | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2917 |  | F | Correction on handling for 5GMM #73 for DoS attack | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2918 |  | F | Correction on MICO indication IE | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2922 |  | F | Collision of error handling on QoS operations | 17.1.0 |
| 2020-12 | CT#90e | CP-203186 | 2924 | 1 | A | Default S-NSSAI for which NSSAA has been successful, is included in allowed NSSAI in case of no eligible requested NSSAI | 17.1.0 |
| 2020-12 | CT#90e | CP-203179 | 2931 | 1 | A | SM/MM coordination for MAPDUs | 17.1.0 |
| 2020-12 | CT#90e | CP-203179 | 2935 | 1 | A | Clarification on release of MA PDU session over both accesses | 17.1.0 |
| 2020-12 | CT#90e | CP-203268 | 2921 | 3 | F | UE reachability after NOTIFICATION RESPONSE | 17.1.0 |
| 2020-12 | CT#90e | CO-203253 | 2926 | 4 | F | Checking ACK bit of the SOR container in the DL NAS TRANSPORT | 17.1.0 |
| 2020-12 | CT#90e | CP-203179 | 2937 | 1 | A | MA PDU session modification rejection during change from S1 mode to N1 mode | 17.1.0 |
| 2020-12 | CT#90e | CP-203177 | 2939 |  | A | Emergency registration not applicable for FN-RG | 17.1.0 |
| 2020-12 | CT#90e | CP-203174 | 2940 | 1 | F | The selected PLMN for emergency services via trusted non-3GPP access | 17.1.0 |
| 2020-12 | CT#90e | CP-203205 | 2941 | 1 | F | Avoid including both PAP/CHAP and EAP identifiers in PDU session establishment request | 17.1.0 |
| 2020-12 | CT#90e | CP-203177 | 2945 |  | A | Addition to the non 5G capable over WLAN (N5CW) device term | 17.1.0 |
| 2020-12 | CT#90e | CP-203274 | 2947 | 2 | F | Delete previously allowed NSSAI upon receipt of "NSSAA to be performed" | 17.1.0 |
| 2021-03 | CT#91e | CP-210117 | 2549 | 2 | F | UE behaviour in case of no allowed NSSAI is available | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2705 | 5 | F | PDU session establishment request attempt during ongoing re-NSSAA procedure | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2864 | 4 | F | Local release of PDU session due to Service Area Restriction | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2865 | 3 | F | Conflict of sub-state NON-ALLOWED-SERVICE with other 5GMM-REGISTERED sub-states | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2898 | 7 | F | Condition to stop timer T3540 | 17.2.0 |
| 2021-03 | CT#91e | CP-210121 | 2948 | 3 | F | Kausf change | 17.2.0 |
| 2021-03 | CT#91e | CP-210121 | 2949 | 1 | F | Clarification on AKMA | 17.2.0 |
| 2021-03 | CT#91e | CP-210121 | 2952 | 3 | F | Obtaining KAKMA and A-KID from NAS | 17.2.0 |
| 2021-03 | CT#91e | CP-210121 | 2953 | 1 | F | Collision of AKMA and NAS AKA procedure handling | 17.2.0 |
| 2021-03 | CT#91e | CP-210121 | 2954 | 2 | F | UE handling in case of no KAUSF available for AKMA | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2956 | 1 | F | Suspention of 5GSM messages during SOR | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2958 | 1 | F | Correction of Requested NSSAI handling | 17.2.0 |
| 2021-03 | CT#91e | CP-210114 | 2960 |  | A | Correction of handling of CAG information from a "PLMN equivalent to the HPLMN" | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2962 |  | D | Minor corrections | 17.2.0 |
| 2021-03 | CT#91e | CP-210114 | 2964 | 1 | A | Correction for SNPN access mode in non-3GPP access | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2965 | 1 | F | NAS signalling connection release triggered by CAG information list without entry of current PLMN | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2967 |  | F | Abnormal cases in the UE for PDU EAP result message transport procedure | 17.2.0 |
| 2021-03 | CT#91e | CP-210095 | 2968 | 2 | F | Handling of Kausf and Kseaf created before EAP-success | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2969 | 1 | F | PDU SESSION ESTABLISHMENT message | 17.2.0 |
| 2021-03 | CT#91e | CP-210249 | 2970 | 3 | F | SOR transparent container coding | 17.2.0 |
| 2021-03 | CT#91e | CP-210107 | 2972 | 1 | A | Fixing mis-implementation of CR2140 | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2973 | 2 | F | NB-N1 mode and max number of user planes resources established for MT case | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2974 |  | F | The handling of a CAG information list with no entry | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2976 | 1 | F | Correction for NB-N1 mode and maximum number of PDU sessions with active user plane resources | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2978 | 1 | F | PEI for UE not supporting any 3GPP access technologies | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2979 |  | F | Reference to UCU procedure is missing for a 5G-GUTI reallocation variant | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2980 | 1 | F | Re-initiation of NSSAA when S-NSSAI rejected for the failed or revoked NSSAA | 17.2.0 |
| 2021-03 | CT#91e | CP-210169 | 2982 | 3 | F | Update of CPSR procedure for low power location event reportingt | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2983 |  | F | UE-requested PDU session release with 5GSM cause #26 | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2984 | 1 | F | Clarify UE handling of receiving DL NAS TRANSPORT message with 5GMM cause #28 | 17.2.0 |
| 2021-03 | CT#91e | CP-210117 | 2985 |  | F | Clarify association of back-off timer for 5GSM cause #27 | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 2986 | 1 | F | Clarify 5GSM non-congestion back-off timer handling for re-registration required | 17.2.0 |
| 2021-03 | CT#91e | CP-210107 | 2989 |  | A | Fix location of 5GSM congestion re-attempt indicator IE in PDU session establishment reject message and PDU session modification reject message | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 2993 | 1 | F | Correct description of #54 by taking into account its applicability in interworking scenarios | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 2995 |  | F | Correction of Notification procedure | 17.2.0 |
| 2021-03 | CT#91e | CP-210133 | 2996 | 1 | F | Actions on T3247 expiry for other supported RATs | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 2997 | 2 | F | Timer related actions upon reception of AUTHENTICATION REJECT | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 2998 | 1 | F | State transition from 5GMM-CONNECTED mode with RRC inactive indication to LIMITED-SERVICE | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3002 | 1 | F | Clarifications to the handling of the stored pending NSSAI | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3004 |  | F | Corrections for 5GS network feature support IE | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3005 |  | F | UE behavior when received cause #62 in the REGISTRATION REJECT message | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3006 |  | F | Consistency of the term on rejection cause"S-NSSAI not available due to the failed or revoked network slice-specific authentication and authorization" | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3007 | 1 | F | Inclusion of Extended rejected NSSAI IE | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3008 | 1 | D | Editorial corrections on the first letter to be lowercase or uppercase | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3009 | 1 | F | Correction of storage of operator-defined access categories | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3010 |  | D | Fix several typos | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3011 | 3 | F | Complement when and how the configured NSSAI, rejected NSSAI and pending NSSAI may be changed | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3012 |  | F | Deletion of the duplicated content about new allowed NSSAI storage | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3013 |  | F | Missing pending NSSAI and rejected NSSAI(s) for the failed or revoked NSSAA for no duplicated PLMN identities or SNPN identities | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3014 |  | F | Add the native security context after changing to N1 mode in connected mode | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3016 | 1 | F | Clarification of maintaining 5G-GUTI in an abnormal case | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3019 |  | F | Delete previously allowed NSSAI upon receipt of "NSSAA to be performed" during initial registration | 17.2.0 |
| 2021-03 | CT#91e | CP-210118 | 3020 |  | F | Cleanup of"NSSAA to be performed set to 1" | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3022 |  | F | Remove the error case for mandatory IE of PDU SESSION MODIFICATION COMMAND message | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3024 | 1 | F | T3540 | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3025 | 2 | F | Exception data in restricted service area for a UE in connected mode | 17.2.0 |
| 2021-03 | CT#91e | CP-210106 | 3027 |  | A | T3575 | 17.2.0 |
| 2021-03 | CT#91e | CP-210135 | 3028 |  | D | Inclusive language review | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3029 |  | F | Alignment of protection of NAS IEs | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3030 | 1 | F | S-NSSAI association for 5GSM non-congestion control | 17.2.0 |
| 2021-03 | CT#91e | CP-210107 | 3033 |  | A | Corrections to congestion control procedure | 17.2.0 |
| 2021-03 | CT#91e | CP-210114 | 3035 | 1 | A | 5GSM back-off mechanisms in PDU session release procedure for SNPN | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3036 | 1 | F | Correction to the QoS operation error handlings in PDU session establishment procedure | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3037 | 1 | F | Handling for collision of PDU session handover procedures | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3038 |  | F | Mapped dedicated EPS bearer without default EPS bearer in the establishment procedure | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3041 | 1 | F | AN Release triggered by CAG information list in Registration Accept message | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3042 |  | F | Clarification on CAG-only UE behaviour for emergency PDU session | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3043 | 2 | F | Clarification on EPS bearer identity handling | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3044 | 1 | F | Clarification on the handling of QoS flow description without associated QoS rule | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3045 | 1 | F | Correct a copy error | 17.2.0 |
| 2021-03 | CT#91e | CP-210133 | 3046 |  | F | Correct the length of IE | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3048 | 3 | F | Error check and handling for match-all packet filter | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3049 | 1 | F | Handling of Rejected NSSAI in registration reject message without integrity protection | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3052 |  | F | Unify terminology about the Authorized QoS rules IE | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3053 |  | F | PLMN Search at Registered State | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3054 |  | F | UE behaviour when rejected with #76 via a non-CAG cell | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3055 | 1 | F | Deregister from emergency registered state as indicated | 17.2.0 |
| 2021-03 | CT#91e | CP-210119 | 3056 |  | F | Disable N1 mode after change to S1 mode for emergency services | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3057 |  | F | Clarification on NSSAI inclusion mode | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3058 | 1 | F | Initiate SMC to provide Selected EPS NAS security algorithms | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3059 | 1 | F | 5GSM cause handling in UE-requested PDU session modification procedure | 17.2.0 |
| 2021-03 | CT#91e | CP-210107 | 3063 | 1 | A | Local IP address in TFT negotiation in 5GS for 5G-4G interworking | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3066 | 1 | F | Consistent ngKSI IE name | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3067 | 1 | F | Correction on semantic errors in QoS operations | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3068 |  | F | Semantic errors in QoS operations on EPS bearers vs. QoS rules | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3069 |  | F | Syntactical errors on lack of mandatory parameters | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3070 | 1 | F | Correction on UE retry restriction for 5GSM causes #50/#51/#57/#58/#61 | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3071 |  | F | Correction on UE retry restriction for 5GSM cause #68 | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3073 |  | F | Rejected NSSAI in registration accept for NSSAA | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3076 | 1 | F | Prevention of loop scenario for 5GMM cause #62 | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3080 | 2 | F | Clarifications on PLMN and SNPN URSP storage - 24.501 part | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3082 | 3 | F | Clarification on SNPN UE policy management procedure abnormal handling | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3087 |  | D | Incorrect reference for NAS security algorithms | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3088 |  | F | Clarification on NAS security context alignment on 3GPP access and non-3GPP access | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3089 | 1 | F | Default configured NSSAI for PLMN | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3090 |  | F | "No suitable cells in tracking area" not applicable to non-3GPP access | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3091 | 1 | F | The UE behavior when the UE receives the allowed NSSAI | 17.2.0 |
| 2021-03 | CT#91e | CP-210120 | 3093 | 1 | F | Correction on service area list IEs | 17.2.0 |
| 2021-03 | CT#91e | CP-210114 | 3097 |  | A | T3245 of a UE operating in SNPN access operation mode | 17.2.0 |
| 2021-04 | CT#91e |  |  |  |  | Correction of misimplementation of CR 3091 | 17.2.1 |
| 2021-06 | CT#92e | CP-211131 | 3196 | 1 | A | Clarification on MA PDU session for LADN | 17.3.0 |
| 2021-06 | CT#92e | CP-211136 | 3140 |  | F | Clarification on a PDU session for time synchronization: SSC mode, always-on-ness | 17.3.0 |
| 2021-06 | CT#92e | CP-211136 | 3141 |  | F | DS-TT Ethernet port MAC address only sent when the PDU session type is Ethernet | 17.3.0 |
| 2021-06 | CT#92e | CP-211136 | 3142 | 1 | F | UE-DS-TT residence time used for UE-UE TSC | 17.3.0 |
| 2021-06 | CT#92e | CP-211136 | 3139 | 4 | B | Introduction of NAS enablers for IIoT | 17.3.0 |
| 2021-06 | CT#92e | CP-211136 | 3188 | 1 | F | Clarification on port management information container | 17.3.0 |
| 2021-06 | CT#92e | CP-211136 | 3190 | 1 | F | Clarification on EPS interworking of a PDU session for time synchronization or TSC | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3144 | 1 | C | Emergency services in an SNPN | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3137 | 1 | B | SNN verification for SNPN supporting AAA-Server for primary authentication and authorization | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3128 | 1 | B | Lists of 5GS forbidden tracking areas | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3129 | 1 | B | Forbidden SNPNs | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3130 | 1 | B | Enabling selection of an SNPN other than the subscribed SNPN | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3205 |  | F | Emergency service fallback and SNPN | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3206 |  | B | Inter-network mobility | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3133 | 3 | B | "List of subscriber data"handling for SNPN supporting AAA-Server for primary authentication and authorization | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3262 | 1 | C | Storage of 5GMM information for UEs in SNPN access operation mode | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3259 | 1 | C | The usage of the last visited registered TAI | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3260 | 1 | B | Support of the default configured NSSAI in the SNPN | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3204 | 1 | B | Onboarding in SNPN - slicing in initial registration | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3319 | 1 | B | Reject handling of registration for SNPN onboarding | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3320 | 1 | B | Slice handling in registration for SNPN onboarding | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3321 | 1 | B | De-registration for SNPN onboarding registered UE | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3322 | 1 | B | DNN/S-NSSAI providing in PDU session establishment for SNPN onboarding | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3323 | 1 | B | PVS information providing in PDU session establishment for onboarding | 17.3.0 |
| 2021-06 | CT#92e | CP-211137 | 3211 | 1 | B | Onboarding in SNPN - mobility registration update | 17.3.0 |
| 2021-06 | CT#92e | CP-211138 | 3208 | 1 | B | Support for MA PDU Session with 3GPP access in EPC | 17.3.0 |
| 2021-06 | CT#92e | CP-211138 | 3194 | 1 | F | Indication of UE supporting 3GPP access leg in EPC during MA PDU session establishment procedure | 17.3.0 |
| 2021-06 | CT#92e | CP-211138 | 3248 | 1 | B | Add target QoS flow capability for access performance measurement | 17.3.0 |
| 2021-06 | CT#92e | CP-211139 | 3124 | 1 | B | Handling the paging cause in the UE and the network for MUSIM in 5GS | 17.3.0 |
| 2021-06 | CT#92e | CP-211139 | 3119 | 5 | B | Definitions and abbreviations for Multi-USIM in 5GS | 17.3.0 |
| 2021-06 | CT#92e | CP-211139 | 3166 | 1 | B | Remove paging restriction via Registration | 17.3.0 |
| 2021-06 | CT#92e | CP-211139 | 3224 | 1 | B | Considering paging restrictions while paging the UE that is MUSIM capable in 5GS | 17.3.0 |
| 2021-06 | CT#92e | CP-211139 | 3225 | 1 | B | The MUSIM capable UE shall not initiate Service Request procedure for Leaving the network if Emergency service is ongoing in 5GS | 17.3.0 |
| 2021-06 | CT#92e | CP-211139 | 3226 | 1 | B | Using Service Request procedure for removing paging restrictions in 5GS for a Multi-USIM UE | 17.3.0 |
| 2021-06 | CT#92e | CP-211139 | 3267 | 3 | B | Updates to Registration procedure for MUSIM Leaving in 5GS | 17.3.0 |
| 2021-06 | CT#92e | CP-211139 | 3170 | 2 | C | Handling of service request when responding to paging with voice service indication | 17.3.0 |
| 2021-06 | CT#92e | CP-211139 | 3121 | 3 | B | Multi-USIM UE support indications in 5GS | 17.3.0 |
| 2021-06 | CT#92e | CP-211140 | 3106 | 1 | B | New cause value for rejected NSSAI | 17.3.0 |
| 2021-06 | CT#92e | CP-211140 | 3249 | 1 | F | Correction of the definition of the Rejected NSSAI | 17.3.0 |
| 2021-06 | CT#92e | CP-211140 | 3111 | 3 | B | Introducion of Network Slice Admission Control | 17.3.0 |
| 2021-06 | CT#92e | CP-211140 | 3112 | 3 | B | Clarificaiton on behaviors of the UE and the network supporting Network Slice Admission Control | 17.3.0 |
| 2021-06 | CT#92e | CP-211140 | 3123 | 4 | B | S-NSSAI rejected due to maximum number of UEs reached and BO timer value | 17.3.0 |
| 2021-06 | CT#92e | CP-211140 | 3213 | 2 | B | Maximum number of established PDU sessions already reached for a NW slice | 17.3.0 |
| 2021-06 | CT#92e | CP-211141 | 3135 | 1 | B | General section for ID_UAS | 17.3.0 |
| 2021-06 | CT#92e | CP-211141 | 3218 | 1 | B | Definition of UAV for purpose of UE NAS | 17.3.0 |
| 2021-06 | CT#92e | CP-211141 | 3244 | 1 | B | UE configuration update procedure update for UUAA | 17.3.0 |
| 2021-06 | CT#92e | CP-211141 | 3138 | 3 | B | Update on Registration procedure for UUAA-MM | 17.3.0 |
| 2021-06 | CT#92e | CP-211142 | 3125 | 1 | B | ProSe as a trigger for Service Request procedure | 17.3.0 |
| 2021-06 | CT#92e | CP-211142 | 3126 | 1 | B | Network shall not release the RRC connection for ProSe services | 17.3.0 |
| 2021-06 | CT#92e | CP-211142 | 3127 | 1 | B | ProSe policy provisioning start and stop indications | 17.3.0 |
| 2021-06 | CT#92e | CP-211142 | 3159 | 2 | B | UE ProSe capability negotiation with 5GC | 17.3.0 |
| 2021-06 | CT#92e | CP-211142 | 3110 | 3 | B | UE ProSe policy transmission | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3160 |  | F | Correction of a message name | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3174 |  | F | Revisions on the description of IEs in Service Request message | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3181 |  | F | Clarification on handling maximum number of established PDU sessions for MA PDU session | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3182 |  | F | Clarification of MA PDU session handling after network initiated deregistration | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3197 |  | D | Correction on "security control mode procedure | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3198 |  | F | Update cause of start T3540 | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3212 |  | F | Removal of editor's note on CAG information list in USIM | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3220 |  | D | Minor corrections | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3234 |  | F | Conditions for applying 5G-EA0 for the initial NAS message | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3238 |  | F | The UE enters the state 5GMM-SERVICE-REQUEST-INITIATED after sending the SERVICE REQUEST message | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3253 |  | D | Editorial corrections in TS 24.501 | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3263 |  | F | Abnormal cases in the PDU session authentication and authorization procedure | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3296 |  | F | Use the latest UE security capability when selecting 5G security algorithms | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3297 |  | F | null integrity protection algorithm used when UE has an emergency PDU session | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3300 |  | F | Clarification on the setting of packet filter identifier value | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3051 | 2 | F | Perform slice-independent services when no allowed NSSAI available | 17.3.0 |
| 2021-06 | CT#92e | CP-211144 | 3327 |  | F | UL DRB setup collided with DL 5GSM message | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3325 |  | F | Alignment on UE retry restriction for 5GSM causes #50/#51/#57/#58/#61 | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3345 |  | F | MNC digit 3 in the CAG information list IE | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3192 | 1 | F | T3447 value parameter in gUCU procedure | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3193 | 1 | F | CIoT, nw initiated re-negotiation of any header compression configuration | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3294 | 1 | F | NSSAA and de-registration procedures collision | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3039 | 2 | F | Handling of multiple SM Retry Timer values configured in a UE | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3344 | 1 | F | Correction in the CAG only UE | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3278 | 1 | F | Correction to resetting of the registration update counter | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3246 | 2 | F | UE behavior when the UE receives the Allowed NSSAI | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3279 | 1 | F | Correction to T3540 handling | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3280 | 1 | F | Updation of stored pending NSSA for equivalent PLMN(s) | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3072 | 3 | F | Excluding re-NSSAA for creating pending NSSAI | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 2961 | 2 | F | Handling of collisions between UE-requested 5GSM procedures and N1 NAS signalling connection release | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3329 | 1 | F | Transmission failure handling for NETWORK SLICE-SPECIFIC AUTHENTICATION COMPLETE | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3233 | 1 | F | LADN T3396 handling | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3272 | 2 | F | Forbidding registration area when no slice available | 17.3.0 |
| 2021-06 | CT#92e | CP-211145 | 3236 | 2 | F | Access barring for access categories '0' and '2' while timer RRC T302 is active | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3328 |  | F | Correction on UE radio capability update | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3335 |  | F | Relaxing requirement for NSSAA timing | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3346 |  | F | AMF decision on the use of a 5G NAS security context | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3172 | 1 | F | Retransmission timer starting for T3520 with emergency PDU session | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3175 | 1 | F | Add EMM SR procedure for non-integrity protected reject message | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 2913 | 3 | F | Clarification of access control checks for specific procedures initiated in 5GMM-CONNECTED mode with RRC Inactive | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3185 | 1 | F | Clarification of Collision of PDU session establishment procedure and network-requested PDU session release procedure for MA PDU sessions | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3230 | 1 | F | Disabling of N1 mode capability after failure in service request procedure triggered due to Emergency Service Fallback | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3240 | 1 | F | Correcting the NOTEs related to changes in some IEI values across releases | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3291 | 1 | F | Handling of abnormal cases of PDU session establishment procedure | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3292 | 1 | F | UE handling of S-NSSAI when interworking with ePDG and EPC | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3031 | 3 | F | Handling of 5GMM cause #91 | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3318 | 1 | F | DNN as an optional parameter when interworking with EPS | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3232 | 1 | F | AMF handling when none of the DNN's in LADN Indication IE are part of subscribed DNN list | 17.3.0 |
| 2021-06 | CT#92e | CP-211146 | 3239 | 1 | F | ESFB handling in case of network authentication failure | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3270 | 1 | F | RAT disable when re-attempts are not allowed | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3305 | 1 | D | Remove duplicated text about semantic error handling | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3293 | 1 | F | Correction to description of #54 | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3295 | 1 | F | Add a note to reference 24.173 | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3299 | 1 | F | Storage on counters and keys in 5G AKA | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3301 | 1 | F | UE does not delete 5G NAS security context in connected mode | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3302 | 1 | F | Clarification on CAG information list handling received in HPLMN | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3303 | 1 | F | Send REGISTRATION COMPLETE message only if the SOR information is received | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3187 | 1 | F | Clarification on UE initialted MA PDU deactivation | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3347 | 1 | F | 5GMM procedure updating the default configured NSSAI | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3330 | 1 | F | Correction to Ciphering key data IE | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3331 | 1 | F | Registration attempt counter reset when in SNPN | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3264 | 1 | F | Updating timer table for stopping timer T3540 | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3261 | 1 | F | Updating timer talbe for stopping timer T3565 when receiving CONTROL PLANE SERVICE REQUEST message | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3265 | 1 | F | The list of NSSAI(s) | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3221 | 1 | F | Second SMC procedure after RINMR | 17.3.0 |
| 2021-06 | CT#92e | CP-211147 | 3247 | 2 | F | Correction of Requested NSSAI handling | 17.3.0 |
| 2021-06 | CT#92e | CP-211148 | 3178 |  | F | Non-3GPP access T3540 timer after service procedure | 17.3.0 |
| 2021-06 | CT#92e | CP-211148 | 3191 | 1 | F | Non-3GPP access cannot use PLMN-SEARCH state | 17.3.0 |
| 2021-06 | CT#92e | CP-211148 | 3179 | 1 | F | Non-3GPP access and 5GMM cause 76 | 17.3.0 |
| 2021-06 | CT#92e | CP-211148 | 3050 | 5 | F | MMTELVoice and MMTEL Video in non-3GPP | 17.3.0 |
| 2021-06 | CT#92e | CP-211149 | 3145 | 3 | B | Introduction of handling of Edge computing for 5GS | 17.3.0 |
| 2021-06 | CT#92e | CP-211149 | 2977 | 7 | B | ECS address support indication and provisioning in ePCO | 17.3.0 |
| 2021-06 | CT#92e | CP-211150 | 3237 |  | D | Various editorial corrections | 17.3.0 |
| 2021-06 | CT#92e | CP-211150 | 3243 | 1 | F | Incorrect reference in subclause 4.5.4.2 | 17.3.0 |
| 2021-06 | CT#92e | CP-211150 | 3336 | 1 | B | Update Non-3GPP TAI to support N3SLICE | 17.3.0 |
| 2021-06 | CT#92e | CP-211151 | 3105 | 1 | F | Support of SOR-CMCI | 17.3.0 |
| 2021-06 | CT#92e | CP-211151 | 3131 | 1 | F | "ME support of SOR-CMCI" indicator | 17.3.0 |
| 2021-06 | CT#92e | CP-211151 | 3207 | 1 | B | SOR-CMCI transport and usage | 17.3.0 |
| 2021-06 | CT#92e | CP-211152 | 3143 | 1 | B | 5QI for satellite access | 17.3.0 |
| 2021-06 | CT#92e | CP-211152 | 3101 | 2 | B | New 5GMM cause for satellite access | 17.3.0 |
| 2021-06 | CT#92e | CP-211152 | 3219 | 2 | B | UE's handling of the indication of country of UE location | 17.3.0 |
| 2021-06 | CT#92e | CP-211152 | 3348 | 1 | B | PDU session establishment for NR satellite access | 17.3.0 |
| 2021-06 | CT#92e | CP-211152 | 3100 | 3 | B | MCC list for 5GMM message | 17.3.0 |
| 2021-06 | CT#92e | CP-211153 | 3115 |  | F | UE handling in case of no valid KAUSF for AKMA | 17.3.0 |
| 2021-06 | CT#92e | CP-211165 | 3103 | 4 | B | Encoding of API-based DN-AA | 17.3.0 |
| 2021-06 | CT#92e | CP-211311 | 3258 | 2 | B | Update of registrationprocedureforSNPNcase | 17.3.0 |
| 2021-06 | CT#92e | CP-211312 | 2843 | 10 | F | S-NSSAI providing in UE-requested PDU session establishment procedure with "existing PDU session" request type | 17.3.0 |
| 2021-06 | CT#92e | CP-211316 | 3202 | 3 | B | Onboarding in SNPN - initial registration | 17.3.0 |
| 2021-06 | CT#92e | CP-211322 | 3268 | 4 | B | Updates to Service Request for MUSIM Leaving and Reject Paging in 5GS | 17.3.0 |
| 2021-06 | CT#92e | CP-211325 | 3215 | 3 | F | Providing wildcard CAG-ID in the USIM | 17.3.0 |
| 2021-06 | CT#92e |  |  |  |  | Editorial correction in clause 5.3.19a | 17.3.1 |
| 2021-09 | CT#93e | CP-212120 | 3425 | 1 | A | Enabling storing two 5G NAS security contexts | 17.4.0 |
| 2021-09 | CT#93e | CP-212239 | 3546 | 2 | A | 5G NAS Security Context handling for multiple registrations | 17.4.0 |
| 2021-09 | CT#93e | CP-212160 | 3521 | 2 | B | Multiple round-trips of AA messages during UUAA-MM | 17.4.0 |
| 2021-09 | CT#93e | CP-212240 | 3581 | - | F | Correction for incorrect CR implementation | 17.4.0 |
| 2021-09 | CT#93e | CP-212263 | 3250 | 6 | B | C2 pairing authorization at PDU session establishment | 17.4.0 |
| 2021-09 | CT#93e | CP-212264 | 3251 | 6 | B | C2 pairing authorization at PDU session modification | 17.4.0 |
| 2021-09 | CT#93e | CP-212125 | 3567 | 1 | F | MINT: Added new registration type for disaster roaming. | 17.4.0 |
| 2021-09 | CT#93e | CP-212125 | 3512 | 1 | B | Deregister for disaster inbound roaming services | 17.4.0 |
| 2021-09 | CT#93e | CP-212128 | 3463 | - | F | UE-DS-TT residence time defined in 3GPP TS 23.501 | 17.4.0 |
| 2021-09 | CT#93e | CP-212128 | 3464 | - | F | Replacement of TS 24.519 with TS 24.539 | 17.4.0 |
| 2021-09 | CT#93e | CP-212128 | 3538 | 1 | F | Cleanup limitation about Ethernet DS-TT port and Ethernet type PDU session | 17.4.0 |
| 2021-09 | CT#93e | CP-212128 | 3539 | 1 | F | Supporting of TSCTSF | 17.4.0 |
| 2021-09 | CT#93e | CP-212128 | 3569 | 1 | F | IEEE Std 1588-2019 reference update | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3558 | - | F | Consistent terms on SNPN onboarding | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3557 | 1 | B | Slice handling for SNPN onboarding | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3519 | 1 | F | NSSAAF : Network slice-specific and SNPN authentication and authorization function | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3507 | 1 | F | Handling of AUTHENTICATION REJECT message in ON-SNPN | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3448 | 1 | C | Association of NSSAI, UE radio capability ID and back-off timers for UE supporting access to an SNPN using credentials from a credentials holder | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3446 | 1 | C | No support for eCall over IMS in SNPNs | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3392 | 1 | F | UE identity when onboarding in SNPN for which the UE has 5G-GUTI | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3391 | 1 | F | Editor's note on onboarding SUCI derivation | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3390 | 1 | F | S-NSSAI not provided when registered for onboarding services in SNPN | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3389 | - | F | Network identifier is not specified | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3387 | 1 | B | Authentication handling | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3384 | 1 | F | NID of SNPN which assigned 5G-GUTI in mobility registration update | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3383 | - | F | NID as cleartext IE | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3382 | 1 | F | PVS PCO parameter providing | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3377 | 1 | B | Clarification of UE status during registration procedure for onboarding | 17.4.0 |
| 2021-09 | CT#93e | CP-212129 | 3368 | 1 | B | Service request not accepted by an ON-SNPN | 17.4.0 |
| 2021-09 | CT#93e | CP-212130 | 3410 | 1 | F | Rename the 5GSM capability of supporting access performance measurements per QoS flow | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3489 | 2 | F | Corrections in Service Request procedure | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3488 | 3 | B | Reject RAN Paging using Service Request in RRC Inactive | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3487 | - | F | Corrections to Paging restriction IE | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3476 | 1 | B | NAS leaving to reject RAN paging | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3439 | - | B | Using Service Request procedure for removing paging restrictions in 5GS for MUSIM UE that uses the control plane CIoT 5GS optimization | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3438 | 1 | B | Resolving the Editor's note related to Paging Rejection for MUSIM UE in 5GS | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3421 | 2 | F | Timer handling for MUSIM UEs (for 24.501) | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3372 | - | D | Editorial corrections to CR#3170 | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3360 | 1 | B | MUSIM features are not applicable for non-3GPP access | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3354 | 1 | B | T3540 for MUSIM | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3352 | 1 | B | MUSIM and PEIs | 17.4.0 |
| 2021-09 | CT#93e | CP-212131 | 3350 | 1 | B | NOTIFICATION RESPONSE message indicating failure | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3570 | 1 | B | Clarification of the UCU procedure upon completion of NSSAA | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3561 | 1 | F | Correction on AMF actions on NSAC | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3560 | 1 | B | NSAC in de-registration procedure | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3559 | 1 | B | AMF handling on NSAC based on EAC mode | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3535 | 1 | F | Clarification on rejected NSSAI term | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3534 | - | F | Stop associated back-off timer when remove S-NSSAI from rejected NSSAI for the maximum number of UEs reached | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3517 | 1 | F | Removal of unnecessary ENs | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3516 | 1 | B | Clarify mobility management based on NSAC per access type independently | 17.4.0 |
| 2021-09 | CT#93e | CP-212142 | 3361 | - | F | Removal of CR3100r3 (C1-213895) (MCC list for 5GMM message) | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3515 | 1 | B | Clarification of mobility management based NSAC for roaming case | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3468 | 1 | B | Update to session management based NSAC | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3467 | 1 | F | Clarification on network behavior when all S-NSSAIs included in the requested NSSAI are rejected | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3417 | 1 | F | Update the description of NSAC about SNPN | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3416 | 1 | C | Resolution of an EN about pre-Rel-17 UE on NSAC | 17.4.0 |
| 2021-09 | CT#93e | CP-212132 | 3415 | 1 | C | The exception in Network Slice Admission Control for Emergency and Priority Services | 17.4.0 |
| 2021-09 | CT#93e | CP-212142 | 3510 | 1 | F | Handling of a reject message including 5GMM cause value #78 without integrity protection | 17.4.0 |
| 2021-09 | CT#93e | CP-212142 | 3414 | 1 | F | Update the description for satellite access | 17.4.0 |
| 2021-09 | CT#93e | CP-212142 | 3217 | 3 | B | 5GMM procedures for satellite access for reject cause on UE location - alternative handling | 17.4.0 |
| 2021-09 | CT#93e | CP-212133 | 3566 | - | F | Consistent term on USS communication | 17.4.0 |
| 2021-09 | CT#93e | CP-212133 | 3565 | 1 | F | EN resolution on delivering UUAA-MM result via UCU | 17.4.0 |
| 2021-09 | CT#93e | CP-212133 | 3564 | 1 | B | PDU session establishment reject for UUAA-SM | 17.4.0 |
| 2021-09 | CT#93e | CP-212133 | 3563 | 1 | B | UAV registered as normal UE | 17.4.0 |
| 2021-09 | CT#93e | CP-212133 | 3523 | 1 | F | Update of general section for ID_UAS | 17.4.0 |
| 2021-09 | CT#93e | CP-212133 | 3522 | 1 | B | Multiple round-trip of AA messages during UUAA-SM | 17.4.0 |
| 2021-09 | CT#93e | CP-212133 | 3520 | 1 | F | Clarification on UE behavior after Registration reject with UAV service is not allowed | 17.4.0 |
| 2021-09 | CT#93e | CP-212133 | 3418 | 1 | B | PDU session establishment request for UAS services | 17.4.0 |
| 2021-09 | CT#93e | CP-212133 | 3406 | 2 | B | NW initiated de-registration upon failure of ongoing UUAA-MM | 17.4.0 |
| 2021-09 | CT#93e | CP-212134 | 3486 | - | F | Add the missing description on ProSe under avoiding double barring | 17.4.0 |
| 2021-09 | CT#93e | CP-212134 | 3430 | 1 | F | Requesting ProSe resources as a trigger for Service Request procedure | 17.4.0 |
| 2021-09 | CT#93e | CP-212134 | 3426 | 1 | B | Introducing the Remote UE report procedure | 17.4.0 |
| 2021-09 | CT#93e | CP-212134 | 3420 | 1 | F | Resuming a connection due to ProSe discovery/communication over PC5 | 17.4.0 |
| 2021-09 | CT#93e | CP-212136 | 3386 | 1 | B | EAS rediscovery | 17.4.0 |
| 2021-09 | CT#93e | CP-212136 | 3385 | 1 | B | (Re)configuring DNS server addresses | 17.4.0 |
| 2021-09 | CT#93e | CP-212139 | 3399 | 1 | B | Network-requested PDU session modification procedure to be used for removing joined UE from MBS session(s) | 17.4.0 |
| 2021-09 | CT#93e | CP-212139 | 3395 | 1 | B | Introducing the MBS join and leave procedures | 17.4.0 |
| 2021-09 | CT#93e | CP-212139 | 3394 | 1 | B | Adding MBS join and Leave as purposes of the UE-requested PDU session modification procedure | 17.4.0 |
| 2021-09 | CT#93e | CP-212139 | 3370 | 2 | B | Multicast join procedure - Alt.1 | 17.4.0 |
| 2021-09 | CT#93e | CP-212139 | 3369 | 1 | C | Paging with TMGI for multicast services | 17.4.0 |
| 2021-09 | CT#93e | CP-212140 | 3529 | 1 | F | Correction on value of UE radio capability ID deletion indication IE | 17.4.0 |
| 2021-09 | CT#93e | CP-212140 | 3527 | 1 | F | Sending P-CSCF address(es) | 17.4.0 |
| 2021-09 | CT#93e | CP-212140 | 3457 | - | F | Incorrect reference in subclause 6.2.16 | 17.4.0 |
| 2021-09 | CT#93e | CP-212140 | 3453 | - | D | Editorial corrections | 17.4.0 |
| 2021-09 | CT#93e | CP-212140 | 3423 | - | F | Add handling of 5GMM cause #76 when UE does not have any stored CAG information list | 17.4.0 |
| 2021-09 | CT#93e | CP-212141 | 3525 | - | D | Corrected S-NSSAI SST for SOR-CMCI | 17.4.0 |
| 2021-09 | CT#93e | CP-212141 | 3365 | 1 | B | Alignments for the introduction of SOR-CMCI | 17.4.0 |
| 2021-09 | CT#93e | CP-212143 | 3452 | - | F | Resolving the Editor's note in AKMA procedure related to K_AUSF change after 5G AKA based primary authentication | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3483 | - | D | Superfluous description | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3482 | - | F | Non-IP MTU request in the PDU session establishment procedure | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3478 | - | F | Handling of multiple S-TAGs in the Ethernet header | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3477 | - | F | Clarification of destination and source MAC addresses | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3475 | - | F | Add a missing message to relax SM congestion control | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3470 | - | D | Editorial corrections | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3460 | - | F | Clarification of NSAAA abnormal failure handling | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3458 | - | F | Correction to CPSR handling in AMF | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3455 | - | F | Correction to #62 handling | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3454 | - | F | Clarification to collision of PDU sessions release procedures. | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3432 | - | D | Editorial corrections | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3422 | - | F | Fix inconsistent QoS handling for network-requested PDU session modification procedure | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3411 | - | F | AMF provides the CAG information list | 17.4.0 |
| 2021-09 | CT#93e | CP-212152 | 3409 | - | F | The incorrectly placed NOTE in QoS rule | 17.4.0 |
| 2021-09 | CT#93e | CP-212153 | 3542 | - | F | 5GSM state transition of MA PDU session | 17.4.0 |
| 2021-09 | CT#93e | CP-212153 | 3514 | - | F | Asignment of IEI values | 17.4.0 |
| 2021-09 | CT#93e | CP-212153 | 3505 | - | F | ANDSP not specified for a UE operating in SNPN access operation mode | 17.4.0 |
| 2021-09 | CT#93e | CP-212153 | 3502 | 1 | F | Processing Authentication Reject only if timer T3516 or T3520 is running | 17.4.0 |
| 2021-09 | CT#93e | CP-212153 | 3495 | 1 | F | UE changing from N1 mode to S1 mode | 17.4.0 |
| 2021-09 | CT#93e | CP-212153 | 3494 | - | F | Deleting forbidden PLMNs list when UE is switched off | 17.4.0 |
| 2021-09 | CT#93e | CP-212153 | 3474 | 1 | F | Align deregistration #62 with initial registration reject | 17.4.0 |
| 2021-09 | CT#93e | CP-212153 | 3473 | 1 | F | Clarification on NSSAI storage | 17.4.0 |
| 2021-09 | CT#93e | CP-212153 | 3472 | 1 | F | Clarify on T3245 in each specific procedure | 17.4.0 |
| 2021-09 | CT#93e | CP-212153 | 3471 | 1 | D | Remove duplicated MCC | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3568 | 1 | F | Handling redirection cause #31 for UE does not support S1 mode | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3550 | 1 | F | Rejected S-NSSAI update | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3549 | 1 | F | Correction on N5GC indication IE Format | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3544 | 1 | F | Not start T3540 if 5GMM cause is considered as abnormal cases | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3531 | 1 | F | Include UE radio capability ID deletion indication IE and UE radio capability ID IE simultaneously | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3506 | 1 | F | Handling two available native 5G-GUTIs during the registration procedure | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3504 | 1 | F | Maximum number of S-NSSAIs in an NSSAI | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3481 | 1 | F | Clarification of PF for Ethernet PDU session | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3427 | 1 | F | Trigger PDU SESSION MODIFICATION for deletion of mapped EPS to ensure sync with network | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3408 | 1 | F | Support MAC address range in packet filter | 17.4.0 |
| 2021-09 | CT#93e | CP-212154 | 3168 | 2 | F | 24.501 Redirect with MPS | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3555 | 1 | F | Correction on UE parameters update data set type | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3554 | 1 | F | Correction on indication of support of local address in TFT in S1 mode | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3553 | 1 | F | Correction on UE error handling on QoS operations | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3503 | 2 | F | SMC after Primary Authentication | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3493 | 1 | F | Discarding the content of the container for SOR when the security check about the container is failed. | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3469 | 1 | F | Simplification of description about rejected NSSAI and correction of requested NSSAI handling | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3461 | 1 | F | Starting T3540 for 5GMM cause #22 with T3346 value | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3449 | 1 | F | Resuming the RRC connection upon requesting resources for V2X communication over PC5 | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3443 | 1 | F | Clarification that IP and Ethernet packets can be delivered over Control Plane | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3435 | 1 | F | Uplink data status IE inclusion criteria clarification | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3434 | 1 | F | Correction of PCO related terminology | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3433 | 1 | F | Correction on providing Selected EPS NAS security algorithms in SMC | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3359 | 1 | D | Correction of MA PDU session network upgrade is allowed | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3326 | 3 | F | Registered for emergency services due to CAG restrictions | 17.4.0 |
| 2021-09 | CT#93e | CP-212155 | 3183 | 3 | F | Clarification of reactivation requested in PDU SESSION MODIFICATION COMMAND for an MA PDU session | 17.4.0 |
| 2021-09 | CT#93e | CP-212156 | 3480 | - | F | Correction on handling of the IMS VoPS over non-3GPP access indicator | 17.4.0 |
| 2021-09 | CT#93e | CP-212156 | 3279 | 1 | F | Handling of N1 mode capability for non-3GPP access for voice domain selection | 17.4.0 |
| 2021-09 | CT#93e | CP-212156 | 3401 | - | F | UE identity in NAS signalling connection establishment over wireline access | 17.4.0 |
| 2021-09 | CT#93e | CP-21215 | 3400 | 1 | F | SMSoIP triggering mo-SMS establishment cause for non-3GPP access | 17.4.0 |
| 2021-09 | CT#93e |  |  |  |  | Editorial correctionsandIEIs values added in tables8.3.1.1.1, 8.3.2.1.1, 8.3.7.1.1 and 8.3.9.1.1 | 17.4.1 |
| 2021-12 | CT#94e | CP-213211 | 3803 | 2 | B | Paging Early Indication with Paging Subgrouping Assistance | 17.5.0 |
| 2021-12 | CT#94e | CP-213252 | 3786 | 2 | B | Paging Subgrouping | 17.5.0 |
| 2021-12 | CT#94e | CP-213255 | 3780 | 2 | F | Access attempt of 5GMM CM management procedure without ongoing 5G-MO-LR | 17.5.0 |
| 2021-12 | CT#94e | CP-213027 | 3445 | 1 | A | Signalling support for UPIP for UEs not supporting standalone NR connected to 5GCN | 17.5.0 |
| 2021-12 | CT#94e | CP-213030 | 3701 | 1 | B | Introduction of EPS-UPIP support indication in 5GC | 17.5.0 |
| 2021-12 | CT#94e | CP-213030 | 3796 | 1 | F | PTI assignment in MANAGE UE POLICY COMMAND triggered by UE POLICY PROVISIONING REQUEST | 17.5.0 |
| 2021-12 | CT#94e | CP-213030 | 3800 | - | D | Miscellaneous corrections | 17.5.0 |
| 2021-12 | CT#94e | CP-213030 | 3811 | - | F | Remove PLMN from the extension of the forbidden PLMNs list upon T3247 expiry | 17.5.0 |
| 2021-12 | CT#94e | CP-213032 | 3688 | 1 | B | Add requirements to support NR RedCap devices | 17.5.0 |
| 2021-12 | CT#94e | CP-213032 | 3699 | 1 | C | Paging using eDRX for NR RedCap UE | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3695 | - | F | Error handling for QRI and QFI set to zero by the network | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3696 | - | F | DNS server security information UE capability | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3700 | - | F | Correction for the protection of initial NAS messages in case of CPSR message | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3707 | 2 | F | Abort deregistration for emergency | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3715 | - | D | Minor corrections | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3731 | - | D | Add abbreviations of MPS and MCS | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3735 | - | F | Clarification of N1 mode capability | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3738 | - | F | UE handling upon receipt of 5GSM cause #33 | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3739 | - | F | Access type of the PDU session when re-activation failure | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3753 | - | F | Correction to item code | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3755 | - | F | UE re-initiate initial registration procedure if authentication procedure is failed | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3761 | - | F | Correction to 5GSM cause value list | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3768 | - | F | Resolution of an EN about CAG-ID range-24.501 | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3774 | - | F | Clarification on destination and source MAC address range | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3806 | - | F | Correction of PDU sessions release procedures | 17.5.0 |
| 2021-12 | CT#94e | CP-213034 | 3814 | - | F | Align mapping of SMS over IP & SMS over NAS during double barring | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3584 | 3 | B | CP SoR in SNPN - procedures and coding | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3393 | 2 | F | Forbidden lists when an entry of the list of subscriber data is updated or UICC containing USIM is removed | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3586 | 2 | F | NSSAI when registered for onboarding services in SNPN | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3625 | - | F | SMF selection for SNPN onboarding | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3632 | 4 | B | De-registration for onboarding registered UE | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3633 | 1 | F | AMF Onboarding Configuration Data | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3634 | 1 | F | an indication registered for SNPN onboarding | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3668 | 4 | F | Handling of emergency numbers in SNPN | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3674 |  | F | T3510 expiry for the UE registered for onboarding services in SNPN | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3675 | 4 | F | Kausf generation when AAA server of CH is EAP server of EAP based primary authentication and key agreement procedure | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3748 | 1 | F | DNN and S-NSSAI used for onboarding in PLMN | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3750 | 1 | F | SMF configuring to UE with PVS address | 17.5.0 |
| 2021-12 | CT#94e | CP-213037 | 3751 | 1 | F | Secondary authentication/authorization by a DN-AAA server | 17.5.0 |
| 2021-12 | CT#94e | CP-213038 | 3778 | 1 | F | Updating ATSSS parameter update with network-requested PDU session modification | 17.5.0 |
| 2021-12 | CT#94e | CP-213039 | 3589 | 1 | B | Paging timing collision control support in 5GS | 17.5.0 |
| 2021-12 | CT#94e | CP-213039 | 3590 | - | B | Reject RAN paging with optional paging restrictions | 17.5.0 |
| 2021-12 | CT#94e | CP-213039 | 3591 | 1 | F | Clarification on removal of paging restrictions | 17.5.0 |
| 2021-12 | CT#94e | CP-213039 | 3601 | 1 | C | Always-on PDU sessions for MUSIM UE | 17.5.0 |
| 2021-12 | CT#94e | CP-213039 | 3619 | 1 | F | Service request procedure due to MUSIM when no allowed NSSAI is available | 17.5.0 |
| 2021-12 | CT#94e | CP-213039 | 3622 | 1 | F | Service request procedure for NAS connection release when T3346 is running (for 24.501) | 17.5.0 |
| 2021-12 | CT#94e | CP-213039 | 3623 | 1 | F | NAS connection release from 5GMM-CONNECTED mode with RRC inactive indication | 17.5.0 |
| 2021-12 | CT#94e | CP-213039 | 3665 | - | B | 5GS MUSIM SR transmission failure | 17.5.0 |
| 2021-12 | CT#94e | CP-213039 | 3667 | - | D | 5GS MUSIM Editorial Correction | 17.5.0 |
| 2021-12 | CT#94e | CP-213040 | 3402 | 4 | B | MUSIM capability negotiation in 5GCN | 17.5.0 |
| 2021-12 | CT#94e | CP-213040 | 3722 | 1 | F | T3447 handling for MUSIM capable UE | 17.5.0 |
| 2021-12 | CT#94e | CP-213040 | 3727 | 1 | F | MRU procedure for allocation of 5G-GUTI when T3346 is running | 17.5.0 |
| 2021-12 | CT#94e | CP-213040 | 3766 | 1 | F | Remove duplicated MUSIM definition | 17.5.0 |
| 2021-12 | CT#94e | CP-213040 | 3767 | 1 | F | Resolve EN on SR for rejecting RAN paging in 5GMM-CONNECTED mode with RRC inactive | 17.5.0 |
| 2021-12 | CT#94e | CP-213040 | 3773 | 1 | C | Remove paging restrictions in case of service area restrictions | 17.5.0 |
| 2021-12 | CT#94e | CP-213040 | 3794 | - | F | Only Paging for voice service | 17.5.0 |
| 2021-12 | CT#94e | CP-213040 | 3807 | 1 | F | Corrections for paging restriction preferences terminology in 5GS | 17.5.0 |
| 2021-12 | CT#94e | CP-213040 | 3808 | 1 | F | Releasing NAS signalling connection and Paging restriction during mobility registration in a TA outside the current Registration Area for MUSIM UE in 5GS | 17.5.0 |
| 2021-12 | CT#94e | CP-213040 | 3809 | 1 | B | Network to accept or reject the paging restriction requested by MUSIM capable UE in 5GS | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3349 | 4 | B | Network slice simultaneous registration group | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3599 | 1 | F | Add rejected nssai for max UE reached for #62 | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3617 | 1 | F | Clarification of the timer T3526 | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3618 | 1 | F | Removing the rejected S-NSSAI for the maximum number of UEs reached in case of IWK with EPC | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3620 | 1 | F | Support of NSAC and interworking with EPC | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3621 | 1 | F | Skip NSAC for existing PDU session request type | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3626 | 1 | F | NSAC for legacy UEs | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3627 | 1 | F | Removal of S-NSSAI from rejected NSSAI for the maximum number of UEs reached | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3640 | 2 | F | AMF handling of NSAC function for legacy UE. | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3655 | 1 | F | Clarification on rejected NSSAI for the maximum number of UEs reached with value 0 back-off timer | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3673 | 1 | F | 5GSM procedure when EAC is disabled | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3692 | 1 | F | Correction of the rejected NSSAI for the maximum number of UEs reached handling | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3698 | - | F | Correction on SM based NSAC | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3724 | - | F | Clarification of registration procedure in which NSAC is performed | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3744 | 1 | F | Clarification on SMF performing NSAC for an MA PDU session | 17.5.0 |
| 2021-12 | CT#94e | CP-213041 | 3763 | 1 | F | Local timer for AMF to update rejected NSSAI | 17.5.0 |
| 2021-12 | CT#94e | CP-213042 | 3689 | - | F | Change the reference to LPP protocol | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3628 | 2 | B | Common IE for C2 authorization | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3629 | 3 | B | 5GSM cause value of PDU session establishment reject for UAS services | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3630 | 1 | F | Missed CAA-Level UAV ID for C2 authorization | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3631 | 1 | F | Miscellaneous corrections on Service-level-AA container IE | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3637 | 1 | C | Update the general part for Authentication and authorization of UAV | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3638 | 1 | B | UUAA revocation for the case of UUAA-MM | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3641 | 3 | B | C2 aviation payload | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3645 | 3 | F | Using Service-level AA container for C2 authorization | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3648 | 1 | F | Service-level-AA pending indication | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3649 | 1 | F | Restriction to non3gpp access | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3651 | 1 | C | UUAA-SM procedure for re-authorization or re-authentication | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3653 | 1 | F | Remove EN on payload differentiation of Service-level-AA container | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3658 | 3 | B | SM request while UUAA-SM is ongoing | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3770 | 1 | B | Requirements related to UAS subscription change | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3789 | 1 | B | Collision between UUAA-MM and UE initiated deregistration | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3790 | 1 | B | Collision between UUAA-SM and UE requested PDU session release | 17.5.0 |
| 2021-12 | CT#94e | CP-213043 | 3791 | 1 | B | UUAA abnormal case | 17.5.0 |
| 2021-12 | CT#94e | CP-213045 | 3595 | 1 | B | Add the SMF shall provide the QoS flow description(s) for the PDU sessions used for relaying | 17.5.0 |
| 2021-12 | CT#94e | CP-213045 | 3616 | 1 | F | NAS signalling recovery from fallback when the UE was only performing ProSe PC5 procedures | 17.5.0 |
| 2021-12 | CT#94e | CP-213045 | 3644 | - | D | Editorial corrections for the ProSe relay terminologies and capabilities | 17.5.0 |
| 2021-12 | CT#94e | CP-213045 | 3683 | 1 | B | Triggering Service Request procedure due to lower layers request for ProSe layer-2 UE-to-network relay | 17.5.0 |
| 2021-12 | CT#94e | CP-213045 | 3775 | 1 | B | IPv6 prefix delegation via DHCPv6 for 5G ProSe layer-3 UE-to-network relay | 17.5.0 |
| 2021-12 | CT#94e | CP-213045 | 3776 | 1 | F | The type of the port number in Remote UE context list information element | 17.5.0 |
| 2021-12 | CT#94e | CP-213045 | 3782 | 1 | F | Merging UE triggered V2X and ProSe policy provision procedure in UAC | 17.5.0 |
| 2021-12 | CT#94e | CP-213045 | 3812 | - | F | Correcting the reference of the spec in which the UE requests the PCF to provide ProSeP | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3690 | 1 | F | SNPN for NSSAI inclusion mode | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3725 | 1 | F | Correction in mobility registration reject | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3729 | 1 | F | Clarification on when a 5GSM procedure can be initiated for LADN | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3732 | 1 | F | PDU session modification after inter-system change into a non-allowed area | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3733 | 1 | F | The order of PDU sessions to be transferred to EPS | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3734 | 1 | F | Collision handling of UE-requested PDU session establishment procedure and network-requested PDU session modification procedure | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3736 | 1 | F | PDU session type required in PDU session establishment request | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3741 | 1 | F | Issues with the condition of FIRST inter-system change for PDU session modification | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3756 | 1 | F | Reattempting LADN DNN rejected with #46 | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3757 | 1 | F | UE behaviour on #29 related back-off timer | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3760 | 1 | F | Add missing 5GSM cause values | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3762 | 1 | F | Correction on unidentifiable example for syntactical error | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3772 | 1 | F | Reservation of a bit in an entry of the CAG information list IE | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3805 | 1 | F | Clarification for UE parameters update data handling | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3813 | 1 | D | Reference correction - Editorial | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3823 | - | D | Editorial corrections in TS 24.501 | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3831 | - | F | Correction to condition to include the 5GS registration result IE in the REGISTRATION ACCEPT message | 17.5.0 |
| 2021-12 | CT#94e | CP-213047 | 3706 | 1 | F | Handling of the non-current 5G NAS security context at inter-system change from N1 mode to S1 mode | 17.5.0 |
| 2021-12 | CT#94e | CP-213048 | 3412 | 3 | F | The solution to the case the allowed CAG IDs of a PLMN beyond the limit of one Entry-1 | 17.5.0 |
| 2021-12 | CT#94e | CP-213048 | 3447 | 2 | F | Authentication failure when emergency service is ongoing | 17.5.0 |
| 2021-12 | CT#94e | CP-213048 | 3716 | 1 | F | MA PDU session information IE update | 17.5.0 |
| 2021-12 | CT#94e | CP-213048 | 3737 | 1 | F | Delete the PCO parameters after handover between 3GPP and non-3GPP access | 17.5.0 |
| 2021-12 | CT#94e | CP-213048 | 3752 | 1 | F | Acknowledgment for the security packet of SOR information | 17.5.0 |
| 2021-12 | CT#94e | CP-213048 | 3754 | 3 | F | Clarification on semantic error about match-all packet filter | 17.5.0 |
| 2021-12 | CT#94e | CP-213048 | 3795 | 1 | B | Derived QoS for UDP encapsulated IPsec packets | 17.5.0 |
| 2021-12 | CT#94e | CP-213048 | 3713 | 1 | F | Storing Allowed NSSAI for EPLMNs | 17.5.0 |
| 2021-12 | CT#94e | CP-213048 | 3714 | 1 | F | Deleting rejected S-NSSAI | 17.5.0 |
| 2021-12 | CT#94e | CP-213048 | 3712 | 2 | F | S-NSSAI with non-standard values | 17.5.0 |
| 2021-12 | CT#94e | CP-213049 | 3804 | 1 | F | Clarification for parameters associated with non-3GPP access | 17.5.0 |
| 2021-12 | CT#94e | CP-213050 | 3654 | 1 | B | Update on ECS configuration information | 17.5.0 |
| 2021-12 | CT#94e | CP-213050 | 3681 | 1 | F | ECS configuration information provisioning corrections | 17.5.0 |
| 2021-12 | CT#94e | CP-213053 | 3660 | 1 | B | Updating MBS service area for the MBS session that the UE has joined | 17.5.0 |
| 2021-12 | CT#94e | CP-213053 | 3661 | - | F | The MBS service area received in PDU SESSION ESTABLISHMENT ACCEPT message can include both of MBS TAI list and NR CGI list | 17.5.0 |
| 2021-12 | CT#94e | CP-213053 | 3662 | 1 | B | Introducing MBS back-off timer for MBS join rejection | 17.5.0 |
| 2021-12 | CT#94e | CP-213053 | 3663 | 1 | F | Aligning the MBS procedures across different clauses | 17.5.0 |
| 2021-12 | CT#94e | CP-213053 | 3709 | 1 | B | MBS operation in Requested MBS container IE | 17.5.0 |
| 2021-12 | CT#94e | CP-213053 | 3777 | 1 | F | Correction to type of MBS session ID source specific IP multicast address | 17.5.0 |
| 2021-12 | CT#94e | CP-213053 | 3815 | - | B | The impact of the De-registration procedure on the MBS sessions | 17.5.0 |
| 2021-12 | CT#94e | CP-213053 | 3816 | - | B | SMF to consider the UE as removed from the associated MBS sessions due to the PDU session release procedure | 17.5.0 |
| 2021-12 | CT#94e | CP-213053 | 3817 | 1 | B | Removing the joined UE from MBS session due to becoming outside an updated MBS service area | 17.5.0 |
| 2021-12 | CT#94e | CP-213053 | 3818 | - | B | Removing joined UE from MBS sessions at inter-system change from N1 mode to S1 mode | 17.5.0 |
| 2021-12 | CT#94e | CP-213054 | 3670 | 1 | B | Introduction of redundant PDU sessions | 17.5.0 |
| 2021-12 | CT#94e | CP-213054 | 3671 | 3 | B | 5GSM protocol update for redundant PDU sessions | 17.5.0 |
| 2021-12 | CT#94e | CP-213055 | 3437 | 6 | B | Provisioning of parameters for disaster roaming in the UE | 17.5.0 |
| 2021-12 | CT#94e | CP-213055 | 3585 | 4 | B | PLMN with disaster condition | 17.5.0 |
| 2021-12 | CT#94e | CP-213055 | 3614 | 3 | B | Addition of 5GS registration type for initial registration disaster roaming. | 17.5.0 |
| 2021-12 | CT#94e | CP-213055 | 3642 | - | F | Correction of implementation errors of CR3512 (C1-215139) | 17.5.0 |
| 2021-12 | CT#94e | CP-213055 | 3656 | 4 | F | Registration result IE indicate UE is registered for disaster roaming service | 17.5.0 |
| 2021-12 | CT#94e | CP-213055 | 3679 | 1 | B | Introducing access identity 3 for disaster roamer | 17.5.0 |
| 2021-12 | CT#94e | CP-213055 | 3742 | - | B | Unnecessary signalling for providing selected EPS NAS security algorithms to disaster roaming UEs | 17.5.0 |
| 2021-12 | CT#94e | CP-213055 | 3820 | 1 | B | Updating initial registration for disaster roaming services | 17.5.0 |
| 2021-12 | CT#94e | CP-213055 | 3825 | 1 | B | Adding definition for registered for disaster roaming services | 17.5.0 |
| 2021-12 | CT#94e | CP-213056 | 3669 | 1 | F | SOR-CMCI storage | 17.5.0 |
| 2021-12 | CT#94e | CP-213056 | 3702 | - | B | Adding the SOR security check criterion to the SOR-CMCI | 17.5.0 |
| 2021-12 | CT#94e | CP-213056 | 3797 | 1 | F | UE performing deregistration procedure in 5GMM-CONNECTED mode | 17.5.0 |
| 2021-12 | CT#94e | CP-213057 | 3431 | 4 | B | Validity of cause code #78 | 17.5.0 |
| 2021-12 | CT#94e | CP-213057 | 3606 | 1 | B | Alignment to KI#2 conclusions on EPLMN list | 17.5.0 |
| 2021-12 | CT#94e | CP-213057 | 3636 | - | F | Access Technology Identifier satellite NG-RAN | 17.5.0 |
| 2021-12 | CT#94e | CP-213057 | 3833 | 1 | C | Clarification of UE location verification in registration procedure | 17.5.0 |
| 202203 | CT#95e | CP-220022 | 3981 | 2 | B | Failure case for 5G SRVCC | 17.6.0 |
| 2022-03 | CT#95e | CP-220147 | 4131 | - | B | Handling of forbidden TAI(s) within broadcast TACs in registration procedure | 17.6.0 |
| 2022-03 | CT#95e | CP-220213 | 3711 | 4 | F | Paging restrictions with Connection Release in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220233 | 3948 | 2 | F | MUSIM capabilities exchange while Emergency service is ongoing in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220234 | 4077 | 2 | F | Adding the paging timing collision control in the definition of the MUSIM UE in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220250 | 3850 | 2 | B | MUSIM support for SNPN access mode | 17.6.0 |
| 2022-03 | CT#95e | CP-220317 | 3868 | 2 | B | UUAA-MM completion alignment | 17.6.0 |
| 2022-03 | CT#95e | CP-220318 | 3867 | 2 | B | UUAA revocation alignment | 17.6.0 |
| 2022-03 | CT#95e | CP-220319 | 3765 | 5 | B | UAS security information obtained during UUAA | 17.6.0 |
| 2022-03 | CT#95e | CP-220337 | 3916 | 2 | F | General description on Multi-USIM UE in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220229 | 3984 | 1 | A | RID for SNPN UEs | 17.6.0 |
| 2022-03 | CT#95e | CP-220229 | 3985 | 2 | A | RID update for SNPN UEs | 17.6.0 |
| 2022-03 | CT#95e | CP-220229 | 4002 | 1 | A | NSSAA applicable for SNPN in Rel-17 | 17.6.0 |
| 2022-03 | CT#95e | CP-220236 | 3849 | - | F | SUPI type of onboarding SUPI | 17.6.0 |
| 2022-03 | CT#95e | CP-220236 | 3871 | 1 | F | Clarification on lists of forbidden SNPNs in an ON-SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220236 | 3872 | 1 | F | Handling of 5GMM cause values #3 and #6 in an ON-SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220236 | 3873 | 1 | F | Handling of 5GMM cause value #7 in an ON-SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220236 | 3874 | - | F | Handling of non-integrity protected reject messages with 5GMM cause value #3, #6, or #7 in an ON-SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220236 | 3917 | 1 | F | UE operation after adding the ID of an ON-SNPN in the permanently forbidden SNPNs list | 17.6.0 |
| 2022-03 | CT#95e | CP-220236 | 3918 | 1 | F | Handling of a non-integrity protected AUTHENTICATION REJECT message received from an ON-SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220236 | 3925 | - | F | Correction in 5GMM cause value #93 handling | 17.6.0 |
| 2022-03 | CT#95e | CP-220236 | 3933 | 1 | F | Onboarding indication | 17.6.0 |
| 2022-03 | CT#95e | CP-220237 | 3844 | 1 | F | Two available native 5G-GUTIs during the registration procedure not applicable in SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220237 | 3845 | 1 | F | NID IE inclusion condition | 17.6.0 |
| 2022-03 | CT#95e | CP-220237 | 3846 | 1 | F | 3GPP PS data off and UE in non-subscribed SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220237 | 3847 | 1 | B | Anonymous SUCI | 17.6.0 |
| 2022-03 | CT#95e | CP-220237 | 3905 | 1 | F | NSAC for S-NSSAI used for onboarding services in SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220237 | 3923 | 1 | B | Onboarding indication over N11 in an ON-SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220237 | 3966 | 1 | F | Onboarding DNN/S-NSSAI | 17.6.0 |
| 2022-03 | CT#95e | CP-220237 | 3986 | - | F | Providing PVS information for obtaining credentials for NSSAA or PDU session authentication and authorization procedure in SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220237 | 3924 | 1 | F | Correction in the UE behavior upon receipt of a DEREGISTRATION REQUEST message with 5GMM cause value #75 from an ON-SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220238 | 3839 | 4 | B | Enabling update of SOR-SNPN-SI in a PLMN | 17.6.0 |
| 2022-03 | CT#95e | CP-220238 | 3843 | 2 | B | Usage of indication to use MSK for derivation of KAUSF after success of primary authentication and key agreement procedure | 17.6.0 |
| 2022-03 | CT#95e | CP-220238 | 3934 | 3 | F | NSAC for SNPN onboarding | 17.6.0 |
| 2022-03 | CT#95e | CP-220238 | 3987 | 1 | F | UE requesting PVS information | 17.6.0 |
| 2022-03 | CT#95e | CP-220238 | 3988 | 1 | B | Providing PVS addresses for obtaining SO-SNPN credentials when registered for non-onboarding services in SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220238 | 3990 | 1 | B | EAP-TTLS with two phases of authentication | 17.6.0 |
| 2022-03 | CT#95e | CP-220238 | 4019 | 1 | F | Congestion control for onboarding in SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220238 | 4048 | 1 | F | Clarification of the UE behavior for the pending NSSAI for the current SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220238 | 4049 | 1 | F | Clarification of the UE behavior for the rejected NSSAI for the failed or revoked NSSAA for the current SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220238 | 4064 | 1 | F | Missing cause value number for Onboarding services terminated | 17.6.0 |
| 2022-03 | CT#95e | CP-220239 | 3860 | 1 | B | Local deactivation of UP resource for an MA PDU session with PDN leg - 24501 Part | 17.6.0 |
| 2022-03 | CT#95e | CP-220239 | 3861 | 1 | F | Clarification on maximum number of PDU sessions has been reached | 17.6.0 |
| 2022-03 | CT#95e | CP-220239 | 3862 | 1 | F | UE receives ATSSS not supported | 17.6.0 |
| 2022-03 | CT#95e | CP-220239 | 3863 | 1 | F | Abnormal handling for adding non-3GPP leg to an MA PDU session already with PDN leg | 17.6.0 |
| 2022-03 | CT#95e | CP-220239 | 3864 | 1 | F | Clarification on QoS rules merge for MA PDU session | 17.6.0 |
| 2022-03 | CT#95e | CP-220240 | 3666 | 2 | B | 5GS MUSIM Paging restriction | 17.6.0 |
| 2022-03 | CT#95e | CP-220240 | 3851 | - | F | Condition for removing the paging restriction | 17.6.0 |
| 2022-03 | CT#95e | CP-220240 | 3853 | - | F | N1 NAS signalling connection release reformulation | 17.6.0 |
| 2022-03 | CT#95e | CP-220240 | 3854 | - | F | Paging restriction in N1 NAS signalling connection release upon RAN paging rejection | 17.6.0 |
| 2022-03 | CT#95e | CP-220240 | 3857 | 1 | F | Correction of T3540 start scenarios for MRU procedure | 17.6.0 |
| 2022-03 | CT#95e | CP-220240 | 3913 | 1 | F | The interaction of AS-NAS layer on RAN paging | 17.6.0 |
| 2022-03 | CT#95e | CP-220240 | 3914 | 1 | F | Connection release for emergency service in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220240 | 3949 | - | F | UE to release NAS signalling connection and indicate Paging restriction during mobility Registration only if no emergency service is ongoing in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220240 | 3960 | 1 | C | PTCC handling during emergency registration | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 3912 | 2 | F | The handling of paging cause support indicator in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 3937 | 1 | F | Collision between UCU and SR | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 3939 | 2 | F | Clarification on Paging cause | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 3982 | - | F | Terminology clean up in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 4038 | 1 | F | Paging restriction with connection release in non-allowed area | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 4039 | 1 | F | Correction of T3447 handling for Multi-USIM UE | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 4040 | - | F | Correction of T3346 handling for Multi-USIM UE | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 4078 | - | F | Harmonization of the paging restriction terminology for MUSIM in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 4081 | 1 | F | Uplink data status IE not included when requesting release | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 4051 | 1 | F | Clearing paging restrictions when no Allowed NSSAI is available | 17.6.0 |
| 2022-03 | CT#95e | CP-220241 | 4050 | 2 | F | Clearing paging restrictions during lower layer failure in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3536 | 2 | F | Rejected NSSAI for the maximum number of UE reached with different PLMNs in RA | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3855 | 3 | B | PDU session establishment reject for network slice data rate control | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3875 | 1 | F | NSAC for number of PDU sessions taking access type into account | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3876 | 1 | F | Clarification on NSAC for emergency and priority services | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3877 | 1 | F | NSAC for existing PDU session with inter access handover | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3878 | 1 | F | S-NSSAIs in allowed NSSAI share common NSSRG value | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3879 | 2 | F | Provide all subscribed S-NSSAIs in configured NSSAI | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3881 | 1 | F | NSAC during PDU session transfer with the Allowed PDU session status IE | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3886 | 1 | F | 5GSM message not forwarded in case of NSAC reject | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3906 | 1 | F | Access type for rejected NSSAI for the maximum number of UEs reached | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3907 | - | F | NSSAA result not impacted by NSAC | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3926 | 2 | F | Clarification on an S-NSSAI not allowed solely due to NSSRG restriction | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3929 | 1 | F | NSAC applicable for SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 3999 | 1 | F | Removal of several Editor's notes related to NSAC and NSSRG | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 4015 | 1 | F | Coding of NSSRG information IE | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 4016 | 1 | F | NSSRG feature applicable to SNPN | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 4111 | 1 | F | 5GSM message not forwarded in case of NSAC reject: AMF operation | 17.6.0 |
| 2022-03 | CT#95e | CP-220242 | 4112 | - | F | Correction on EAC mode to per slice level | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 3792 | 5 | B | PDU session establishment with the DNN/S-NSSAI for UAS service from the UE whch has valid aerial subscription but UUAA-MM is failed abnormally | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 3841 | 1 | F | Clarification of including Service-level-AA container in PDU SESSION MODIFICATION REQUEST message | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 3865 | 3 | F | Adding missing UUAA-SM text | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 3889 | 1 | F | Clarification on PDU session establishment for valid subscription of DNN/S-NSSAI | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 3890 | 1 | F | Generalizing 5GMM cause for UAS service not allowed. | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 3891 | 1 | F | Clarification when valid UUAA result is available in the UE MM context | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 3892 | - | F | Remove resolved ENs | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 3893 | 1 | F | SA3 requirement for security protected UAS parameters. | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 3945 | 1 | F | Correction to the general part for UUAA | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 3947 | 2 | C | The handling of 5GMM#79 | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 4010 | 1 | F | Modify service-level-AA parameters | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 4011 | 1 | F | Correction of procedure and text for UAS services | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 4054 | 1 | F | Clarification for revocation of C2 authorization | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 4089 | - | F | Update IEI of Service-level-AA container | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 4113 | 1 | F | Correction on description of C2 authorization parameters | 17.6.0 |
| 2022-03 | CT#95e | CP-220244 | 4114 | - | F | Correction on service-level-AA response bit name | 17.6.0 |
| 2022-03 | CT#95e | CP-220245 | 3882 | 1 | F | Remote UE report not allowed when 5GSM BO timer is running | 17.6.0 |
| 2022-03 | CT#95e | CP-220245 | 3884 | 1 | F | Collision of network initiated PDU session release and remote UE report procedures | 17.6.0 |
| 2022-03 | CT#95e | CP-220245 | 3956 | - | F | Corrections for Service Request procedure when requesting 5G ProSe resources is the trigger for the procedure | 17.6.0 |
| 2022-03 | CT#95e | CP-220245 | 3995 | 1 | B | Update to NAS security mode command during PC5 link establishment | 17.6.0 |
| 2022-03 | CT#95e | CP-220245 | 4065 | 1 | F | Correction of IEI values for the REMOTE UE REPORT message | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 3967 | - | F | DNN as an optional parameter for emergency PDU session when interworking with EPS | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 3968 | - | F | Applicability of NULL integrity protection algorithm in case of a established emergency PDU session | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 3969 | - | F | Disabling of N1 mode in case of #10 while Emergency call pending | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 3989 | - | F | Lost text in 6.4.1.2 | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4000 | - | D | Two editorial corrections | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4004 | - | F | Clarification to payload container IE | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4006 | - | F | Correction to 5GSM capability IE | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4021 | - | F | Correct Re-attempt indicator IE for #39 in PDU session release | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4024 | - | F | Adding the missing implementation of C1-215154 | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4026 | - | D | Editorial correction of 5GS network support | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4027 | - | F | UE is allowed to use PCO IE after inter-system change from N1 mode to S1 mode | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4037 | - | F | CIoT user data container not forwarded due to congestion control | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4041 | - | F | Correction for enabling use of MICO mode | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4042 | - | F | Correction of eDRX handling in 5GS | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4053 |  | F | Clarification of Notification response message | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4061 | - | F | Correction on UAC exception handling | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4063 | - | F | Correction to the MBS back-off timer | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 4079 | - | F | Correcting the terminology of the signalling between the UE and the SMF | 17.6.0 |
| 2022-03 | CT#95e | CP-220247 | 3997 | 1 | F | Alignment of 5GSM state machine to procedural descriptions | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4023 | 1 | F | Correction on #62 | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4031 | 1 | F | Handling of ESM non-congestion back-off timer | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4032 | 1 | F | Correction to the PDU session release procedure | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4034 | 1 | F | Starting T3540 only considers Service Request message but not the CPSR Message | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4085 | - | F | Correction on creating Qos rule in an ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST message | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4087 | - | F | Correction on number of standardized access category | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4093 | - | F | No modification operation permitted in ACTIVATE BEARER CONTEXT REQUEST message | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4102 | - | F | 5GMM cause #31 not used instead of #76 | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4106 | - | F | Counter management in a UE | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4107 | - | F | Clarification on SM_RetryAtRATChange values configured in both ME and USIM | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4116 | - | F | Correction on establishment of NAS signalling connection over non-3GPP access | 17.6.0 |
| 2022-03 | CT#95e | CP-220248 | 4118 | - | F | Correction on UE handling on semantic errors in QoS operations | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4007 | 1 | F | Duplicate 5GMM message type values | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4008 | 1 | F | Indication of pending PDU session for NAS recovery | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4017 | 1 | F | Correct Coding of PEIPS assistance information IE | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4036 | 1 | F | Clarification on Allowed PDU session status IE included in registration request message and service request message | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4043 | 1 | F | The handling of eDRX in the AMF | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4069 | 1 | F | Change in CIoT optimizations preferred network behavior | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4080 | 1 | F | Clarifications on the mapped 5G-GUTI terminology | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4083 | 1 | D | Service request for redirecting CIoT UEs to EPC | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4086 | 1 | F | Correction on syntactical error in QoS operation | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4090 | 1 | F | Initiate PDU session modification procedure for emergency PDU session | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4091 | 2 | F | Indicate change of PS data off UE status outside of LADN service area | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4092 | 1 | F | Error handling about QoS rule without corresponding QoS flow description | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4094 | 1 | F | Clarification on QoS flow handling | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4096 | 1 | F | Protect emergency PDU session when receiving #28 in the service reject message | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4104 | 1 | F | Correction in the AMF operation upon initiating a UCU for CAG information update | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4105 | 1 | F | Correction in the UE operation upon receipt of a CAG information list during the initial registration | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4117 | 1 | F | Authorized QoS flow provided by network | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4119 | 1 | F | Correction on UE handling on syntactical errors in packet filters | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4120 | 1 | F | Correction on attempt counter reset | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4124 | 1 | C | The solution to CAG IDs of a PLMN beyond the limit of one Entry-IE part | 17.6.0 |
| 2022-03 | CT#95e | CP-220249 | 4125 | 1 | C | The solution to CAG IDs of a PLMN beyond the limit of one Entry-Procedure part | 17.6.0 |
| 2022-03 | CT#95e | CP-220251 | 3996 | 1 | F | Updates to 5GS session management aspects over non-3GPP access | 17.6.0 |
| 2022-03 | CT#95e | CP-220252 | 3848 | 1 | B | EDC related PCO parameters usage | 17.6.0 |
| 2022-03 | CT#95e | CP-220252 | 3895 | 3 | B | Spatial validity condition coding | 17.6.0 |
| 2022-03 | CT#95e | CP-220252 | 3957 | 3 | B | Support of updating ECS configuration info | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3856 | 2 | B | Update for multicast session release | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3900 | 2 | B | UE MBS session local release at PDU session release | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3903 | 1 | F | Correction of the length field of the requested MBS container IE | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3920 | 1 | B | UE handling of MBS back-off timer | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3921 | - | B | UE Locally leaves the MBS session when the PDU session is released | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3922 | 1 | F | Associate the MBS service area with the TMGI | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3950 | - | B | Using separate QoS flows dedicated for multicast | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3951 | 1 | B | Introducing the security aspects for MBS | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3952 | - | F | Removing UE from MBS session when the UE moves outside all the MBS service area(s) of that MBS session | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3953 | 2 | F | Including the reason of removing a joined UE from an MBS session by the network | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3954 | 1 | F | Correction to MBS service area | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3955 | 1 | F | Correction for NR CGI list in the MBS service area | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 3992 | 1 | F | MCC and MNC coding in Received MBS container IE | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 4028 | 1 | B | Remove UE from MBS session when the PDU session is released implicitly | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 4029 | - | B | UE MBS session local leave when the 3GPP access UP resources are released | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 4035 | 1 | F | UE locally leaves the MBS sessions locally when the PDU session is released locally | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 4072 | - | D | Moving the impact of inter-system change from N1 mode to S1 mode on MBS to the correct clauses | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 4073 | 1 | F | Correcting the type of the Requested MBS container IE and the Received MBS container IE to be type 6 | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 4075 | - | F | MBS inapplicability over non-3GPP access | 17.6.0 |
| 2022-03 | CT#95e | CP-220256 | 4076 | - | F | The impact of PDU session hand-over from 3GPP access to non-3GPP access on MBS sessions | 17.6.0 |
| 2022-03 | CT#95e | CP-220257 | 3870 | 3 | F | TAI configuration for non-3GPP access | 17.6.0 |
| 2022-03 | CT#95e | CP-220258 | 3919 | 1 | B | PDU session associating with PDU session pair ID and RSN | 17.6.0 |
| 2022-03 | CT#95e | CP-220258 | 3928 | 1 | F | Clarification in the NSAC for redundant PDU sessions | 17.6.0 |
| 2022-03 | CT#95e | CP-220258 | 3888 | 1 | F | End of disaster condition during an emergency PDU session | 17.6.0 |
| 2022-03 | CT#95e | CP-220258 | 3940 | 1 | B | AMF behaviors during the registration for disaster roaming | 17.6.0 |
| 2022-03 | CT#95e | CP-220260 | 4097 | - | F | Correction to usage of disaster return wait range | 17.6.0 |
| 2022-03 | CT#95e | CP-220260 | 4098 | - | F | Correction on disaster roaming information updating data | 17.6.0 |
| 2022-03 | CT#95e | CP-220260 | 4101 | - | F | Correction to disaster return wait range in Service reject message. | 17.6.0 |
| 2022-03 | CT#95e | CP-220260 | 4062 | 1 | F | Correction of IEI value of the Disaster return wait range IE | 17.6.0 |
| 2022-03 | CT#95e | CP-220260 | 3970 | 1 | B | PLMN with disaster condition IE as cleartext | 17.6.0 |
| 2022-03 | CT#95e | CP-220260 | 4067 | 1 | F | Clarifications on wait timer | 17.6.0 |
| 2022-03 | CT#95e | CP-220260 | 4066 | 1 | F | HPLMN control in roaming area | 17.6.0 |
| 2022-03 | CT#95e | CP-220260 | 3887 | 2 | F | Non supporting PLMN for disaster service | 17.6.0 |
| 2022-03 | CT#95e | CP-220261 | 3909 | 1 | F | Mismatch for MO SMS over NAS or MO SMSoIP service type criterion between TS23.122 and TS24.501 | 17.6.0 |
| 2022-03 | CT#95e | CP-220261 | 3941 | 1 | F | List indication not apply for secured packet | 17.6.0 |
| 2022-03 | CT#95e | CP-220261 | 3904 | 2 | F | High Priority PLMN search due to SOR | 17.6.0 |
| 2022-03 | CT#95e | CP-220261 | 3908 | 1 | F | De-registration handling due to Tsor-cm timer expiry | 17.6.0 |
| 2022-03 | CT#95e | CP-220261 | 4088 | 1 | F | Clarification on list indication with secured packet | 17.6.0 |
| 2022-03 | CT#95e | CP-220262 | 3944 | - | C | About the decision on eDRX parameters IE in AMF | 17.6.0 |
| 2022-03 | CT#95e | CP-220264 | 3974 | - | F | Remove Editor's Note in TS24.501 about RAN work on UPIP support for EPC | 17.6.0 |
| 2022-03 | CT#95e | CP-220265 | 3902 | - | F | Addition of NAS over Non-Terrestrial Network general clause text | 17.6.0 |
| 2022-03 | CT#95e | CP-220265 | 3975 | 1 | F | Applicability condition of the list of PLMNs not allowed to operate at the present UE location | 17.6.0 |
| 2022-03 | CT#95e | CP-220265 | 3998 | 1 | F | Storage and deletion of PLMNs not allowed to operate at the present UE location list | 17.6.0 |
| 2022-03 | CT#95e | CP-220265 | 4129 | 1 | C | Taking GNSS fix time into account in UE NAS layer | 17.6.0 |
| 2022-03 | CT#95e | CP-220265 | 3901 | 3 | B | Addition of extended NAS timers via a satellite NG-RAN cell - Alternative A | 17.6.0 |
| 2022-03 | CT#95e | CP-220265 | 4057 | 1 | F | Update the contents of an entry in the PLMN List for #78 | 17.6.0 |
| 2022-03 | CT#95e | CP-220265 | 4009 | 1 | F | Handling of PDU session modification not forwarded due to #78 | 17.6.0 |
| 2022-03 | CT#95e | CP-220282 | 4123 | 1 | B | Extension of SNN description for NSWO | 17.6.0 |
| 2022-03 | CT#95e | CP-220283 | 3896 | 3 | C | Paging Subgrouping updates in Registration and UE Configuration Update procedure | 17.6.0 |
| 2022-03 | CT#95e | CP-220283 | 4055 | 1 | F | Paging subgroup during emergency call | 17.6.0 |
| 2022-03 | CT#95e |  |  |  |  | Editorial correction in clause 5.3.25 | 17.6.1 |
| 2022-06 | CT#96 | CP-221195 | 4275 | 1 | A | SSC mode corrections | 17.7.0 |
| 2022-06 | CT#96 | CP-221189 | 4139 | 4 | F | Anonymous SUCI usage | 17.7.0 |
| 2022-06 | CT#96 | CP-221226 | 4255 | 2 | A | Indicating Supported SSC Mode(s) by the UE | 17.7.0 |
| 2022-06 | CT#96 | CP-221280 | 4190 | 4 | F | Correction on terminology and description for ID_UAS | 17.7.0 |
| 2022-06 | CT#96 | CP-221343 | 4327 | 3 | F | UE enter in substate NO-SUPI | 17.7.0 |
| 2022-06 | CT#96 | CP-221202 | 4199 | 5 | B | Network slice AS group - General aspects | 17.7.0 |
| 2022-06 | CT#96 | CP-221202 | 4292 | 1 | B | Support NSAG - Procedure Message and NSAG information IE coding | 17.7.0 |
| 2022-06 | CT#96 | CP-221202 | 4295 | 1 | B | Support NSAG in 5GMM capability | 17.7.0 |
| 2022-06 | CT#96 | CP-221202 | 4308 | 2 | B | NSAG information storage | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4166 | 2 | B | Onboarding SNPN and secondary authentication support | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4261 | 1 | F | list of configuration data | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4264 | - | F | PVS address providing correction | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4266 | 1 | F | Editor's note in subclause 9.11.3.51 | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4267 | 1 | F | AMF onboarding configuration data clean up | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4268 | 1 | F | S-NSSAI when URSP rule triggering establishment of PDU session was signalled by non-subscribed SNPN | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4285 | 1 | F | UE parameter update data set for ME routing indicator update data | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4286 |  | D | Editorial change : onboarding indicator | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4337 | 1 | F | No NSSAI provided to lower layer for onboarding service | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4368 | 1 | F | Usage of the onboarding SUCI | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4369 | - | F | Correction for the note about the UE policy sections stored for PLMNs or SNPNs | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4375 | 2 | F | Mapped S-NSSAI applicable for SNPN | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4421 | 1 | F | SUPI handling in case of CH using AAA server | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4422 | 1 | F | Storage of SNPN Forbidden List Across Power Cycle | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4257 | 1 | F | Correction of non-3GPP access in SNPN | 17.7.0 |
| 2022-06 | CT#96 | CP-221203 | 4424 | 2 | F | Storage of 5GMM parameters mapping with SUPI from USIM for AKA based SNPN | 17.7.0 |
| 2022-06 | CT#96 | CP-221204 | 4162 | - | F | Correction on session-AMBR for MA PDU session | 17.7.0 |
| 2022-06 | CT#96 | CP-221204 | 4234 | 3 | F | DEREGISTRATION handling for MA PDU session with PDN leg | 17.7.0 |
| 2022-06 | CT#96 | CP-221204 | 4354 | - | F | Clarification on PDU session establishment for MA PDU session | 17.7.0 |
| 2022-06 | CT#96 | CP-221205 | 4140 | - | F | Completing terminology clean up in 5GS | 17.7.0 |
| 2022-06 | CT#96 | CP-221205 | 4156 | 1 | F | Uplink data status handling for removing paging restriction in 5GS | 17.7.0 |
| 2022-06 | CT#96 | CP-221205 | 4157 | - | F | Uplink data status handling for NAS connection release | 17.7.0 |
| 2022-06 | CT#96 | CP-221205 | 4159 | 1 | F | The handling of paging cause in 5GS | 17.7.0 |
| 2022-06 | CT#96 | CP-221205 | 4160 | 1 | F | PEI handling for the MUSIM UE | 17.7.0 |
| 2022-06 | CT#96 | CP-221205 | 4229 | 1 | F | Correction for setting the Follow-on request indicator in abnormal cases for MUSIM UE in 5GS | 17.7.0 |
| 2022-06 | CT#96 | CP-221205 | 4230 | - | F | Referring to the correct terminology for the paging indication for voice services for MUSIM handling in 5GS | 17.7.0 |
| 2022-06 | CT#96 | CP-221205 | 4374 | 2 | F | UE no longer a MUSIM UE | 17.7.0 |
| 2022-06 | CT#96 | CP-221205 | 4427 | 1 | F | Clarification to MUSIM UEs operating in NB-N1 mode and WB-N1 CE mode B | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4144 | 1 | F | Alignment for NSAC for emergency and priority services | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4182 | 1 | F | Clarification on NSAC for SNPN onboarding | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4183 | 1 | F | Default subscribed S-NSSAI not subject to NSAC | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4184 | 1 | F | Clarification on condition of registration rejection | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4185 | - | F | Clarification on update of pending NSSAI if UE receives rejected NSSAI | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4187 | 1 | F | Addition of the NSSRG information in the Network slicing information | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4200 | 2 | F | Trigger to update configured NSSAI and NSSRG information | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4204 | - | F | The S-NSSAIs in an NSSAI associated with one or more common NSSRG values | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4238 | 3 | F | Clarification on the confliction between the NSSRG information IE and the Configured NSSAI IE | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4240 | 1 | F | Exemptions for the network slice data rate limitation control | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4241 | 1 | F | EAC mode is activated when the number of UEs associated with S-NSSAI reaches a certain threshold | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4242 | 1 | F | PDU sessions reactivation failure due to NSAC | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4334 | - | F | Manage NSSRG information over 3GPP access and non-3GPP access type | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4335 | 1 | F | Correcton on NSSRG information | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4363 |  | F | Differential backoff timer in NSAC | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4381 | - | F | NSSRG information value | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4382 | - | F | Incorrect statement subscribed S-NSSAI(s) marked as default subject to NSAC | 17.7.0 |
| 2022-06 | CT#96 | CP-221206 | 4383 | 1 | F | Extended rejected NSSAI IE mandatory support | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 3866 | 5 | F | Correction of procedures providing UUAA authorization payload | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4168 | - | F | Correction to the Service-level-AA container IEI value | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4173 |  | F | Correction on DL NAS TRANSFER for UUAA procedure | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4174 | 4 | F | Completion of service-level-AA procedure | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4175 | 1 | F | USS FQDN as service-level-AA server address | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4177 | - | F | Correction on UUAA-MM handling at AMF | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4178 | 1 | F | UUAA-MM failure delivery | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4179 | - | F | Retry restriction for 5GSM cause #86 | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4180 | - | F | Parameters in Service-level-AA container IE are not standalone IE | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4191 | 2 | F | Resolving editor's note for ID_UAS | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4192 | 1 | F | Correction of the condition when the network initiates de-registration | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4252 | - | F | Correction of the definition of UE supporting UAS services | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4367 | 1 | F | Editorial correction | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4387 | 1 | F | Clarification on service level AA procedure for NI PDU modification | 17.7.0 |
| 2022-06 | CT#96 | CP-221208 | 4405 | - | F | Handling of EMM parameters on getting #79 in SRM | 17.7.0 |
| 2022-06 | CT#96 | CP-221209 | 4262 | - | F | IE coded as 'comprehension required' | 17.7.0 |
| 2022-06 | CT#96 | CP-221209 | 4316 | 1 | F | Interaction between 5GSM entity and upper layers with respect to the ProSeP | 17.7.0 |
| 2022-06 | CT#96 | CP-221209 | 4317 | - | F | A few cleanups on 5G ProSe | 17.7.0 |
| 2022-06 | CT#96 | CP-221209 | 4318 | 1 | B | The timer for authentication and key agreement for 5G ProSe UE-to-network relay | 17.7.0 |
| 2022-06 | CT#96 | CP-221209 | 4360 | - | F | Invalid PDU session identity in Remote UE Report message | 17.7.0 |
| 2022-06 | CT#96 | CP-221209 | 4365 | 1 | B | Secondary authentication via L3 relay | 17.7.0 |
| 2022-06 | CT#96 | CP-221210 | 4219 | 3 | B | Authentication and key agreement for 5G ProSe UE-to-network relay | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4280 | - | F | Correction on UE 5GMM state for 5GMM cause #76 | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4281 | - | F | Correction on AMF handling on PDU session release | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4282 | - | F | Correction on RRC resume indication at AMF | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4289 | - | F | Correction to PDU session type | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4299 | - | F | Taking into account information from the NG-RAN when determining the Paging subgroup ID | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4301 | 1 | F | Conditions for an inactive UE to request the lower layers to transition to the connected mode | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4269 | - | F | Skipping access control checking for NAS signalling connection recovery after IRAT change from LTE to NR | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4311 | - | F | Condition of including new configured NSSAI in Registration Accept message | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4312 | - | F | Simplify enumeration of all kinds of rejected NSSAI | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4325 | - | F | Removing the obsolete description of C1-211443 | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4330 | - | F | Correction on 5GMM deregistration state for CC #62 and #79 | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4338 | - | F | Correction on Extended rejected NSSAI IE | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4341 | - | F | Coordination between 5GMM and EMM state | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4343 | - | F | Perform deregistration procedure in 5GMM- REGISTERED state | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4352 | - | F | Clarification on CPSR procedure and minor correction | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4353 | - | F | Correction on session-AMBR during the PDU session establishment | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4356 | - | F | Storing Allowed NSSAIs for EPLMNs during registration | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4371 | - | D | Wording correction for the UE policy classmark | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4377 | - | F | N1 NAS signalling Connection maintenance for abnormal cases and PLMN selection | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4378 | - | F | Start T3540 when non-switch-off de-registration procedure complete | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4379 | - | F | Clarification for Semantic error in the mapped EPS bearer | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4390 | - | F | Clarification of UE initiated PDU procedure and NAS signalling connection release | 17.7.0 |
| 2022-06 | CT#96 | CP-221211 | 4259 | 1 | F | Correction of duplicated info in the Generic UE Configuration Update procedure | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4251 | 1 | F | Correction of the condition that the UE removes the pending NSSAI | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4294 | 1 | F | Clarification on the update of allowed NSSAI | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4300 | 1 | F | Note on the default configured NSSAI | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4302 | 1 | F | Emergency registration without allowed NSSAI | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4320 | 1 | D | Delete repeat description | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4321 | 1 | F | Scenarios to stop T3526 | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4322 | 1 | F | QoS error checks for unstructured PDU session type in PCO | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4324 | 1 | F | Missing state when disabling N1 mode for 3GPP access | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4329 | 1 | F | Perform eCall inactivity procedure in 5GMM-REGISTERED.NON-ALLOWED-SERVICE substate | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4331 | 1 | F | No need to include Uplink data status IE in periodic registration message | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4344 | 1 | F | Correction on trigger to initiate registration procedure | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4347 | 1 | F | Correction on the IE coding | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4366 | 2 | F | UE delete NAS security context only when not be used | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4385 | 1 | F | Use of definition default S-NSSAI | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4414 | 1 | F | Length information correction of 5GS update type IE | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4357 | 1 | F | Abnormal cases in Registration procedure for handling Paging subgroup ID | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4358 | 1 | F | Abnormal cases in Generic UE configuration update procedure for handling Paging subgroup ID | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4359 | 1 | F | Deleting PEIPS assistance information on Registration procedure failure | 17.7.0 |
| 2022-06 | CT#96 | CP-221212 | 4256 | 1 | F | Mismatch of the Legth Indicators between two similar IEs | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4284 | 1 | F | Correction on UE handling on extended local emergency numbers list via non-3GPP access | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4309 | 1 | F | Network slicing features applicable in SNPN | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4313 | 1 | D | Editorial corrections | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4323 | 1 | F | Correction on using T3540 | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4326 | 1 | F | Clarification on UE action for not forwarded 5GSM message | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4345 | 1 | F | Correction on access category about MO IMS registration related signalling | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4348 | 2 | F | Support MAC address range in packet filter | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4350 | 1 | F | The handling of establishing an emergency PDU session after WUS negotiation in 5GS | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4351 | 1 | F | Correction on the WUS assistance information | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4376 | 1 | F | Indication for no 5GMM or 5GSM messages to the lower layers | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4380 | 1 | F | Handling of multiple TAGs in the Ethernet header for signalled and derived QoS rules | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4388 | 1 | F | Correction to TFT check for PDU session establishment procedure | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4389 | 1 | F | Correction to TFT check for PDU session modification procedure | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4391 | 2 | F | Clarification of Release of non-emergency PDU sessions | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4392 | 1 | F | Clarification of UE configuration parameter updates | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4393 | 1 | F | Clarification of handlings of 5GMM cause #65 maximum number of PDU sessions reached for SNPN | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4394 | 1 | F | Storage of NSSAI | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4395 | 1 | D | Editorial corrections | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 4399 | 1 | D | Editorial correction to operation codes | 17.7.0 |
| 2022-06 | CT#96 | CP-221213 | 3497 | 6 | F | NSSAI mapping during transfer of PDU session from HPLMN to VPLMN & VPLMN to HPLMN | 17.7.0 |
| 2022-06 | CT#96 | CP-221214 | 4431 | 1 | B | Support of provisioning ECS configuration info per ECSP | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4163 | 1 | F | Correction on MBS service area indication | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4167 | - | F | Correction to the Requested MBS container and the Received MBS container IEI values | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4225 | 1 | F | Updating the MBS service area of MBS multicast session using MBS Service Announcement | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4226 | 1 | F | Corrections related to MBS multicast sessions | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4227 | - | F | Delivering multiple MBS service areas to the UE for Location dependent MBS service | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4228 | 1 | F | Applicability of security protection for MBS session | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4235 | 1 | F | Deregistration procedure impacts for MBS session | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4236 | 1 | B | MBS backoff timer in PDU SESSION ESTABLISHMENT ACCEPT message | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4270 | 1 | F | Maximum number of associated MBS sessions | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4396 | 1 | F | Correction to MBS service area indication | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4397 | 1 | D | Minor editorial | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4406 | 1 | F | Removing the EN related to the maximum lengths of the Received MBS container IE | 17.7.0 |
| 2022-06 | CT#96 | CP-221218 | 4407 | 1 | F | Correcting the implementation of MBS containers IEs lengths in the spec | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4141 | 1 | F | MS determined PLMN with disaster condition and broadcasting disaster related indication | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4149 | 1 | F | Cause code for MINT | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4170 | 3 | F | Resolution of Editor's note on handling of the indication of whether disaster roaming is enabled in the UE and the indication of 'applicability of lists of PLMN(s) to be used in disaster condition provided by a VPLMN' | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4209 | 1 | F | Trigger of UE-initiated de-registration procedure | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4223 | 1 | F | Clarification on DREI. | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4233 | 2 | F | Clarify that S1 mode is not supported for MINT | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4243 | - | F | Correct on List of PLMNs to be used in disaster condition list IEI | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4265 | 1 | F | Editor's notes in subclause 5.4.4.1 and subclause 5.4.4.2 | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4349 | 2 | F | Emergency PDU session while the timer for disaster roaming wait range is running | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4361 | - | F | Non-emergency PDU sessions are not transferable to EPS during disaster roaming | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4384 | 1 | F | Storage of List of PLMNs to be used in disaster condition to NVM | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4411 | - | F | Resolution of editors note for registration type | 17.7.0 |
| 2022-06 | CT#96 | CP-221219 | 4413 | 1 | F | Handling of EMM parameters on getting #80 | 17.7.0 |
| 2022-06 | CT#96 | CP-221223 | 4340 | 1 | D | Correction on CAG information list format | 17.7.0 |
| 2022-06 | CT#96 | CP-221223 | 4362 | 1 | B | SDT support | 17.7.0 |
| 2022-06 | CT#96 | CP-221223 | 4409 | - | D | Aligning the terminologies of signalling messages | 17.7.0 |
| 2022-06 | CT#96 | CP-221223 | 4410 | 1 | F | Clarification for the encoding of MCC and MNC parameters in TS 24.501 | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 3588 | 11 | B | Multiple TACs from the lower layers | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4148 | - | C | Removal of the indication of the country of UE location | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4152 | 3 | C | Update the description on the lists of 5GS forbidden tracking areas | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4165 | 1 | B | Definition of last visited registered TAI for 5GSat | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4194 | - | F | Correction in the applicability of 5GMM cause value #78 | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4195 | 1 | F | Correction on the note on GNSS fix time | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4272 | - | B | Addition of lower bound IEs for #78, alt 2 | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4305 | - | F | Correction in the AMF operation to determine forbidden TAIs | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4306 | 1 | F | Forbidden TAIs delivered to a UE during a successful MRU and SR procedures | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4372 | 1 | F | Clarification on emergency service intiation via the PLMN which is not allowed to operate at the present UE location | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4401 | 1 | F | Handling of EMM parameters on getting #78 | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 4404 | - | F | Handling of PDU session release request not forwarded due to #78 | 17.7.0 |
| 2022-06 | CT#96 | CP-221224 | 3976 | 7 | C | Forbidden TAI handling in case of multiple TACs | 17.7.0 |
| 2022-06 | CT#96 | CP-221227 | 4433 | 1 | B | Support of MC slicing configuration as part of UE local configuration | 17.7.0 |
| 2022-06 | CT#96 | CP-221241 | 4231 | - | F | The remote UE report procedure is initiated by a 5G ProSe layer-3 UE-to-network relay UE | 17.7.0 |
| 2022-06 | CT#96 | CP-221242 | 4221 | 1 | F | UE-requested PDU session establishment procedure based on ProSeP | 17.7.0 |
| 2022-06 | CT#96 | CP-221245 | 4150 | 1 | C | Considering eDRX parameter in the USIM | 17.7.0 |
| 2022-06 | CT#96 | CP-221249 | 4135 | 1 | B | UE required to not accept URSP signalled by non-subscribed SNPNs | 17.7.0 |
| 2022-06 | CT#96 | CP-221249 | 4137 | 1 | F | Editor's note in subclause 5.5.1.3.4 | 17.7.0 |
| 2022-06 | CT#96 | CP-221249 | 4138 | - | F | Access identities when UE accesses SNPN using PLMN subscription | 17.7.0 |
| 2022-06 | CT#96 | CP-221249 | 4171 | 1 | F | Signalling UE support for SOR-SNPN-SI in SOR ACK | 17.7.0 |
| 2022-06 | CT#96 | CP-221249 | 4186 | 1 | F | Support of mapped S-NSSAI in SNPN | 17.7.0 |
| 2022-06 | CT#96 | CP-221249 | 4196 | - | F | ON-SNPN: Correction in the operation of a UE entering the 5GMM-DEREGISTERED.PLMN-SEARCH state | 17.7.0 |
| 2022-06 | CT#96 | CP-221249 | 4202 | -1 | F | NSSAA performed for a UE operating in SNPN access operation mode | 17.7.0 |
| 2022-06 | CT#96 | CP-221249 | 4203 | 2 | F | Clarification of ProSe support in NPN | 17.7.0 |
| 2022-06 | CT#96 | CP-221249 | 4208 | 1 | F | URSP rules for SNPN | 17.7.0 |
| 2022-06 | CT#96 | CP-221249 | 4213 | - | F | Correction of definition given in TS 23.501 about GIN | 17.7.0 |
| 2022-06 | CT#96 | CP-221256 | 4145 | 1 | F | UCU for MPS | 17.7.0 |
| 2022-06 | CT#96 | CP-221257 | 3927 | 4 | B | Access category assignment for an access attempt occurred due to call pull | 17.7.0 |
| 2022-06 | CT#96 | CP-221258 | 4218 | 1 | F | Clarification on lists of 5GS forbidden tracking areas over non-3GPP access | 17.7.0 |
| 2022-06 | CT#96 |  |  |  |  | Some IEI values assigned by the rapporteur of the TS | 17.7.1 |
| 2022-09 | CT#97e | CP-222137 | 4442 | 1 | F | Correction for default UE credentials | 17.8.0 |
| 2022-09 | CT#97e | CP-222137 | 4444 | - | F | PVS addresses for NSSAA not associated with DNN | 17.8.0 |
| 2022-09 | CT#97e | CP-222137 | 4445 | 1 | F | Precedence between PVS addresses or PVS names | 17.8.0 |
| 2022-09 | CT#97e | CP-222137 | 4446 | 1 | F | Alignment with SA3 on 5G AKA and EAP-AKA' based primary authentication and key agreement procedure used for onboarding services in SNPN | 17.8.0 |
| 2022-09 | CT#97e | CP-222137 | 4548 | 1 | F | Put the NOTE about network slice used for onboarding under correponding bullet | 17.8.0 |
| 2022-09 | CT#97e | CP-222137 | 4549 | 1 | F | PVS information in SMF | 17.8.0 |
| 2022-09 | CT#97e | CP-222137 | 4557 | - | F | HPLMN S-NSSAI in case of SNPN | 17.8.0 |
| 2022-09 | CT#97e | CP-222137 | 4620 | 1 | F | Resolving EN on KSEAF derivation indicator in USIM | 17.8.0 |
| 2022-09 | CT#97e | CP-222137 | 4636 | 1 | F | Storage and access of 5GMM parameters mapping with SUPI from USIM for AKA based SNPN | 17.8.0 |
| 2022-09 | CT#97e | CP-222139 | 4538 | 1 | F | The RAN paging handling for MUSIM UE in 5GS | 17.8.0 |
| 2022-09 | CT#97e | CP-222139 | 4613 | - | F | Harmonization for the paging restriction terminology for MUSIM UE | 17.8.0 |
| 2022-09 | CT#97e | CP-222139 | 4619 | 1 | F | Rejection of paging correction | 17.8.0 |
| 2022-09 | CT#97e | CP-222140 | 4495 | 1 | F | Additional parameter with generic UE configuration update procedure | 17.8.0 |
| 2022-09 | CT#97e | CP-222140 | 4499 | 1 | F | NSSRG and allowed NSSAI for the other access | 17.8.0 |
| 2022-09 | CT#97e | CP-222140 | 4525 | 1 | F | Provide new NSSRG information to UE | 17.8.0 |
| 2022-09 | CT#97e | CP-222140 | 4566 | 2 | F | Associate NSSRG values with HPLMN S-NSSAI | 17.8.0 |
| 2022-09 | CT#97e | CP-222140 | 4596 | 1 | F | Correction on the rejected NSSAI due to maximum number of UEs reached | 17.8.0 |
| 2022-09 | CT#97e | CP-222143 | 4591 | - | F | Service-level-AA timer name correction | 17.8.0 |
| 2022-09 | CT#97e | CP-222143 | 4598 | 1 | F | Correction on Service-level-AA container IEI | 17.8.0 |
| 2022-09 | CT#97e | CP-222144 | 4456 | - | F | Add ProSeP request in UAC | 17.8.0 |
| 2022-09 | CT#97e | CP-222144 | 4458 | - | F | Use the term 5G ProSe | 17.8.0 |
| 2022-09 | CT#97e | CP-222145 | 4448 | 1 | F | Remote UE IP info of REMOTE UE REPORT for IPv4 | 17.8.0 |
| 2022-09 | CT#97e | CP-222145 | 4455 | 1 | F | UAC not applied to L2 relay | 17.8.0 |
| 2022-09 | CT#97e | CP-222145 | 4457 | 1 | C | Remove secondary authentication for U2N relay | 17.8.0 |
| 2022-09 | CT#97e | CP-222145 | 4487 | 1 | F | Clarification on the expiry of T3586 timer | 17.8.0 |
| 2022-09 | CT#97e | CP-222145 | 4514 | 1 | F | Correction to timer T35xx | 17.8.0 |
| 2022-09 | CT#97e | CP-222146 | 4553 | 1 | F | Providing HPLMN ID together with PRUK ID in 64-bit string format | 17.8.0 |
| 2022-09 | CT#97e | CP-222146 | 4614 | 1 | F | Resolving the ENs related to the UE Identities used in the Remote UE report procedure | 17.8.0 |
| 2022-09 | CT#97e | CP-222146 | 4615 | 1 | F | Some corrections related to the Relay Key Request procedure | 17.8.0 |
| 2022-09 | CT#97e | CP-222146 | 4616 | 1 | B | Introducing the 5GPRUK ID in the Relay key Request procedure | 17.8.0 |
| 2022-09 | CT#97e | CP-222146 | 4617 | 1 | F | ProSe relay transaction identity as a type 3 IE | 17.8.0 |
| 2022-09 | CT#97e | CP-222146 | 4639 | 2 | F | Setting RRC establishment cause value when relay UE has its own service | 17.8.0 |
| 2022-09 | CT#97e | CP-222147 | 4501 | 1 | C | New 5QI values to support Advance Interactive Services (AIS) in 5G | 17.8.0 |
| 2022-09 | CT#97e | CP-222147 | 4542 | 1 | F | Correction on serving PLMN rate control | 17.8.0 |
| 2022-09 | CT#97e | CP-222148 | 4482 | 2 | F | Correction to ECS Address Provisioning | 17.8.0 |
| 2022-09 | CT#97e | CP-222148 | 4492 | - | F | Clarification on indicating the EDC support to network | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4491 | 1 | F | Handling of the MBS multicast session on local release of PDU session | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4568 | 1 | F | Providing TMGI to lower layer for paging | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4582 | 1 | F | MBS session maintenance when releasing user-plane resources of a MA PDU session | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4583 | 1 | F | MBS back-off timer for IP address | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4584 | 1 | F | Clarification on the determination of outside the MBS service area | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4585 | 1 | F | PDU session status IE handling for MBS session | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4586 | - | F | MBS session maintenance after handover | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4587 | 1 | F | Request to join MBS session during establishment procedure | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4607 | - | F | Delivering list of keys in MBS Security container | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4609 | - | F | Correction for the condition of including the Security container in the Received MBS container IE | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4610 | 1 | F | MBS Security keys update to the UE | 17.8.0 |
| 2022-09 | CT#97e | CP-222151 | 4621 | 1 | F | Correction to timers of multicast/broadcast services | 17.8.0 |
| 2022-09 | CT#97e | CP-222152 | 4440 | - | F | Errors in PLMN ID IE | 17.8.0 |
| 2022-09 | CT#97e | CP-222155 | 4641 | - | F | Addition of the length value of the Negotiated eDRX parameters IE | 17.8.0 |
| 2022-09 | CT#97e | CP-222156 | 4534 | 1 | F | Add satellite E-UTRAN as an UE supported access technology | 17.8.0 |
| 2022-09 | CT#97e | CP-222158 | 4450 | 1 | F | Clarification that the NSAG information can not be sent with a request to perform the registration procedure | 17.8.0 |
| 2022-09 | CT#97e | CP-222158 | 4452 | 1 | F | Clarification that the NSAG information is sent over 3GPP aceess only | 17.8.0 |
| 2022-09 | CT#97e | CP-222158 | 4471 | 1 | F | Indicating the deletion or invalidation of the NSAG information to lower layers | 17.8.0 |
| 2022-09 | CT#97e | CP-222158 | 4483 | 1 | F | Support NSAG for SNPN | 17.8.0 |
| 2022-09 | CT#97e | CP-222158 | 4484 | 1 | F | NSAG priority | 17.8.0 |
| 2022-09 | CT#97e | CP-222158 | 4560 | 1 | F | IEI assignment for the NSAG information IE | 17.8.0 |
| 2022-09 | CT#97e | CP-222159 | 4469 | 1 | F | The consideration of avoiding unnecessary TAI change | 17.8.0 |
| 2022-09 | CT#97e | CP-222159 | 4475 | 1 | F | Extended NAS timers based on satellite NG-RAN RAT type | 17.8.0 |
| 2022-09 | CT#97e | CP-222159 | 4476 | 1 | F | Alignment of terminology in current TAI definition | 17.8.0 |
| 2022-09 | CT#97e | CP-222159 | 4533 | - | F | Suggest simplifying the selection for the current TAI | 17.8.0 |
| 2022-09 | CT#97e | CP-222159 | 4535 | 1 | F | Update of conditions for deleting entries in # 78 list | 17.8.0 |
| 2022-09 | CT#97e | CP-222159 | 4556 | 1 | F | Current TAI | 17.8.0 |
| 2022-09 | CT#97e | CP-222159 | 4624 | 2 | F | Clarification on handling related to #78 | 17.8.0 |
| 2022-09 | CT#97e | CP-222159 | 4625 | 2 | F | Clarification on timer instance associated with the entry | 17.8.0 |
| 2022-09 | CT#97e | CP-222163 | 4498 | 1 | F | MPS exemption in Attempting to reRegister | 17.8.0 |
| 2022-09 | CT#97e | CP-222163 | 4518 | 1 | F | MPS exemption in Attempting to Register | 17.8.0 |
| 2022-09 | CT#97e | CP-222168 | 4526 | 1 | F | Condition of returning REGISTRATION COMPLETE by UE | 17.8.0 |
| 2022-09 | CT#97e | CP-222147 | 4447 | 1 | F | Correcting minor issues in TS 24.501 | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4460 | 1 | F | Check the match-all packet filter in QoS rule | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4461 | 1 | F | Missing EPS-UPIP bit in the S1 UE network capability IE of the mobility and periodic REGISTRATION REQUEST | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4462 | 1 | F | QoS error checks for unstructured PDU session type in PCO | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4463 | 1 | F | Add back off timer handling for rejected nssai for max UE reached for MT Deregistration procedure with cause #62. | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4478 | - | F | Clarification of UE paging probability information value | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4481 | - | F | Clarification of IWK N26 bit when received in non-3GPP access | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4489 | - | F | Correction to QoS rule error checking operation. | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4497 | 1 | F | Service gap control correction | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4510 | 1 | F | Correcting a NOTE | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4551 | 1 | F | Clarification of interworking between N1 mode over non-3GPP access and ePDG | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4552 | 1 | F | T3540 handling upon receipt of 5GMM common procedure | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4554 | - | F | ODAC decision for a UE is in state 5GMM-REGISTERED.ATTEMPTING-REGISTRATION-UPDATE | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4571 | - | F | Registration attempt counter reset for successful TAU | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4572 | - | F | Correction to 5GMM-Deregistration attempting registration state | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4589 | 1 | F | Clarification when authentication fails | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4605 | - | F | Handling the DRX parameter on the AMF side | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4611 | - | F | Adding missing abbreviation and other corrections | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4626 | 1 | F | At least one default subscribed S-NSSAI in user subscription | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4628 | 1 | F | Handling when FPLMN is declared allowable PLMN by network | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4523 | 1 | F | Abnormal cases in Registration procedure for handling WUS assistance information | 18.0.0 |
| 2022-09 | CT#97e | CP-222167 | 4524 | 1 | F | Deleting WUS assistance information on Registration procedure failure | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4451 | 1 | D | Editorial corrections to TS 24.501 | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4468 | 1 | F | Precluding inclusion of both a destination (resp. source) MAC address type and a destination (resp. source) MAC address range type packet filter components in a packet filter | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4473 | 2 | F | Correction to the 5GMM capability IE | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4479 | 1 | F | Clarification of 5GS registration result value handling | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4480 | 1 | F | MPS and MCS indicators for 3GPP and non-3GPP accesses | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4500 | 2 | F | 5GSM coordination: UE behaviour in case of missing EPS bearer parameters | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4527 | 1 | F | Storage of NSSAI for EPLMNs in updated registration area | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4528 | 1 | F | Handling of re-NSSAA or network slice-specific authorization revocation result | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4529 | 1 | F | Alignment of term re-NSSAA | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4531 | 1 | F | UE behavior after receiving registration requested in CUC message | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4532 | 1 | D | Editorial corrections | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4564 | 3 | F | No NSSAI provided to lower layer for SERVICE REQUEST message | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4574 | 1 | F | Corrections related to cause value #78 PLMN not allowed to operate at the present UE location | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4580 | 1 | F | Access handling when stopping T3585 | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4593 | 1 | F | Correction on UE handling on syntactical errors in QoS operations | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4594 | 1 | F | Covering a missing semantic errors in QoS operations | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4595 | 1 | F | UE handling on local emergency numbers | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4604 | 1 | F | Correction on disabling the N1 mode capability when all S-NSSAI was rejected | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4612 | 1 | F | Corrections for UE behaviour upon receiving CONFIGURATION UPDATE COMMAND message that indicates registration requested | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4519 | 1 | F | Registering slices removed from rejected NSSAI list | 18.0.0 |
| 2022-09 | CT#97e | CP-222168 | 4520 | 2 | F | Including S-NSSAIs received in S1 mode in configured NSSAI | 18.0.0 |
| 2022-09 | CT#97e |  |  |  |  | Editorial correction done by MCC | 18.0.1 |
| 2022-12 | CT#98e | CP-223158 | 4304 | 2 | F | Abnormal cases for the SMC initiated for context synchronization between 3GPP access and non-3GPP access | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4502 | 4 | F | Cause #62 handling in case of "S-NSSAI not available in the current registration area" | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4506 | 3 | F | Using UE local configuration for default DNN and S-NSSAI | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4579 | 2 | F | Clarification on the SD value in Rejected NSSAI | 18.1.0 |
| 2022-12 | CT#98e | CP-223122 | 4642 | 2 | A | Editor's note in 6.4.1.2 | 18.1.0 |
| 2022-12 | CT#98e | CP-223122 | 4643 | 2 | A | Editor's note in subclause 5.3.2 | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4644 | 3 | D | Re-use of S-NSSAI after removal of S-NSSAI from rejected NSSAI. | 18.1.0 |
| 2022-12 | CT#98e | CP-223136 | 4652 | 1 | A | Correction to the NSAG priority field reference | 18.1.0 |
| 2022-12 | CT#98e | CP-223116 | 4654 | 1 | A | Correction to PDU session types | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4656 | 1 | F | Added further clarification in handling of T3502, T3346 in SNPN. | 18.1.0 |
| 2022-12 | CT#98e | CP-223116 | 4658 | 2 | A | Correction to the CONFIGURATION UPDATE COMMAND message | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4660 | 1 | F | Clarification on packet filter in signalled QoS rule | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4661 |  | F | Correction to the PDU session modification for LADN | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4662 |  | F | Correction to QoS rules IE | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4663 | 1 | F | Correction to default NSSAI inclusion mode | 18.1.0 |
| 2022-12 | CT#98e | CP-223127 | 4664 | 2 | F | Error handling to PTI | 18.1.0 |
| 2022-12 | CT#98e | CP-223136 | 4666 |  | A | Correction to NSAG default area | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4669 | 1 | F | Abnormal case handling | 18.1.0 |
| 2022-12 | CT#98e | CP-223133 | 4671 | 1 | A | Correction to name of List of PLMNs offering disaster roaming services | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4672 | 1 | F | Max limit for NSSRG values per S-NSSAI | 18.1.0 |
| 2022-12 | CT#98e | CP-223144 | 4673 | 1 | D | Editorial Corrections | 18.1.0 |
| 2022-12 | CT#98e | CP-223136 | 4679 | 1 | A | Maximum and minimum length of NSAG information IE | 18.1.0 |
| 2022-12 | CT#98e | CP-223136 | 4681 | 1 | A | Maximum number of TAI list restriction for NSAG | 18.1.0 |
| 2022-12 | CT#98e | CP-223136 | 4683 | 1 | A | NSAG priority handling at the AMF | 18.1.0 |
| 2022-12 | CT#98e | CP-223136 | 4685 | 1 | A | Correction on NSAG information handling | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4686 |  | F | Correction on identical QFIs semantic errors in QoS operations | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4687 |  | F | Correction on identical QRIs semantic errors in QoS operations | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4688 | 1 | F | Exemption of 5GS update status removal for causes #3, #6 and #7 | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4689 |  | F | Mapped dedicated EPS bearer without default EPS bearer in the establishment procedure | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4692 |  | F | Update the description on the subscribed SNPN | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4694 |  | D | Remove duplicated context | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4695 |  | F | Correct the message for joining multicast session | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4696 | 1 | F | Correction on semantic error about UL PF of TFT | 18.1.0 |
| 2022-12 | CT#98e | CP-223136 | 4702 | 5 | A | NAS operation for network slice-based random access | 18.1.0 |
| 2022-12 | CT#98e | CP-223148 | 4704 | 1 | A | Corrections on UE-initiated authentication and key agreement procedure | 18.1.0 |
| 2022-12 | CT#98e | CP-223121 | 4706 | 1 | A | Registration update triggered by NSSRG update in UCU procedure | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4708 | 1 | F | NSSRG restriction applicability for the other access type | 18.1.0 |
| 2022-12 | CT#98e | CP-223121 | 4710 | 2 | F | UE behaviour when receiving cause #62 with rejected NSSAI for maximum number of UEs reached | 18.1.0 |
| 2022-12 | CT#98e | CP-223136 | 4712 | 1 | A | NSAG information provision over 3GPP access only | 18.1.0 |
| 2022-12 | CT#98e | CP-223101 | 4713 | 2 | F | Clarification on equivalent PLMN applicability | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4714 |  | Fa | Clarification on condition of sending 5GMM cause #62 | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4715 | 1 | F | Condition of including equivalent PLMNs in Registration Accept message | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4717 | 1 | F | EAP-TTLS used between the UE and the DCS | 18.1.0 |
| 2022-12 | CT#98e | CP-223148 | 4719 | 1 | A | Initiation of authentication and key agreement procedure for 5G ProSe U2N relay UE in NORMAL-SERVICE state | 18.1.0 |
| 2022-12 | CT#98e | CP-223127 | 4721 |  | A | Correction on USS FQDN | 18.1.0 |
| 2022-12 | CT#98e | CP-223127 | 4723 | 1 | A | Clarification on authorization of UAV flight | 18.1.0 |
| 2022-12 | CT#98e | CP-223158 | 4724 | 3 | F | Correction for CIoT data not forwarded from a CPSR message | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4726 | 1 | F | Clarification on initiating registration procedure when timer T3512 expires | 18.1.0 |
| 2022-12 | CT#98e | CP-223116 | 4728 |  | A | Correction on single-registration subclause | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4729 | 1 | F | Alignment for the emergency registered bit of the 5GS registration result IE | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4730 |  | F | Alignment of the abbreviation NITZ | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4731 |  | F | Clarification on UE supporting S1 mode | 18.1.0 |
| 2022-12 | CT#98e | CP-223117 | 4734 | 1 | A | Alignment of terminology on multicast MBS session | 18.1.0 |
| 2022-12 | CT#98e | CP-223117 | 4736 |  | A | Correction on handling of the MBS multicast session | 18.1.0 |
| 2022-12 | CT#98e | CP-223117 | 4738 |  | A | Handling of the MBS multicast sessions when the PDU session is locally released | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4739 |  | F | Correction on S1 UE network capability IE | 18.1.0 |
| 2022-12 | CT#98e | CP-223144 | 4740 | 1 | F | Correction on WUS handling in 5GS | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4741 | 2 | F | MUSIM features considered not used when the UE’s normal registration changes to registered for emergency services | 18.1.0 |
| 2022-12 | CT#98e | CP-223148 | 4744 | 1 | A | Rename 5GPRUK ID and 5GPRUK in CP based solution and rename PRUK and PRUK ID in UP based solution | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4747 | 1 | F | NSSAA and SR procedure collision handling | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4749 |  | F | Providing NSSRG information to the lower layers | 18.1.0 |
| 2022-12 | CT#98e | CP-223127 | 4751 | 1 | A | Correction on unused value of payload type | 18.1.0 |
| 2022-12 | CT#98e | CP-223116 | 4757 | 3 | A | Mapped S-NSSAI when UE is roaming | 18.1.0 |
| 2022-12 | CT#98e | CP-223116 | 4759 | 2 | A | Addition of UE requested T3512 value at MICO | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4760 | 1 | F | Treating an MRU as an initial registration when UE identity cannot be derived | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4761 |  | F | Clarification on the S-NSSAIs included in the rejected NSSAI of the REGISTRATION REJECT message | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4765 | 1 | B | Access Category and establishment cause for the MT call and the MT SMSoIP | 18.1.0 |
| 2022-12 | CT#98e | CP-223117 | 4766 | 1 | A | MBS address information type in the received MBS information | 18.1.0 |
| 2022-12 | CT#98e | CP-223148 | 4776 | 2 | A | Including TCP/UDP port ranges in REMOTE UE REPORT | 18.1.0 |
| 2022-12 | CT#98e | CP-223135 | 4778 | 2 | F | MUSIM UE and PEI | 18.1.0 |
| 2022-12 | CT#98e | CP-223135 | 4779 | 1 | F | MUSIM and notification message over non-3GPP access | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4783 |  | F | Addition of missing maximum size for Default configured NSSAI | 18.1.0 |
| 2022-12 | CT#98e | CP-223148 | 4788 | 1 | A | Mandatory inclusion of 5GPRUK ID in the RELAY KEY ACCEPT message | 18.1.0 |
| 2022-12 | CT#98e | CP-223148 | 4790 | 1 | A | Correcting the reference for the PRTI | 18.1.0 |
| 2022-12 | CT#98e | CP-223144 | 4791 |  | F | Adding ANDSP to abbreviations | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4796 | 1 | F | CAG restrictions is not applied to emergency services fallback | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4798 | 1 | F | Correction on UE behavior about rejected NSSAI | 18.1.0 |
| 2022-12 | CT#98e | CP-223135 | 4804 | 1 | A | Paging rejection in RRC inactive | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4806 | 1 | F | Correction on Emergency PDU Sessions | 18.1.0 |
| 2022-12 | CT#98e | CP-223121 | 4807 | 1 | A | Remove redundant content about NSSRG information R18 | 18.1.0 |
| 2022-12 | CT#98e | CP-223117 | 4810 | 1 | A | Indicate to lower layer to delete stored TMGI R18 | 18.1.0 |
| 2022-12 | CT#98e | CP-223122 | 4813 | 2 | A | Clarification on providing SOR-CMCI in SNPN access operation mode R18 | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4816 |  | F | UE DS-TT Residence time | 18.1.0 |
| 2022-12 | CT#98e | CP-223144 | 4827 |  | F | 5GC MPS exemption for non-congestion back-off | 18.1.0 |
| 2022-12 | CT#98e | CP-223116 | 4829 | 1 | A | Correction of implementation error of CR4124 | 18.1.0 |
| 2022-12 | CT#98e | CP-223148 | 4831 | 1 | A | Correction of implementation error of CR4615 | 18.1.0 |
| 2022-12 | CT#98e | CP-223133 | 4833 |  | A | Allowed access attempts while timer precluding registration is running in 24.501 | 18.1.0 |
| 2022-12 | CT#98e | CP-223120 | 4834 | 2 | B | Providing Equivalent SNPNs | 18.1.0 |
| 2022-12 | CT#98e | CP-223120 | 4835 | 2 | B | Providing registered SNPNs | 18.1.0 |
| 2022-12 | CT#98e | CP-223120 | 4836 |  | B | Equivalent SNPNs usage for mobility | 18.1.0 |
| 2022-12 | CT#98e | CP-223120 | 4837 |  | B | Equivalent SNPNs usage for NSAG information storage | 18.1.0 |
| 2022-12 | CT#98e | CP-223120 | 4838 |  | B | Equivalent SNPNs usage for congestion control | 18.1.0 |
| 2022-12 | CT#98e | CP-223120 | 4839 | 2 | B | Equivalent SNPNs usage in 5GMM-CONNECTED mode with RRC inactive indication | 18.1.0 |
| 2022-12 | CT#98e | CP-223120 | 4840 | 2 | B | Equivalent SNPN usage for mobile identity selection | 18.1.0 |
| 2022-12 | CT#98e | CP-223120 | 4841 | 1 | B | Equivalent SNPN usage in UAC | 18.1.0 |
| 2022-12 | CT#98e | CP-223100 | 4842 | 2 | F | Issues in slicing and SNPN | 18.1.0 |
| 2022-12 | CT#98e | CP-223116 | 4844 | 1 | A | Lost scope of AMF requirements for allowed NSSAI in NB-N1 mode | 18.1.0 |
| 2022-12 | CT#98e | CP-223115 | 4848 | 1 | F | Handling of current TAI in case of reception of Forbidden TAI IEs | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4849 |  | F | Removal of duplicated info in CIoT small data container | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4850 | 1 | F | Corrections and clarifications for the case when T3502 is “Zero” | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4852 | 3 | F | Add the invalid RA case to multiple TACs handling | 18.1.0 |
| 2022-12 | CT#98e | CP-223115 | 4854 | 3 | A | AMF behaviour on Forbidden TAIs list IEs | 18.1.0 |
| 2022-12 | CT#98e | CP-223115 | 4856 | 1 | A | UE behaviour on Forbidden TAIs list IEs | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4859 |  | F | Terminology alignment on SNPN-enabled UE | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4860 | 2 | F | Alignment on procedure name | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4861 |  | F | Correction on session-AMBR handling | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4862 | 1 | F | Clarification on SNPN access operation mode | 18.1.0 |
| 2022-12 | CT#98e | CP-223116 | 4864 | 1 | A | Registration procedure triggered by a change of UE Requested T3512 | 18.1.0 |
| 2022-12 | CT#98e | CP-223159 | 4865 | 3 | F | The handling on high priority access in SNPN | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4866 | 1 | F | Correction on the length of IE | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4868 |  | F | Correction to the emergency service | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4870 | 1 | F | QoS flow description correction | 18.1.0 |
| 2022-12 | CT#98e | CP-223116 | 4872 | 1 | A | Correction on conditions for using SPI for UE derived QoS rules | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4874 | 1 | F | Correction of terminology related to the rejected NSSAI due to maximum number of UEs reached | 18.1.0 |
| 2022-12 | CT#98e | CP-223142 | 4875 | 2 | B | Support for Unavailability Period | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4876 | 1 | F | Correction to other syntactical errors in TFT | 18.1.0 |
| 2022-12 | CT#98e | CP-223118 | 4877 | 2 | B | N3IWF with slice capability | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4878 |  | F | Missing registration updates for emergency service fallback in 5GMM-REGISTERED.ATTEMPTING-REGISTRATION-UPDATE. | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4879 |  | F | UE handling on PCO or EPCO syntactical errors inQoS operations | 18.1.0 |
| 2022-12 | CT#98e | CP-223136 | 4882 | 1 | A | Maximum length of NSAG information IE | 18.1.0 |
| 2022-12 | CT#98e | CP-223136 | 4884 | 2 | A | TAI lists restriction for NSAG information | 18.1.0 |
| 2022-12 | CT#98e | CP-223127 | 4886 |  | A | Procedure type for service-level authentication and authorization procedure | 18.1.0 |
| 2022-12 | CT#98e | CP-223115 | 4887 | 1 | F | Forbidden TAl lists update via satellite access | 18.1.0 |
| 2022-12 | CT#98e | CP-223143 | 4889 | 1 | A | Modify network handling of PDU sessions for emergency request in abnormal case | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4890 |  | F | Correction to references | 18.1.0 |
| 2022-12 | CT#98e | CP-223156 | 4891 | 1 | F | Multiple DHCP requests with different IA_NA options by RG | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4894 | 1 | F | Correction to MA PDU session status when user plane resources are establishing | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4895 |  | F | Mapped S-NSSAI for rejected NSSAI for the maximum number of UEs reached | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4896 |  | F | Consistency on rejection cause "S-NSSAI not available due to maximum number of UEs reached” | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4899 | 1 | F | Deleting NSSRG Information | 18.1.0 |
| 2022-12 | CT#98e | CP-223127 | 4905 | 2 | A | Clarification on payload and payload type for UUAA and C2 authorization | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4908 |  | F | Clarification of UE behaviour when the UE receives the "Network slicing subscription changed". | 18.1.0 |
| 2022-12 | CT#98e | CP-223121 | 4910 | 3 | A | Handling of pending NSSAI in NSSRG procedure Rel18 - option 1 | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4914 | 1 | F | Octets 7 to 10 in the S-NSSAI IE | 18.1.0 |
| 2022-12 | CT#98e | CP-223115 | 4920 | 3 | A | Correction in the forbidden TAI lists in NAS messages over satellite access | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4923 |  | F | S-NSSAI added to configured NSSAI only if there is less than 16 entries | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4929 | 1 | F | Remove S-NSSAI from NSAG if S-NNSAI is not in configured NSSAI (Rel-18) | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4933 |  | F | Considering the access type in the de-registration type IE when handling the 5GMM cause | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4934 |  | F | Clarification on derived QoS Rules for an IPv6 UDP encapsulated ESP packet | 18.1.0 |
| 2022-12 | CT#98e | CP-223120 | 4936 |  | B | WLANSP provisioning in SNPN | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4937 | 1 | F | No specific DRX parameter nogotiation in periodic registration procedure | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4938 | 1 | F | Correction on format of Extended rejected NSSAI | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4939 |  | F | Semantic error in QoS operations about unstructure PDU session type | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4940 |  | F | Perform eCall inactivity precedure in RRC inactive state | 18.1.0 |
| 2022-12 | CT#98e | CP-223117 | 4943 | 2 | A | Multicast MBS session join or leave for local multicast service | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4945 | 1 | F | Cause 80 handling | 18.1.0 |
| 2022-12 | CT#98e | CP-223115 | 4946 | 1 | F | Correction to #78 timer handling | 18.1.0 |
| 2022-12 | CT#98e | CP-223121 | 4951 | 1 | A | Maximum length of NSSRG information IE | 18.1.0 |
| 2022-12 | CT#98e | CP-223118 | 4961 | 1 | B | UE to indicate its support for Slice-based N3IWF selection to the network | 18.1.0 |
| 2022-12 | CT#98e | CP-223118 | 4963 | 1 | B | Rejecting the UE Registration due to the selected N3IWF by the UE is not compatible with the used slices | 18.1.0 |
| 2022-12 | CT#98e | CP-223145 | 4964 | 1 | B | Indicating the capability of supporting SDNAEPC during the PDU session establishment procedure | 18.1.0 |
| 2022-12 | CT#98e | CP-223144 | 4965 | 1 | F | Adding missing Abbreviations and other miscellaneous corrections in TS 24.501 | 18.1.0 |
| 2022-12 | CT#98e | CP-223160 | 4968 | 1 | F | UE behavior when an always-on PDU sessioin is subject to ODAC | 18.1.0 |
| 2022-12 | CT#98e | CP-223115 | 4971 |  | A | Correction of IEI values | 18.1.0 |
| 2022-12 | CT#98e | CP-223279 | 4973 | 3 | A | Notification of change of aerial service availability to the UE | 18.1.0 |
| 2023-03 | CT#99 | CP-230265 | 4977 | - | B | Enhanced CAG selection - enforcement in successful cases | 18.2.0 |
| 2023-032022-12 | CT#99 | CP-230265 | 4978 | - | B | Enhanced CAG selection - enforcement in unsuccessful cases | 18.2.0 |
| 2023-03 | CT#99 | CP-230220 | 4995 | - | D | Editorial corrections | 18.2.0 |
| 2023-03 | CT#99 | CP-230260 | 5011 | - | B | General updates for LADN per DNN & S-NSSAI | 18.2.0 |
| 2023-03 | CT#99 | CP-230217 | 5021 | - | F | Correction to the coding of N3IWF address IE | 18.2.0 |
| 2023-03 | CT#99 | CP-230252 | 5024 | - | B | IPv6 prefix delegation in 5GS | 18.2.0 |
| 2023-03 | CT#99 | CP-230231 | 5025 | - | B | Equivalent SNPNs: 5GS forbidden tracking areas in TS 24.501 | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5027 | - | B | Equivalent SNPNs: NSSAIs, network-assigned UE radio capability ID, maximum number of established PDU sessions and 5GMM parameters in annex C stored per selected entry | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5028 | - | B | Equivalent SNPNs: entry of list of subscriber data becoming invalid | 18.2.0 |
| 2023-03 | CT#99 | CP-230214 | 5033 | - | A | Fix encoding of 5QI 87 | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5041 | - | F | Clarification on PDU session type in PDU session establishment request | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5052 | - | F | Corrections to TAI list handling in deregistration and FTAI storing | 18.2.0 |
| 2023-03 | CT#99 | CP-230224 | 5055 | - | A | Correction of implementation error of CR4615 | 18.2.0 |
| 2023-03 | CT#99 | CP-230250 | 5074 | - | F | Clarification on determination of T3512 value based on unavailability period duration | 18.2.0 |
| 2023-03 | CT#99 | CP-230285 | 5075 | - | F | NSAC applicability in SNPN | 18.2.0 |
| 2023-03 | CT#99 | CP-230285 | 5076 | - | F | Correction on reference of S-NSSAI inclusion in ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST message | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5082 | - | F | Correction on the equivalent SNPNs | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5085 | - | F | Correction on the equivalent SNPNs usage for congestion control | 18.2.0 |
| 2023-03 | CT#99 | CP-230214 | 5090 | - | A | Correction of incomplete implementation of CR4380 (C1-224129) | 18.2.0 |
| 2023-03 | CT#99 | CP-230250 | 5103 | - | F | Abnormal case handling for registration procedure due to Unavailability period duaration | 18.2.0 |
| 2023-03 | CT#99 | CP-230217 | 5119 | - | B | Aborting registration procedure when the selected N3IWF is not compatible with the allowed NSSAI | 18.2.0 |
| 2023-03 | CT#99 | CP-230217 | 5120 | - | F | Correction for N3IWF identifier IE | 18.2.0 |
| 2023-03 | CT#99 | CP-230285 | 5152 |  | F | Store the rejected NSSAI for failed or revoked NSSAA associated with EPLMN | 18.2.0 |
| 2023-03 | CT#99 | CP-230285 | 5153 |  | F | Handing pending paging message if access attempt for registration procedure is barred | 18.2.0 |
| 2023-03 | CT#99 | CP-230278 | 4983 | 1 | B | Equivalent SNPNs: error cases and abnormal cases | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5026 | 1 | B | Equivalent SNPNs: forbidden SNPNs in TS 24.501 | 18.2.0 |
| 2023-03 | CT#99 | CP-230232 | 5078 | 1 | A | UE and AMF comply with NSSRG restriction across different access types over the same PLMN and different PLMNs | 18.2.0 |
| 2023-03 | CT#99 | CP-230271 | 5125 | 1 | A | Correction for SNN related to 5G NSWO | 18.2.0 |
| 2023-03 | CT#99 | CP-230307 | 5073 | 1 | A | Clarification on NSAG information validity when TAI list is absent | 18.2.0 |
| 2023-03 | CT#99 | CP-230214 | 4993 | 1 | A | 5GMM IEI Duplicated in Registration Accept | 18.2.0 |
| 2023-03 | CT#99 | CP-230312 | 5128 | 1 | A | Impact on network and relay UE behaviour when CP-PRUK is not found | 18.2.0 |
| 2023-03 | CT#99 | CP-230236 | 5037 | 1 | F | Added DNN and S-NSSAI as indication for UUAA-SM and C2 authorization | 18.2.0 |
| 2023-03 | CT#99 | CP-230307 | 5164 | 2 | A | Correction of misimplementation of CR 4883, 4665, and 4678 (Rel 18) | 18.2.0 |
| 2023-03 | CT#99 | CP-230311 | 5112 | 4 | F | Forbidden lists handling due to SNPN mode switch. | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5016 | 2 | F | Correction on NAS signalling connection | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 4991 | 2 | F | Clarification on UE policy part contents | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5017 | 1 | F | Correction on Back-off timer value IE conditions in network-initiated NAS transport procedure | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5084 | 1 | F | The equivalent SNPNs usage for access identities | 18.2.0 |
| 2023-03 | CT#99 | CP-230214 | 5010 | 2 | F | No PDU session release for non-current access | 18.2.0 |
| 2023-03 | CT#99 | CP-230217 | 5002 | 1 | F | Correction N3IWF address information element | 18.2.0 |
| 2023-03 | CT#99 | CP-230210 | 5015 | 1 | B | User plane positioning capability indication | 18.2.0 |
| 2023-03 | CT#99 | CP-230278 | 4985 | 1 | B | Equivalent SNPNs: MPS and MCS indicators | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5063 | 1 | F | The AMF shall not provide equivalent SNPN/PLMN list when the UE is registered in PLMN/SNPN | 18.2.0 |
| 2023-03 | CT#99 | CP-230310 | 4982 | 1 | B | Equivalent SNPNs: LADN service area | 18.2.0 |
| 2023-03 | CT#99 | CP-230278 | 4981 | 1 | B | Equivalent SNPNs: service area restrictions | 18.2.0 |
| 2023-03 | CT#99 | CP-230278 | 4984 | 1 | B | Equivalent SNPNs: applicability of network-assigned UE radio capability ID, NSSAI inclusion mode IE and operator-defined access category definitions | 18.2.0 |
| 2023-03 | CT#99 | CP-230278 | 5014 | 1 | F | Term definition for SNPN access mode | 18.2.0 |
| 2023-03 | CT#99 | CP-230218 | 4944 | 3 | B | Support for UE accessing SNPN services using non-3GPP access | 18.2.0 |
| 2023-03 | CT#99 | CP-230217 | 5121 | 1 | B | UE to indicate its support for Slice-based TNGF selection to the network | 18.2.0 |
| 2023-03 | CT#99 | CP-230217 | 5122 | 1 | B | Aborting registration procedure when the selected TNGF is not compatible with the allowed NSSAI | 18.2.0 |
| 2023-03 | CT#99 | CP-230217 | 5123 | 1 | B | Introducing the TNAN information IE | 18.2.0 |
| 2023-03 | CT#99 | CP-230217 | 5020 | 1 | F | Correction to the IP address type and minor fixes on N3IWF address IE | 18.2.0 |
| 2023-03 | CT#99 | CP-230250 | 4999 | - | B | UE initiated de-registration procedure for Unavailability Period | 18.2.0 |
| 2023-03 | CT#99 | CP-230250 | 5053 | 1 | B | Handling UE NAS timers in duration of unavailability period | 18.2.0 |
| 2023-03 | CT#99 | CP-230254 | 5061 | 1 | B | Instructing a UE to reconnect to the network upon receiving an indication of a change in the RAN timing synchronization status | 18.2.0 |
| 2023-03 | CT#99 | CP-230260 | 5012 | 1 | B | 5GMM procedure updates for LADN per DNN & S-NSSAI | 18.2.0 |
| 2023-03 | CT#99 | CP-230262 | 5081 | 1 | B | Introduction of general aspects of PIN | 18.2.0 |
| 2023-03 | CT#99 | CP-230220 | 4989 | 2 | F | Missing message in the inclusion criteria of Additional 5G security information | 18.2.0 |
| 2023-03 | CT#99 | CP-230265 | 4976 | 1 | B | Enhanced CAG selection - providing additional information | 18.2.0 |
| 2023-03 | CT#99 | CP-230257 | 5003 | 1 | B | Update UE handling of the MA PDU session | 18.2.0 |
| 2023-03 | CT#99 | CP-230257 | 5138 | 1 | B | Redundant steering mode is not applicable for ATSSS-LL functionality (impact on TS 24.501) | 18.2.0 |
| 2023-03 | CT#99 | CP-230264 | 5008 | 1 | B | UE capability indication to the network for A2X | 18.2.0 |
| 2023-03 | CT#99 | CP-230260 | 5013 | 1 | B | 5GSM procedure updates for LADN per DNN & S-NSSAI | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5004 | 1 | F | Use default configured NSSAI because of no configured NSSAI | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 4867 | 3 | F | Clarification to the Mapped EPS bearer contexts | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5031 | 1 | B | Protocol error handling enhancements for Type 6 IE container IEs | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5047 | 1 | F | Extended CAG information list in CONFIGURATION UPDATE COMMAND | 18.2.0 |
| 2023-03 | CT#99 | CP-230285 | 5091 | 1 | F | UE handling for cause78 in DL NAS TRANSPORT and connection management | 18.2.0 |
| 2023-03 | CT#99 | CP-230236 | 5135 | 1 | A | Rejecting PDU session for C2 communication when UAS service is not allowed | 18.2.0 |
| 2023-03 | CT#99 | CP-230285 | 5093 | 1 | F | Clarification on remote UE ID | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 4998 | 1 | F | UE-requested PDU session modification after inter-system change from S1 mode to N1 mode | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5044 | 1 | F | Support for S-NSSAI(s) added in S1 mode without NSSRG Information | 18.2.0 |
| 2023-03 | CT#99 | CP-230220 | 5049 | 1 | F | MBS handling in abnormal and PDU session rejection cases | 18.2.0 |
| 2023-03 | CT#99 | CP-230258 | 5069 | 1 | B | General introduction of network slice replacement | 18.2.0 |
| 2023-03 | CT#99 |  | 5070 | 1 | B | Support of network slice replacement during registration procedure | 18.2.0 |
| 2023-03 | CT#99 | CP-230258 | 5071 | 1 | B | Support of network slice replacement during UCU procedure | 18.2.0 |
| 2023-03 | CT#99 | CP-230278 | 4996 | 1 | F | Equivalent SNPNs: identification | 18.2.0 |
| 2023-03 | CT#99 | CP-230278 | 4997 | 1 | F | Equivalent SNPNs: 5G-GUTI selection | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5029 | 1 | B | Equivalent SNPNs: last visited TAI | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5007 | 1 | F | NSSAI applicable to equivalent PLMNs in registration area | 18.2.0 |
| 2023-03 | CT#99 | CP-230285 | 5154 | 1 | F | Start T3540 upon receiving #22 along with a T3346 value | 18.2.0 |
| 2023-03 | CT#99 | CP-230285 | 5019 | 1 | F | Correction to NSAG | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5045 | 1 | F | NSAG and lower layer failure | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 5060 | 2 | F | No transfer of LADN PDU session to S1 mode | 18.2.0 |
| 2023-03 | CT#99 | CP-230232 | 4910 | 6 | F | Handling of pending NSSAI in NSSRG procedure-option 1 | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5087 | 2 | B | The enhancement on onboarding services in SNPN supporting localized services | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5113 | 2 | F | Extending Re-attempt indicator IE & 5GSM congestion re-attempt indicator IE for equivalent SNPN | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5118 | 4 | F | Save NID value of registered SNPN in NV memory. | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5116 | 3 | F | Mobility registration update for SNPNs. | 18.2.0 |
| 2023-03 | CT#99 | CP-230285 | 5114 | 2 | F | Deletion of 5GS forbidden tracking areas for roaming added due to rejected S-NSSAI | 18.2.0 |
| 2023-03 | CT#99 | CP-230254 | 5056 | 2 | B | Indication of support for reconnection to the network due to RAN timing synchronization status change via the 5GMM capability IE | 18.2.0 |
| 2023-03 | CT#99 | CP-230214 | 5107 | 3 | A | Update MPS indicator in CUC message R18 | 18.2.0 |
| 2023-03 | CT#99 | CP-230234 | 5117 | 2 | B | Add new indication on the UE support of URSP Provisioning in EPS | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5097 | 3 | B | Equivalent SNPN information provided to lower layers for cell reselection | 18.2.0 |
| 2023-03 | CT#99 | CP-230215 | 4994 | 2 | B | Type 6 IE container | 18.2.0 |
| 2023-03 | CT#99 | CP-230307 | 5058 | 2 | A | Slices provided to the lower layers for NSAG | 18.2.0 |
| 2023-03 | CT#99 | CP-230219 | 5036 | 3 | B | CH controlled prioritized list of preferred SNPNs and GINs for access for localized services in SNPN | 18.2.0 |
| 2023-03 | CT#99 | CP-230257 | 5165 | 2 | B | Capability for MPQUIC Steering Functionality | 18.2.0 |
| 2023-03 | CT#99 |  |  |  |  | Correction of Formatting errors and mis implementation | 18.2.1 |
| 2023-06 | CT#100 | CP-231216 | 5167 | - | F | Inconsistent description of UE policy section management list IE | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5181 | - | F | Use defined term Alternative NSSAI | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5182 | - | F | UE behaviour after receiving rejected NSSAI | 18.3.0 |
| 2023-06 | CT#100 | CP-231277 | 5050 | 1 | B | Transmission of A2X Policy | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5198 | - | F | Remove the NOTE not applicable to SNPN scenario | 18.3.0 |
| 2023-06 | CT#100 | CP-231219 | 5199 | - | F | Remove NSWO from abbreviation list | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5202 | - | F | Correcting few errors in UE handing of QoS rules | 18.3.0 |
| 2023-06 | CT#100 | CP-231232 | 5218 | - | F | NF name correction for UUAA-MM | 18.3.0 |
| 2023-06 | CT#100 | CP-231232 | 5219 | - | F | Correction on referred table No. to 24.008 | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5233 | - | F | Correction of Paging Subgroup ID value | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5224 | 1 | F | Clarification on UE policy part contents length | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5295 | - | F | NW handling when treating an MRU as an initial registration | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5298 | - | F | Correction to handling of FTAI list on receiving #62 | 18.3.0 |
| 2023-06 | CT#100 | CP-231238 | 5303 | - | F | Clarification on Emergency PDU session release | 18.3.0 |
| 2023-06 | CT#100 | CP-231228 | 5312 | - | B | AMF to indicate the capability of supporting non-3GPP access path switching | 18.3.0 |
| 2023-06 | CT#100 | CP-231228 | 5313 | - | B | UE to indicate the capability of supporting non-3GPP access path switching | 18.3.0 |
| 2023-06 | CT#100 | CP-231221 | 5320 | - | B | Indicating Uplink data status IE in REGISTRATION REQUEST message after failure of resumption of the RRC connection for UE that has joined Multicast session | 18.3.0 |
| 2023-06 | CT#100 | CP-231304 | 5225 | 2 | B | Ranging capability over NAS | 18.3.0 |
| 2023-06 | CT#100 | CP-231277 | 5250 | 1 | B | AMF should not release NAS signalling after Registration procedure if the UE is authorized A2X | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5272 | 1 | F | Not include uplink data status IE in mobility registration procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5279 | 1 | F | Clearing maximum number of PDU sessions | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5332 | 1 | F | TAIs belonging to different PLMNs which are equivalent PLMNs in forbidden tracking areas for regional provision of service or forbidden tracking areas for roaming | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5176 | 1 | B | Mobility management for the support of optimised handling of temporarily available network slices | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5274 | 1 | F | No need to include rejected NSSAI for 5GMM causes other than #62 | 18.3.0 |
| 2023-06 | CT#100 | CP-231223 | 5309 | 1 | F | Adding reject cause values #81 and #82 under the Annex A | 18.3.0 |
| 2023-06 | CT#100 | CP-231207 | 5323 | 1 | F | Support of PRUs in NAS transport procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5205 | 2 | B | Indication of partial network slice support in a registration area when registering | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5186 | 2 | F | Enabling UE to send UE STATE INDICATION message even when UE does not have stored UE policy sections - Option B | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5329 | 1 | B | Capability indication to support of network slice usage control | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5171 | 1 | F | Correction of handling of the PDU session reactivation result error cause | 18.3.0 |
| 2023-06 | CT#100 | CP-231276 | 5192 | 1 | F | MRU for RAN timing synchronization status change | 18.3.0 |
| 2023-06 | CT#100 | CP-231245 | 5188 | 1 | F | Correction to LADN restriction for UE to create PDU session | 18.3.0 |
| 2023-06 | CT#100 | CP-231245 | 5189 | 1 | F | Clarify the behavior of Service area restriction and the LADN per DNN/S-NSSAI | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5204 | 2 | F | Network Slice replacement | 18.3.0 |
| 2023-06 | CT#100 | CP-231277 | 5193 | 1 | B | Authorization of A2X Direct C2 Communications in 5GS | 18.3.0 |
| 2023-06 | CT#100 | CP-231265 | 5197 | 1 | B | Transmission of Ranging/SL Positioning Policy | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5327 | 1 | F | Correction on a missing parameter in the UE-initiated NAS transport procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5149 | 3 | F | Add the definition of satellite NG-RAN cell and non-satellite NG-RAN cell | 18.3.0 |
| 2023-06 | CT#100 | CP-231265 | 5226 | 1 | B | Service request for ranging | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5178 | 1 | F | Define maximum length of Alternative NSSAI IE | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5180 | 1 | F | Clarify AMF behaviour when S-NSSAI to be replaced is available | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5183 | 1 | F | Send 5GMM cause #62 during NW-initiated de-registration procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5184 | 1 | F | Correction to the conditions for inclusion of the PDU session reactivation result IE | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5185 | 1 | D | 5G AKA based primary authentication and key agreement procedure initiation | 18.3.0 |
| 2023-06 | CT#100 | CP-231238 | 5263 | 1 | F | Condition for mobility registration update in SNPN | 18.3.0 |
| 2023-06 | CT#100 | CP-231282 | 5220 | 1 | B | General section for MBSR | 18.3.0 |
| 2023-06 | CT#100 | CP-231216 | 5266 | 1 | F | Minor correction on the T3540 | 18.3.0 |
| 2023-06 | CT#100 | CP-231238 | 5299 | 1 | F | Correction in references of non-3GPP access for SNPNs | 18.3.0 |
| 2023-06 | CT#100 | CP-231264 | 5261 | 1 | F | Resolution of editor's note on the request frequency of non-3GPP delay | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5328 | 2 | B | General introduction on support of network slice usage control | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5288 | 2 | F | Clarification on handling of received T3502 in registration accept message | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5283 | 1 | B | The partially allowed NSSAI - UE storage | 18.3.0 |
| 2023-06 | CT#100 | CP-231207 | 5285 | 1 | B | User plane positioning capability | 18.3.0 |
| 2023-06 | CT#100 | CP-231217 | 5172 | 1 | F | Emergency service handling when low layer failure and NW initiated deregistration | 18.3.0 |
| 2023-06 | CT#100 | CP-231276 | 5191 | 1 | B | UAC for RAN timing synchronization status change - RRC inactive UE | 18.3.0 |
| 2023-06 | CT#100 | CP-231238 | 5265 | 2 | F | Resolution of editor's note on NID assignment | 18.3.0 |
| 2023-06 | CT#100 | CP-231245 | 5187 | 2 | F | Correction to Extended LADN information | 18.3.0 |
| 2023-06 | CT#100 | CP-231232 | 5245 | 1 | F | Updation to REGISTERED LIMITED service state. | 18.3.0 |
| 2023-06 | CT#100 | CP-231219 | 5168 | 1 | F | Creation of access stratum connection for wireline access used by 5G-RG | 18.3.0 |
| 2023-06 | CT#100 | CP-231238 | 5166 | 1 | F | Removal of redundant description of NID coding in SNPN list IE | 18.3.0 |
| 2023-06 | CT#100 | CP-231221 | 5318 | 1 | B | Supporting multicast MBS session for UE in MICO mode | 18.3.0 |
| 2023-06 | CT#100 | CP-231217 | 5246 | 2 | F | Deregistration procedure and access type | 18.3.0 |
| 2023-06 | CT#100 | CP-231223 | 5322 | 1 | F | Correction related to receiving N3IWF identifier IE in the REGISTRATION REJECT | 18.3.0 |
| 2023-06 | CT#100 | CP-231211 | 5326 | 1 | B | RRC Establishment cause when RSC is dedicated for Emergency for layer-2 relay | 18.3.0 |
| 2023-06 | CT#100 | CP-231217 | 5276 | 3 | F | Paging to re-establish user-plane resources over 3GPP access | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5248 | 2 | B | Supoort of network slice replacement during PDU session modification procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231217 | 5241 | 1 | F | Correction in the 5GSM sublayer state transition in terms of the PDU SESSION MODIFICATION REJECT message including 5GSM cause value #43 | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5255 | 2 | B | Support of network slice replacement during PDU session release procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5310 | 1 | F | Restriction in the requested NSSAI creation if an S-NSSAI is temporarily unavailable | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5307 | 1 | B | UE capability indication for the support of optimized handling of temporarily available network slices | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5308 | 2 | B | AMF operation upon being requested an S-NSSAI which is unavailable according to the validity time | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5316 | 1 | B | Storing validity time | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5304 | 1 | B | S-NSSAI location availability information in the registration procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5305 | 1 | B | Storing S-NSSAI location availability information | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5306 | 1 | B | S-NSSAI location availability information via UCU | 18.3.0 |
| 2023-06 | CT#100 | CP-231282 | 5301 | 2 | B | UE handling upon CAG validity state change | 18.3.0 |
| 2023-06 | CT#100 | CP-231217 | 5349 | - | F | Clarification on MRU/PRU initiation | 18.3.0 |
| 2023-06 | CT#100 | CP-231233 | 5330 | 1 | D | Editorial corrections to the ECS address clause | 18.3.0 |
| 2023-06 | CT#100 | CP-231277 | 5357 | - | B | Request resources for A2X communication over PC5 | 18.3.0 |
| 2023-06 | CT#100 | CP-231245 | 5213 | 2 | B | AMF enforcement for LADN per DNN & S-NSSAI | 18.3.0 |
| 2023-06 | CT#100 | CP-231245 | 5370 | - | B | LADN per DNN & S-NSSAI handling for legacy UE | 18.3.0 |
| 2023-06 | CT#100 | CP-231238 | 5371 | - | F | Correction on SOR-SNPN-SI-LS IE coding | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5377 | - | F | Partially allowed NSSAI for slice based cell re-selection and random access | 18.3.0 |
| 2023-06 | CT#100 | CP-231240 | 5378 | - | F | Partially allowed NSSAI for RFSP derivation | 18.3.0 |
| 2023-06 | CT#100 | CP-231217 | 5379 | - | D | Editorial corrections | 18.3.0 |
| 2023-06 | CT#100 | CP-231228 | 5381 | - | F | Correction in mapping supported ATSSS steering funtionalities and modes | 18.3.0 |
| 2023-06 | CT#100 | CP-231238 | 5262 | 1 | F | Correction on onboarding in SNPN supporting localized services | 18.3.0 |
| 2023-06 | CT#100 | CP-231243 | 5424 |  | B | Resolve EN on URSP provisioning in EPS support indication when the UE does not have UPSIs | 18.3.0 |
| 2023-06 | CT#100 | CP-231232 | 5270 | 1 | F | Updation of DEREGISTERED LIMITED service state for CAG | 18.3.0 |
| 2023-06 | CT#100 | CP-231232 | 5445 | - | F | UE-ID based Paging Early Indication | 18.3.0 |
| 2023-06 | CT#100 | CP-231228 | 5314 | 1 | B | SMF to indicate the capability of supporting non-3GPP access path switching | 18.3.0 |
| 2023-06 | CT#100 | CP-231236 | 5412 | 1 | A | Coding of NID of SNPN identity and GIN of SOR transparent container - alternative 2 | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5355 | 1 | F | Interaction between a 5GSM entity and upper layers for URSP handling | 18.3.0 |
| 2023-06 | CT#100 | CP-231206 | 5404 | 1 | A | Correction to the CIoT small data container IE | 18.3.0 |
| 2023-06 | CT#100 | CP-231246 | 5364 | 1 | A | Correction to the Service-level-AA server address IE | 18.3.0 |
| 2023-06 | CT#100 | CP-231207 | 5215 | 3 | B | UL/DL NAS transport updates for user plane positioning | 18.3.0 |
| 2023-06 | CT#100 | CP-231226 | 5407 | 1 | A | Correction to the MA PDU session information IE | 18.3.0 |
| 2023-06 | CT#100 | CP-231239 | 5414 | 1 | F | Equivalent SNPNs: re-attempt control not due to congestion - enforcement | 18.3.0 |
| 2023-06 | CT#100 | CP-231243 | 5362 | 1 | B | UE reporting of URSP rule enforcement in TS 24.501 | 18.3.0 |
| 2023-06 | CT#100 | CP-231243 | 5339 | 3 | B | Indicating the support of URSP rule enforcement in the UE policy classmark | 18.3.0 |
| 2023-06 | CT#100 | CP-231243 | 5169 | 3 | B | Providing VPLMN specific URSP | 18.3.0 |
| 2023-06 | CT#100 | CP-231239 | 5415 | 1 | B | Handling of forbidden SNPN lists for localized services | 18.3.0 |
| 2023-06 | CT#100 | CP-231239 | 5438 | 1 | F | Deletion of 5GS forbidden tracking area per entry of list of subscriber data. | 18.3.0 |
| 2023-06 | CT#100 | CP-231239 | 5413 | 1 | F | SOR transparent container clean up | 18.3.0 |
| 2023-06 | CT#100 | CP-231239 | 5203 | 3 | B | CH controlled prioritized list of preferred SNPNs and GINs for access for localized services in SNPN | 18.3.0 |
| 2023-06 | CT#100 | CP-231239 | 5444 | 1 | F | Clarification for SOR-SNPN-SI-LS in SOR ACK | 18.3.0 |
| 2023-06 | CT#100 | CP-231211 | 5466 | 1 | B | Introducing the capabilities related to supporting UE-to-UE relay | 18.3.0 |
| 2023-06 | CT#100 | CP-231277 | 5430 | 1 | B | Clarification about the condition of the PCF initiating the Network-requested UE policy management procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231282 | 5408 | 1 | F | Location validity information for enhanced CAG list in TS 24.501 | 18.3.0 |
| 2023-06 | CT#100 | CP-231223 | 5356 | 2 | F | Slice-based N3IWF or TNGF selection | 18.3.0 |
| 2023-06 | CT#100 | CP-231223 | 5421 | 1 | B | Support of AUN3/NAUN3 device behind 5G-RG | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5177 | 2 | B | UE storage of alternative NSSAI | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5179 | 3 | B | Provision alternative NSSAI during registration procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5375 | 1 | F | Clarification on alternative S-NSSAI being part of the subscribed S-NSSAIs | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5376 | 1 | F | Clarification on when to provide alternative NSSAI to UE | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5400 | 1 | F | Handling Alternative NSSAI when SM backoff timer is running | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5401 | 1 | F | Deleting Alternative NSSAI | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5247 | 7 | B | Support of network slice replacement during PDU session establishment procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5297 | 2 | B | Network slices with NS-AoS not matching deployed tracking areas | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5425 | 1 | B | The condition that the UE does not trigger a service request procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5344 | 1 | B | Session management for optimized handling of temporarily available network slices | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5317 | 3 | B | Provisioning validity time | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5372 | 1 | B | Enhancement on partial network slice storage | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5383 | 1 | B | UE storage - partially rejected NSSAI | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5462 | 1 | B | Allowed PDU session status | 18.3.0 |
| 2023-06 | CT#100 | CP-231271 | 5346 | 1 | F | Adding inclusion criteria for newly added IE | 18.3.0 |
| 2023-06 | CT#100 | CP-231271 | 5374 | 1 | F | Unavailability period duration IE as a non-cleartext IE | 18.3.0 |
| 2023-06 | CT#100 | CP-231271 | 5388 | 1 | F | The AMF behaviour on the unavailability period duration | 18.3.0 |
| 2023-06 | CT#100 | CP-231271 | 5458 | 1 | B | 5GMM state for unavailability period | 18.3.0 |
| 2023-06 | CT#100 | CP-231271 | 5459 | 1 | B | Coming out of unavailability period when deregistered | 18.3.0 |
| 2023-06 | CT#100 | CP-231220 | 5238 | 3 | B | New trigger for registration procedure to indicate loss of coverage | 18.3.0 |
| 2023-06 | CT#100 | CP-231220 | 5240 | 3 | B | New Maximum signalling waiting time due to discontinuous coverage | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5281 | 3 | B | The partially allowed NSSAI - registration procedures | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5423 | 1 | B | Adding mapped S-NSSAI for partially allowed NSSAI to the definition | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5433 | 1 | B | The AMF sends the partially allowed NSSAI to the UE after NSSAA | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5228 | 4 | B | Partial rejected NSSAI to registration procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231265 | 5437 | 1 | B | Capability of SL Positioning Server UE over PC5 | 18.3.0 |
| 2023-06 | CT#100 | CP-231277 | 5427 | 2 | F | Removing ENs | 18.3.0 |
| 2023-06 | CT#100 | CP-231245 | 5214 | 3 | B | Inclusion of Extended LADN information IE in REGISTRATION ACCEPT message | 18.3.0 |
| 2023-06 | CT#100 | CP-231223 | 5222 | 3 | B | PDU session modification procedure for supporting N3QAI and non3gpp delay budget | 18.3.0 |
| 2023-06 | CT#100 | CP-231228 | 5315 | 2 | B | Introducing the non-3GPP access path switching procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231228 | 5449 | 1 | B | PDU session IDs not included in Uplink data status IE during non-3GPP access path switching | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5450 | 1 | F | Abort registration procedure for initiating an emergency PDU session because of lower layer failure | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5467 |  | F | Start timer T3540 upon receiving #78 | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5244 | 3 | F | Correction on UE handling of NAS security context | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5348 | 1 | F | Clarification on disabling and enabling N1 mode and SNPN selection for onboarding services | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5234 | 2 | F | Storing the indication of interworking without N26 interface in NVM | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5428 | 1 | F | Clarification of T3540 and CAG cell | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 4772 | 9 | F | Clarification to handling of multiple 5G NAS security contexts | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5440 | 1 | F | Emergency call not allowed while registered for onboarding services | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5420 | 1 | F | QoS rule handling for a GBR QoS flow during modification procedure | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5447 | 1 | F | Additional handling on T3245 expiry. | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5399 | 1 | F | Rejected NSSAI with cause #62 | 18.3.0 |
| 2023-06 | CT#100 | CP-231277 | 5358 | 3 | B | Authorization of A2X direct C2 communication during registration in 5GS | 18.3.0 |
| 2023-06 | CT#100 | CP-231223 | 5453 | 1 | F | Including last visited registered TAI for registration procedure over non-3gpp access | 18.3.0 |
| 2023-06 | CT#100 | CP-231243 | 5208 | 3 | F | URSP support in EPS | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5345 | 1 | F | Correction of the deletion of mapped S-NSSAIs for the rejected NSSAI | 18.3.0 |
| 2023-06 | CT#100 | CP-231239 | 5387 | 2 | F | Clarification on the UE mobility for SNPN | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5336 | 3 | B | SSC mode 2/3 PDU session relocation for network slice instance change | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5280 | 4 | B | The partial network slice feature - general introduction | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5431 | 2 | B | Partial network slice applicable on 3GPP access only | 18.3.0 |
| 2023-06 | CT#100 | CP-231233 | 5373 | 2 | F | Correction on S-NSSAI provision to lower layers for NSAG | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5451 | 1 | F | Additional NAS handling for SNPN related to timers T3584 T3585 & SM level rejection causes #50 and #51. | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5456 | 1 | F | SR for emergency services failing due to LLF or NW initiated deregistration | 18.3.0 |
| 2023-06 | CT#100 | CP-231271 | 5368 | 3 | B | Unavailability period duration for MUSIM UE | 18.3.0 |
| 2023-06 | CT#100 | CP-231241 | 5207 | 6 | B | UE configuration update when supporting the partial network slice support | 18.3.0 |
| 2023-06 | CT#100 | CP-231264 | 5259 | 4 | B | Update of general aspects of PIN | 18.3.0 |
| 2023-06 | CT#100 | CP-231227 | 5380 | 2 | A | ATSSS capabilities of MA PDU session | 18.3.0 |
| 2023-06 | CT#100 | CP-231215 | 5448 | 2 | A | Sending registration complete message for PEIPS information acknowledgment. | 18.3.0 |
| 2023-06 | CT#100 | CP-231221 | 5321 | 4 | B | Indicating Uplink data status IE considering multicast MBS session reception in 5GMM-CONNECTED mode with RRC inactive indication | 18.3.0 |
| 2023-06 | CT#100 | CP-231218 | 5398 | 2 | F | Coordination between 5GMM and EMM states in single registration mode | 18.3.0 |
| 2023-06 | CT#100 | CP-231232 | 5441 | 2 | F | NSSAI in Requested mapped NSSAI IE Share NSSRG value | 18.3.0 |
| 2023-06 | CT#100 | CP-231215 | 5436 | 4 | A | Sending the registration complete message after receiving the NSAG information | 18.3.0 |
| 2023-06 | CT#100 | CP-231292 | 5351 | 5 | F | AMF including configured NSSAI for IWK scenarios | 18.3.0 |
| 2023-06 | CT#100 |  |  |  |  | Clashes and other editorials addressed | 18.3.1 |
| 2023-09 | CT#101 | CP-232223 | 5510 | - | F | Missing references for pre-configuration | 18.4.0 |
| 2023-09 | CT#101 | CP-232233 | 5512 | - | F | Alignment on MBS start time for multicast MBS sessions | 18.4.0 |
| 2023-09 | CT#101 | CP-232201 | 5522 | - | B | Handling on UE requested UPP not authorized by network | 18.4.0 |
| 2023-09 | CT#101 | CP-232220 | 5528 | - | F | Resolve EN about access category for RAN timing synchronization status change | 18.4.0 |
| 2023-09 | CT#101 | CP-232201 | 5538 | - | F | Correction to wrong reference | 18.4.0 |
| 2023-09 | CT#101 | CP-232204 | 5542 | - | F | Correction to clause reference to the Non-3GPP delay budget IE | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5554 | - | F | Missing parts of agreed C1-232764 and C1-233959 for network slice replacement | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5557 | - | F | General cleanup regarding S-NSSAI location validity information and S-NSSAI time validity information | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5561 | - | F | Condition on providing S-NSSAI time validity information to supporting UE | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5562 | - | F | S-NSSAI rejection for UE not supporting S-NSSAI time validity information | 18.4.0 |
| 2023-09 | CT#101 | CP-232231 | 5541 | - | A | Correction to the Service-level-AA service status indication IE | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5563 | - | F | General cleanup regarding partial network slice | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5567 | - | F | Registration update triggered by update of partially allowed NSSAI | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5569 | - | D | Editorial corrections | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5581 | - | F | Clarification on the usage of WUS | 18.4.0 |
| 2023-09 | CT#101 | CP-232191 | 5587 |  | F | Handling of forbidden SNPN list for localized services on T3245 expiry | 18.4.0 |
| 2023-09 | CT#101 | CP-232191 | 5588 |  | F | Saving forbidden list of SNPNs for localized servicesin NV | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5591 | - | F | Clarification in the Delete existing EPS bearer operation | 18.4.0 |
| 2023-09 | CT#101 | CP-232198 | 5620 | - | F | Correction to the trigger for deregistration procedure in the UE. | 18.4.0 |
| 2023-09 | CT#101 | CP-232233 | 5637 | - | F | Correction for including the Uplink data status IE in REGISTRATION REQUEST message after failure of resumption of the RRC connection for UE that has joined Multicast session | 18.4.0 |
| 2023-09 | CT#101 | CP-232191 | 5658 |  | F | Forbidden SNPN list for localized services for 3GPP access only | 18.4.0 |
| 2023-09 | CT#101 | CP-232210 | 5660 | - | B | Path switching for PDU sessions is still establishing | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5665 | - | F | Network control of the slice usage in roaming aspects | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5669 | - | F | Default NSSAI inclusion mode pre-configuration | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5694 | - | B | Resolve the EN for the partial network slice feature | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5667 | 1 | F | Addition of SNPNs with GINs in forbidden lists | 18.4.0 |
| 2023-09 | CT#101 | CP-232191 | 5492 | 1 | F | Clarification of the use of counters regarding SNPN | 18.4.0 |
| 2023-09 | CT#101 | CP-232191 | 5544 | 1 | F | TWIF handling of decorated NAI for N5CW device | 18.4.0 |
| 2023-09 | CT#101 | CP-232200 | 5539 | 1 | F | Correction to reference to the VPS URSP configuration IE | 18.4.0 |
| 2023-09 | CT#101 | CP-232232 | 5498 | 1 | B | MBSR authorization update | 18.4.0 |
| 2023-09 | CT#101 | CP-232266 | 5551 | 1 | C | Updates to allow N3IWF and TNGF relocation | 18.4.0 |
| 2023-09 | CT#101 | CP-232266 | 5642 | 1 | B | N3QAI inclusion in NAS SM signalling for 5G-RG | 18.4.0 |
| 2023-09 | CT#101 | CP-232266 | 5643 | 1 | B | Requirements for supporting AUN3 devices connected to 5G-RG | 18.4.0 |
| 2023-09 | CT#101 | CP-232266 | 5645 | 1 | B | Impact on registration procedure for authenticating AUN3 device behind 5G-RG | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5504 | 1 | F | Correction of style and wording | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5532 | 1 | F | Correction to the Registration accept type 6 IE container IE | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5533 | 1 | F | Correction to the CONFIGURATION UPDATE COMMAND message content | 18.4.0 |
| 2023-09 | CT#101 | CP-232230 | 5536 | 1 | A | Correction to the clause on the ECS address IE | 18.4.0 |
| 2023-09 | CT#101 | CP-232204 | 5575 | 1 | F | Correction on the PIN communication | 18.4.0 |
| 2023-09 | CT#101 | CP-232204 | 5530 | 1 | F | Include N3QAI in PDU session establishment procedure | 18.4.0 |
| 2023-09 | CT#101 | CP-232204 | 5531 | 1 | F | Correction to N3QAI coding | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5553 | 1 | F | Update the definition of network slicing information | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5555 | 1 | F | PDU session re-establishment on the alternative S-NSSAI | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5556 | 1 | F | Minimum length of Alternative NSSAI IE | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5505 | 1 | F | Correction of 5GMM aspects of NS-AoS | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5506 | 1 | C | PDU session establishment from non-supporting UE outside AoS | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5519 | 1 | F | Correction on S-NSSAI location validity information | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5559 | 1 | F | Service request as per S-NSSAI location validity information | 18.4.0 |
| 2023-09 | CT#101 | CP-232187 | 5593 | 1 | B | 5GMM operation of a UE with S-NSSAI location validity information | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5594 | 1 | B | 5GSM operation for a UE with S-NSSAI location validity information | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5596 | 1 | F | KI#3-2 - No new AMF/UE operation when an S-NSSAI becomes available again | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5597 | 1 | B | Coding of the Per-S-NSSAI time validity information for the S-NSSAI field | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5520 | 1 | F | Correction on Partial NSSAI IE coding | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5534 | 1 | F | Correction to clause reference to Mobility management for partial network slice | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5564 | 1 | F | Further clarification on partially allowed NSSAI and NSSAA | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5565 | 1 | F | Clarification on partially allowed NSSAI and NSAC | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5612 | 1 | B | control plane user data associated with S-NSSAI not allowed in current TA | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5571 | 1 | F | NSSAI inclusion to AS layer considering partailly allowed NSSAI | 18.4.0 |
| 2023-09 | CT#101 | CP-232220 | 5529 | 1 | F | Correction to the condition of RAN timing synchronization status change | 18.4.0 |
| 2023-09 | CT#101 | CP-232220 | 5680 | 1 | F | RAN timing synchronization and T3502 and T3525 timer | 18.4.0 |
| 2023-09 | CT#101 | CP-232198 | 5604 | 1 | B | Handling emergency services during discontinuous waiting time | 18.4.0 |
| 2023-09 | CT#101 | CP-232198 | 5617 | 1 | B | Clarification to storage of NAS context | 18.4.0 |
| 2023-09 | CT#101 | CP-232263 | 5632 | 3 | F | Signalling of the unavailability period duration from the AMF to the UE | 18.4.0 |
| 2023-09 | CT#101 | CP-232198 | 5618 | 1 | B | Updation to the periodic timer determination at AMF | 18.4.0 |
| 2023-09 | CT#101 | CP-232198 | 5623 | 1 | B | Clarification to the trigger of mobility registration due to unavailability | 18.4.0 |
| 2023-09 | CT#101 | CP-232198 | 5690 | 1 | F | Correction of the IE name for discontinuous coverage overload control | 18.4.0 |
| 2023-09 | CT#101 | CP-232195 | 5524 | 1 | F | Correction on network handling in DL NAS transport for CIoT user data transfer | 18.4.0 |
| 2023-09 | CT#101 | CP-232195 | 5647 | 1 | F | Correction on the Received MBS container IE | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5673 | 1 | F | equivalent PLMN list when UE registers to two PLMNs | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5657 | 2 | F | Slice Usage Policy for on-demand NSSAI | 18.4.0 |
| 2023-09 | CT#101 | CP-232201 | 5696 | 1 | F | Update the terminology of user plane positioning connection management information | 18.4.0 |
| 2023-09 | CT#101 | CP-232190 | 5609 | 2 | F | Clarifications on UE behavior for several reject causes for no CH support case | 18.4.0 |
| 2023-09 | CT#101 | CP-232232 | 5473 | 1 | B | Support for MBSR authorization signaling during registration | 18.4.0 |
| 2023-09 | CT#101 | CP-232210 | 5659 | 2 | F | Path switching while using old n3 for at least one PDU session supporting path switching | 18.4.0 |
| 2023-09 | CT#101 | CP-232266 | 5640 | 2 | F | Resolving the EN related to preventing the legacy UEs from loop of registration requests due to incompatible N3IWF/TNGF with the allowed NSSAI | 18.4.0 |
| 2023-09 | CT#101 | CP-232200 | 5472 | 2 | F | VPLMN specific URSP changes | 18.4.0 |
| 2023-09 | CT#101 | CP-232205 | 5627 | 2 | A | Handling of un-authorized IAB UEs | 18.4.0 |
| 2023-09 | CT#101 | CP-232190 | 5491 | 2 | F | Condition for inclusion of Allowed PDU session status IE | 18.4.0 |
| 2023-09 | CT#101 | CP-232190 | 4785 | 6 | F | Condition for inclusion of Uplink data status IE in non-allowed service area | 18.4.0 |
| 2023-09 | CT#101 | CP-232192 | 5475 | 2 | F | Equivalent SNPNs: congestion control corrections | 18.4.0 |
| 2023-09 | CT#101 | CP-232192 | 5579 | 2 | F | Resolution of EN on equivalent SNPNs assignment during onboarding registration | 18.4.0 |
| 2023-09 | CT#101 | CP-232201 | 5501 | 2 | B | Support indications for user plane positioning | 18.4.0 |
| 2023-09 | CT#101 | CP-232201 | 5503 | 2 | B | Identification of PRU related to forwarded LCS messages | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5668 | 3 | B | Network Slice Replacement in roaming | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5624 | 2 | B | How to determine if the UE is in the NS-AoS | 18.4.0 |
| 2023-09 | CT#101 | CP-232198 | 5549 | 3 | B | UE unavailability period reporting overrides mobility management congestion control | 18.4.0 |
| 2023-09 | CT#101 | CP-232198 | 5616 | 2 | B | Updation of general section for unavailability period | 18.4.0 |
| 2023-09 | CT#101 | CP-232198 | 5630 | 2 | B | Updates to conditions for the support of unavailability period | 18.4.0 |
| 2023-09 | CT#101 | CP-232196 | 5572 | 3 | F | Release PDU session to share NSSRG value | 18.4.0 |
| 2023-09 | CT#101 | CP-232192 | 5471 | 2 | F | SOR-SNPN-SI-LS separate from SOR-SNPN-SI | 18.4.0 |
| 2023-09 | CT#101 | CP-232196 | 5525 | 3 | F | Handling of PDU session modification command when there are semantic errors in packet filters or QoS operations | 18.4.0 |
| 2023-09 | CT#101 | CP-232190 | 5543 | 2 | F | Cleanup on N5CW device supporting 3GPP access | 18.4.0 |
| 2023-09 | CT#101 | CP-232200 | 5608 | 2 | B | Resolve Editor's Note about URSP rule enforcement report indication | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5548 | 4 | F | Reestablishment of NAS connection with UP resource request | 18.4.0 |
| 2023-09 | CT#101 | CP-232241 | 5682 | 3 | B | Time validity information and location assistance information in SOR transport container | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5545 | 1 | F | LADN PDU session and data over NAS | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5654 | 1 | F | Correction on 5GMM capability IE encoding | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5663 | 1 | F | Use the null scheme if USIM is valid | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5600 | 1 | F | Correction to reject cause #62 | 18.4.0 |
| 2023-09 | CT#101 | CP-232204 | 5497 | 2 | F | Encoding of non-3gpp delay budget | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5568 | 1 | F | Optional support of network slice related features | 18.4.0 |
| 2023-09 | CT#101 | CP-232189 | 5671 | 1 | F | Ignore 5GSM congestion re-attempt indicator IE if receiving #39 | 18.4.0 |
| 2023-09 | CT#101 | CP-232190 | 5686 | 1 | F | Clarification on Back-off timer value IE conditions in network-initiated NAS transport procedure | 18.4.0 |
| 2023-09 | CT#101 | CP-232190 | 5672 | 1 | F | Clarification on abnormal case handling when PEIPS information is negotiatied | 18.4.0 |
| 2023-09 | CT#101 | CP-232190 | 5547 | 1 | F | Avoid UAC for UE acting as NCR-MT node | 18.4.0 |
| 2023-09 | CT#101 | CP-232190 | 5488 | 1 | F | Registration procedure handling for RACS | 18.4.0 |
| 2023-09 | CT#101 | CP-232190 | 5537 | 1 | F | Correction to the Payload container IE | 18.4.0 |
| 2023-09 | CT#101 | CP-232191 | 5470 | 1 | F | Time validity information format | 18.4.0 |
| 2023-09 | CT#101 | CP-232190 | 5516 | 1 | F | Not using mapped S-NSSAI when roaming in pre-Rel-17 network | 18.4.0 |
| 2023-09 | CT#101 | CP-232266 | 5646 | 1 | B | EAP methods for authenticating AUN3 devices behind 5G-RG | 18.4.0 |
| 2023-09 | CT#101 | CP-232191 | 5676 | 1 | F | NAS procdure collision with Validity information becomes not met | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5443 | 4 | F | NAS message handling in case of transmission failure for UE supporting partial network slice | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5692 | 1 | F | Correction on the maximum number of S-NSSAIs in partial NSSAI IE | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5693 | 1 | B | The partial network slice usage during the PDU session establishment procedure | 18.4.0 |
| 2023-09 | CT#101 | CP-232188 | 5493 | 1 | F | Clarification of handling of the slice deregistration inactivity timer in a case of MA PDU session | 18.4.0 |
| 2023-12 | CT#102 | CP-233162 | 5703 | - | D | Editorial corrections of SOR transparent container | 18.5.0 |
| 2023-12 | CT#102 | CP-233189 | 5726 | - | F | Correction to DNS over (D)TLS | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5517 | 1 | F | Correction to starting T3540 timer | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5518 | 1 | F | Correction to QoS handlling for empty packet filter list | 18.5.0 |
| 2023-12 | CT#102 | CP-233195 | 5733 | - | F | Resolution of editor's note for UAS_Ph2 | 18.5.0 |
| 2023-12 | CT#102 | CP-233182 | 5738 | - | F | Correction to ranging and sidelink positioning capability | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5751 | - | F | Correction to support for partial network slice | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5757 | - | F | Missing consideration of the allowed NSSAI and partially allowed NSSAI when using the Allowed PDU session status IE in the CPSR message | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5762 | - | F | Alternative NSSAI update during UCU and registration procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233166 | 5809 |  | F | URSP rule enforcement indication corrections | 18.5.0 |
| 2023-12 | CT#102 | CP-233151 | 5813 | - | F | Clarification on maintaining the user plane resources of the old non-3GPP access during the non-3GPP access path switching | 18.5.0 |
| 2023-12 | CT#102 | CP-233149 | 5815 | - | F | Clarification on the Key domain ID | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5666 | 1 | F | Correction on starting timer T3540 if indicate re-registration required | 18.5.0 |
| 2023-12 | CT#102 | CP-233140 | 5768 | 1 | A | Allowed NSSAI includes S-NSSAI(s) not contained in requested NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233148 | 5707 | 1 | B | Encoding of unavailability information and related corrections | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5783 | 1 | F | Clarify on Discontinuous Coverage Support negotiation | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5691 | 4 | B | Addition of the parameters of the Unavailability Period due to DC | 18.5.0 |
| 2023-12 | CT#102 | CP-233148 | 5752 | 1 | B | Encoding of unavailability configuration | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5791 | 1 | B | Updation for the timer handling for unavailability period activation. | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5801 | 1 | F | Solve EN about the unavailability period | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5810 | 1 | B | Updating the name for maximum time offset for unavailability period | 18.5.0 |
| 2023-12 | CT#102 | CP-233148 | 5606 | 3 | B | AS deactivation/activation during unavailability period | 18.5.0 |
| 2023-12 | CT#102 | CP-233128 | 5712 | 1 | F | Corrections on PRU | 18.5.0 |
| 2023-12 | CT#102 | CP-233128 | 5740 | 1 | F | Correction on term name of UPP information container | 18.5.0 |
| 2023-12 | CT#102 | CP-233128 | 5739 | 1 | F | Editor's note resolution on UPP-CMI container | 18.5.0 |
| 2023-12 | CT#102 | CP-233166 | 5705 | 1 | F | VPS URSP terminology alignment in 24.501 | 18.5.0 |
| 2023-12 | CT#102 | CP-233166 | 5706 | 1 | F | Received VPS URSP configuration when UE has no stored VPS URSP configuration | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5480 | 2 | F | UE policy sections and associated UPSCs | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5485 | 2 | F | Added UE policy section management list IE for SNPN operation mode | 18.5.0 |
| 2023-12 | CT#102 | CP-233150 | 5724 | 1 | C | Forbidden Area for AUN3 device behind 5G-RG | 18.5.0 |
| 2023-12 | CT#102 | CP-233150 | 5811 | 1 | B | Authentication for AUN3 devices supporting 5G key hierarchy | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5760 | 1 | F | NSAG information for alternative S-NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5761 | 1 | F | NS-AoS of alternative S-NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5710 | 1 | B | Updating the S-NSSAI location validity information IE coding | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5758 | 1 | F | Request lower layer to enter connected state for data over UP based on NS-AoS | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5763 | 1 | F | Control plane user data when the UE is outside NS-AoS | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5764 | 1 | F | Acknowledge the reception of S-NSSAI location or time validity information | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5728 | 1 | F | Reject cause for UE not supporting S-NSSAI time validity information | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5749 | 1 | F | Correction to the CONFIGURATION UPDATE COMMAND message | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5839 | 1 | B | Applicability of validity time information across access type | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5721 | 1 | F | Performing MRU for partially rejected NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5756 | 1 | F | Missing consideration of partially allowed NSSAI for handover of a session from non-3gpp to 3gpp | 18.5.0 |
| 2023-12 | CT#102 | CP-233166 | 5526 | 2 | C | Update the handling on collision of PDU session modification procedures | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5804 | - | B | UE storage of network slice usage control information | 18.5.0 |
| 2023-12 | CT#102 | CP-233162 | 5779 | 1 | F | Addition of SNPNs for localized service in SNPN along with GINs in forbidden lists | 18.5.0 |
| 2023-12 | CT#102 | CP-233162 | 5795 | 1 | B | Handling of equivalent SNPN for localized services | 18.5.0 |
| 2023-12 | CT#102 | CP-233151 | 5773 | 1 | F | Clarification on the non-3GPP path switching capability when a UE is registered to different PLMNs over 3GPP and non-3GPP accesses | 18.5.0 |
| 2023-12 | CT#102 | CP-233167 | 5828 | 1 | F | Extended LADN information deletion when enter deregistered | 18.5.0 |
| 2023-12 | CT#102 | CP-233189 | 5741 | 1 | F | UE act upon receiving 5GMM cause #76 | 18.5.0 |
| 2023-12 | CT#102 | CP-233190 | 5817 | 1 | F | Correction related to N5GC device supporting acting as EAP peer | 18.5.0 |
| 2023-12 | CT#102 | CP-233189 | 5711 | 1 | F | Correction on the Received MBS container IE coding | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5800 | 1 | F | Clarification of the UE behavior disabling N1 mode capability | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5800 | 1 | F | Clarification of the UE behavior disabling N1 mode capability | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5825 | 1 | F | Clarification related to Exception Data Reporting | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5489 | 2 | F | Access check of IMS registration during an ongoing IMS voice or video call | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5716 | 1 | F | Correction to PEIPS information in abnormal case | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5826 | 1 | F | The PLMN for pending and rejected NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233149 | 5814 | 1 | B | Deactivate MICO mode at the broadcast start time/activation times of a broadcast MBS session | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5743 | 1 | F | UE Behavior on expiry of timer | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5823 | 1 | F | Clarification on 5GMM status and Notification for T3540 handling | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5670 | 2 | F | Correction on use of and/or term | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5487 | 1 | F | 5GMM context storage when emergency attached | 18.5.0 |
| 2023-12 | CT#102 | CP-233140 | 5770 | 2 | A | Update configured NSSAI if slice subscription changed | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5717 | 2 | F | Remove coverage loss indication | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5639 | 4 | B | Update to discontinuous coverage overload control for mobility registration update | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5235 | 5 | F | UAC for Multiple Events | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5486 | 3 | F | Release of the NAS signalling connection established from 5GMM-IDLE mode | 18.5.0 |
| 2023-12 | CT#102 | CP-233150 | 5812 | 2 | B | Impact on NAS signalling for supporting authentication of AUN3 devices supporting and not supporting 5G key hierarchy | 18.5.0 |
| 2023-12 | CT#102 | CP-233199 | 5735 | 2 | F | Removing ENs for VMR | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5729 | 2 | F | Clarification of slice deregistration inactivity timer handling for MA PDU sessions | 18.5.0 |
| 2023-12 | CT#102 | CP-233151 | 5774 | 2 | F | Correction on handling of PDU sessions that are not requested to be moved to the new non-3GPP access | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5792 | 2 | F | Updation to Note to allign with stage-2 | 18.5.0 |
| 2023-12 | CT#102 | CP-233162 | 5746 | 3 | F | Removal of SNPN(s) from the equivalent SNPN list | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5834 | 2 | F | PDU session release collision | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5782 | 3 | F | Saving SNPN selection parameters for USIM in NV | 18.5.0 |
| 2023-12 | CT#102 | CP-233150 | 5725 | 2 | C | Service area restriction for AUN3 device behind 5G-RG | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5772 | 3 | B | Support of network slice usage control during the registration procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233189 | 5742 | 2 | F | Clarification on remove S-NSSAI from NSAG information | 18.5.0 |
| 2023-12 | CT#102 | CP-233162 | 5794 | 3 | B | T3247 for localized service | 18.5.0 |
| 2023-12 | CT#102 | CP-233130 | 5704 | 1 | B | Remote UE identified by PEI | 18.5.0 |
| 2023-12 | CT#102 | CP-233130 | 5820 | 1 | B | Authentication and key agreement procedure for 5G ProSe UE-to-UE relay | 18.5.0 |
| 2023-12 | CT#102 | CP-233195 | 5732 | 1 | F | Security and privacy for Direct C2 communications for UUAA-SM procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233182 | 5754 | 1 | F | Clarification on service request for ranging | 18.5.0 |
| 2023-12 | CT#102 | CP-233180 | 5713 | 1 | F | Correction to general clause for PIN service | 18.5.0 |
| 2023-12 | CT#102 | CP-233180 | 5714 | 1 | F | The PDU session handling related to PIN service | 18.5.0 |
| 2023-12 | CT#102 | CP-233195 | 5821 | 1 | B | Adding the A2X capability | 18.5.0 |
| 2023-12 | CT#102 | CP-233195 | 5731 | 2 | F | Security and privacy for Direct C2 communications for UUAA-MM procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5736 | 3 | F | Corrections to conditions for unavailability period reporting to override mobility management congestion control | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5831 | 2 | F | Handling of emergency services request when auth rejected | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5490 | 2 | F | E bit description in Mapped EPS bearer contexts IE and QoS flow descriptions IE | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5734 | 2 | F | URSP handling for UE configured with EHPLMN list | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5844 | 1 | F | Correction to the condition for stopping timer T3584 and T3585 | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5871 | - | F | Adding the Deregistration Request message | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5872 | - | B | Including alternative S-NSSAI in allowed and configured NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5837 | 1 | F | Clarification for the PDU session status IE in NOTIFICATION RESPONSE message | 18.5.0 |
| 2023-12 | CT#102 | CP-233164 | 5883 | - | F | Applicability of partially allowed NSSAI and partially rejected NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5886 | - | F | Applicable access type of S-NSSAI location or time validity information | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5892 | - | F | Corrections in storage of Extended Rejected NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5527 | 2 | F | PEIPS: Indicating Paging subgroup ID to Access Stratum layer | 18.5.0 |
| 2023-12 | CT#102 | CP-233140 | 5915 |  | A | Add missing posSibType to ciphering key data Rel-18 | 18.5.0 |
| 2023-12 | CT#102 | CP-233162 | 5918 | - | B | WLANSP from RSNPN | 18.5.0 |
| 2023-12 | CT#102 | CP-233182 | 5919 | - | B | SLPP transport | 18.5.0 |
| 2023-12 | CT#102 | CP-233195 | 5922 | - | F | Correction to service request trigger bullet numbering | 18.5.0 |
| 2023-12 | CT#102 | CP-233167 | 5923 | - | F | Clarification of LADN service area | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5929 | - | F | Remove the redundant case for unavailability during registration | 18.5.0 |
| 2023-12 | CT#102 | CP-233166 | 5931 |  | F | EN resolution on the UE to inform the stored tuples to the network | 18.5.0 |
| 2023-12 | CT#102 | CP-233150 | 5932 | - | B | Protecting the N3IWF/TNGF identifier information in the REGISTRATION REJECT message | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5944 | - | F | partially allowed NSSAI storage | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5953 | - | D | Clarification of abnormal case handling in service request procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5958 | - | F | Selection of an S-NSSAI by the AMF | 18.5.0 |
| 2023-12 | CT#102 | CP-233189 | 5868 | 1 | F | MPS NSAC note fix | 18.5.0 |
| 2023-12 | CT#102 | CP-233189 | 5866 | 1 | F | Redirection with MPS corrections | 18.5.0 |
| 2023-12 | CT#102 | CP-233184 | 5840 | 1 | F | Correction to SOR for Signal level enhanced network selection | 18.5.0 |
| 2023-12 | CT#102 | CP-233185 | 5911 | 1 | F | Correction on periodic update timer | 18.5.0 |
| 2023-12 | CT#102 | CP-233185 | 5913 | 1 | F | Clarification on UE behavior upon registration fails | 18.5.0 |
| 2023-12 | CT#102 | CP-233185 | 5959 | 1 | F | Clarification on support for unavailability period in non-3GPP accss | 18.5.0 |
| 2023-12 | CT#102 | CP-233162 | 5879 | 1 | F | Covering user reselection for localized service | 18.5.0 |
| 2023-12 | CT#102 | CP-233162 | 5847 | 1 | F | Congestion handling for UE accessing SNPN for localized services | 18.5.0 |
| 2023-12 | CT#102 | CP-233162 | 5698 | 6 | F | 5GMM sub-state handling for localized services in SNPN | 18.5.0 |
| 2023-12 | CT#102 | CP-233150 | 5723 | 2 | B | AUN3 device de-registration | 18.5.0 |
| 2023-12 | CT#102 | CP-233150 | 5644 | 5 | C | Rejecting the registration request of AUN3 device due to no existing 5G-RG connected to the same line | 18.5.0 |
| 2023-12 | CT#102 | CP-233150 | 5934 | 1 | F | Clarification for NAUN3 device connecting to 5GC via 5G-RG that is connected to NG-RAN | 18.5.0 |
| 2023-12 | CT#102 | CP-233128 | 5850 | 1 | F | Clarification on UE capability supporting the user plane connection between UE and LCS client or AF | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5924 | 1 | F | Correction on the UE state indication procedure initiation | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5775 | 3 | B | General introduction on support of network slice usage control | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5772 | 5 | B | Support of network slice usage control during the registration procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5771 | 4 | B | Support of network slice usage control during the UE configuration update procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5882 | 1 | F | Partially rejected NSSAI for RFSP derivation | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5884 | 1 | F | PDU session establishment associated to partially allowed S-NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5885 | 1 | F | Clarification on TA list associated with partial NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5908 | 1 | F | Releasing PDU sessions for temporarily available network slices | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5909 | 1 | F | Splitting of location and time validity information for S-NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5846 | 1 | F | Correction to the AMF handling for unavailability period | 18.5.0 |
| 2023-12 | CT#102 | CP-233148 | 5859 | 1 | B | The end of unavailability period report handling | 18.5.0 |
| 2023-12 | CT#102 | CP-233148 | 5861 | 1 | B | Handling T3448 timer during unavailability period | 18.5.0 |
| 2023-12 | CT#102 | CP-233145 | 5755 | 2 | F | Timer for NAS release when the start of unavailability period is not sent | 18.5.0 |
| 2023-12 | CT#102 | CP-233151 | 5935 | 2 | F | Corrections related to ATSSS steering functionalities and their usage (TS 24.501) | 18.5.0 |
| 2023-12 | CT#102 | CP-233167 | 5877 | 1 | B | PDU session establishment rejection for Maximum Group Data Rate control | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5949 | 1 | F | Updating MCS indicator via configuration update command procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5955 | 1 | D | Editorial corrections for NOTEs | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5887 | 1 | F | Abnormal case handling for T3550 time out | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5888 | 1 | F | Clarification on NSSAI storage | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5952 | 1 | F | Clarification of MPS validity | 18.5.0 |
| 2023-12 | CT#102 | CP-233142 | 5894 | 1 | F | Registration Reject in shared networks | 18.5.0 |
| 2023-12 | CT#102 | CP-233143 | 5954 | 1 | F | Consideration of satellite cell after disabling N1 mode | 18.5.0 |
| 2023-12 | CT#102 | CP-233143 | 5906 | 1 | F | List of networks where the N1 mode capability was disabled upon receipt of 5GMM cause #62 | 18.5.0 |
| 2023-12 | CT#102 | CP-233143 | 5956 | 1 | F | Missing DEREGISTRATION REQUEST message as content of a NAS message container IE | 18.5.0 |
| 2023-12 | CT#102 | CP-233143 | 5857 | 1 | F | Equivalent PLMN or SNPN list handling of rejecting message and network no response cases | 18.5.0 |
| 2023-12 | CT#102 | CP-233144 | 5856 | 1 | F | Correction due to PLMN Search state is not applicable to non-3GPP access | 18.5.0 |
| 2023-12 | CT#102 | CP-233190 | 5880 | 1 | F | Correction on additional information IE inclusion for LPP message transfer | 18.5.0 |
| 2023-12 | CT#102 | CP-233143 | 5479 | 5 | F | Correction of UE policy sections management | 18.5.0 |
| 2023-12 | CT#102 | CP-233140 | 5870 | 2 | A | Correction of definition and handling of HPLMN S-NSSAIs | 18.5.0 |
| 2023-12 | CT#102 | CP-233179 | 5875 | 2 | A | Correction on NSAG priority | 18.5.0 |
| 2023-12 | CT#102 | CP-233162 | 5702 | 4 | F | TAI based location assistance information | 18.5.0 |
| 2023-12 | CT#102 | CP-233185 | 5912 | 2 | F | Clarification on 5GMM context | 18.5.0 |
| 2023-12 | CT#102 | CP-233143 | 5893 | 1 | F | Locally setting mapped NSSAI for the Extended rejected NSSAI | 18.5.0 |
| 2023-12 | CT#102 | CP-233150 | 5933 | 2 | B | 5GMM context for the AUN3 device | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5930 | 2 | B | On-demand NSSAI storage | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5896 | 2 | F | Update slice deregistration inactivity timer value | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5873 | 1 | B | Alternative S-NSSAI not part of subscribed S-NSSAIs | 18.5.0 |
| 2023-12 | CT#102 | CP-233185 | 5957 | 2 | F | Minor corrections of ambiguous texts in clause related to unavailability period | 18.5.0 |
| 2023-12 | CT#102 | CP-233132 | 5950 | 1 | F | Clarification on determining the RRC establishment cause value for 5G ProSe L2 U2N relay UE | 18.5.0 |
| 2023-12 | CT#102 | CP-233182 | 5881 | 1 | F | Network capability to UE | 18.5.0 |
| 2023-12 | CT#102 | CP-233143 | 5863 | 2 | F | UE behaviour in case of RRC Connection failure and fallback indication from lower layers | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5898 | 2 | B | Clarification of the UE storage of network slice usage control information. | 18.5.0 |
| 2023-12 | CT#102 | CP-233128 | 5903 | 2 | F | PRU enhancement of UE-initiated NAS transport of messages accepted by the network | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5895 | 3 | F | Clarification on UE stored slice usage control information | 18.5.0 |
| 2023-12 | CT#102 | CP-233148 | 5860 | 2 | B | Receiving unavailability period duration from the network | 18.5.0 |
| 2023-12 | CT#102 | CP-233149 | 5937 | 2 | B | Supporting multicast MBS session and Broadcast MBS session for UE that uses eDRX | 18.5.0 |
| 2023-12 | CT#102 | CP-233143 | 5832 | 3 | F | Correction to forbidden TAI handling for reject cause #62 | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5940 | 2 | B | UE behaviour of slice deregistration inactivity timer regarding MA PDU session in PDU session release procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5948 | 2 | F | Network behavior for on-demand NSSAI in the Generic UE configuration update procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233165 | 5942 | 2 | B | UE behaviour of slice deregistration inactivity timer regarding MA PDU session in PDU session establishment procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233167 | 5926 | 5 | F | UE behavior in overlapping areas between LADN service area and partial network slice support area | 18.5.0 |
| 2023-12 | CT#102 | CP-233143 | 5864 | 2 | D | Miscellaneous corrections | 18.5.0 |
| 2023-12 | CT#102 | CP-233189 | 5917 | 2 | F | Clarificaiton on storage of NSAG information | 18.5.0 |
| 2023-12 | CT#102 | CP-233121 | 5921 | 3 | B | UPP-CMI container transport | 18.5.0 |
| 2023-12 | CT#102 | CP-233204 | 5878 | 6 | B | Location validity information for localized services | 18.5.0 |
| 2023-12 | CT#102 | CP-233317 | 5927 | 3 | F | Clarification on the unavalability period in deregistration procedure | 18.5.0 |
| 2023-12 | CT#102 | CP-233141 | 5653 | 5 | F | Clarification on the network behavior when sending CC #76 via non-CAG cell | 18.5.0 |
| 2024-03 | CT#103 | CP-240087 | 5963 | 1 | F | Minor corrections for Payload container information IE | 18.6.0 |
| 2024-03 | CT#103 | CP-240087 | 5965 | 1 | F | Correction on the definition of UPP-CMI | 18.6.0 |
| 2024-03 | CT#103 | CP-240087 | 5966 | 1 | F | Correction on network indication of supported user plane location solution(s) | 18.6.0 |
| 2024-03 | CT#103 | CP-240125 | 5977 | - | D | Minor corrections | 18.6.0 |
| 2024-03 | CT#103 | CP-240125 | 5993 | - | F | UE capability indication to the network for network verified UE location support | 18.6.0 |
| 2024-03 | CT#103 | CP-240089 | 6014 | - | F | Correction on capability indication for 5G ProSe layer-2 end UE | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6016 | - | F | Clarification on the access type of on-demand NSSAI | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6017 | - | F | Corrections on coding description of the Service-level-AA container | 18.6.0 |
| 2024-03 | CT#103 | CP-240097 | 6020 | - | F | Correction to the TNAN information IE | 18.6.0 |
| 2024-03 | CT#103 | CP-240125 | 6021 | - | F | Correction to IEEE standards references | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6023 | - | F | Correction to an unnecessary sentence | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6029 | - | F | AMF behavior when non-supporting UE is outside NS-AoS | 18.6.0 |
| 2024-03 | CT#103 | CP-240119 | 6035 | - | F | Correction on the N3QAI and non-3GPP delay budget | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6036 | - | F | Correction on the PLMN code | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6037 | - | F | Correction on the PEIPS assistance information | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6051 | - | F | Service-level AA and congestion | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6072 | - | F | Performing both UUAA-MM and UUAA-SM | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6086 | - | F | Correction to 5GMM cause and table number for 5GMM STATUS | 18.6.0 |
| 2024-03 | CT#103 | CP-240099 | 6088 | - | F | Corrections for the UE capabilities related to the ATSSS steering functionalities | 18.6.0 |
| 2024-03 | CT#103 | CP-240125 | 6091 | - | F | Corrections for setting the TPMIC bit in the 5GSM capability IE | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 6114 | - | F | Correction to encoding of unavailability configuration | 18.6.0 |
| 2024-03 | CT#103 | CP-240109 | 6061 | 1 | A | Correction on the minimum length of the SLAC | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6028 | 1 | F | Network slice replacement considering NS-AoS | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6079 | 1 | B | Removal of replaced slice from allowed NSSAI due to being out of NS-AoS | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6075 | 1 | F | Addition of Alternative slice in Allowed and/or Configured NSSAI for network slice replacement | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 5987 | 1 | F | Registration accept type 6 IE container corrections | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6030 | 1 | F | Downlink data handling when UE location is unknown | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6031 | 1 | F | Session management when the UE is in a cell not within NS-AoS of S-NSSAI | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6085 | 1 | F | Correction regarding S-NSSAI location validity information | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6044 | 1 | F | Condition for inclusion of partially allowed NSSAI | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6012 | 1 | F | Correction on On-demand NSSAI IE coding | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6033 | 1 | F | Network slice usage control not applicable for emergency services | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6056 | 1 | F | Clarifies when the slice deregistration inactivity timer starts when it is updated. | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6125 | 1 | F | Termilogy align of the Network slice usage control information | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6129 | - | F | Correction to timers handling in MICO mode | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 6024 | 1 | F | Correction to the term unavailability duration | 18.6.0 |
| 2024-03 | CT#103 | CP-240097 | 6068 | 1 | F | Registration rejection due to AUN3 device connectivity not allowed | 18.6.0 |
| 2024-03 | CT#103 | CP-240097 | 6084 | 1 | B | USRP rule enforcement reporting is not supported by 5G-RG and FN-RG | 18.6.0 |
| 2024-03 | CT#103 | CP-240105 | 6010 | 1 | F | UE handling of SOR-SNPN-SI-LS | 18.6.0 |
| 2024-03 | CT#103 | CP-240105 | 6011 | 1 | F | Reference on SNPN selected for localized services in SNPN | 18.6.0 |
| 2024-03 | CT#103 | CP-240087 | 6019 | 1 | B | Add Additional information IE for UPP-CMI container in UE inititated NAS transport procedure | 18.6.0 |
| 2024-03 | CT#103 | CP-240108 | 5360 | 8 | B | Connection Capabilities in N1 SM container | 18.6.0 |
| 2024-03 | CT#103 | CP-240108 | 6069 | 1 | F | URSP provisioning in EPS and PDU session / PDN connection transferred between 5GS and EPS | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 6001 | 1 | B | Handling NOTIFICATION when UE unavailable | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 6098 | 1 | F | Clarification on the periodic registration update timer | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 6104 | 1 | F | Clarification on NAS timer value handling for satellite NG-RAN access | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6047 | 1 | F | Correction in clause for AUTH failure in SNPN with no CH support | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6009 | 1 | F | Storing NAS security context due to registering to different PLMN in the same access | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 5938 | 3 | F | Correction for PDU session type selection in the RSD | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6046 | 1 | F | Clarification of USIM validity for 5GS services | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6048 | 1 | F | Missing clause for KAMF derivation for SNPN | 18.6.0 |
| 2024-03 | CT#103 | CP-240131 | 6063 | 1 | F | Clarification of MBSR authorization indication during registration procedure | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 5985 | 1 | F | 5GSM message transfer in a TA with service area restrictions in 5GMM-CONNECTED mode | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6050 | 1 | F | DL NAS TRANSPORT message with N1 SM information and undefined cause value | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 5043 | 3 | F | Handling of SOR counter and the UE parameter update counter if stored in NVM | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6096 | 1 | F | Minor Correction for AMF supporting interworking with EPS | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6101 | 1 | F | Provision of NSAG information to lower layers for SR for UL signalling | 18.6.0 |
| 2024-03 | CT#103 | CP-240093 | 6078 | 1 | F | Correction to referred SM NAS timer table for satellite | 18.6.0 |
| 2024-03 | CT#103 | CP-240120 | 5992 | 1 | F | Corrections to the network indication to the UE for ranging and sidelink positioning support | 18.6.0 |
| 2024-03 | CT#103 | CP-240120 | 6015 | 1 | F | Modification on naming of ranging and sidelink capability | 18.6.0 |
| 2024-03 | CT#103 | CP-240120 | 6100 | 3 | C | Update UE ranging and sidelink positioning capability per role | 18.6.0 |
| 2024-03 | CT#103 | CP-240088 | 6053 | 1 | F | Remote UE report collision with connection release | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6022 | 1 | F | Clarfication on the MRU procedure for on-demand S-NSSAI(s) registration | 18.6.0 |
| 2024-03 | CT#103 | CP-240125 | 5939 | 3 | F | Clarification on NSSAI provide to lower layers | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6107 | 1 | F | Clarification on requested NSSAI on alternative NSSAI | 18.6.0 |
| 2024-03 | CT#103 | CP-240094 | 6105 | 1 | F | Clarification on maximum number of S-NSSAI in requested NSSAI | 18.6.0 |
| 2024-03 | CT#103 | CP-240097 | 6083 | 2 | F | The handling of 5GMM parameters upon receiving Registration Reject with cause #81 or #82 | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6027 | 2 | F | Alternative S-NSSAI or S-NSSAI to be replaced subject to NSSAA | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6043 | 2 | F | Deleting Partially Allowed and Partially Rejected NSSAI | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6128 | 2 | F | Clarification on UE, AMF and SMF behaviour regarding network slice replacement | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 5981 | 2 | C | Handling of unavailability period in the initial registration procedure | 18.6.0 |
| 2024-03 | CT#103 | CP-240094 | 6049 | 2 | F | 5GMM handling when receiving cause 80 | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 6054 | 2 | F | Stop discontinuous coverage maximum time offset timer on receiving NOTIFICATION message. | 18.6.0 |
| 2024-03 | CT#103 | CP-240094 | 6109 | 1 | F | Delete QoS rule when rejected with CC #31 | 18.6.0 |
| 2024-03 | CT#103 | CP-240094 | 6073 | 1 | F | UAC and network-requested PDU session modification procedure | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6034 | 2 | F | Correction on NSUC bit in the 5GMM capability IE | 18.6.0 |
| 2024-03 | CT#103 | CP-240096 | 6102 | 3 | F | Support of MBS data reception for UEs using power saving functions | 18.6.0 |
| 2024-03 | CT#103 | CP-240105 | 5920 | 4 | B | CP-SOR corrections in 24.501 | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6123 | 3 | F | Further clarification on the handle of changed TAI case | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6124 | 3 | F | Network slice usage control applicability in roaming scenarios | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 6099 | 2 | F | Clarification on the unavailability period duration | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 5978 | 3 | F | S-NSSAI time validity expiry for last allowed S-NSSAI, alternative 1 | 18.6.0 |
| 2024-03 | CT#103 | CP-240132 | 6013 | 2 | B | Clarification on PDU set handling | 18.6.0 |
| 2024-03 | CT#103 | CP-240132 | 5649 | 11 | B | General description of PDU set handling | 18.6.0 |
| 2024-03 | CT#103 | CP-240094 | 6108 | 3 | F | Clarification on inter-system change for UE registered for emergency services | 18.6.0 |
| 2024-03 | CT#103 | CP-240094 | 6110 | 3 | F | Clarification on failed instruction order | 18.6.0 |
| 2024-03 | CT#103 | CP-240094 | 6040 | 3 | F | MRU to register additional slices available from Configured NSSAI. | 18.6.0 |
| 2024-03 | CT#103 | CP-240105 | 6055 | 3 | F | Re-enable N1 mode for SNPN on validity condition met | 18.6.0 |
| 2024-03 | CT#103 | CP-240131 | 6059 | 2 | F | Release the PDU session to support of the MBSR | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6062 | 2 | F | PDU session associated with replaced S-NSSAI | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 6092 | 3 | B | Slice replacement back to the replaced S-NSSAI | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 6066 | 2 | B | Addition of start of unavailability configuration from the NW to the UE | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 5928 | 6 | F | Clarification on the unavailability period | 18.6.0 |
| 2024-03 | CT#103 | CP-240095 | 6115 | 4 | F | Correction on support for unavailability period | 18.6.0 |
| 2024-03 | CT#103 | CP-240128 | 6065 | 3 | F | LADN Provisioning when there is existing PDU session | 18.6.0 |
| 2024-03 | CT#103 | CP-240094 | 6103 | 3 | F | Clarification on common NSSRG value for for pending NSSAI | 18.6.0 |
| 2024-03 | CT#103 | CP-240125 | 6018 | 2 | F | Correction of the conditions for initiating a de-registration in 5GMM-REGISTERED.ATTEMPTING-TO-UPDATE and 5GMM-REGISTERED.UPDATE-NEEDED | 18.6.0 |
| 2024-03 | CT#103 | CP-240094 | 5983 | 3 | F | Corrections to the access identity 1 & 2 handling | 18.6.0 |
| 2024-03 | CT#103 | CP-240106 | 5989 | 3 | F | PDU Session management when the UE is outside the area of slice support or availability | 18.6.0 |
| 2024-03 | CT#103 | CP-240219 | 5988 | 6 | F | Clarifications on Network slice replacement | 18.6.0 |
| 2024-03 | CT#103 | CP-240248 | 5973 | 6 | B | Protocol description support | 18.6.0 |
| 2024-03 | CT#103 | CP-240250 | 5976 | 1 | F | Unavailability information IE inclusion | 18.6.0 |
| 2024-03 | CT#103 | CP-240286 | 6106 | 3 | F | Reset counter when activating unavailability period | 18.6.0 |
| 2024-03 | CT#103 | CP-240291 | 5986 | 4 | F | Inclusion of SSC mode IE in case of inter-system change to N1 mode | 18.6.0 |
| 2024-03 | CT#103 | CP-240293 | 6007 | 4 | F | Change in unavailability information | 18.6.0 |
| 2024-03 | CT#103 | CP-240294 | 6008 | 3 | F | Correction to timers handling in unavailability period | 18.6.0 |
| 2024-03 | CT#103 | CP-240295 | 5996 | 2 | F | 5GMM state when disaster wait timer is running | 18.6.0 |
| 2024-06 | CT#104 | CP-241178 | 6141 | - | F | Correction to abnormal cases on the network side | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6142 | - | F | Corrections to incorrect agreed CR5983 not noticed till CR implementation | 18.7.0 |
| 2024-06 | CT#104 | CP-241164 | 6143 | - | F | Handling of T3444 and T3445 during UA activation | 18.7.0 |
| 2024-06 | CT#104 | CP-241178 | 6146 | - | F | Correction to the PDU SESSION ESTABLISHMENT REQUEST message | 18.7.0 |
| 2024-06 | CT#104 | CP-241176 | 6158 | - | F | Congestion handling for SNPN providing access for localized services in SNPN | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6167 | - | D | Removal of duplicated paragraph for on-demand NSSAI in initial registration | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6171 | - | F | SMF performs NSAC for replaced S-NSSAI and alternative S-NSSAI | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6172 | - | F | Term consistency for replaced S-NSSAI | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6181 | - | F | Corrections to subject of subclause 5.4.5.3.3 | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6203 | - | F | Correction on N1 mode capability handling during SoR procedure in connected mode | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6212 | - | F | Correction for the Start of the unavailability period | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6216 | - | F | Clarification for AMF behaviour on UE location verification for satellite access | 18.7.0 |
| 2024-06 | CT#104 | CP-241203 | 6223 | - | D | Editorial correction for MBSR | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6147 | 1 | F | Correction to the CONFIGURATION UPDATE COMMAND message | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6173 | 1 | F | Correction on CIoT user data transmission for network slice with NS-AoS and partial network slice | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6175 | 1 | F | Inclusion of Allowed PDU session status IE considering S-NSSAI location validity information | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6217 | 1 | F | Correction on the parameter name in the S-NSSAI time validity information IE | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6150 | 1 | F | Correcting requirements for emergency services and the network slice usage control for the S-NSSAI | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6177 | 1 | F | Term definition for on-demand S-NSSAI and on-demand NSSAI | 18.7.0 |
| 2024-06 | CT#104 | CP-241175 | 6153 | 1 | F | SOR-SNPN-SI and SOR-SNPN-SI-SL indicators set in UL NAS transport | 18.7.0 |
| 2024-06 | CT#104 | CP-241176 | 6221 | 1 | F | Reference corrections in SNPN clause | 18.7.0 |
| 2024-06 | CT#104 | CP-241165 | 6136 | 1 | F | Handling of abnormal cases of cause 81 and 82 | 18.7.0 |
| 2024-06 | CT#104 | CP-241165 | 6192 | 1 | F | Definitions and abbreviations for NAUN3 device and AUN3 device | 18.7.0 |
| 2024-06 | CT#104 | CP-241178 | 6206 | 1 | F | URSP rule enforcement reporting after an inter-system change from S1 mode to N1 mode | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6164 | 1 | F | Consideration of discontinuous coverage maximum time offset for determination of periodic T3512 timer. | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6166 | 1 | F | Tsense timer handling for MICO mode | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6201 | 1 | F | Updation of the initial registration accept handling for the start of unavailability period time. | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6215 | 1 | F | Clarification on the unavailability case in registration procedure | 18.7.0 |
| 2024-06 | CT#104 | CP-241167 | 6185 | 1 | F | Corrections to NAS transport for Non-3GPP access path switching | 18.7.0 |
| 2024-06 | CT#104 | CP-241204 | 6200 | 1 | F | Abbreviations for PDU set handling | 18.7.0 |
| 2024-06 | CT#104 | CP-241179 | 6154 | 1 | F | AMF handling on LADN provisioning for an existing PDU session | 18.7.0 |
| 2024-06 | CT#104 | CP-241179 | 6191 | 1 | F | Correction to the area restriction for LADN | 18.7.0 |
| 2024-06 | CT#104 | CP-241179 | 6193 | 1 | F | Correction to the inclusion condition of extended LADN information | 18.7.0 |
| 2024-06 | CT#104 | CP-241179 | 6194 | 1 | F | Correction to the wrong message name for LADN information | 18.7.0 |
| 2024-06 | CT#104 | CP-241179 | 6219 | 1 | F | Clarification of ambiguous statement for LADN | 18.7.0 |
| 2024-06 | CT#104 | CP-241165 | 6182 | 1 | F | Clarification of ANDSP and URSP coding | 18.7.0 |
| 2024-06 | CT#104 | CP-241199 | 6195 | 1 | F | Add abbreviation for ABBAf | 18.7.0 |
| 2024-06 | CT#104 | CP-241199 | 6197 | 1 | D | Minor corrections | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6052 | 2 | F | Clarification on disabling and enabling N1 mode for deregistration abnormal | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6160 | 1 | F | The UE handling on the MICO mode | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6186 | 1 | F | Correction to PDU session reactivation result IE | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6202 | 1 | F | Handling of congestion control for transport of user data via the control plane timer for emergency services | 18.7.0 |
| 2024-06 | CT#104 | CP-241164 | 6130 | 2 | F | Clarification on the negotiation of the unavailability period duration during initial registration procedure | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6170 | 2 | F | Remove alternative S-NSSAI from allowed NSSAI and configured NSSAI | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6071 | 4 | F | Inter-system change for SSC mode 2 or SSC mode 3 PDU session | 18.7.0 |
| 2024-06 | CT#104 | CP-241159 | 6152 | 3 | F | Handling of regulatory prioritized services in non-allowed area | 18.7.0 |
| 2024-06 | CT#104 | CP-241179 | 6188 | 2 | F | Clarification to the S-NSSAI in extended LADN information | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6207 | 2 | F | Handling of collision between 5GMM common procedure and deregistration procedure. | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6199 | 2 | F | Updation on the condition for AMF to determine periodic timer | 18.7.0 |
| 2024-06 | CT#104 | CP-241192 | 6139 | 1 | F | Minor corrections | 18.7.0 |
| 2024-06 | CT#104 | CP-241161 | 6135 | 2 | F | Handling of Restricted service area cause in non-restricting cases | 18.7.0 |
| 2024-06 | CT#104 | CP-241180 | 6137 | 2 | F | Handling of UAS services not allowed cause for a UE not supporting UAS services | 18.7.0 |
| 2024-06 | CT#104 | CP-241164 | 6178 | 2 | F | Corrected that the deregistration procedure is used only for non satellite cases. | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6237 | - | F | Applicability of DefaultNSSAIInclusionMode | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6251 | - | F | Missing occurrence of the CPSR message for existing abnormal cases | 18.7.0 |
| 2024-06 | CT#104 | CP-241153 | 6253 | - | F | Removal of UPP-CM | 18.7.0 |
| 2024-06 | CT#104 | CP-241204 | 6228 | 5 | F | Corrections for aligning statements for UL PDU set handling | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6257 | - | F | Network slice replacement during PDU session establishment procedure | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6262 | - | F | Remove redundant paragraph for network slice usage control | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6263 | - | F | Network slice usage control for non-supporting UE | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6264 | - | F | Slice deregistration inactivity timer per access type | 18.7.0 |
| 2024-06 | CT#104 | CP-241153 | 6265 | - | F | DL NAS transport of UPP-CMI container | 18.7.0 |
| 2024-06 | CT#104 | CP-241204 | 6198 | 2 | F | Correction to RTP header extension in Protocol description IE | 18.7.0 |
| 2024-06 | CT#104 | CP-241204 | 6270 | - | F | Delete protocol description associated with a QoS rule | 18.7.0 |
| 2024-06 | CT#104 | CP-241164 | 6294 | - | F | Correction to handling of Follow-on request indicator in MRU for UA | 18.7.0 |
| 2024-06 | CT#104 | CP-241164 | 6298 | - | F | Clarification of T3324 in UA | 18.7.0 |
| 2024-06 | CT#104 | CP-241164 | 6299 | - | F | NR disable timers and unavailability period | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6305 |  | F | Clarification on initial registration for emergency services | 18.7.0 |
| 2024-06 | CT#104 | CP-241175 | 6306 | - | D | Minor correction of wrong NOTE numbering | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6309 | - | F | Add reference to the satellite coverage availability information | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6321 | - | F | Correction on missing abbreviations | 18.7.0 |
| 2024-06 | CT#104 | CP-241204 | 6180 | 2 | F | Clarification on UL PDU set handling | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6248 | 1 | F | Correction on coding of S-NSSAI location validity information | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6259 | 1 | F | Transition to RRC_CONNECTED state considering partially allowed NSSAI and S-NSSAI location validity information | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6260 | 1 | F | Maximum number of S-NSSAIs in allowed NSSAI and partially allowed NSSAI | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6250 | 1 | F | Slice deregistration timer during MICO | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6300 | 1 | F | Clarification of slice deregistration timer in deregistered state | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6313 | 1 | F | Slice deregistration inactivity timer for PDU session release | 18.7.0 |
| 2024-06 | CT#104 | CP-241164 | 6268 | 1 | D | Editorial corrections on unavailability configuration and unavailability information | 18.7.0 |
| 2024-06 | CT#104 | CP-241175 | 6240 | 1 | F | Corrections for forbidden SNPNs in 24.501 | 18.7.0 |
| 2024-06 | CT#104 | CP-241176 | 6266 | 1 | D | Correction on 5GMM capability indication for equivalent SNPNs support | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6174 | 1 | F | Maximum number of S-NSSAIs in S-NSSAI location validity information IE | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6307 | 1 | F | Correction about terminology regarding 5GSAT | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6279 | 1 | F | Clarification on the unavailability due to UE reasons | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6277 | 1 | F | Clarification on the end of unavailability period report | 18.7.0 |
| 2024-06 | CT#104 | CP-241204 | 6229 | 4 | F | Update UL PDU Set handling when inter-system change | 18.7.0 |
| 2024-06 | CT#104 | CP-241165 | 6274 | 1 | F | Correction for the TNGF ID | 18.7.0 |
| 2024-06 | CT#104 | CP-241184 | 6242 | 1 | D | Replacement of MS with UE for the term MS determined PLMN with disaster condition | 18.7.0 |
| 2024-06 | CT#104 | CP-241198 | 6273 | 1 | F | Clarifications related to QoS flow descriptions | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6261 | 1 | F | Registration complete message to acknowledge the reception of on-demand NSSAI | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6140 | 2 | F | UE identity handling in case of a USIM removal during a registration procedure | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6267 | 1 | F | Clarification on purpose of service request procedure | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6280 | 1 | F | Clarification on some causes received in cell belonging to SNPN | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6281 | 1 | F | Correction on Extended CAG information list IE | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6196 | 3 | F | Correction to the checking of allowed TAI list in attempting to update state. | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6304 | 1 | D | Minor corrections in cause#36 and #62 | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6317 | 1 | F | Revise confusing statement in HPLMN S-NSSAI(s) handling | 18.7.0 |
| 2024-06 | CT#104 | CP-241164 | 6289 | 2 | D | Clarification of ambiguity in clause 5.3.26 | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6258 | 2 | F | Clarification when the only allowed S-NSSAI expires | 18.7.0 |
| 2024-06 | CT#104 | CP-241167 | 6275 | 2 | F | Corrections on supporting steering modes for the MA PDU session | 18.7.0 |
| 2024-06 | CT#104 | CP-241204 | 6224 | 2 | F | Clarification for QoS rule associated with UL Protocol description | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6156 | 7 | F | Re-enable N1 Mode based on timer validity information | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6190 | 4 | F | Handling of PDU session reactivation when the UE is not located in NS-AoS | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6278 | 2 | F | Clarification on the unavailability configuration during initial registration | 18.7.0 |
| 2024-06 | CT#104 | CP-241198 | 6234 | 2 | F | T3448 exemption for MPS | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 6074 | 5 | F | MINT corrections in 24.501 | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 5997 | 5 | F | Disaster timers handling | 18.7.0 |
| 2024-06 | CT#104 | CP-241203 | 6272 | 2 | F | Clarification on AMF behavior during the deregistration procedure | 18.7.0 |
| 2024-06 | CT#104 | CP-241160 | 5995 | 5 | F | MM parameter handling when receiving DL NAS transport message with cause 78 | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6288 | 2 | F | Update of partially allowed NSSAI for network slice replacement operation in the configuration update procedure and registration procedure | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6314 | 2 | F | Slice deregistration inactivity timer at unavailability activation | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6252 | 4 | F | Start of the slice inactivity timer based on the PDU session status IE | 18.7.0 |
| 2024-06 | CT#104 | CP-241198 | 6247 | 2 | F | Corrections to satellite access technologies in disabling and re-enabling of UE's N1 mode capability for 3GPP access | 18.7.0 |
| 2024-06 | CT#104 | CP-241177 | 6311 | 3 | F | NSSAI List Clarification | 18.7.0 |
| 2024-06 | CT#104 | CP-241198 | 6245 | 2 | A | Custom throttling to temporary failed 5GSM procedure | 18.7.0 |
| 2024-06 | CT#104 | CP-241170 | 6244 | 2 | F | Remove NOTE on DNS over (D)TLS | 18.7.0 |
| 2024-06 | CT#104 | CP-241170 | 5968 | 6 | B | Update to add security parameter to ECS address IE | 18.7.0 |
| 2024-06 | CT#104 | CP-241163 | 6249 | 4 | C | 5GMM cause code #15 indicating Satellite NG-RAN not allowed in PLMN | 18.7.0 |
| 2024-06 | CT#104 | CP-241227 | 6149 | 3 | F | Correction of the procedure's name | 18.7.0 |
| 2024-06 | CT#104 | CP-241231 | 6162 | 4 | F | Disaster return wait range timer | 18.7.0 |
| 2024-09 | CT#105 | CP-242165 | 6330 | - | A | Adding inclusion criteria and correcting information element | 18.8.0 |
| 2024-09 | CT#105 | CP-242167 | 6398 | - | F | Collision handling for NSSAA procedure and MRU for release connection | 18.8.0 |
| 2024-09 | CT#105 | CP-242205 | 6334 | 1 | F | Correction of IEI for Protocol description IE | 18.8.0 |
| 2024-09 | CT#105 | CP-242184 | 6365 | 1 | F | Handling of PDU session reactivation in the Mobility registration update procedure | 18.8.0 |
|  |  |  |  |  |  |  |  |
| 2024-09 | CT#105 | CP-242184 | 6410 | 1 | F | Network slice replacement including an on-demand S-NSSAI | 18.8.0 |
| 2024-09 | CT#105 | CP-242167 | 6338 | 1 | F | 5GMM capability IE definition errors | 18.8.0 |
| 2024-09 | CT#105 | CP-242184 | 6347 | 1 | F | Correction to the 5GMM capability IE because of implementation error of CR6034 | 18.8.0 |
|  |  |  |  |  |  |  |  |
| 2024-09 | CT#105 | CP-242167 | 6352 | 1 | F | Clarification for coding and usage of UE POLICY PROVISIONING REQUEST message | 18.8.0 |
| 2024-09 | CT#105 | CP-242167 | 6387 | 1 | F | Correction of incomplete timer table for T3540 | 18.8.0 |
| 2024-09 | CT#105 | CP-242190 | 6391 | 1 | F | Correction to requirements upon determining that a disaster condition has ended for MINT because of implementation collision of CR6074 and CR6162 | 18.8.0 |
| 2024-09 | CT#105 | CP-242167 | 6405 | 1 | F | Update description on requirements to be met for MT SMSoIP | 18.8.0 |
|  |  |  |  |  |  |  |  |
| 2024-09 | CT#105 | CP-242171 | 6434 | 1 | F | Resolution of editor's notes on Maximum time offset | 18.8.0 |
| 2024-09 | CT#105 | CP-242193 | 6341 | 1 | F | Correction for undefined names | 18.8.0 |
| 2024-09 | CT#105 | CP-242177 | 6345 | 2 | F | Add list of supported PLMNs with ECSP information to the ECS address information | 18.8.0 |
| 2024-09 | CT#105 | CP-242205 | 6348 | 2 | F | Correction to the uplink PDU set handling at the UE side | 18.8.0 |
| 2024-09 | CT#105 | CP-242171 | 6002 | 8 | F | No T3540 entering unavailability period | 18.8.0 |
| 2024-09 | CT#105 | CP-242183 | 6424 | 2 | F | FSNPN in shared network | 18.8.0 |
| 2024-09 | CT#105 | CP-242199 | 6301 | 4 | F | Handling of ecall timers during intersystem between 2G/3G and 5G | 18.8.0 |
| 2024-09 | CT#105 | CP-242171 | 6342 | 2 | F | Corrections for Cause value 15, satellite disabling | 18.8.0 |
| 2024-09 | CT#105 | CP-242230 | 6429 | 4 | F | Correction to the Note for UEs supporting MUSIM | 18.8.0 |
| 2024-09 | CT#105 | CP-242184 | 6404 | 1 | F | Correction on description of the slice deregistration inactivity timer in 4.6.2.9 | 19.0.0 |
| 2024-09 | CT#105 | CP-242201 | 6419 | 1 | F | Missing handling of cause #36 | 19.0.0 |
| 2024-09 | CT#105 | CP-242171 | 6364 | 1 | F | Clarification on the maximum time offset | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6344 | - | F | Storage of N26 support in NVM | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6346 | - | D | Corrigenda | 19.0.0 |
| 2024-09 | CT#105 | CP-242171 | 6362 | - | F | Consistent usage of EUPR bit of Unavailability configuration IE | 19.0.0 |
| 2024-09 | CT#105 | CP-242184 | 6363 | - | D | Remove duplicated paragraph regarding UE behavior after receiving on-demand NSSAI | 19.0.0 |
| 2024-09 | CT#105 | CP-242170 | 6372 | - | F | Non-3GPP path switching while using old non-3GPP for MA PDU session | 19.0.0 |
| 2024-09 | CT#105 | CP-242164 | 6380 | - | F | Correction to the inconsistent LCS correlation identifier | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6397 | - | F | Performing service request for emergency services fallback when the network is performing NSSAA | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6399 | 1 | F | Correction on the 5GSM cause reason | 19.0.0 |
| 2024-09 | CT#105 | CP-242171 | 6388 | 1 | F | Correction regarding the discontinuous coverage maximum time offset timer | 19.0.0 |
| 2024-09 | CT#105 | CP-242165 | 6390 | 1 | F | Correction of terminology related to 5GProSe | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6413 | 1 | D | Miscellaneous editorial corrections | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6366 | 1 | F | Correction to the trigger for the de-registration procedure | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6356 | 1 | F | Correction on the definition of HPLMN S-NSSAI | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6371 | 1 | F | Correction to the De-registration type IE | 19.0.0 |
| 2024-09 | CT#105 | CP-242174 | 6349 | 1 | F | Correction to the condition for UE-initiated de-registration procedure at the UE side | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6435 | 1 | F | Clarification of NAS timer handling for NG-RAN Satellite Access | 19.0.0 |
| 2024-09 | CT#105 | CP-242171 | 6375 | 1 | F | Correction on maximum time offset | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6430 | - | F | Correction on format and grammar issues | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6368 | 2 | F | T3525 abnormal case in SNPN | 19.0.0 |
| 2024-09 | CT#105 | CP-242190 | 6418 | 1 | F | Correction to the applicability of MINT | 19.0.0 |
| 2024-09 | CT#105 | CP-242193 | 6241 | 4 | F | Ranging UE capabilities | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6420 | 1 | F | ESFB handling due to SMC failure | 19.0.0 |
| 2024-09 | CT#105 | CP-242184 | 6337 | 2 | F | UE restrictions for partial network slice and for NS-AoS | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6432 | 1 | F | Correction on the wrong message name in network slice statement | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6431 | 1 | F | Correction on the wrong descprition of 5QI value | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6238 | 4 | F | Timer T3540 handling for causes triggering cell or PLMN selection | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6374 | 2 | F | Correction on UPU and SOR transparent container | 19.0.0 |
| 2024-09 | CT#105 | CP-242201 | 6423 | 2 | F | Discontinuous offset timer handling for MUSIM capable UE | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6417 | 2 | F | Use of native 4G-GUTI | 19.0.0 |
| 2024-09 | CT#105 | CP-242175 | 6350 | 2 | B | The clarification of the applicability of RAT utilization control | 19.0.0 |
| 2024-09 | CT#105 | CP-242169 | 6396 | 2 | F | Handling of Tsor-cm timer expiry or stopped while MRU procedure is ongoing | 19.0.0 |
| 2024-09 | CT#105 | CP-242201 | 6331 | 3 | F | MPS exemption for T3540 | 19.0.0 |
| 2024-09 | CT#105 | CP-242190 | 6379 | 2 | D | Editorial correction in the MINT | 19.0.0 |
| 2024-09 | CT#105 | CP-242175 | 6343 | 3 | B | Control of UE RAT utilization by 5GS | 19.0.0 |
| 2024-09 | CT#105 | CP-242209 | 6392 | 2 | B | ProSe and NPN | 19.0.0 |
| 2024-09 | CT#105 | CP-242183 | 6367 | 2 | F | Handling of TAs on validity information met | 19.0.0 |
| 2024-09 | CT#105 | CP-242184 | 6378 | 3 | F | Slice deregistration inactivity timers | 19.0.0 |
| 2024-09 | CT#105 | CP-242175 | 6377 | 3 | B | The handling on the RAT utilization restriction information | 19.0.0 |
| 2024-12 | CT#106 | CP-243179 | 6437 | - | F | Condition to stop timer T3511 in case of MRU due to fallback indication from lower layers | 19.1.0 |
| 2024-12 | CT#106 | CP-243207 | 6473 | - | F | RAT utilization control in periodic registration update | 19.1.0 |
| 2024-12 | CT#106 | CP-243207 | 6475 | - | F | Update and alignment of RAT utilization control in UCU | 19.1.0 |
| 2024-12 | CT#106 | CP-243180 | 6487 | - | F | Clarification on non-3GPP path switching while using old non-3GPP | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6493 | - | F | Miscellaneous corrections | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6254 | 4 | F | Corrections for NSSAI Inclusion mode | 19.1.0 |
| 2024-12 | CT#106 | CP-243207 | 6499 | - | F | IEI assignment for RAT utilization control | 19.1.0 |
| 2024-12 | CT#106 | CP-243200 | 6521 |  | F | Clarification to triggering registration procedure after unavailability period when UE needs to report unavailability | 19.1.0 |
| 2024-12 | CT#106 | CP-243177 | 6522 | - | F | Correcting wrong terms related to 5G ProSe | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6540 | - | F | Handling of the abnormal case when unavailability information IE contains the start of the unavailability period. | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6548 | - | F | Addition of a condition for the removal of memorized PLMN and SNPN Ids. | 19.1.0 |
| 2024-12 | CT#106 | CP-243206 | 6527 | 2 | A | Correction to #62 handling in Initial registration | 19.1.0 |
| 2024-12 | CT#106 | CP-243187 | 6447 | 1 | A | Conditions when to remove alternative S-NSSAI from configured NSSAI | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6449 | 1 | F | UE behavior at expiry of discontinuous coverage maximum time offset timer | 19.1.0 |
| 2024-12 | CT#106 | CP-243182 | 6480 | 1 | A | AMF provision of unavailability information at DC only | 19.1.0 |
| 2024-12 | CT#106 | CP-243209 | 6495 | 1 | A | Correction to the 5G-RG de-registration | 19.1.0 |
| 2024-12 | CT#106 | CP-243207 | 6460 | 1 | B | Storage and replacement of RAT utilization control information associated to the current PLMN | 19.1.0 |
| 2024-12 | CT#106 | CP-243207 | 6474 | 1 | F | No RAT utilization control IE in REGISTRATION ACCEPT | 19.1.0 |
| 2024-12 | CT#106 | CP-243200 | 6501 | 1 | F | Stop discontinuous coverage maximum time offset timer | 19.1.0 |
| 2024-12 | CT#106 | CP-243200 | 6505 | 1 | F | Clarification on MRU during NAS congestion | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6402 | 4 | F | Timer T3587 handling when power-off | 19.1.0 |
| 2024-12 | CT#106 | CP-243187 | 6510 | 1 | F | Handling of the UE when the UE is located in the non-allowed area and the NS-AoS simultaneously | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6436 | 1 | F | Abnormal case handling Inter-system change from N1 mode to S1 mode triggered during UE-requested PDU session establishment procedure | 19.1.0 |
| 2024-12 | CT#106 | CP-243180 | 6488 | 1 | F | IE naming correction | 19.1.0 |
| 2024-12 | CT#106 | CP-243230 | 6500 | 1 | F | Unavailability period start and duration for UE reasons | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6534 | 1 | F | Correction to handling of MRU due to collision of NW deregistration procedure | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6478 | 1 | F | Requested NSSAI IE inclusion criteria | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6459 | 1 | F | The correction on discontinuous coverage maximum time offset | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6511 | 2 | F | T3485 timer name correction | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6546 | 1 | F | Missing NOTE for T3540 for a UE with high priority access in selected PLMN or SNPN | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6528 | 2 | F | Correction to clause 5.3.1.3 and editorials | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6533 | 1 | F | Correcting cause #36 and #73 handling in shared network | 19.1.0 |
| 2024-12 | CT#106 | CP-243207 | 6461 | 1 | B | RAT utilization control support in 3GPP access | 19.1.0 |
| 2024-12 | CT#106 | CP-243187 | 6482 | 2 | F | Correction of requirements of AoS for S-NSSAI | 19.1.0 |
| 2024-12 | CT#106 | CP-243207 | 6497 | 2 | F | Alternative 1: Following access technology as defined in TS 23.122 | 19.1.0 |
| 2024-12 | CT#106 | CP-243207 | 6468 | 2 | B | Storing RAT utilization control information in non-volatile-memory | 19.1.0 |
| 2024-12 | CT#106 | CP-243187 | 6509 | 2 | F | Storing alternative NSSAI in the non-volatile memory in the ME | 19.1.0 |
| 2024-12 | CT#106 | CP-243187 | 6508 | 2 | F | Alternative S-NSSAI deletion upon S-NSSAI time validity information indicates that the S-NSSAI is not available | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6483 | 2 | F | Remove TPMIC from every PDU session modification procedure | 19.1.0 |
| 2024-12 | CT#106 | CP-243181 | 6491 | 2 | F | Satellite access technology considerations for requirements related to disabling N1 mode capability because voice service was not available | 19.1.0 |
| 2024-12 | CT#106 | CP-243233 | 6450 | 1 | B | List of USS addresses in 5GS | 19.1.0 |
| 2024-12 | CT#106 | CP-243204 | 6552 | 1 | B | Enhancement of 5G ProSe capability for multi-hop relays | 19.1.0 |
| 2024-12 | CT#106 | CP-243207 | 6445 | 3 | B | RAT utilization control information for equivalent PLMNs | 19.1.0 |
| 2024-12 | CT#106 | CP-243298 | 6489 | 2 | F | Update on UE capability indication for rangingsl | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6484 | 2 | F | Allow re-registration without connection release for SMSF change | 19.1.0 |
| 2024-12 | CT#106 | CP-243182 | 6553 | 3 | A | AMF indication for unavailability | 19.1.0 |
| 2024-12 | CT#106 | CP-243186 | 6486 | 3 | B | Information for ensuring appropriate cell reselection for localized services in SNPN | 19.1.0 |
| 2024-12 | CT#106 | CP-243185 | 6463 | 4 | F | URSP and ANDSP storage in non-volatile memory | 19.1.0 |
| 2024-12 | CT#106 | CP-243176 | 6492 | 1 | D | Editorial correction | 19.1.0 |
| 2024-12 | CT#106 | CP-243200 | 6574 | - | D | Miscellaneous corrections | 19.1.0 |
| 2024-12 | CT#106 | CP-243187 | 6583 | - | F | Clarification on NR CGIs included in S-NSSAI location validity information | 19.1.0 |
| 2024-12 | CT#106 | CP-243179 | 6584 | - | D | Correct usage of term camp on | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6532 | 1 | F | Clarification for periodic timer upon transition from idle suspend to idle without suspend | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6601 |  | F | T3584 and T3585 handling on removal of S-NSSAI | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6610 | - | F | Modified description regarding UE's handling of the unavailability information | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6612 | - | F | Storage of UPSI(s) for stored signalled URSP rules | 19.1.0 |
| 2024-12 | CT#106 | CP-243177 | 6613 | - | F | Storage in non-volatile memory | 19.1.0 |
| 2024-12 | CT#106 | CP-243200 | 6614 | - | F | Periodic registration update excluded cases | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6616 | - | F | Minor corrections | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6617 | - | F | Correction of faulty bit number for NSAG | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6624 | - | F | Correction to usage of the term satellite NG-RAN access RAT type | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6638 | - | F | Clarification for NAS signaling upon cause #80 | 19.1.0 |
| 2024-12 | CT#106 | CP-243186 | 6456 | 3 | F | The recognition of SNPN providing access for localized services | 19.1.0 |
| 2024-12 | CT#106 | CP-243187 | 6581 | 1 | A | Paging procedure for PDU session associated with partially allowed S-NSSAI | 19.1.0 |
| 2024-12 | CT#106 | CP-243222 | 6570 | 1 | B | MPS for Messaging Paging Priority | 19.1.0 |
| 2024-12 | CT#106 | CP-243202 | 6576 | 1 | B | (S)RTP multiplexed media information support | 19.1.0 |
| 2024-12 | CT#106 | CP-243202 | 6577 | 1 | B | PDU set identification for non-3GPP access | 19.1.0 |
| 2024-12 | CT#106 | CP-243237 | 6627 | 1 | F | Support of PDU set handing for non-3GPP access | 19.1.0 |
| 2024-12 | CT#106 | CP-243200 | 6602 | 1 | F | PLMN-specific counter reset | 19.1.0 |
| 2024-12 | CT#106 | CP-243200 | 6422 | 4 | F | Correcting handling NAS timers in ecall inactive state | 19.1.0 |
| 2024-12 | CT#106 | CP-243200 | 6466 | 2 | F | Update on re-enabling UE's N1 mode capability | 19.1.0 |
| 2024-12 | CT#106 | CP-243200 | 6641 | 1 | F | No N1 mode capability disabling when deregistering for eCall inactivity | 19.1.0 |
| 2024-12 | CT#106 | CP-243200 | 6642 | 1 | F | Handling of EPLMN list and attempt counters due to AUTH reject | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6543 | 4 | F | Missing NOTE for T3540 for a UE with high priority access in selected PLMN or SNPN | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6563 | 1 | F | Correction to the handling of abnormal cases for RRC inactive state | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6547 | 2 | F | UE behaviour when the UE receives the Unavailability configuration IE without values | 19.1.0 |
| 2024-12 | CT#106 | CP-243187 | 6607 | 1 | F | Alternative 2 - Procedures related to unavailable alternative slice | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6531 | 1 | F | Clarification for EPLMN list upon reject cause #78 | 19.1.0 |
| 2024-12 | CT#106 | CP-243186 | 6502 | 2 | F | FTA list for localized services in SNPN with GIN | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6536 | 2 | F | Correcting handling NAS timers in MICO mode and unavailability | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6560 | 1 | F | Alternative-2 for avoiding two unified access control checks for non-emergency communication with IMS over NG-RAN connected to 5GCN - 24.501 | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6535 | 2 | D | Clarification to de-registration message types | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6529 | 2 | F | Clarification to deregistration procedure with power off in attempting to update state | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6564 | 1 | F | Correction to the Note for SOR-CMCI length | 19.1.0 |
| 2024-12 | CT#106 | CP-243211 | 6559 | 1 | B | Update procedures to consider satellite NG-RAN RAT in the IE | 19.1.0 |
| 2024-12 | CT#106 | CP-243211 | 6462 | 5 | B | Additional provision of RAT utilization control information | 19.1.0 |
| 2024-12 | CT#106 | CP-243211 | 6561 | 1 | F | Removal of RAT utilization control information using Generic UE configuration update procedure | 19.1.0 |
| 2024-12 | CT#106 | CP-243198 | 6621 | 2 | D | Correction to SDNAEPC in 5GSM capability IE | 19.1.0 |
| 2024-12 | CT#106 | CP-243233 | 6451 | 4 | B | No-transmit zone restriction in 5GS | 19.1.0 |
| 2024-12 | CT#106 | CP-243236 | 6452 | 5 | B | MWAB operation in VMR_Ph2 | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6562 | 2 | F | IMS emergency services in eCALL-INACTIVE state | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6503 | 5 | F | Aligning DC max time offset timer behavior with SA2 requirement | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6586 | 2 | F | Clarify the handling on unavailability | 19.1.0 |
| 2024-12 | CT#106 | CP-243232 | 6569 | 2 | B | Support of indirect network sharing | 19.1.0 |
| 2024-12 | CT#106 | CP-243211 | 6530 | 6 | B | Handling of RAT Restriction in DEREGISTRAION | 19.1.0 |
| 2024-12 | CT#106 | CP-243211 | 6585 | 2 | F | Update of RAT utilization control | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6565 | 2 | F | Re-enabling N1 mode when T3526 expires | 19.1.0 |
| 2024-12 | CT#106 | CP-243187 | 6600 | 3 | F | On-demand NSSAI for the alternative S-NSSAI | 19.1.0 |
| 2024-12 | CT#106 | CP-243196 | 6587 | 2 | F | Clarification of the association between the QoS flow and the mapped EPS bearer context | 19.1.0 |
| 2024-12 | CT#106 | CP-243237 | 6626 | 2 | B | Support of ECN marking for L4S for 5G-RG | 19.1.0 |
| 2024-12 | CT#106 | CP-243185 | 6463 | 6 | F | URSP and ANDSP storage in non-volatile memory | 19.1.0 |
| 2024-12 | CT#106 | CP-243182 | 6542 | 1 | F | Clarification of the mobile reachable tmer to avoid an expired timer in the unavailability period | 19.1.0 |
| 2024-12 | CT#106 |  |  |  |  | Editorial corrections and formatting | 19.1.1 |