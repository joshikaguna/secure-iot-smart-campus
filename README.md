# 🔐 Secure IoT Network for Smart Campus

## 📌 Project Overview

The rapid adoption of Internet of Things (IoT) devices in smart campuses has introduced new cybersecurity challenges. Devices such as smart cameras, environmental sensors, smart lighting systems, biometric systems and smart access-control systems continuously communicate over the network.

Weak authentication, insecure communication protocols, exposed network services and poor network segmentation can allow attackers to gain unauthorized access to IoT devices and potentially move toward other campus systems.

This project focuses on analyzing common IoT vulnerabilities and designing a secure IoT network architecture using authentication, encryption, network segmentation and firewall controls.

---

## 🎯 Objectives

* Identify common security vulnerabilities in IoT devices.
* Analyze exposed network services using Nmap.
* Monitor and analyze network traffic using Wireshark.
* Implement secure communication using TLS and OpenSSL.
* Design network segmentation for IoT devices.
* Apply firewall rules to restrict unauthorized communication.
* Compare the security posture before and after implementing security controls.

---

## 🏫 Smart Campus IoT Environment

The proposed environment consists of simulated smart-campus IoT devices such as:

* Smart Cameras
* Environmental Sensors
* Smart Lighting
* Smart Access-Control Devices
* Smart Energy Meters

These devices are placed in a dedicated IoT network and are separated from administrative and student networks.

---

## 🛡️ Security Approach

The project follows a layered security approach:

```text
                SMART CAMPUS
                     |
                 FIREWALL
                     |
              CORE NETWORK
                     |
        +------------+------------+
        |            |            |
      ADMIN         IoT        STUDENTS
        |            |            |
     Admin PCs   IoT Devices   Student PCs
                     |
          +----------+----------+
          |          |          |
       Camera     Sensor     Access
```

### Security Controls

**Authentication**

* Strong credentials
* Unique device accounts
* Removal of default passwords
* Role-based access

**Encryption**

* TLS-secured communication
* OpenSSL certificates
* Protection against plaintext transmission

**Network Segmentation**

* Dedicated IoT network
* Separation of administrative systems
* Separation of student and guest networks
* Restricted inter-network communication

**Firewall**

* Restrict unnecessary inbound connections
* Allow only required services
* Limit IoT access to external networks
* Prevent unauthorized communication between network segments

---

## 🔎 Security Testing Tools

| Tool      | Purpose                                   |
| --------- | ----------------------------------------- |
| Nmap      | Network discovery and service enumeration |
| Wireshark | Network traffic analysis                  |
| OpenSSL   | TLS and certificate testing               |
| Firewall  | Network access control                    |
| Python    | IoT device/network simulation             |

---

## 📊 Security Testing

The project evaluates the network in two stages:

### Before Security Implementation

* Identify exposed services.
* Analyze insecure communication.
* Identify weak access controls.
* Evaluate potential attack surfaces.

### After Security Implementation

* Verify restricted services.
* Verify encrypted communication.
* Verify authentication controls.
* Verify firewall restrictions.
* Confirm network segmentation.

---

## 📈 Expected Outcome

The proposed security architecture is expected to:

* Reduce the IoT attack surface.
* Prevent unauthorized device access.
* Protect data during transmission.
* Limit lateral movement after device compromise.
* Improve visibility into network activity.
* Protect critical campus systems from compromised IoT devices.

---

## ⚠️ Ethical Use

All security testing in this project is intended for an authorized laboratory environment. Nmap scans, traffic analysis and other security tests should only be performed against systems and networks for which permission has been obtained.

---

## 👩‍💻 Project Status

**Status:** In Development

The project will be developed incrementally by implementing the IoT simulation, authentication, TLS encryption, network segmentation, firewall controls and security testing.

---

## 📚 Technologies

`Python` · `Nmap` · `Wireshark` · `OpenSSL` · `Firewall` · `GitHub`
