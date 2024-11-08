# MikroTik API Service Example Usage

This API provides endpoints to manage `ppp secret` entries on a MikroTik router, including CRUD operations, enabling, and disabling entries. Each endpoint requires API key authentication.

## Prerequisites

- **Python** (version 3.7+)
- **MikroTik Router** with API access enabled
- **Flask** and **librouteros** libraries
  ```bash
  pip install Flask librouteros
  ```

## Configuration

1. Create a configuration file at `./config/mikrotik_config.py` then add your MikroTik connection settings and create `./config/api_key.py` then add your API key:

   ```python
   # src/config/mikrotik_config.py

   # MikroTik Configuration
   MIKROTIK_IP = '192.168.88.1'        # Replace with your MikroTik IP address
   MIKROTIK_USERNAME = 'admin'         # Replace with your MikroTik username
   MIKROTIK_PASSWORD = 'password'      # Replace with your MikroTik password
   MIKROTIK_PORT = 8728                # MikroTik API port (default is 8728)

   ```

   ```python
   # src/config/api_key.py

   # API Key for authentication
   API_KEY = 'your_api_key_here'
   ```

2. **Project Directory Structure**:
   ```
   project_folder/
   ├── config/
   │   └── config.py            # Configuration file with MikroTik and API key settings
   ├── core/
   │   ├── models/
   │   │   └── ppp_secret_model.py    # Model for ppp_secret
   │   └── services/
   │       └── ppp_secret_service.py  # Service for CRUD and other operations
   └── main.py                     # Main file to run the application
   ```

## Running the API

Start the API by running:

```bash
python main.py
```

The API will be accessible at `http://127.0.0.1:8888`.

## Endpoint Documentation

### API Authentication

All endpoints require API key authentication. You can provide the API key in two ways:
1. As a header: `x-api-key`
2. As a URL parameter: `?api_key=your_api_key_here`

### Endpoints

#### 1. Create a PPP Secret

- **URL**: `/ppp-secret`
- **Method**: `POST`
- **Headers**: 
  - `x-api-key`: Your API key
- **Body**:
  ```json
  {
    "name": "testuser",
    "password": "testpass",
    "profile": "default"
  }
  ```
- **Response**:
  - **201 Created**:
    ```json
    {
      "message": "PPP Secret 'testuser' created successfully."
    }
    ```
  - **400 Bad Request**:
    ```json
    {
      "error": "Name, password, and profile are required"
    }
    ```

#### 2. Get a PPP Secret by Name

- **URL**: `/ppp-secret/<name>`
- **Method**: `GET`
- **Headers**: 
  - `x-api-key`: Your API key
- **Response**:
  - **200 OK**: Returns data for the specified `ppp secret`
  - **404 Not Found**:
    ```json
    {
      "error": "PPP Secret 'testuser' not found"
    }
    ```

#### 3. Get All PPP Secrets

- **URL**: `/ppp-secret`
- **Method**: `GET`
- **Headers**: 
  - `x-api-key`: Your API key
- **Response**:
  - **200 OK**: Returns a list of all `ppp secret` entries

#### 4. Update a PPP Secret

- **URL**: `/ppp-secret/<name>`
- **Method**: `PUT`
- **Headers**: 
  - `x-api-key`: Your API key
- **Body** (optional):
  ```json
  {
    "password": "newpass",
    "profile": "newprofile"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "PPP Secret 'testuser' updated successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": "PPP Secret 'testuser' not found"
    }
    ```

#### 5. Disable a PPP Secret

- **URL**: `/ppp-secret/<name>/disable`
- **Method**: `POST`
- **Headers**: 
  - `x-api-key`: Your API key
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "PPP Secret 'testuser' disabled successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": "PPP Secret 'testuser' not found"
    }
    ```

#### 6. Enable a PPP Secret

- **URL**: `/ppp-secret/<name>/enable`
- **Method**: `POST`
- **Headers**: 
  - `x-api-key`: Your API key
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "PPP Secret 'testuser' enabled successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": "PPP Secret 'testuser' not found"
    }
    ```

#### 7. Delete a PPP Secret

- **URL**: `/ppp-secret/<name>`
- **Method**: `DELETE`
- **Headers**: 
  - `x-api-key`: Your API key
- **Response**:
  - **200 OK**:
    ```json
    {
      "message": "PPP Secret 'testuser' deleted successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": "PPP Secret 'testuser' not found"
    }
    ```

### Example Requests

#### Using `cURL`

1. **Create a PPP Secret**:
   ```bash
   curl -X POST http://127.0.0.1:8888/ppp-secret -H "Content-Type: application/json" -H "x-api-key: your_api_key_here" -d "{\"name\":\"testuser\", \"password\":\"testpass\", \"profile\":\"default\"}"
   ```

2. **Get All PPP Secrets**:
   ```bash
   curl -X GET http://127.0.0.1:8888/ppp-secret -H "x-api-key: your_api_key_here"
   ```

3. **Disable a PPP Secret**:
   ```bash
   curl -X POST http://127.0.0.1:8888/ppp-secret/testuser/disable -H "x-api-key: your_api_key_here"
   ```

### Accessing the API from a Browser

If you want to access the API from a browser, you can pass the API key as a URL parameter, like this:

```
http://127.0.0.1:8888/ppp-secret?api_key=your_api_key_here
```

---

This documentation provides a complete guide on how to use the API. Make sure to replace `your_api_key_here` with your actual API key as defined in the configuration file.
