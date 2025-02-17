import typesense

client = typesense.Client({
    "nodes": [{
        "host": "localhost",
        "port": "8108",
        "protocol": "http"
    }],
    "api_key": "308"
})

# Tìm kiếm sách có từ khóa "Harry Potter"
search_parameters = {
    "q": "Harry Potter",
    "query_by": "title"
}

results = client.collections["books"].documents.search(search_parameters)

print("🔎 Kết quả tìm kiếm:", results)
