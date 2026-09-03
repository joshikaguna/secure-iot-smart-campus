# 🔐 IoT Authentication

## Purpose

Authentication is used to prevent unauthorized users from accessing
smart-campus IoT device information.

## Implementation

The IoT simulation requires credentials before protected device
endpoints can be accessed.

The authentication mechanism:

1. Receives the username and password through request headers.
2. Hashes the supplied password using SHA-256.
3. Compares the resulting hash with the stored password hash.
4. Grants access only when valid credentials are provided.
5. Rejects unauthenticated or invalid requests.

## Protected IoT Services

The following endpoints require authentication:

- `/devices`
- `/temperature`
- `/lighting`
- `/door`

The `/` endpoint is maintained as a basic health-check endpoint.

## Authentication Flow

```text
IoT Client
    |
    | Username + Password
    v
IoT Server
    |
    v
Credential Verification
    |
    +---- Invalid ----> Access Denied
    |
    +---- Valid ------> IoT Device Data
