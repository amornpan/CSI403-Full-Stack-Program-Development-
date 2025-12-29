# Workshop 4: 🎨 Frontend Basics

## 📋 Overview
| Item | Detail |
|------|--------|
| **Duration** | 3 คาบ (2.5 ชม.) |
| **Score** | 8% (4 × 2%) |
| **Goal** | HTML + Bootstrap + JavaScript |

---

## 💻 CP1: HTML + Bootstrap Setup (2%)

### app/static/index.html
```html
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;TaskFlow&lt;/title&gt;
    &lt;link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;nav class="navbar navbar-dark bg-primary"&gt;
        &lt;div class="container"&gt;
            &lt;span class="navbar-brand"&gt;TaskFlow&lt;/span&gt;
        &lt;/div&gt;
    &lt;/nav&gt;
    &lt;main class="container my-4"&gt;
        &lt;h1&gt;Tasks&lt;/h1&gt;
        &lt;div id="task-list"&gt;&lt;/div&gt;
    &lt;/main&gt;
    &lt;script src="js/app.js"&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```

---

## 💻 CP2: Task List UI (2%)

Add stats cards and task list container.

---

## 💻 CP3: Create Form (2%)

Add Bootstrap modal with form.

---

## 💻 CP4: JavaScript + Fetch (2%)

### app/static/js/app.js
```javascript
const API_URL = '/api/tasks';

async function loadTasks() {
    const response = await fetch(API_URL);
    const tasks = await response.json();
    displayTasks(tasks);
}

async function createTask() {
    const title = document.getElementById('task-title').value;
    await fetch(API_URL, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title})
    });
    loadTasks();
}

document.addEventListener('DOMContentLoaded', loadTasks);
```

```bash
git add . &amp;&amp; git commit -m "Add frontend" &amp;&amp; git push
```

---

[📖 Extended →](../../docs/extended/week04-css-responsive.md)
