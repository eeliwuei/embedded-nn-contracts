# Private GitHub Setup

Create the repository under account `eeliwuei` as private first.

```bash
cd <LOCAL_REPO>
git init -b main
git add .
git commit -m "Prepare private code package v0.1.0-private-freeze"
gh repo create eeliwuei/embedded-nn-contracts --private --source . --remote origin --push
```

If `gh` is unavailable, create a private repository in the GitHub web UI, then add the remote and push.
