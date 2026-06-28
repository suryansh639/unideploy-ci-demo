# UniDeploy CI Demo

A tiny demo app showing how **UniDeploy** automatically diagnoses a failing CI
pipeline.

- `cart.py` contains a real bug.
- The CI workflow runs the tests and **fails**.
- The UniDeploy workflow reads the code, finds the bug, and reports the exact fix.

See the **Actions** tab to watch it happen.
