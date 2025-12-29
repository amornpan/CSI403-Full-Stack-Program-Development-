# Workshop 5: 🔗 Full Integration

## 📋 Overview
| Item | Detail |
|------|--------|
| **Duration** | 3 คาบ (2.5 ชม.) |
| **Score** | 8% (4 × 2%) |
| **Goal** | Jinja2 + Session Auth |

---

## 💻 CP1: Jinja2 Setup (2%)

```bash
pip install jinja2 python-multipart
```

```python
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
```

---

## 💻 CP2: Template Inheritance (2%)

### app/templates/base.html
```html
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;{% block title %}TaskFlow{% endblock %}&lt;/title&gt;
    &lt;link href="bootstrap.css" rel="stylesheet"&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;nav&gt;...&lt;/nav&gt;
    &lt;main&gt;{% block content %}{% endblock %}&lt;/main&gt;
&lt;/body&gt;
&lt;/html&gt;
```

---

## 💻 CP3: Login/Register (2%)

Create login.html and register.html templates with forms.

---

## 💻 CP4: Session Auth (2%)

```python
from starlette.middleware.sessions import SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="secret")

@router.post("/login")
def login(request: Request, username: str = Form(), password: str = Form()):
    # Verify user
    request.session["user_id"] = user.id
    return RedirectResponse("/dashboard")
```

---

[📖 Extended →](../../docs/extended/week05-security.md)
