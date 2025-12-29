# Extended: Git Advanced

## Branching
```bash
git checkout -b feature/task-api
git push -u origin feature/task-api
git checkout main
git merge feature/task-api
```

## Useful Commands
```bash
git log --oneline --graph
git stash
git stash pop
git reset --soft HEAD~1
```

## Conventional Commits
```
feat: add task API
fix: resolve login bug
docs: update README
```
