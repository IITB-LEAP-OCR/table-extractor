# TSR API (Table Structure Recognition)

A Dockerized Flask API for performing physical and logical table structure recognition on document images.

---

## 🚀 1. Creating the Docker Image

You can either build the Docker image locally or pull it from Docker Hub.

### 🔨 Build Locally

```bash
docker build -t tsr-image:1 .
```

### 📦 Pull from Docker Hub

```bash
docker pull your-dockerhub-username/tsr-image:1
```

> Replace `your-dockerhub-username` with your actual Docker Hub username.

---

## 🧱 2. Running the API Server (Container)

Run the container as a long-running service on port `8000`:

```bash
docker run --gpus all -d -p 8000:8000 \
  --name tsr-api-instance \
  -v /data/DHRUV/table-api/table-extractor/uploads:/app/uploads \
  tsr-image:1
```

### 🛠 Container Management Commands

| Action  | Command                           |
| ------- | --------------------------------- |
| Start   | `docker start tsr-api-instance`   |
| Restart | `docker restart tsr-api-instance` |
| Stop    | `docker stop tsr-api-instance`    |
| Logs    | `docker logs tsr-api-instance`    |

---

## 📡 3. API Usage

### ✅ Health Check

Verify the server is up:

```
GET http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

---

### 📤 Table Structure Recognition

Send a POST request to process an image:

```
POST http://localhost:8000/tsr
```

#### Example using `curl`:

```bash
curl -X POST http://localhost:8000/tsr -F "file=@/path/to/your/image.jpg"
```

#### Response (example):

```json
{
  "status": "success",
  "table_structure": "<table><tr><td>...</td></tr></table>"
}
```

---

## ⚠️ Common Errors

* **Tesseract Not Found**
  Ensure Tesseract is installed inside the container and accessible via PATH.

* **No NVIDIA Driver Found**
  Make sure NVIDIA GPU drivers are correctly installed on the host, and `--gpus all` is used when starting the container.

---

## 📁 Notes

* The mounted `uploads` folder at `/data/DHRUV/table-api/table-extractor/uploads` is used to store uploaded files during processing.
* Ensure that this path exists on the host and has the appropriate permissions.
