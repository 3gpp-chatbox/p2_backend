# Registration Procedure Flow

```mermaid
flowchart TD
    start([Start]) --> node_1[UE sends REGISTRATION REQUEST to AMF]
    node_1[UE sends REGISTRATION REQUEST to AMF] --> node_2[UE starts timer T3510, stops timer T3502 (if running), and stops timer T3511 (if running).]
    node_2[UE starts timer T3510, stops timer T3502 (if running), and stops timer T3511 (if running).] --> node_3{{Network initiates 5GMM common procedures}}
    node_3{{Network initiates 5GMM common procedures}} --> node_4{{Initial registration accepted by the network}}
    node_4{{Initial registration accepted by the network}} -- Registration accepted --> node_5[AMF sends REGISTRATION ACCEPT to UE]
    node_4{{Initial registration accepted by the network}} -- Registration rejected --> node_9[AMF sends REGISTRATION REJECT to UE]
    node_5[AMF sends REGISTRATION ACCEPT to UE] --> node_6[UE receives REGISTRATION ACCEPT, resets registration attempt counter, enters state 5GMM-REGISTERED and sets the 5GS update status to 5U1 UPDATED.]
    node_5[AMF sends REGISTRATION ACCEPT to UE] -- 5G-GUTI or SOR transparent container IE is included in the REGISTRATION ACCEPT message --> node_5G_GUTI[If a 5G-GUTI or the SOR transparent container IE is included in the REGISTRATION ACCEPT message, the AMF shall start timer T3550 and enter state 5GMM-COMMON-PROCEDURE-INITIATED.]
    node_6[UE receives REGISTRATION ACCEPT, resets registration attempt counter, enters state 5GMM-REGISTERED and sets the 5GS update status to 5U1 UPDATED.] --> node_7{{REGISTRATION COMPLETE (Conditional)}}
    node_7{{REGISTRATION COMPLETE (Conditional)}} -- Certain IEs are included in the REGISTRATION ACCEPT message --> node_8[UE sends REGISTRATION COMPLETE to AMF]
    node_7{{REGISTRATION COMPLETE (Conditional)}} -- Certain IEs are not included in the REGISTRATION ACCEPT message --> end_success([End])
    node_8[UE sends REGISTRATION COMPLETE to AMF] --> node_10[AMF stops timer T3550 and changes to state 5GMM-REGISTERED]
    node_9[AMF sends REGISTRATION REJECT to UE] --> node_11[UE takes actions based on 5GMM cause value]
    node_10[AMF stops timer T3550 and changes to state 5GMM-REGISTERED] --> end_success([End])
    node_11[UE takes actions based on 5GMM cause value] --> end_failure([End])
    node_2[UE starts timer T3510, stops timer T3502 (if running), and stops timer T3511 (if running).] -.-> node_12{{Abnormal Cases in the UE - T3510 timeout}} |Timer T3510 starts|
    node_12{{Abnormal Cases in the UE - T3510 timeout}} -- Timer T3510 expires --> node_13{{Retry or PLMN Selection}}
    node_13{{Retry or PLMN Selection}} -- Registration attempt counter < 5 --> end_failure([End])
    node_13{{Retry or PLMN Selection}} -- Registration attempt counter = 5 --> node_14{{PLMN Selection}}
    node_14{{PLMN Selection}} -- Value of T3502 as indicated by the network is not zero --> end_failure([End])
    node_5G_GUTI[If a 5G-GUTI or the SOR transparent container IE is included in the REGISTRATION ACCEPT message, the AMF shall start timer T3550 and enter state 5GMM-COMMON-PROCEDURE-INITIATED.] --> end_success([End])
```
