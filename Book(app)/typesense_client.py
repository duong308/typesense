import typesense

client = typesense.Client({
    "nodes": [{
        "host": "localhost",  # Nếu chạy trên cùng máy
        "port": "8108",
        "protocol": "http"
    }],
    "api_key": "308308",
    "connection_timeout_seconds": 2
})

print("✅ Đã kết nối với Typesense!")
