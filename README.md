# CSI403 Full Stack Development - Teaching Materials

## Course Information
- **Course Code:** CSI403
- **Credits:** 3 (2-3-5)
- **Semester:** 2/2568 (January - April 2026)
- **Instructor:** Aj. Methas Khamjad
- **University:** Sripatum University Chonburi

## Technology Stack
| Layer | Technologies |
|-------|-------------|
| Frontend | Jinja2, HTML5, CSS3, Bootstrap 5 |
| Backend | FastAPI, Python, Pydantic |
| Database | MSSQL (Docker), SQLAlchemy |
| DevOps | Docker, Docker Compose, Jenkins |
| Tools | GitHub, Notion, VS Code |

## Project Structure
```
CSI403-FullStack-Teaching/
├── 00-course-info/          # Syllabus, calendar, grading
├── 01-starter-code/         # Loan Management System starter
│   ├── loan-management-system/
│   └── weekly-examples/
├── 02-templates/            # Document templates for students
├── 03-sample-data/          # Loan dataset samples
├── 04-lab-exercises/        # Weekly lab exercises
├── 05-quizzes/              # Quiz materials
└── presentations/           # LaTeX Beamer slides
    ├── common/              # Theme and preamble
    ├── lectures/            # Weekly lecture slides
    └── labs/                # Lab session slides
```

## Case Study: Lending Club Loan System
Students will build a complete loan management system featuring:
- User authentication (Admin/Borrower roles)
- Loan application and approval workflow
- Payment tracking and history
- Status management (Current → Paid/Default)
- Dockerized deployment
- CI/CD pipeline with Jenkins

## Weekly Schedule (15 Weeks)
| Week | Dates | Topic | Assessment |
|------|-------|-------|------------|
| 1 | Jan 7-9 | Course Intro, Full Stack Overview | Team Formation |
| 2 | Jan 14-16 | Project Planning, SRS | - |
| 3 | Jan 21-23 | HTML/CSS, Bootstrap | G2 Present (5%) |
| 4 | Jan 28-30 | Jinja2 Templates | - |
| 5 | Feb 4-6 | FastAPI Introduction | Lab1 (5%) |
| 6 | Feb 11-13 | SQLAlchemy, Database | - |
| 7 | Feb 18-20 | Validation, Business Logic | G3 Present (5%) |
| 8 | Feb 25-27 | Authentication | - |
| 9 | Mar 4-6 | Full Stack Integration | P1 (5%), Q1 (5%) |
| 10 | Mar 11-13 | Docker Basics | - |
| 11 | Mar 18-20 | Docker Compose, Jenkins | Q2 (5%) |
| 12 | Mar 25-27 | Testing with pytest | - |
| 13 | Apr 1-3 | Test Documentation | P2 (5%) |
| 14 | Apr 8-10 | Final Presentation #1 | Groups 1-3 |
| - | Apr 13-15 | **Songkran Holiday** | - |
| 15 | Apr 22-24 | Final Presentation #2 | Groups 4-6, Project (40%) |

## Building Presentations
Presentations use LaTeX Beamer with SPU custom theme.

### Requirements
- LaTeX distribution (TeX Live, MiKTeX)
- Required packages: beamer, tikz, tcolorbox, listings, minted

### Compile
```bash
cd presentations/lectures/week01
pdflatex -shell-escape week01-intro.tex
```

## License
Educational use only - Sripatum University Chonburi

## Contact
- Email: methas@spuchonburi.ac.th
- GitHub: github.com/csi403-fullstack
