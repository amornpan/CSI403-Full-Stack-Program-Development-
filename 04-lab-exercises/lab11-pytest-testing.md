# Lab 11: Testing with pytest

**Week 12 | March 25-27, 2026 | 2%**

## 🎯 Objectives
- Write unit tests with pytest
- Test FastAPI endpoints
- Mock database operations
- Generate test coverage reports

## 🔧 Setup

```bash
pip install pytest pytest-asyncio httpx pytest-cov
mkdir tests
touch tests/__init__.py
```

## 💻 Part 1: pytest Basics (20 min)

### Exercise 1.1: First Tests
Create `tests/test_basic.py`:
```python
import pytest

# Simple test function
def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "hello".upper() == "HELLO"

def test_list():
    items = [1, 2, 3]
    assert len(items) == 3
    assert 2 in items

# Test with exception
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# Parametrized tests
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (10, 20),
])
def test_double(input, expected):
    assert input * 2 == expected
```

Run: `pytest tests/test_basic.py -v`

### Exercise 1.2: Test Business Logic
Create `tests/test_loan_calculations.py`:
```python
import pytest
from app.services.loan_service import LoanService

class TestLoanCalculations:
    
    def test_calculate_monthly_payment(self):
        # 100,000 THB at 7.5% for 36 months
        payment = LoanService.calculate_monthly_payment(100000, 7.5, 36)
        assert payment > 0
        assert 3000 < payment < 3500  # Reasonable range
    
    def test_calculate_monthly_payment_zero_rate(self):
        payment = LoanService.calculate_monthly_payment(100000, 0, 36)
        assert payment == pytest.approx(100000 / 36, rel=0.01)
    
    @pytest.mark.parametrize("income,years,expected_grade", [
        (1000000, 10, "A"),
        (600000, 5, "B"),
        (400000, 3, "C"),
        (250000, 2, "D"),
        (150000, 1, "E"),
        (100000, 0, "F"),
    ])
    def test_calculate_grade(self, income, years, expected_grade):
        grade = LoanService.calculate_grade(income, years)
        assert grade == expected_grade
    
    def test_get_interest_rate(self):
        assert LoanService.get_interest_rate("A") == 6.0
        assert LoanService.get_interest_rate("B") == 7.5
        assert LoanService.get_interest_rate("F") == 15.0
        assert LoanService.get_interest_rate("X") == 15.0  # Unknown grade


class TestPaymentSchedule:
    
    def test_generate_schedule_length(self):
        from app.services.payment_service import PaymentService
        
        schedule = PaymentService.generate_payment_schedule(100000, 7.5, 36)
        assert len(schedule) == 36
    
    def test_schedule_final_balance_zero(self):
        from app.services.payment_service import PaymentService
        
        schedule = PaymentService.generate_payment_schedule(100000, 7.5, 36)
        final_balance = schedule[-1]["balance"]
        assert final_balance == pytest.approx(0, abs=1)  # Within 1 THB
    
    def test_schedule_decreasing_balance(self):
        from app.services.payment_service import PaymentService
        
        schedule = PaymentService.generate_payment_schedule(100000, 7.5, 36)
        
        for i in range(1, len(schedule)):
            assert schedule[i]["balance"] < schedule[i-1]["balance"]
```

## 💻 Part 2: Testing FastAPI (30 min)

### Exercise 2.1: API Test Setup
Create `tests/conftest.py`:
```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db

# Test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database for each test"""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db_session):
    """Create test client with test database"""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()

@pytest.fixture
def sample_user(db_session):
    """Create a sample user for testing"""
    from app.models import User
    from app.auth.security import hash_password
    
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash=hash_password("TestPass123"),
        role="borrower"
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

@pytest.fixture
def sample_borrower(db_session, sample_user):
    """Create a sample borrower for testing"""
    from app.models import Borrower
    
    borrower = Borrower(
        user_id=sample_user.id,
        first_name="Test",
        last_name="User",
        phone="0812345678",
        annual_income=600000
    )
    db_session.add(borrower)
    db_session.commit()
    db_session.refresh(borrower)
    return borrower

@pytest.fixture
def auth_headers(client, sample_user):
    """Get authentication headers for protected routes"""
    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "TestPass123"}
    )
    # Return cookies for session auth
    return {"cookies": response.cookies}
```

### Exercise 2.2: API Tests
Create `tests/test_api.py`:
```python
import pytest
from fastapi import status

class TestHealthEndpoint:
    
    def test_health_check(self, client):
        response = client.get("/health")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["status"] == "healthy"


class TestUserEndpoints:
    
    def test_register_success(self, client):
        response = client.post(
            "/auth/register",
            json={
                "username": "newuser",
                "email": "new@example.com",
                "password": "NewPass123",
                "confirm_password": "NewPass123"
            }
        )
        assert response.status_code == status.HTTP_200_OK
        assert "user_id" in response.json()
    
    def test_register_duplicate_username(self, client, sample_user):
        response = client.post(
            "/auth/register",
            json={
                "username": "testuser",  # Already exists
                "email": "another@example.com",
                "password": "NewPass123",
                "confirm_password": "NewPass123"
            }
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_register_weak_password(self, client):
        response = client.post(
            "/auth/register",
            json={
                "username": "weakuser",
                "email": "weak@example.com",
                "password": "weak",
                "confirm_password": "weak"
            }
        )
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
    def test_login_success(self, client, sample_user):
        response = client.post(
            "/auth/login",
            json={"username": "testuser", "password": "TestPass123"}
        )
        assert response.status_code == status.HTTP_200_OK
        assert "session_token" in response.cookies or "message" in response.json()
    
    def test_login_wrong_password(self, client, sample_user):
        response = client.post(
            "/auth/login",
            json={"username": "testuser", "password": "WrongPass"}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestLoanEndpoints:
    
    def test_create_loan_unauthorized(self, client):
        response = client.post(
            "/loans",
            json={"amount": 100000, "term": 36}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_list_loans_empty(self, client, sample_user):
        # Login first
        client.post(
            "/auth/login",
            json={"username": "testuser", "password": "TestPass123"}
        )
        
        response = client.get("/loans")
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)
    
    def test_get_loan_not_found(self, client, sample_user):
        client.post(
            "/auth/login",
            json={"username": "testuser", "password": "TestPass123"}
        )
        
        response = client.get("/loans/99999")
        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestValidation:
    
    @pytest.mark.parametrize("amount,term,expected_status", [
        (100000, 36, 200),      # Valid
        (0, 36, 422),           # Zero amount
        (-1000, 36, 422),       # Negative amount
        (100000, 0, 422),       # Zero term
        (100000, 100, 422),     # Term too long
        (10000000, 36, 422),    # Amount too high
    ])
    def test_loan_validation(self, client, sample_user, sample_borrower, amount, term, expected_status):
        # This test would need proper authentication and borrower setup
        pass  # Implement based on your actual validation
```

## 💻 Part 3: Mocking (20 min)

### Exercise 3.1: Using Mocks
Create `tests/test_with_mocks.py`:
```python
import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

class TestWithMocks:
    
    def test_mock_database(self):
        """Test with mocked database"""
        mock_db = Mock()
        mock_db.query.return_value.filter.return_value.first.return_value = {
            "id": 1,
            "amount": 100000,
            "status": "current"
        }
        
        # Your function that uses db
        # result = get_loan(mock_db, 1)
        # assert result["id"] == 1
    
    @patch('app.services.loan_service.crud')
    def test_loan_eligibility(self, mock_crud):
        """Test eligibility check with mocked crud"""
        from app.services.loan_service import LoanService
        
        # Setup mock borrower
        mock_borrower = Mock()
        mock_borrower.annual_income = 600000
        mock_borrower.loans = []
        
        mock_crud.get_borrower.return_value = mock_borrower
        
        # Create mock db
        mock_db = Mock()
        
        eligible, message = LoanService.validate_loan_eligibility(
            borrower_id=1,
            loan_amount=200000,
            db=mock_db
        )
        
        assert eligible == True
    
    @patch('app.services.payment_service.datetime')
    def test_payment_with_mocked_date(self, mock_datetime):
        """Test payment processing with mocked datetime"""
        mock_datetime.now.return_value = datetime(2026, 3, 15)
        
        # Test your payment logic that uses datetime
        pass
```

## 💻 Part 4: Test Coverage (20 min)

### Exercise 4.1: Generate Coverage Report
```bash
# Run tests with coverage
pytest --cov=app tests/ --cov-report=html --cov-report=term

# View terminal report
pytest --cov=app tests/ --cov-report=term-missing

# Open HTML report
# open htmlcov/index.html
```

### Exercise 4.2: Coverage Configuration
Create `pytest.ini`:
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
```

Create `.coveragerc`:
```ini
[run]
source = app
omit = 
    app/__init__.py
    app/config.py
    tests/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
    if __name__ == .__main__.:

[html]
directory = htmlcov
```

## 📝 Assignment

Create comprehensive tests for the Loan Management System:

1. **Unit Tests** (40%):
   - Test all calculation functions
   - Test validation logic
   - Test business rules

2. **API Tests** (40%):
   - Test all CRUD endpoints
   - Test authentication flows
   - Test error handling

3. **Coverage** (20%):
   - Achieve at least 70% code coverage
   - Document untested areas

### Test File Structure:
```
tests/
├── __init__.py
├── conftest.py
├── test_calculations.py
├── test_validation.py
├── test_api_auth.py
├── test_api_loans.py
├── test_api_payments.py
└── test_integration.py
```

## 📤 Submission
```bash
# Run all tests
pytest -v

# With coverage
pytest --cov=app --cov-report=html

git add .
git commit -m "Lab 11: pytest testing"
git push
```

## ✅ Grading (2%)
| Criteria | Points |
|----------|--------|
| Unit tests | 0.5% |
| API tests | 0.5% |
| Mocking | 0.5% |
| Coverage > 70% | 0.5% |

---
**Deadline:** Before Week 13 class
