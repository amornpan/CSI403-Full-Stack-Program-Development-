# Extended: REST Best Practices

## Use Nouns
```
GET /users      ✅
GET /getUsers   ❌
```

## HTTP Status Codes
| Code | Use |
|------|-----|
| 200 | GET success |
| 201 | POST success |
| 204 | DELETE success |
| 404 | Not found |
| 422 | Validation error |

## Pagination
```
GET /tasks?page=1&amp;per_page=10
```

## Filtering
```
GET /tasks?status=pending&amp;priority=high
```
