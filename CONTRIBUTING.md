# Contributing to Project-Euler-Library-Code
 - [Pull Request Guidelines](#pull-request-guidelines)
 - [Rebasing / Squashing Commits](#rebasing-squashing-commits)
 - [Commit Message Format](#commit-message-format)
 
## Pull Request Guidelines
Pull requests should be created with a the pull request template.  Pull requests should also include a short description in the title.

The associated branch can have one or more commits until it has at least one thumbs up, until we have more contributors.
```
<Short Description>
<BLANK LINE>
<Insert Pull Request Template>
```

After one or more core team members have given it a **Thumbs Up**:
1. [Rebase](#rebasing-squashing-commits) the branch locally into a single commit following the [commit message format](#commit-message-format).
2. Force Push the local, rebased branch back to Git.
3. If the Merge Request still displays the old commits, then close and re-open the request.
 
## Rebasing / Squashing Commits

### Bash
1. Find out how many new commits there are on the branch
2. Run the command ```git rebase -i HEAD~<Number of new commits on your branch>```
3. Replace pick with squash on the lines until you have between 8 to 10 commits, you can also replace pick with reword to change the commit message
4. Save and close the editor window
5. Change the squashed commits' messages if needed, following the [commit message format](#commit-message-format)

### IntelliJ
1. Fetch the latest changes by going to VCS->Git->Fetch
2. Check out the latest version of master to your local branches.
3. Go to VCS->Git->Rebase.
4. Select the branch you want to rebase in the `Branch:` dropdown.
5. Select Interactive option.
6. Select your local master branch in the `Onto:` dropdown and continue.
7. For the `Action` dropdowns, select `squash` for all commits except the first 8 to 10 and continue.
8. Resolve any merge conflicts that come up by using the `Merge...` button.
9. Follow the [commit message format](#commit-message-format) when prompted for a commit message.
 
## Commit Message Format
Each commit message consists of a **header** and a **body**.  The header has a special
format that includes a **type** and a **subject**:

```
<type>: <subject>
<BLANK LINE>
<body>
```

The **header** is mandatory.

Any line of the commit message cannot be longer 100 characters! This allows the message to be easier
to read on Git as well as in various git tools.

### Type
Must be one of the following:

* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **perf**: A code change that improves performance
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* **test**: Adding missing tests or correcting existing tests

### Subject
The subject contains succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize first letter
* no dot (.) at the end

### Body
Just as in the **subject**, use the imperative, present tense: "change" not "changed" nor "changes".
The body should include the motivation for the change and contrast this with previous behavior.

### Revert
If the commit reverts a previous commit, it should begin with `revert: `, followed by the header of the reverted commit. In the body it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit being reverted.

### Sample Commit
```
fix: syntax error on function 
```