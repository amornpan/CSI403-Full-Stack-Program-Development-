# Extended: DevOps Best Practices

## CI/CD Pipeline
```
Push → Build → Test → Deploy
```

## Blue-Green Deployment
```
Blue (current) ←── Traffic
Green (new)    ←── Switch when ready
```

## GitFlow
```
main ─────●───────●─────
          │       │
develop ──●───●───●─────
           \   /
feature     ●─●
```

## 12-Factor App
1. Codebase in version control
2. Dependencies declared
3. Config in environment
4. Backing services as resources
5. Strict build/run separation
