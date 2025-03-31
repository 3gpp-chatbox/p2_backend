```mermaid
flowchart TD
    start["Procedure starts"]
    1("UE sends REGISTRATION REQUEST to AMF")
    2[["UE starts timer T3510"]]
    3{"Decision based on initial registration request acceptance"}
    4("AMF sends REGISTRATION ACCEPT to UE. AMF may start T3550 and enter 5GMM-COMMON-PROCEDURE-INITIATED if 5G-GUTI or SOR transparent container IE is included.")
    5("UE receives REGISTRATION ACCEPT and enters 5GMM-REGISTERED, resets registration attempt counter, sets 5GS update status to 5U1 UPDATED")
    6{"Decision: UE sends REGISTRATION COMPLETE based on content of REGISTRATION ACCEPT"}
    7("UE sends REGISTRATION COMPLETE to AMF")
    8("AMF receives REGISTRATION COMPLETE, stops T3550, and enters 5GMM-REGISTERED")
    end["Procedure ends"]
    reject_handling("UE Behavior on Rejection - based on 5GMM Cause Code in REGISTRATION REJECT")
    start --> 1
    1 --> 2
    2 --> 3
    3 -..-> 4
    3 -..-> reject_handling
    4 --> 5
    5 --> 6
    6 -..-> 7
    6 -..-> end
    7 --> 8
    8 --> end
    reject_handling --> end
```