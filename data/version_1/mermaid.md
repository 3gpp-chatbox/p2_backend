# Registration Procedure Flow

```mermaid
flowchart TD
    start([Start]) --> deregistered["UE is in 5GMM-DEREGISTERED state"]
    deregistered --> reg_req_sent[UE sends REGISTRATION REQUEST message to AMF] |UE initiates registration procedure|
    deregistered --> timer_start[UE starts timer T3510] |UE starts timer T3510|
    reg_req_sent --> amf_proc[AMF is processing the REGISTRATION REQUEST] |REGISTRATION REQUEST received by AMF|
    amf_proc --> reg_accepted{{Initial registration request accepted by network}}
    amf_proc --> reg_rejected{{Initial registration request cannot be accepted by the network}}
    reg_accepted -- Yes --> amf_send_accept[AMF sends REGISTRATION ACCEPT message to UE] |AMF sends REGISTRATION ACCEPT message|
    reg_accepted -- Yes --> timer_t3550_start[AMF starts timer T3550 and enters state 5GMM-COMMON-PROCEDURE-INITIATED] |AMF starts timer T3550 and enters state 5GMM-COMMON-PROCEDURE-INITIATED|
    reg_rejected -- No --> amf_send_reject[AMF sends REGISTRATION REJECT message to UE] |AMF sends REGISTRATION REJECT message|
    amf_send_accept --> ue_waiting[UE is waiting for REGISTRATION ACCEPT] |REGISTRATION ACCEPT message sent to UE|
    ue_waiting --> registered["UE enters 5GMM-REGISTERED state"] |REGISTRATION ACCEPT message received by UE|
    registered --> reg_complete_sent{{UE sends REGISTRATION COMPLETE message to AMF if certain conditions are met (Service-level device ID, Network slicing, CAG information, PEIPS, UE radio capability ID)}}
    reg_complete_sent -- Yes --> common_proc_init["AMF in 5GMM-COMMON-PROCEDURE-INITIATED"] |REGISTRATION COMPLETE received by AMF|
    common_proc_init --> timer_t3550_stop[AMF stops timer T3550] |AMF stops timer T3550|
    timer_t3550_stop --> registered |AMF returns to 5GMM Registered state|
    registered --> finish([End])
```
