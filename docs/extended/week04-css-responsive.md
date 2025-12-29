# Extended: CSS &amp; Responsive

## Flexbox
```css
.container {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
}
```

## Grid
```css
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}
```

## Responsive
```css
@media (max-width: 768px) {
    .card { width: 100%; }
}
```

## Bootstrap Breakpoints
| Class | Width |
|-------|-------|
| sm | ≥576px |
| md | ≥768px |
| lg | ≥992px |
