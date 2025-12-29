# Extended: Git Advanced

## Branching

```bash
git checkout -b feature/new-feature
git push -u origin feature/new-feature
git checkout main
git merge feature/new-feature
git branch -d feature/new-feature
```

## Useful Commands

```bash
git log --oneline --graph
git stash
git stash pop
git reset --soft HEAD~1
git revert HEAD
```

## Conventional Commits

```
feat: add login feature
fix: resolve null pointer bug
docs: update README
refactor: reorganize utils
test: add unit tests
```

## .gitignore

```
# Python
__pycache__/
*.pyc
venv/
.env

# IDE
.vscode/
.idea/
```
