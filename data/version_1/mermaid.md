```mermaid
graph TD;
  5GMM-DEREGISTERED["UE is in 5GMM-DEREGISTERED state"];
  event_reg_request["UE sends REGISTRATION REQUEST"];
  timer_T3510_start["UE starts timer T3510"];
  AMF_processing_req["AMF is processing REGISTRATION REQUEST"];
  event_reg_accept["AMF sends REGISTRATION ACCEPT"];
  timer_T3550_start["AMF starts timer T3550"];
  5GMM-COMMON-PROCEDURE-INITIATED["AMF enters 5GMM-COMMON-PROCEDURE-INITIATED state"];
  UE_waiting_accept["UE is waiting for REGISTRATION ACCEPT"];
  5GMM-REGISTERED["UE enters 5GMM-REGISTERED state and sets 5GS update status to 5U1 UPDATED"];
  event_reg_complete["UE sends REGISTRATION COMPLETE"];
  timer_T3550_stop["AMF stops timer T3550"];
  5GMM-DEREGISTERED -->|UE initiates registration| event_reg_request;
  event_reg_request -->|UE sends REGISTRATION REQUEST and starts T3510| timer_T3510_start;
  timer_T3510_start -->|REGISTRATION REQUEST received at AMF| AMF_processing_req;
  AMF_processing_req -->|Initial registration request accepted| event_reg_accept;
  event_reg_accept -->|If 5G-GUTI or SOR transparent container IE included in REGISTRATION ACCEPT| timer_T3550_start;
  timer_T3550_start -->|AMF starts T3550 and enters COMMON PROCEDURE INITIATED state| 5GMM-COMMON-PROCEDURE-INITIATED;
  AMF_processing_req -->|If initial registration request cannot be accepted, AMF sends REGISTRATION REJECT (Not included in this successful registration flow)| event_reg_accept;
  AMF_processing_req -->|Initial registration request accepted| event_reg_accept;
  AMF_processing_req -->|AMF sending Registration Accept| UE_waiting_accept;
  UE_waiting_accept -->|UE receives REGISTRATION ACCEPT| 5GMM-REGISTERED;
  5GMM-REGISTERED -->|Specific conditions are met (CAA UAV ID, Network slicing indication, CAG information, PEIPS, or UE radio capability ID)| event_reg_complete;
  event_reg_complete -->|UE sends Registration Complete, AMF recieves it| timer_T3550_stop;
  timer_T3550_stop -->|AMF stops T3550 and returns to Registered state| 5GMM-REGISTERED;
```
