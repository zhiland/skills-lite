# Publication notes

Project: [zhiland/skills-lite](https://github.com/zhiland/skills-lite).
The default branch is `main`. Versions v0.1 through v0.5 are described in [HISTORY.md](HISTORY.md).

The repository includes six Matt Pocock skill packages, a README, MIT notices, source mapping, and revision history.
Install by copying selected skill directories. No installer, Python dependency, or CI workflow is required.

## Publish your own copy

Review the license and notices. Authenticate GitHub CLI, then run from a checkout without an existing `origin`:

```sh
gh repo create YOUR-ACCOUNT/YOUR-REPO --public --source=. --remote=origin --push
git push origin --tags
```

Choose the account, name, and visibility deliberately. This creates a new repository rather than updating this project's upstream.
