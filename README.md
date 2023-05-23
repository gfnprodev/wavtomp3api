# FastAPI WAV to MP3

WAV to MP3 is an API service for creating users, and downloading their files. 

Database: Postgresql
File manager: min.io

## Startup

Use [docker-compose](https://docs.docker.com/compose/) to start project.

Edit env.example to .env and enter your data


For start project use:
```bash
docker compose up
```

## API

### Endpoints

POST /user - Add user Example

```bash
curl -X 'POST' \
  'http://localhost:8000/user/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "username"
}'
```
Answer 
```json
{
  "id": 0,
  "token": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "username": "string",
  "audiofiles": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "user_id": 0,
      "created_at": "2023-05-23T16:38:18.440Z"
    }
  ],
  "created_at": "2023-05-23T16:38:18.440Z"
}
```
POST /record - Add new record
```bash
curl -X 'POST' \
  'http://localhost:8000/record/?user_id=123&token=3fa85f64-5717-4562-b3fc-2c963f66afa6' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@203713f6-bbe3-45b4-8163-e6ef74e5b6a5.mp3;type=audio/mpeg'
```
Answer
```json
{
  "url": "string"
}
```

GET /record - Download File
```bash
curl -X 'GET' \
  'http://localhost:8000/record/?id=3fa85f64-5717-4562-b3fc-2c963f66afa6&user_id=123' \
  -H 'accept: application/json'
```

### API DOCS /docs
