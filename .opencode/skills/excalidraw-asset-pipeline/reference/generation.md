# Generation

Use the shared kit in `generators/common/`.

```python
from ekit import *
new()
title("Course Title", 60, 40)
box(60, 140, 220, 90, "Concept")
arrow(280, 185, 360, 185)
save("001 Scene Name")
```

Use brand tokens from `generators/common/tokens.py`. Do not hardcode colors or raw Excalidraw JSON unless necessary.
