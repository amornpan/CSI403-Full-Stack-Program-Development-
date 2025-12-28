# Lab 04: Frontend Basics (HTML/CSS/JS + Bootstrap)

**Week 5 | 8%**

## 🎯 Objectives

เมื่อจบ Lab นี้ นักศึกษาจะสามารถ:
- สร้างหน้าเว็บด้วย HTML5
- จัดรูปแบบด้วย CSS3 และ Bootstrap 5
- ใช้ JavaScript สำหรับ DOM manipulation
- สร้าง UI สำหรับ TaskFlow

## 📋 Prerequisites

- Lab 3 เสร็จแล้ว (มี API + Database)
- ความรู้พื้นฐาน HTML/CSS

---

## 💻 Part 1: HTML Structure (30 min)

### 1.1 Create Static HTML Files

สร้างโฟลเดอร์ `app/static/html/` สำหรับทดสอบ HTML แบบ Static

```bash
mkdir -p app/static/html
```

### 1.2 Create Dashboard Page

สร้างไฟล์ `app/static/html/dashboard.html`:

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - TaskFlow</title>
    
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link href="../css/style.css" rel="stylesheet">
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="dashboard.html">
                <i class="bi bi-check2-square"></i> TaskFlow
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link active" href="dashboard.html">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="tasks.html">
                            <i class="bi bi-list-task"></i> Tasks
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="categories.html">
                            <i class="bi bi-folder"></i> Categories
                        </a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">
                            <i class="bi bi-person-circle"></i> John Doe
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end">
                            <li><a class="dropdown-item" href="#">Profile</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="login.html">Logout</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container mt-4">
        <h1 class="mb-4">
            <i class="bi bi-speedometer2"></i> Dashboard
        </h1>

        <!-- Statistics Cards -->
        <div class="row mb-4">
            <div class="col-md-3">
                <div class="card bg-warning text-dark">
                    <div class="card-body">
                        <div class="d-flex justify-content-between">
                            <div>
                                <h2 class="mb-0" id="pendingCount">5</h2>
                                <p class="mb-0">Pending</p>
                            </div>
                            <i class="bi bi-hourglass-split fs-1 opacity-50"></i>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card bg-primary text-white">
                    <div class="card-body">
                        <div class="d-flex justify-content-between">
                            <div>
                                <h2 class="mb-0" id="progressCount">3</h2>
                                <p class="mb-0">In Progress</p>
                            </div>
                            <i class="bi bi-arrow-repeat fs-1 opacity-50"></i>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card bg-success text-white">
                    <div class="card-body">
                        <div class="d-flex justify-content-between">
                            <div>
                                <h2 class="mb-0" id="doneCount">12</h2>
                                <p class="mb-0">Done</p>
                            </div>
                            <i class="bi bi-check-circle fs-1 opacity-50"></i>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card bg-danger text-white">
                    <div class="card-body">
                        <div class="d-flex justify-content-between">
                            <div>
                                <h2 class="mb-0" id="overdueCount">2</h2>
                                <p class="mb-0">Overdue</p>
                            </div>
                            <i class="bi bi-exclamation-triangle fs-1 opacity-50"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <!-- Quick Add Task -->
            <div class="col-md-6">
                <div class="card mb-4">
                    <div class="card-header bg-primary text-white">
                        <i class="bi bi-plus-circle"></i> Quick Add Task
                    </div>
                    <div class="card-body">
                        <form id="quickAddForm">
                            <div class="mb-3">
                                <input type="text" class="form-control" id="quickTitle" 
                                       placeholder="Task title..." required>
                            </div>
                            <div class="row">
                                <div class="col-md-6 mb-3">
                                    <select class="form-select" id="quickPriority">
                                        <option value="low">🟢 Low</option>
                                        <option value="medium" selected>🟡 Medium</option>
                                        <option value="high">🔴 High</option>
                                    </select>
                                </div>
                                <div class="col-md-6 mb-3">
                                    <input type="date" class="form-control" id="quickDueDate">
                                </div>
                            </div>
                            <button type="submit" class="btn btn-primary w-100">
                                <i class="bi bi-plus"></i> Add Task
                            </button>
                        </form>
                    </div>
                </div>
            </div>

            <!-- Upcoming Tasks -->
            <div class="col-md-6">
                <div class="card mb-4">
                    <div class="card-header bg-info text-white d-flex justify-content-between">
                        <span><i class="bi bi-calendar-event"></i> Upcoming Tasks</span>
                        <a href="tasks.html" class="btn btn-sm btn-light">View All</a>
                    </div>
                    <div class="list-group list-group-flush" id="upcomingTasks">
                        <a href="#" class="list-group-item list-group-item-action">
                            <div class="d-flex w-100 justify-content-between">
                                <h6 class="mb-1">Complete Lab 4</h6>
                                <small class="text-danger">Tomorrow</small>
                            </div>
                            <small>
                                <span class="badge bg-danger">High</span>
                                <span class="badge bg-warning text-dark">Pending</span>
                            </small>
                        </a>
                        <a href="#" class="list-group-item list-group-item-action">
                            <div class="d-flex w-100 justify-content-between">
                                <h6 class="mb-1">Review Python</h6>
                                <small class="text-muted">Jan 25</small>
                            </div>
                            <small>
                                <span class="badge bg-warning text-dark">Medium</span>
                                <span class="badge bg-primary">In Progress</span>
                            </small>
                        </a>
                        <a href="#" class="list-group-item list-group-item-action">
                            <div class="d-flex w-100 justify-content-between">
                                <h6 class="mb-1">Setup Database</h6>
                                <small class="text-muted">Jan 28</small>
                            </div>
                            <small>
                                <span class="badge bg-success">Low</span>
                                <span class="badge bg-warning text-dark">Pending</span>
                            </small>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Custom JS -->
    <script src="../js/main.js"></script>
    <script src="../js/dashboard.js"></script>
</body>
</html>
```

---

## 💻 Part 2: Tasks Page (40 min)

### 2.1 Create Tasks Page

สร้างไฟล์ `app/static/html/tasks.html`:

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tasks - TaskFlow</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
    <link href="../css/style.css" rel="stylesheet">
</head>
<body>
    <!-- Navbar (same as dashboard) -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="dashboard.html">
                <i class="bi bi-check2-square"></i> TaskFlow
            </a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="dashboard.html">Dashboard</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="tasks.html">Tasks</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="categories.html">Categories</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        <!-- Header -->
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1><i class="bi bi-list-task"></i> Tasks</h1>
            <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#taskModal">
                <i class="bi bi-plus-circle"></i> New Task
            </button>
        </div>

        <!-- Filters -->
        <div class="card mb-4">
            <div class="card-body">
                <div class="row g-3">
                    <div class="col-md-4">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-search"></i></span>
                            <input type="text" class="form-control" id="searchInput" placeholder="Search tasks...">
                        </div>
                    </div>
                    <div class="col-md-2">
                        <select class="form-select" id="statusFilter">
                            <option value="">All Status</option>
                            <option value="pending">⏳ Pending</option>
                            <option value="in_progress">🔄 In Progress</option>
                            <option value="done">✅ Done</option>
                        </select>
                    </div>
                    <div class="col-md-2">
                        <select class="form-select" id="priorityFilter">
                            <option value="">All Priority</option>
                            <option value="low">🟢 Low</option>
                            <option value="medium">🟡 Medium</option>
                            <option value="high">🔴 High</option>
                        </select>
                    </div>
                    <div class="col-md-2">
                        <select class="form-select" id="categoryFilter">
                            <option value="">All Categories</option>
                            <option value="1">📚 Study</option>
                            <option value="2">💼 Work</option>
                            <option value="3">🏠 Personal</option>
                        </select>
                    </div>
                    <div class="col-md-2">
                        <button class="btn btn-outline-secondary w-100" onclick="clearFilters()">
                            <i class="bi bi-x-circle"></i> Clear
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tasks Table -->
        <div class="card">
            <div class="table-responsive">
                <table class="table table-hover mb-0">
                    <thead class="table-dark">
                        <tr>
                            <th style="width: 40px;">
                                <input type="checkbox" class="form-check-input" id="selectAll">
                            </th>
                            <th>Title</th>
                            <th>Category</th>
                            <th>Status</th>
                            <th>Priority</th>
                            <th>Due Date</th>
                            <th style="width: 150px;">Actions</th>
                        </tr>
                    </thead>
                    <tbody id="tasksTableBody">
                        <!-- Tasks will be loaded here via JavaScript -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Task Modal -->
    <div class="modal fade" id="taskModal" tabindex="-1">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header bg-primary text-white">
                    <h5 class="modal-title" id="taskModalTitle">
                        <i class="bi bi-plus-circle"></i> New Task
                    </h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <form id="taskForm">
                        <input type="hidden" id="taskId">
                        <div class="mb-3">
                            <label class="form-label">Title *</label>
                            <input type="text" class="form-control" id="taskTitle" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Description</label>
                            <textarea class="form-control" id="taskDescription" rows="3"></textarea>
                        </div>
                        <div class="row">
                            <div class="col-md-4 mb-3">
                                <label class="form-label">Status</label>
                                <select class="form-select" id="taskStatus">
                                    <option value="pending">⏳ Pending</option>
                                    <option value="in_progress">🔄 In Progress</option>
                                    <option value="done">✅ Done</option>
                                </select>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label class="form-label">Priority</label>
                                <select class="form-select" id="taskPriority">
                                    <option value="low">🟢 Low</option>
                                    <option value="medium">🟡 Medium</option>
                                    <option value="high">🔴 High</option>
                                </select>
                            </div>
                            <div class="col-md-4 mb-3">
                                <label class="form-label">Category</label>
                                <select class="form-select" id="taskCategory">
                                    <option value="">No Category</option>
                                    <option value="1">📚 Study</option>
                                    <option value="2">💼 Work</option>
                                </select>
                            </div>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Due Date</label>
                            <input type="datetime-local" class="form-control" id="taskDueDate">
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    <button type="button" class="btn btn-primary" onclick="saveTask()">
                        <i class="bi bi-save"></i> Save
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div class="modal fade" id="deleteModal" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header bg-danger text-white">
                    <h5 class="modal-title"><i class="bi bi-trash"></i> Delete Task</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <p>Are you sure you want to delete this task?</p>
                    <p class="fw-bold" id="deleteTaskTitle"></p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    <button type="button" class="btn btn-danger" onclick="confirmDelete()">
                        <i class="bi bi-trash"></i> Delete
                    </button>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="../js/main.js"></script>
    <script src="../js/tasks.js"></script>
</body>
</html>
```

---

## 💻 Part 3: CSS Styling (30 min)

### 3.1 Create Custom CSS

สร้างไฟล์ `app/static/css/style.css`:

```css
/* app/static/css/style.css */
/* TaskFlow - Custom Styles */

/* ===== Global Styles ===== */
:root {
    --primary-color: #0d6efd;
    --success-color: #198754;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
    --info-color: #0dcaf0;
}

body {
    background-color: #f8f9fa;
    min-height: 100vh;
}

/* ===== Navbar ===== */
.navbar-brand {
    font-weight: bold;
    font-size: 1.5rem;
}

.navbar-brand i {
    margin-right: 8px;
}

/* ===== Cards ===== */
.card {
    border: none;
    box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
    transition: box-shadow 0.2s ease;
}

.card:hover {
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}

.card-header {
    font-weight: 600;
}

/* ===== Statistics Cards ===== */
.card h2 {
    font-size: 2.5rem;
    font-weight: bold;
}

/* ===== Tables ===== */
.table th {
    font-weight: 600;
    white-space: nowrap;
}

.table td {
    vertical-align: middle;
}

/* ===== Badges ===== */
.badge {
    font-weight: 500;
    padding: 0.4em 0.6em;
}

/* ===== Buttons ===== */
.btn {
    border-radius: 0.375rem;
    font-weight: 500;
}

.btn-sm {
    padding: 0.25rem 0.5rem;
}

/* ===== Forms ===== */
.form-control:focus,
.form-select:focus {
    border-color: var(--primary-color);
    box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
}

/* ===== List Group ===== */
.list-group-item {
    border-left: none;
    border-right: none;
}

.list-group-item:first-child {
    border-top: none;
}

.list-group-item-action:hover {
    background-color: #f8f9fa;
}

/* ===== Task Status Colors ===== */
.status-pending { color: #ffc107; }
.status-in_progress { color: #0d6efd; }
.status-done { color: #198754; }

/* ===== Priority Colors ===== */
.priority-low { color: #198754; }
.priority-medium { color: #ffc107; }
.priority-high { color: #dc3545; }

/* ===== Overdue ===== */
.overdue {
    color: #dc3545;
    font-weight: bold;
}

/* ===== Modal ===== */
.modal-header {
    border-bottom: none;
}

.modal-footer {
    border-top: none;
}

/* ===== Animations ===== */
.fade-in {
    animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ===== Responsive ===== */
@media (max-width: 768px) {
    .card h2 {
        font-size: 1.5rem;
    }
    
    .table-responsive {
        font-size: 0.875rem;
    }
    
    .btn-sm {
        padding: 0.2rem 0.4rem;
        font-size: 0.75rem;
    }
}

/* ===== Loading Spinner ===== */
.spinner-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
}

/* ===== Toast Notifications ===== */
.toast-container {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 9999;
}
```

---

## 💻 Part 4: JavaScript (40 min)

### 4.1 Create Main JS

สร้างไฟล์ `app/static/js/main.js`:

```javascript
// app/static/js/main.js
// TaskFlow - Main JavaScript

const API_URL = '/api';

// ===== Utility Functions =====

/**
 * Show toast notification
 */
function showToast(message, type = 'success') {
    const toastContainer = document.querySelector('.toast-container') || createToastContainer();
    
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    
    toastContainer.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    toast.addEventListener('hidden.bs.toast', () => toast.remove());
}

function createToastContainer() {
    const container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
    return container;
}

/**
 * Format date for display
 */
function formatDate(dateString) {
    if (!dateString) return '-';
    const date = new Date(dateString);
    return date.toLocaleDateString('th-TH', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

/**
 * Format datetime for input
 */
function formatDateTimeForInput(dateString) {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toISOString().slice(0, 16);
}

/**
 * Get status badge HTML
 */
function getStatusBadge(status) {
    const badges = {
        'pending': '<span class="badge bg-warning text-dark">⏳ Pending</span>',
        'in_progress': '<span class="badge bg-primary">🔄 In Progress</span>',
        'done': '<span class="badge bg-success">✅ Done</span>'
    };
    return badges[status] || status;
}

/**
 * Get priority badge HTML
 */
function getPriorityBadge(priority) {
    const badges = {
        'low': '<span class="badge bg-success">🟢 Low</span>',
        'medium': '<span class="badge bg-warning text-dark">🟡 Medium</span>',
        'high': '<span class="badge bg-danger">🔴 High</span>'
    };
    return badges[priority] || priority;
}

/**
 * Check if date is overdue
 */
function isOverdue(dateString) {
    if (!dateString) return false;
    return new Date(dateString) < new Date();
}

/**
 * Show loading spinner
 */
function showLoading() {
    const overlay = document.createElement('div');
    overlay.className = 'spinner-overlay';
    overlay.id = 'loadingOverlay';
    overlay.innerHTML = `
        <div class="spinner-border text-primary" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    `;
    document.body.appendChild(overlay);
}

/**
 * Hide loading spinner
 */
function hideLoading() {
    const overlay = document.getElementById('loadingOverlay');
    if (overlay) overlay.remove();
}

/**
 * API request wrapper
 */
async function apiRequest(endpoint, options = {}) {
    try {
        const response = await fetch(`${API_URL}${endpoint}`, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'An error occurred');
        }
        
        if (response.status === 204) {
            return null;
        }
        
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// ===== Initialize =====
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 TaskFlow initialized');
});
```

### 4.2 Create Tasks JS

สร้างไฟล์ `app/static/js/tasks.js`:

```javascript
// app/static/js/tasks.js
// TaskFlow - Tasks Page JavaScript

let tasks = [];
let taskToDelete = null;

// ===== Load Tasks =====

async function loadTasks() {
    try {
        showLoading();
        const params = new URLSearchParams();
        
        const status = document.getElementById('statusFilter')?.value;
        const priority = document.getElementById('priorityFilter')?.value;
        const search = document.getElementById('searchInput')?.value;
        
        if (status) params.append('status', status);
        if (priority) params.append('priority', priority);
        if (search) params.append('search', search);
        
        const response = await apiRequest(`/tasks?${params}`);
        tasks = response.tasks;
        renderTasks();
    } catch (error) {
        showToast('Failed to load tasks: ' + error.message, 'danger');
    } finally {
        hideLoading();
    }
}

// ===== Render Tasks =====

function renderTasks() {
    const tbody = document.getElementById('tasksTableBody');
    if (!tbody) return;
    
    if (tasks.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="7" class="text-center py-4">
                    <i class="bi bi-inbox fs-1 text-muted"></i>
                    <p class="text-muted mt-2">No tasks found</p>
                    <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#taskModal">
                        <i class="bi bi-plus"></i> Create Task
                    </button>
                </td>
            </tr>
        `;
        return;
    }
    
    tbody.innerHTML = tasks.map(task => `
        <tr class="fade-in">
            <td>
                <input type="checkbox" class="form-check-input task-checkbox" data-id="${task.id}">
            </td>
            <td>
                <strong>${escapeHtml(task.title)}</strong>
                ${task.description ? `<br><small class="text-muted">${escapeHtml(task.description.substring(0, 50))}...</small>` : ''}
            </td>
            <td>
                ${task.category ? `<span class="badge" style="background-color: ${task.category.color}">${escapeHtml(task.category.name)}</span>` : '-'}
            </td>
            <td>${getStatusBadge(task.status)}</td>
            <td>${getPriorityBadge(task.priority)}</td>
            <td class="${isOverdue(task.due_date) && task.status !== 'done' ? 'overdue' : ''}">
                ${formatDate(task.due_date)}
            </td>
            <td>
                <button class="btn btn-sm btn-outline-primary" onclick="editTask(${task.id})" title="Edit">
                    <i class="bi bi-pencil"></i>
                </button>
                <button class="btn btn-sm btn-outline-success" onclick="toggleStatus(${task.id})" title="Toggle Status">
                    <i class="bi bi-check2"></i>
                </button>
                <button class="btn btn-sm btn-outline-danger" onclick="deleteTask(${task.id}, '${escapeHtml(task.title)}')" title="Delete">
                    <i class="bi bi-trash"></i>
                </button>
            </td>
        </tr>
    `).join('');
}

// ===== CRUD Operations =====

function openNewTaskModal() {
    document.getElementById('taskForm').reset();
    document.getElementById('taskId').value = '';
    document.getElementById('taskModalTitle').innerHTML = '<i class="bi bi-plus-circle"></i> New Task';
    new bootstrap.Modal(document.getElementById('taskModal')).show();
}

async function editTask(id) {
    const task = tasks.find(t => t.id === id);
    if (!task) return;
    
    document.getElementById('taskId').value = task.id;
    document.getElementById('taskTitle').value = task.title;
    document.getElementById('taskDescription').value = task.description || '';
    document.getElementById('taskStatus').value = task.status;
    document.getElementById('taskPriority').value = task.priority;
    document.getElementById('taskCategory').value = task.category_id || '';
    document.getElementById('taskDueDate').value = formatDateTimeForInput(task.due_date);
    
    document.getElementById('taskModalTitle').innerHTML = '<i class="bi bi-pencil"></i> Edit Task';
    new bootstrap.Modal(document.getElementById('taskModal')).show();
}

async function saveTask() {
    const id = document.getElementById('taskId').value;
    const taskData = {
        title: document.getElementById('taskTitle').value,
        description: document.getElementById('taskDescription').value || null,
        status: document.getElementById('taskStatus').value,
        priority: document.getElementById('taskPriority').value,
        category_id: document.getElementById('taskCategory').value || null,
        due_date: document.getElementById('taskDueDate').value || null
    };
    
    try {
        showLoading();
        
        if (id) {
            await apiRequest(`/tasks/${id}`, {
                method: 'PUT',
                body: JSON.stringify(taskData)
            });
            showToast('Task updated successfully!');
        } else {
            await apiRequest('/tasks', {
                method: 'POST',
                body: JSON.stringify(taskData)
            });
            showToast('Task created successfully!');
        }
        
        bootstrap.Modal.getInstance(document.getElementById('taskModal')).hide();
        loadTasks();
    } catch (error) {
        showToast('Failed to save task: ' + error.message, 'danger');
    } finally {
        hideLoading();
    }
}

function deleteTask(id, title) {
    taskToDelete = id;
    document.getElementById('deleteTaskTitle').textContent = title;
    new bootstrap.Modal(document.getElementById('deleteModal')).show();
}

async function confirmDelete() {
    if (!taskToDelete) return;
    
    try {
        showLoading();
        await apiRequest(`/tasks/${taskToDelete}`, { method: 'DELETE' });
        showToast('Task deleted successfully!');
        bootstrap.Modal.getInstance(document.getElementById('deleteModal')).hide();
        loadTasks();
    } catch (error) {
        showToast('Failed to delete task: ' + error.message, 'danger');
    } finally {
        hideLoading();
        taskToDelete = null;
    }
}

async function toggleStatus(id) {
    const task = tasks.find(t => t.id === id);
    if (!task) return;
    
    const statusOrder = ['pending', 'in_progress', 'done'];
    const currentIndex = statusOrder.indexOf(task.status);
    const newStatus = statusOrder[(currentIndex + 1) % statusOrder.length];
    
    try {
        await apiRequest(`/tasks/${id}`, {
            method: 'PUT',
            body: JSON.stringify({ status: newStatus })
        });
        showToast(`Status changed to ${newStatus.replace('_', ' ')}`);
        loadTasks();
    } catch (error) {
        showToast('Failed to update status: ' + error.message, 'danger');
    }
}

// ===== Filters =====

function clearFilters() {
    document.getElementById('searchInput').value = '';
    document.getElementById('statusFilter').value = '';
    document.getElementById('priorityFilter').value = '';
    document.getElementById('categoryFilter').value = '';
    loadTasks();
}

// ===== Utilities =====

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ===== Event Listeners =====

document.addEventListener('DOMContentLoaded', () => {
    loadTasks();
    
    // Filter change events
    document.getElementById('statusFilter')?.addEventListener('change', loadTasks);
    document.getElementById('priorityFilter')?.addEventListener('change', loadTasks);
    document.getElementById('categoryFilter')?.addEventListener('change', loadTasks);
    
    // Search with debounce
    let searchTimeout;
    document.getElementById('searchInput')?.addEventListener('input', () => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(loadTasks, 300);
    });
    
    // Select all checkbox
    document.getElementById('selectAll')?.addEventListener('change', (e) => {
        document.querySelectorAll('.task-checkbox').forEach(cb => {
            cb.checked = e.target.checked;
        });
    });
});
```

---

## 📤 Submission

### Checklist

- [ ] HTML pages ครบ (Dashboard, Tasks)
- [ ] Bootstrap 5 styling ถูกต้อง
- [ ] Custom CSS (style.css)
- [ ] JavaScript functions ทำงานได้
- [ ] Responsive design
- [ ] Modal forms ทำงานได้

### Git Commands

```bash
git checkout -b feature/lab04-frontend
git add .
git commit -m "Lab 4: Frontend basics - HTML/CSS/JS + Bootstrap"
git push -u origin feature/lab04-frontend
```

---

## ✅ Grading Rubric (8%)

| เกณฑ์ | คะแนน |
|-------|:-----:|
| HTML Structure ถูกต้อง | 2% |
| Bootstrap Components | 2% |
| Custom CSS | 1.5% |
| JavaScript Functions | 2% |
| Responsive Design | 0.5% |
| **รวม** | **8%** |

---

**Deadline:** ก่อนเที่ยงคืนวันอาทิตย์ สัปดาห์ที่ 5
