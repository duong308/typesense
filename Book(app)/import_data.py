import typesense
import json

# Khởi tạo kết nối đến Typesense
client = typesense.Client({
    "nodes": [{
        "host": "localhost",
        "port": "8108",
        "protocol": "http"
    }],
    "api_key": "308",  # Thay "xyz" bằng API Key thật của bạn
    "connection_timeout_seconds": 2
})
with open("books.jsonl", "r", encoding="utf-8") as f:
    books = [json.loads(line) for line in f]

response = client.collections["books"].documents.import_(books, {"action": "create"})

print("✅ Đã nhập dữ liệu thành công!")
print(response)
