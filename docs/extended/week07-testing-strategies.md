# Extended: Testing Strategies

## Testing Pyramid
```
     /\     E2E (few)
    /──\    Integration
   /────\   Unit (many)
```

## Fixtures
```python
@pytest.fixture
def sample_task(db):
    task = Task(title="Test")
    db.add(task)
    db.commit()
    return task
```

## Mocking
```python
from unittest.mock import patch

@patch('app.email.send')
def test_register(mock_send, client):
    client.post("/register", data={...})
    mock_send.assert_called_once()
```

## Coverage
```bash
pytest --cov=app --cov-report=html
```
