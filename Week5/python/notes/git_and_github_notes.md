# Git & Github

Git is the most widely used version control system, helping developers track changes, collaborate, and manage code effectively. GitHub builds on Git by providing a cloud platform to host, review, and share projects with ease.

- Git enables version tracking, branching, and seamless teamwork.
- GitHub adds cloud hosting, pull requests, issues, and collaboration tools.
- Together, they power open-source development and large-scale project management.

## Version Control System (VCS)
Tool that tracks and manages all changes made to your project. 

As your project grows and new features are added, it stores every version safely. This allows you to access or restore any version without manually creating separate copies.

- Eliminates the need for folders like MyProject, MyProjectWithFeature1, etc.
- Makes rolling back or comparing versions quick, safe, and effortless.

### Rename the local branch:
git branch -m master main

### Push git repo for first time:
```bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/satyam-techabbot/dummyRepo.git
git push -u origin main
```






