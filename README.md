Jozi
====

Adrian's gig guide.

Workflow
--------

Until you are used to using git, follow this workflow:

- `cd python/django/jozi`
- 'source bin/activate'
- 'git fetch'.  It will ask for your userid and password
- 'git pull'. userid and password again.
- Before you change anything, `git checkout -b <some-name>`
- Change, delete, add files to your heart's content.
- Whenever you feel that the current set of changes are OK:

  + `git commit -a`
  + Check all the files that are changed are there.
  + Type a *meaningful* message.  You can go several lines, as long as there is a blank line between header and the rest of the text.
  + Carry on editing
  
- To release the code:

  + `git checkout master'
  + `git merge <some-name>` as above
  + 'git branch -d <some-name>
  
- If you would rather thraw-away your changes because they turned out to be a disaster:

  + 'git checkout master'
  + 'git branch -D <some-name>`
