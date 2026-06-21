# Private Push Commands

This repo is prepared for account `eeliwuei` as a private repository.

```bash
cd <LOCAL_REPO>
git init -b main
git add .
git commit -m "Prepare private code package v0.1.0-private-freeze"
gh repo create eeliwuei/embedded-nn-contracts --private --source . --remote origin --push
```

If GitHub CLI is not installed, create a private repo in the GitHub web UI
under `eeliwuei/embedded-nn-contracts`, then:

```bash
git remote add origin git@github.com:eeliwuei/embedded-nn-contracts.git
git push -u origin main
```
