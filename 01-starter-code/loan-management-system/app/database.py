"""
CSI403 Full Stack Development
Database Connection - SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# ============================================
# DATABASE CONFIGURATION
# ============================================

# Get database URL from environment variable or use default
# Format: mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mssql+pyodbc://sa:YourStrong@Password123@localhost:1433/LoanDB?driver=ODBC+Driver+17+for+SQL+Server"
)

# For SQLite (development/testing)
SQLITE_URL = "sqlite:///./loan_system.db"

# Use SQLite for development if MSSQL not available
USE_SQLITE = os.getenv("USE_SQLITE", "true").lower() == "true"

if USE_SQLITE:
    engine = create_engine(
        SQLITE_URL,
        connect_args={"check_same_thread": False}  # SQLite specific
    )
else:
    engine = create_engine(DATABASE_URL)

# ============================================
# SESSION CONFIGURATION
# ============================================

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# ============================================
# DEPENDENCY
# ============================================

def get_db():
    """
    Dependency function for FastAPI routes.
    Creates a database session and ensures it's closed after use.
    
    Usage:
        @app.get("/items")
        def get_items(db: Session = Depends(get_db)):
            return db.query(Item).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============================================
# DATABASE INITIALIZATION
# ============================================

def init_db():
    """
    Initialize database tables.
    Call this on application startup.
    """
    # Import models to register them with Base
    import models
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

def drop_db():
    """
    Drop all database tables.
    WARNING: This will delete all data!
    """
    Base.metadata.drop_all(bind=engine)
    print("All database tables dropped!")

# ============================================
# UTILITY FUNCTIONS
# ============================================

def check_connection():
    """Test database connection"""
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        print("Database connection successful!")
        return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False


if __name__ == "__main__":
    # Test connection when running directly
    check_connection()
    init_db()
