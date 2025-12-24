-- CSI403 Full Stack Development
-- Sample Data for Loan Management System

-- Create Database
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'LoanDB')
BEGIN
    CREATE DATABASE LoanDB;
END
GO

USE LoanDB;
GO

-- Insert sample users (password: 'password123' hashed with bcrypt)
INSERT INTO users (username, email, password_hash, role, is_active) VALUES
('admin', 'admin@spuchonburi.ac.th', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewKyNiGRj1hNqCfm', 'admin', 1),
('john_doe', 'john@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewKyNiGRj1hNqCfm', 'borrower', 1),
('jane_smith', 'jane@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewKyNiGRj1hNqCfm', 'borrower', 1),
('bob_wilson', 'bob@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewKyNiGRj1hNqCfm', 'borrower', 1);

-- Insert sample borrowers
INSERT INTO borrowers (user_id, first_name, last_name, phone, annual_income, emp_title, emp_length, home_ownership, grade) VALUES
(2, 'John', 'Doe', '081-234-5678', 720000, 'Software Engineer', 5, 'rent', 'B'),
(3, 'Jane', 'Smith', '082-345-6789', 960000, 'Marketing Manager', 8, 'own', 'A'),
(4, 'Bob', 'Wilson', '083-456-7890', 480000, 'Sales Representative', 3, 'mortgage', 'C');

-- Insert sample loans
INSERT INTO loans (borrower_id, loan_amount, funded_amount, term, interest_rate, installment, purpose, status, application_date, issue_date) VALUES
(1, 500000, 500000, 36, 7.5, 15541.67, 'Home Improvement', 'current', '2026-01-15', '2026-01-20'),
(1, 200000, 200000, 24, 6.5, 8916.67, 'Education', 'fully_paid', '2025-06-01', '2025-06-05'),
(2, 1000000, 1000000, 60, 8.0, 20276.39, 'Business', 'current', '2026-01-10', '2026-01-15'),
(3, 300000, 0, 36, 9.0, 0, 'Personal', 'pending', '2026-01-20', NULL);

-- Insert sample payments
INSERT INTO payments (loan_id, payment_date, payment_amount, principal, interest, late_fee, remaining_balance, is_late, days_late) VALUES
(1, '2026-02-20', 15541.67, 12416.67, 3125.00, 0, 487583.33, 0, 0),
(1, '2026-03-20', 15541.67, 12494.34, 3047.33, 0, 475088.99, 0, 0),
(3, '2026-02-15', 20276.39, 13609.72, 6666.67, 0, 986390.28, 0, 0);

PRINT 'Sample data inserted successfully!';
GO
