# Publication notes

Project: [zhiland/frontier-skills-lite](https://github.com/zhiland/frontier-skills-lite).
The default branch is `main`. The three initial stages have tags described in [HISTORY.md](HISTORY.md).

The repository includes a README, MIT license and upstream notices, source mapping, an installation helper, validation, and GitHub Actions.
CI checks packaging and installation boundaries. It does not establish model behavior or performance.

## Publish your own copy

Review the license and notices. Authenticate GitHub CLI, then run from a checkout without an existing `origin`:

```sh
gh repo create YOUR-ACCOUNT/YOUR-REPO --public --source=. --remote=origin --push
git push origin --tags
```

Choose the account, name, and visibility deliberately. This creates a new repository rather than updating this project's upstream.
