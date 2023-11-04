# RESTful Authentication API with Flask

A token-based authentication api built using Flask and JWT
<br>
**Currently hosted on http://34.127.30.181:5050/**

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation
1. Create .env file with the required variables shown in config.py
2. Adjust exposed port in the Dockerfile to any desired one
3. Build the Dockerfile and run it on your target system

```bash
# Run inside root directory of the repository
docker build -t YOUR_USERNAME/IMAGE_NAME:TAG .
```
## Usage

```bash
# To pull and run the docker image
docker pull YOUR_USERNAME/IMAGE_NAME:TAG

# To run the image
# Note: this assumes your env file is in the current working directory
docker run -d --network="host" --env-file ./.env YOUR_USERNAME/IMAGE_NAME:TAG
```

## API Endpoints

### Register User
```bash
POST /register-user
```

**Description:**
Registers a user

**Request Body:**
- `username` (string, required): The name of the user to be registered.
- `password` (string, required): The user's password

**Example Request:**
```javascript
let response = await fetch(
  "http://url/register-user", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      "username": "testUser",
      "password": "testPassword"
    })
  }
);
```

### Login User
```bash
POST /login-user
```

**Description:**
Logs a user in

**Request Body:**
- `username` (string, required): The user's name.
- `password` (string, required): The user's password.

**Example Request:**
```javascript
let response = await fetch(
  "http://url/login-user", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      "username": "testUser",
      "password": "testPassword"
    })
  }
);
```

**Example Response:**
```javascript
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RVc2VyIiwiaXAiOiI1MC45OC4zOS42MiIsImV4cGlyeVRpbWUiOiIyMDIzLTExLTAzIDA3OjI0OjE1In0.eCREpvQlIN4KPCtax2Nu5bLbr2xIz8LussCSB68c1p8"
}
```

### Authenticate Token
```bash
POST /authenticate-token
```

**Description:**
Checks if a given token is valid

**Request Body:**
- `username` (string, required): The user's name.
- `token` (string, required): The token to be validated.

**Example Request:**
```javascript
let response = await fetch(
  "http://url/authenticate-token", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "username": "testUser"
    },
    body: JSON.stringify({
      "username": "testUser",
      "password": "testPassword"
    })
  }
);
```

**Example Response:**
```javascript
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RVc2VyIiwiaXAiOiI1MC45OC4zOS42MiIsImV4cGlyeVRpbWUiOiIyMDIzLTExLTAzIDA3OjI0OjE1In0.eCREpvQlIN4KPCtax2Nu5bLbr2xIz8LussCSB68c1p8"
}
```

