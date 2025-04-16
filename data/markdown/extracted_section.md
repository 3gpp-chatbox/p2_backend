# 24501

## 4.2 Coordination between the protocols for 5GS mobility management and 5GS session management

A 5GS session management (5GSM) message is piggybacked in specific 5GS mobility management (5GMM) transport messages. To this purpose, the 5GSM messages can be transmitted in an information element in the 5GMM transport messages. In this case, the UE, the AMF and the SMF execute the 5GMM procedure and the 5GSM procedure in parallel. The success of the 5GMM procedure is not dependent on the success of the piggybacked 5GSM procedure.

The UE can only initiate the 5GSM procedure when there is a 5GMM context established at the UE.

During 5GMM procedures, the UE and the AMF shall suspend the transmission of 5GSM messages, except when:

a) the 5GMM procedure is piggybacking 5GSM messages; or

b) the UE is in 5GMM-CONNECTED mode and a service request procedure for re-establishing user-plane resources of PDU session(s) is initiated without including PDU session status IE or Allowed PDU session status IE. In this case, the UE and the AMF need not suspend the transmission of 5GSM messages related to other PDU session(s) than the one(s) for which the user- plane resources re-establishment is requested.

If the UE determines to locally release the N1 NAS signalling connection upon receiving an SOR transparent container during a registration procedure as specified in 3GPP TS 23.122 [5] subclause C.2, the UE shall suspend the transmission of 5GSM messages after sending the REGISTRATION COMPLETE message and until the N1 NAS signalling connection is released to obtain service on a higher priority PLMN, with the exception of the case when the UE has an emergency PDU session.

A 5GMM message piggybacking a 5GSM message for a PDU session shall be delivered via the access associated with the PDU session, if any, with the following exceptions:

a) the AMF shall send, via 3GPP access, a DL NAS TRANSPORT message piggybacking a downlink 5GSM message of a network-requested 5GSM procedure for a PDU session associated with non-3GPP access if the conditions specified in subclause 5.5.1.3.4 or subclause 5.6.1.4 are met;

b) the UE shall send an UL NAS TRANSPORT message piggybacking a response message to the 5GSM message described in a) via either:

1) 3GPP access; or

2) non-3GPP access if the UE is in 5GMM-CONNECTED mode over non-3GPP access; and

NOTE: The interaction between the 5GMM sublayer and the 5GSM sublayer to enable the UE to send the UL NAS TRANSPORT message containing the response message via 3GPP access is required. This is achieved via UE implementation.

c) the UE shall send, via the target access, an UL NAS TRANSPORT message piggybacking a 5GSM message associated with a request type set to "existing PDU session" or "existing emergency PDU session" for handover of an existing PDU session between 3GPP access and non-3GPP access.

A 5GMM message piggybacking a 5GSM message as a response message to a request message associated with an MA PDU session, shall be delivered via the same access that the initial message was received.

## 5.2 Behaviour of the UE in state 5GMM-DEREGISTERED and state 5GMM-REGISTERED

### 5.2.1 General

In this subclause, the detailed behaviour of the UE in the states 5GMM-DEREGISTERED and 5GMM-REGISTERED is described.

### 5.2.2 UE behaviour in state 5GMM-DEREGISTERED

#### 5.2.2.1 General

The state 5GMM-DEREGISTERED is entered in the UE, when:

a) the de-registration is performed either by the UE or by the network (see subclause 5.5.2);

b) the registration request is rejected by the AMF (see subclause 5.5.1.2.5 and 5.5.1.3.5);

c) the service request is rejected by the AMF (see subclause 5.6.1);

d) the UE is switched on; or

e) the UE registered for emergency services is in 5GMM-IDLE mode and its periodic registration update timer expires (see subclause 5.3.7).

In state 5GMM-DEREGISTERED, the UE shall behave according to the substate as explained in subclause 5.2.2.3.

#### 5.2.2.2 Primary substate selection

##### 5.2.2.2.1 Selection of the substate after power on

For a UE configured for eCall only mode as specified in 3GPP TS 31.102 [22], timers T3444 and T3445 are considered to have expired at power on. When the UE is switched on, the substate shall be PLMN-SEARCH if the USIM is available and valid or there are valid entries in the "list of subscriber data". See 3GPP TS 23.122 [5] for further details.

The substate chosen after PLMN-SEARCH, following power on is:

a) if no cell can be selected, the substate shall be NO-CELL-AVAILABLE;

b) if the UE is not operating in SNPN access operation mode, and no USIM is present, or the USIM is considered invalid by the UE, the substate shall be NO-SUPI;

c) if the UE is operating in SNPN access operation mode, and:

1) the selected entry in the "list of subscriber data" does not contain subscription identifier, and no USIM is present, or the USIM is considered invalid by the UE; or

2) no valid entry in the "list of subscriber data" exists;

the substate shall be NO-SUPI;

d) if a suitable cell has been found:

1) the PLMN identity of the cell is not in one of the forbidden PLMN lists;

2) the SNPN is not an SNPN selected for localized services in SNPN (see 3GPP TS 23.122 [5]), the UE is not to perform initial registration for onboarding services in SNPN, and the SNPN identity of the cell is not in one of the "permanently forbidden SNPNs" list or the "temporarily forbidden SNPNs" list which are, if the MS supports access to an SNPN using credentials from a credentials holder, equivalent SNPNs or both, associated with the selected entry of the "list of subscriber data" or the selected PLMN subscription ;

3) the SNPN is an SNPN selected for localized services in SNPN (see 3GPP TS 23.122 [5]), and the SNPN identity of the cell is not in one of the "permanently forbidden SNPNs for access for localized services in SNPN" list or "temporarily forbidden SNPNs for access for localized services in SNPN" list, associated with the selected entry of the "list of subscriber data" or the selected PLMN subscription; or

4) the UE is to perform initial registration for onboarding services in SNPN and the SNPN identity of the cell is not in the "permanently forbidden SNPNs for onboarding services in SNPN" list and the "temporarily forbidden SNPNs for onboarding services in SNPN" list;

and the tracking area is not in one of the lists of 5GS forbidden tracking areas, then the substate shall be NORMAL-SERVICE;

e) if the selected cell is known not to be able to provide normal service, then the UE shall enter the substate LIMITED-SERVICE;

f) if the UE is in manual network selection mode and no cell of the selected PLMN or SNPN has been found, the UE shall enter the substate NO-CELL-AVAILABLE; and

g) if the UE is configured for eCall only mode as specified in 3GPP TS 31.102 [22], the substate shall be eCALL-INACTIVE.

#### 5.2.2.3 Detailed description of UE behaviour in state 5GMM-DEREGISTERED

##### 5.2.2.3.1 NORMAL-SERVICE

The UE shall initiate an initial registration procedure if the timer T3346 is not running. If timer T3346 is running, the UE shall initiate an initial registration procedure on the expiry of timer T3346.

The UE may initiate an initial registration procedure for emergency services or for a UE configured for high priority access in selected PLMN or SNPN, even if timer T3346 is running.

##### 5.2.2.3.2 LIMITED-SERVICE

The UE shall initiate an initial registration procedure when entering a cell which provides normal service.

The UE may initiate initial registration for emergency services.

##### 5.2.2.3.3 ATTEMPTING-REGISTRATION

The UE in 3GPP access:

a) shall initiate an initial registration procedure on the expiry of timers T3502, T3511 or T3346;

b) may initiate an initial registration procedure for emergency services even if timers T3502, T3511 or T3346 are running;

b1) may initiate an initial registration procedure even if timer T3502, T3346 or T3447 is running, if the UE is a UE configured for high priority access in selected PLMN;

b2) may initiate an initial registration procedure even if timer T3502, T3346 is running, if the UE is a UE configured for high priority access in selected SNPN;

c) shall initiate an initial registration procedure when entering a new PLMN or SNPN, except if:

i) timer T3346 is running and the new PLMN or SNPN is equivalent to the PLMN or SNPN where the UE started timer T3346;

ii) the PLMN identity of the new cell is in the forbidden PLMN lists;

iii) the SNPN is not an SNPN selected for localized services in SNPN (see 3GPP TS 23.122 [5]), the UE is not to perform initial registration for onboarding services in SNPN, the SNPN identity of the new cell is in the "permanently forbidden SNPNs" list or the "temporarily forbidden SNPNs" list which are, if the MS supports access to an SNPN using credentials from a credentials holder, equivalent SNPNs or both, associated with the selected entry of the "list of subscriber data" or the selected PLMN subscription;

iv) the SNPN is an SNPN selected for localized services in SNPN (see 3GPP TS 23.122 [5]), the SNPN identity of the new cell is in the "permanently forbidden SNPNs for access for localized services in SNPN" list or the "temporarily forbidden SNPNs for access for localized services in SNPN" list, associated with the selected entry of the "list of subscriber data" or the selected PLMN subscription;

v) the UE is to perform initial registration for onboarding services in SNPN, the SNPN identity of the new cell is in the "permanently forbidden SNPNs for onboarding services in SNPN" list or the "temporarily forbidden SNPNs for onboarding services in SNPN" list; or

vi) the current TAI is in one of the lists of 5GS forbidden tracking areas;

d) shall initiate an initial registration procedure when the current TAI has changed, if timer T3346 is not running,

1) the PLMN identity of the new cell is not in one of the forbidden PLMN lists;

2) the SNPN is not an SNPN selected for localized services in SNPN (see 3GPP TS 23.122 [5]), the UE is not to perform initial registration for onboarding services in SNPN, and the SNPN identity of the new cell is in neither the "permanently forbidden SNPNs" list nor the "temporarily forbidden SNPNs" list which are, if the MS supports access to an SNPN using credentials from a credentials holder, equivalent SNPNs or both, associated with the selected entry of the "list of subscriber data" or the selected PLMN subscription;

3) the SNPN is an SNPN selected for localized services in SNPN (see 3GPP TS 23.122 [5]) and the SNPN identity of the cell is in neither the "permanently forbidden SNPNs for access for localized services in SNPN" list nor the "temporarily forbidden SNPNs for access for localized services in SNPN" list, associated with the selected entry of the "list of subscriber data" or the selected PLMN subscription; or

4) the UE is to perform initial registration for onboarding services in SNPN, and the SNPN identity of the cell is in neither the "permanently forbidden SNPNs for onboarding services in SNPN" list nor the "temporarily forbidden SNPNs for onboarding services in SNPN" list;

and the current TAI is not in one of the lists of 5GS forbidden tracking areas;

e) shall initiate an initial registration procedure if the 5GS update status is set to 5U2 NOT UPDATED, and timers T3511, T3502 and T3346 are not running;

f) may initiate an initial registration procedure for UE in NB-N1 mode upon receiving a request from upper layers to transmit user data related to an exceptional event and the UE is allowed to use exception data reporting (see the ExceptionDataReportingAllowed leaf of the NAS configuration MO in 3GPP TS 24.368 [17]) or the USIM file EFNASCONFIG in 3GPP TS 31.102 [22]) if timer T3346 is not already running for "MO exception data" and even if timer T3502 or timer T3511 is running; and

g) may initiate an initial registration procedure with 5GS registration type IE set to "initial registration" for initiating of an emergency PDU session, upon request of the upper layers to establish the emergency PDU session.

The UE in non-3GPP access:

a) shall initiate an initial registration procedure on the expiry of timers T3502, T3511 or T3346;

b) may initiate an initial registration procedure for emergency services even if timers T3502, T3511 or T3346 are running;

b1) may initiate an initial registration procedure even if timer T3502 or T3346 is running if the UE is a UE configured for high priority access in selected PLMN;

c) shall initiate an initial registration procedure when entering a new PLMN or SNPN, except if timer T3346 is running and the new PLMN or SNPN is equivalent to the PLMN or SNPN where the UE started timer T3346;

d) shall initiate an initial registration procedure if the 5GS update status is set to 5U2 NOT UPDATED, and timers T3511, T3502 and T3346 are not running; and

e) may initiate an initial registration procedure with 5GS registration type IE set to "initial registration" for initiating of an emergency PDU session, upon request of the upper layers to establish the emergency PDU session.

##### 5.2.2.3.4 PLMN-SEARCH

The UE shall perform PLMN selection or SNPN selection. If a new PLMN or SNPN is selected, the UE shall reset the registration attempt counter and initiate the registration procedure for initial registration (see subclause 5.5.1.2.2).

If the selected cell in the new PLMN is known not to be able to provide normal service, the UE may initiate the registration procedure for initial registration for emergency services.

##### 5.2.2.3.5 NO-SUPI

The UE may initiate the registration procedure for initial registration for emergency services.

##### 5.2.2.3.6 NO-CELL-AVAILABLE

The UE shall perform cell selection and choose an appropriate substate when a cell is found.

##### 5.2.2.3.7 eCALL-INACTIVE

The UE camps on a suitable cell or an acceptable cell in a PLMN selected as specified in 3GPP TS 23.122 [5] but initiates no 5GMM signalling with the network and ignores any paging requests.

The UE shall leave substate 5GMM-DEREGISTERED.eCALL-INACTIVE state only when one of the following events occur:

a) if the USIM is removed, the UE enters substate 5GMM-DEREGISTERED.NO-SUPI;

b) if coverage is lost, the UE enters substate 5GMM-DEREGISTERED.PLMN-SEARCH;

c) if the UE is deactivated (e.g. powered off) by the user, the UE enters state 5GMM-NULL;

d) if the UE receives a request from upper layers to establish an eCall over IMS or an IMS emergency session according to subclause H.6 in 3GPP TS 23.167 [6], the UE enters state 5GMM-DEREGISTERED.ATTEMPTING-REGISTRATION. The UE then uses the relevant 5GMM and 5GSM procedures to establish the eCall over IMS or an IMS emergency session according to subclause H.6 in 3GPP TS 23.167 [6] at the earliest opportunity; or

e) if the UE receives a request from upper layers to establish a call to an HPLMN designated non-emergency MSISDN or URI for test or terminal reconfiguration service, the UE enters state 5GMM-DEREGISTERED.ATTEMPTING-REGISTRATION. Once the registration procedure is completed, the UE uses the relevant 5GMM and 5GSM procedures to establish the non-emergency call.

##### 5.2.2.3.8 INITIAL-REGISTRATION-NEEDED

The UE shall initiate the initial registration procedure, if still needed, as soon as the access is allowed in the selected cell for the UE.

The UE may initiate registration procedure for emergency services.

#### 5.2.2.4 Substate when back to state 5GMM-DEREGISTERED from another 5GMM state

When returning to state 5GMM-DEREGISTERED, the UE shall select a cell as specified in 3GPP TS 38.304 [28] or 3GPP TS 36.304 [25C].

The substate depends on the result of the cell selection procedure, the outcome of the previously performed 5GMM specific procedures, on the 5GS update status of the UE, on the tracking area data stored in the UE, on the presence of the USIM, on the UE configuration and on the reason for moving to 5GMM-DEREGISTERED:

a) If no cell has been found, the substate is NO-CELL-AVAILABLE, until a cell is found;

b) If no USIM is present or if the inserted USIM is considered invalid by the UE, the substate shall be NO-SUPI;

c) If a suitable cell has been found and the PLMN or tracking area is not in one of the forbidden lists, the substate shall be NORMAL-SERVICE;

d) If an initial registration shall be performed (e.g. network-requested re-registration), the substate shall be ATTEMPTING-REGISTRATION;

e) If a PLMN reselection or SNPN reselection (according to 3GPP TS 23.122 [5]) is needed, the substate shall be PLMN-SEARCH;

f) If the selected cell is known not to be able to provide normal service, the substate shall be LIMITED-SERVICE; and

g) If the UE is configured for eCall only mode as specified in 3GPP TS 31.102 [22], T3444 and T3445 have expired or are not running, and substate PLMN-SEARCH is not required, the substate shall be eCALL-INACTIVE.

### 5.2.3 UE behaviour in state 5GMM-REGISTERED

#### 5.2.3.1 General

The state 5GMM-REGISTERED is entered at the UE, when the initial registration procedure is performed by the UE (see subclause 5.5.1.2.2).

In state 5GMM-REGISTERED, the UE shall behave according to the substate as explained in subclause 5.2.3.2.

#### 5.2.3.2 Detailed description of UE behaviour in state 5GMM-REGISTERED

##### 5.2.3.2.1 NORMAL-SERVICE

The UE:

a) shall initiate the mobility or the registration procedure for periodic registration update (according to conditions given in subclause 5.5.1.3.2), except that the registration procedure for periodic registration update shall not be initiated over non-3GPP access;

b) shall initiate the service request procedure (according to conditions given in subclause 5.6.1);

c) shall respond to paging;

NOTE 1: Paging is not supported over non-3GPP access.

NOTE 2: As an implementation option, the MUSIM UE is allowed to not respond to paging based on the information available in the paging message, e.g. voice service indication.

d) if configured for eCall only mode as specified in 3GPP TS 31.102 [22], shall perform the eCall inactivity procedure at expiry of timer T3444 or timer T3445 (see subclause 5.5.3);

e) shall initiate a registration procedure for mobility and periodic registration update on the expiry of timer T3511; and

f) if acting as a 5G ProSe UE-to-network relay UE as specified in 3GPP 24.554 [19E], shall initiate the authentication and key agreement procedure (according to the conditions given in subclause 5.5.4).

##### 5.2.3.2.2 NON-ALLOWED-SERVICE

The UE shall behave as specified in subclause 5.3.5.

The UE in 5GMM-REGISTERED.NON-ALLOWED-SERVICE substate, if configured for eCall only mode as specified in 3GPP TS 31.102 [22], shall perform the eCall inactivity procedure at expiry of timer T3444 or timer T3445 (see subclause 5.5.3).

##### 5.2.3.2.3 ATTEMPTING-REGISTRATION-UPDATE

The UE in 3GPP access:

a) shall not send any user data;

b) shall initiate a registration procedure for mobility and periodic registration update on the expiry of timers T3502, T3511, T3346 or discontinuous coverage maximum time offset timer;

c) shall initiate a registration procedure for mobility and periodic registration update when entering a new PLMN or SNPN, if timer T3346 is running and the new PLMN or SNPN is not equivalent to the PLMN or SNPN where the UE started timer T3346, the PLMN identity of the new cell is not in the forbidden PLMN lists, and the current TAI is not in one of the lists of 5GS forbidden tracking areas;

d) shall initiate a registration procedure for mobility and periodic registration update when the current TAI has changed, if timer T3346 is not running and:

1) the PLMN identity of the new cell is not in one of the forbidden PLMN lists;

2) the SNPN is not an SNPN selected for localized services in SNPN (see 3GPP TS 23.122 [5]), the UE is not registered for onboarding services in SNPN, and the SNPN identity of the new cell is in neither the "permanently forbidden SNPNs" list nor the "temporarily forbidden SNPNs" list which are, if the UE supports access to an SNPN using credentials from a credentials holder, equivalent SNPNs or both, associated with the selected entry of the "list of subscriber data" or the selected PLMN subscription;

3) the SNPN is an SNPN selected for localized services in SNPN (see 3GPP TS 23.122 [5]), and the SNPN identity of the new cell is in neither the "permanently forbidden SNPNs for access for localized services in SNPN" list nor the "temporarily forbidden SNPNs for access for localized services in SNPN" list, associated with the selected entry of the "list of subscriber data" or the selected PLMN subscription; or

4) the UE is registered for onboarding services in SNPN, and the SNPN identity of the cell is in neither the "permanently forbidden SNPNs for onboarding services in SNPN" list nor the "temporarily forbidden SNPNs for onboarding services in SNPN" list;

and the current TAI is not in one of the lists of 5GS forbidden tracking areas;

e) may initiate a registration procedure for mobility and periodic registration update upon request of the upper layers to establish an emergency PDU session or perform emergency service fallback;

e1) may initiate a registration procedure for mobility and periodic registration update upon request of the upper layers to establish a PDU session, even if timer T3502, T3346 or T3447 is running, if the UE is a UE configured for high priority access in the selected PLMN;

e2) may initiate a registration procedure for mobility and periodic registration update upon request of the upper layers to establish a PDU session, even if timer T3502, T3346 is running, if the UE is a UE configured for high priority access in selected SNPN;

f) may perform de-registration locally and initiate a registration procedure for initial registration for emergency services even if timer T3346 is running;

g) shall initiate registration procedure for mobility and periodic registration update upon reception of paging, or upon reception of NOTIFICATION message with access type indicating 3GPP access;

NOTE: As an implementation option, the MUSIM UE is allowed to not respond to paging based on the information available in the paging message, e.g. voice service indication.

h) may initiate a registration procedure for mobility and periodic registration update upon request for an MMTEL voice call, MMTEL video call, or an MO IMS registration related signalling from the upper layers, and none of the following conditions is met:

1) timer T3346 is running;

2) the UE has stored a list of "non-allowed tracking areas" and the current TAI is in the list of "non-allowed tracking areas"; or

3) the UE has stored a list of "allowed tracking areas", the UE is camped on a cell which is in the registration area and the current TAI is not in the list of "allowed tracking areas";

i) shall initiate a registration procedure for mobility and periodic registration update if the 5GS update status is set to 5U2 NOT UPDATED, and timers T3511, T3502 and T3346 are not running;

j) if configured for eCall only mode as specified in 3GPP TS 31.102 [22], shall perform the eCall inactivity procedure at expiry of timer T3444 or timer T3445 (see subclause 5.5.3);

k) may initiate a registration procedure for mobility and periodic registration update for UE in NB-N1 mode upon receiving a request from upper layers to transmit user data related to an exceptional event and the UE is allowed to use exception data reporting (see the ExceptionDataReportingAllowed leaf of the NAS configuration MO in 3GPP TS 24.368 [17]) or the USIM file EFNASCONFIG in 3GPP TS 31.102 [22]) if timer T3346 is not already running for "MO exception data" and even if timer T3502 or timer T3511 is running;

l) may initiate the signalling for the de-registration procedure with De-registration type IE indicating "normal de-registration" only if the current TAI is part of the TAI list;

m) shall initiate a registration procedure for mobility and periodic registration update if the UE supports the reconnection to the network due to RAN timing synchronization status change and receives an indication of a change in the RAN timing synchronization status, even if timer T3502 is running.

n) may initiate the signalling for the de-registration procedure with de-registration type "switch off".

The UE in non-3GPP access:

a) shall not send any user data;

b) shall initiate the registration procedure for mobility and periodic registration update on the expiry of timers T3502, T3511 or T3346;

c) may initiate a registration procedure for mobility registration update upon request of the upper layers to establish an emergency PDU session;

c1) may initiate a registration procedure for mobility and periodic registration update upon request of the upper layers to establish a PDU session, if the UE is a UE configured for high priority access in selected PLMN even if timer T3346 or T3502 is running;

d) may perform de-registration locally and initiate a registration procedure for initial registration for emergency services even if timer T3346 is running;

e) may initiate a registration procedure for mobility and periodic registration update upon request for an MMTEL voice call, MMTEL video call, or an MO IMS registration related signalling from the upper layers, if timer T3346 is not running;

f) shall initiate a registration procedure for mobility and periodic registration update if the 5GS update status is set to 5U2 NOT UPDATED, and timers T3511, T3502 and T3346 are not running; and

g) shall not initiate the signalling for the de-registration procedure unless timer T3346 is running.

##### 5.2.3.2.4 LIMITED-SERVICE

The UE:

a) shall perform cell selection/reselection;

b) may perform de-registration locally and initiate an initial registration for emergency services; and

c) if configured for eCall only mode as specified in 3GPP TS 31.102 [22], shall perform the eCall inactivity procedure at expiry of timer T3444 or timer T3445 (see subclause 5.5.3).

##### 5.2.3.2.5 PLMN-SEARCH

The UE shall perform PLMN selection or SNPN selection. If a new PLMN is selected, the UE shall reset the registration attempt counter and initiate a registration procedure for mobility and periodic registration update (see subclause 5.5.1.3). If a new SNPN is selected, the UE shall reset the registration attempt counter and initiate a mobility registration update if the UE supports access to an SNPN using credentials from a credentials holder or when the SNPNs are equivalent SNPNs or both (see subclause 4.14.2) and the last registered SNPN and the newly selected SNPN are both identified by globally-unique SNPN identities. Otherwise the UE, may perform de-registration locally and shall initiate a registration procedure for initial registration (see subclause 5.5.1.2.2).If the selected cell in the new PLMN is known not to be able to provide normal service, the UE may perform de-registration locally and initiate an initial registration for emergency services.

##### 5.2.3.2.6 NO-CELL-AVAILABLE

The UE shall perform cell selection and choose an appropriate substate when a cell is found.

##### 5.2.3.2.7 UPDATE-NEEDED

The UE:

a) shall not send any user data;

b) shall not send signalling information, unless it is a service request as a response to paging or to initiate signalling for emergency services or emergency services fallback;

c) shall perform cell selection/reselection;

d) shall enter the appropriate new substate as soon as the lower layers indicate that the barring is alleviated for the access category with which the access attempt for the registration procedure for mobility and periodic registration update was associated and, if still needed, start the registration procedure for mobility and periodic registration update or the signalling for the de-registration procedure (see subclauses 5.5.1.3.7, item l, and 5.5.2.2.6, item b); and

e) if configured for eCall only mode as specified in 3GPP TS 31.102 [22], shall perform the eCall inactivity procedure at expiry of timer T3444 or T3445 (see subclause 5.5.3).