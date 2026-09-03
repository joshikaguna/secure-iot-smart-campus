# 🌐 Network Segmentation

## Purpose

Network segmentation separates IoT devices from administrative,
student and guest systems. This reduces the risk of an attacker
moving from a compromised IoT device to sensitive campus systems.

## Proposed Campus Network

```text
                         INTERNET
                             |
                         FIREWALL
                             |
                        CORE SWITCH
                             |
        +--------------------+--------------------+
        |                    |                    |
    VLAN 10              VLAN 20              VLAN 30
    ADMIN                  IoT                STUDENTS
        |                    |                    |
   Admin Systems       IoT Devices          Student PCs
                          |
                 +--------+--------+
                 |        |        |
              Camera   Sensor   Smart Lock
