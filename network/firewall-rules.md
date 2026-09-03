# 🧱 Firewall Rules for Smart Campus IoT

## Purpose

The firewall controls traffic between the Internet, IoT devices,
administrative systems, student systems and guest systems.

Only necessary communication is permitted.

## Security Policy

| Source | Destination | Action | Reason |
|---|---|---|---|
| Internet | IoT Network | DENY | Prevent direct external access |
| Student Network | IoT Network | DENY | Prevent unauthorized access |
| Guest Network | IoT Network | DENY | Isolate guest users |
| Admin Network | IoT Network | ALLOW | Required administrative access |
| IoT Network | Required Services | ALLOW | Permit essential communication |
| IoT Network | Unnecessary Services | DENY | Reduce attack surface |

## Default Policy

The recommended approach is:

```text
DEFAULT → DENY
