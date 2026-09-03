# 🔒 TLS Encryption for IoT Communication

## Purpose

IoT devices frequently transmit sensitive information across a network.
If communication is not encrypted, an attacker who can observe the
traffic may be able to read the transmitted data.

TLS (Transport Layer Security) provides encryption and helps protect
the confidentiality and integrity of IoT communication.

## Proposed Secure Communication

```text
IoT Device
     |
     | TLS / HTTPS
     |
     v
IoT Server
