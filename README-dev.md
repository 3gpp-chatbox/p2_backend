# Folder Structure

## 📂 **Project Directory Overview**

This section explains the folder structure of the project to ensure consistency and maintainability.

### 📁 `data/`

- Contains any data used in the application.
- Example: 3GPP documents, dataset files, or external resources.

### 📁 `docs/`

- Stores documentation, notes, and findings related to the project.
- Useful for implementation details and research materials.

### 📁 `src/`

- Houses all source code for the project.
- Can be broken down into multiple subfolders as needed:
  - `utils/` - Utility functions and helpers.
  - `lib/` - External libraries or wrappers.
  - `helpers/` - Common helper functions.
  - `models/` - Database models or machine learning models.
- Example structure:
  ```
  src/
  ├── utils/
  ├── lib/
  ├── helpers/
  ├── models/
  └── main.py
  ```

### 📁 `tests/`

- Contains unit and integration tests.
- Keeps the test code separate from production code for better maintainability.
- Example structure:
  ```
  tests/
  ├── test_utils.py
  ├── test_models.py
  └── test_main.py
  ```

### 📁 `logs/`

- Stores application logs and debugging information.

# Contributing to the Project

Please follow the workflow below to ensure smooth progress and consistency across the project.

## Contribution Workflow

### 1. Pick a Task

- Browse the task board and select a task to work on.
- Assign the task to yourself to prevent duplication of efforts.
- Ensure that all dependent tasks are completed before starting.

### 2. Start Working on the Task

Once you are ready to work on the task:

1. Move the task to the **"In Progress"** column.
2. Create a new branch from the main branch. Use the task name(OR a shortened version) as the branch name, following the format:
   ```
   git checkout main
   git pull origin main  # Make sure you have the latest main branch
   git checkout -b task-name  # Create and switch to a new feature branch
   ```
3. Work on the task and commit your changes regularly.
4. Once the task is completed:

   - Pull the latest changes from the main branch into your working branch to avoid conflicts.

   ```
   git pull origin main --rebase
   ```

   - Resolve any merge conflicts if they occur:
   - Git will pause the rebase and highlight conflicting files with markers like <<<<<<<, =======, and >>>>>>>.
   - Open the affected files, edit them to resolve conflicts (keeping your changes, theirs, or a mix), and save.
   - Mark the resolved files:
     ```
     git add <file-name>
     ```
   - Continue the rebase process:
     ```
     git rebase --continue
     ```
   - Repeat until all conflicts are resolved. If stuck, you can abort the rebase with git rebase --abort and seek help in the discussion channels.

5. Push your completed work to the remote repository:
   ```
   git push origin task-name
   ```
6. Create a Pull Request (PR) to merge your branch into the main branch.
   - Link your PR to the related issue.
   - Move the issue to **"Review"** on the Kanban board.
7. A team member will review your code:
   - If changes are requested, address them and update your PR accordingly.
   - Once approved, the PR will be merged, and the issue will be closed.
8. After merging, delete your branch to keep the repository clean:
   ```
   git branch -d task-name
   git push origin --delete task-name
   ```

## Additional Notes

- Follow coding guidelines and best practices.
- Document your code with docstrings.
- Keep commit messages clear and descriptive.
- If you encounter any problems hindering the task completion, ask for help in the discussion channels.

Happy coding! 🚀
