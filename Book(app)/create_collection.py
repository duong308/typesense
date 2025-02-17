import typesense

# Khởi tạo kết nối đến Typesense
client = typesense.Client({
    "nodes": [{
        "host": "localhost",
        "port": "8108",
        "protocol": "http"
    }],
    "api_key": "308",  # Đổi "xyz" thành API Key thật của bạn
    "connection_timeout_seconds": 2
})

# Định nghĩa schema cho collection "books"
schema = {
    "name": "books",
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "title", "type": "string"},
        {"name": "authors", "type": "string[]", "facet": True},
        {"name": "publication_year", "type": "int32", "facet": True},
        {"name": "ratings_count", "type": "int32"},
        {"name": "average_rating", "type": "float"}
    ],
    "default_sorting_field": "ratings_count"
}

# Xóa collection cũ (nếu có)
try:
    client.collections["books"].delete()
except Exception:
    pass  # Bỏ qua lỗi nếu collection chưa tồn tại

# Tạo mới collection
client.collections.create(schema)
print("✅ Collection 'books' đã được tạo thành công!")
