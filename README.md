# Project: MikrotikLibrouteros

## End-point: read all secrets
### Method: GET
>```
>localhost:8888/ppp-secret?api_key=a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng
>```
### Query Params

|Param|value|
|---|---|
|api_key|a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng|


### 🔑 Authentication inherit

|Param|value|Type|
|---|---|---|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: create secret
### Method: POST
>```
>localhost:8888/ppp-secret?api_key=a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng
>```
### Body (**raw**)

```json
{
  "name": "secret_name",
  "password": "secret_password",
  "profile": "default"
}

```

### Query Params

|Param|value|
|---|---|
|api_key|a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng|


### 🔑 Authentication inherit

|Param|value|Type|
|---|---|---|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: read byname
### Method: GET
>```
>localhost:8888/ppp-secret/secret_name?api_key=a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng
>```
### Body (**raw**)

```json

```

### Query Params

|Param|value|
|---|---|
|api_key|a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng|


### 🔑 Authentication inherit

|Param|value|Type|
|---|---|---|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: update byname
### Method: PUT
>```
>localhost:8888/ppp-secret/secret_name?api_key=a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng
>```
### Body (**raw**)

```json
{
  "password": "new_password",
  "profile": "default"
}
```

### Query Params

|Param|value|
|---|---|
|api_key|a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng|


### 🔑 Authentication inherit

|Param|value|Type|
|---|---|---|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: delete byname
### Method: DELETE
>```
>localhost:8888/ppp-secret/secret_name?api_key=a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng
>```
### Body (**raw**)

```json

```

### Query Params

|Param|value|
|---|---|
|api_key|a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng|


### 🔑 Authentication inherit

|Param|value|Type|
|---|---|---|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: disable byname
### Method: POST
>```
>localhost:8888/ppp-secret/secret_name/disable?api_key=a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng
>```
### Body (**raw**)

```json

```

### Query Params

|Param|value|
|---|---|
|api_key|a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng|


### 🔑 Authentication inherit

|Param|value|Type|
|---|---|---|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: enable byname
### Method: POST
>```
>localhost:8888/ppp-secret/secret_name/enable?api_key=a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng
>```
### Body (**raw**)

```json

```

### Query Params

|Param|value|
|---|---|
|api_key|a0f5b8c0-2b9b-4f8a-9b3b-9a1b2c3d4e5fanskdng|


### 🔑 Authentication inherit

|Param|value|Type|
|---|---|---|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________
Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
