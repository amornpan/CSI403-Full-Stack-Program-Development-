# Extended: Security

## Password Hashing
```python
from passlib.context import CryptContext
pwd = CryptContext(schemes=["bcrypt"])
hash = pwd.hash(password)
pwd.verify(password, hash)
```

## SQL Injection Prevention
```python
# SQLAlchemy handles this automatically
db.query(User).filter(User.id == user_id)
```

## XSS Prevention
```html
{{ user_input | e }}  {# Jinja2 escapes by default #}
```

## CSRF
```python
from starlette_csrf import CSRFMiddleware
app.add_middleware(CSRFMiddleware, secret="key")
```
