# GitHub Activity CLI

A simple **Command Line Interface (CLI)** application to fetch and display a user's recent GitHub activity. This project leverages the **GitHub API** to retrieve user events and displays them directly in the terminal.

## Features
- Fetch recent activity of any GitHub user.
- Display event details, including:
  - Event type (e.g., PushEvent, IssueEvent).
  - Repository name and URL.
  - Commit message (if applicable).
  - Event visibility (public/private).
  - Event creation timestamp.
- Error handling for invalid usernames or API failures.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/EMMD474/github-user-activity.git
   ```
2. Navigate to the project directory:
   ```bash
   cd github-user-activity
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```
4. Install dependencies:
   ```bash
   pip install requests
   ```

## Usage
Run the application and provide a GitHub username:
```bash
python main.py
```
When prompted, enter a command:
```plaintext
github-activity <username>
```
**Example:**
```plaintext
github-activity EMMD474
```

### Sample Output
```
Actor: EMMD474
Type of Event: PushEvent
Repository: EMMD474/project-repo
Repository URL: https://github.com/EMMD474/project-repo
Commit message: Initial commit
Public: True
Created At: 2024-08-01T12:00:00Z
.................................
```

## Error Handling
- Invalid username: Displays an appropriate error message.
- Network/API failure: Handles connection errors gracefully.
- Empty event history: Informs the user when no events are found.

## API Reference
- [GitHub Events API Documentation](https://docs.github.com/en/rest/activity/events)

## Contribution
Feel free to contribute to the project. Open an issue or submit a pull request.

## License
This project is licensed under the **MIT License**.

---
**Project Challenge Link:** [Roadmap.sh GitHub User Activity](https://roadmap.sh/projects/github-user-activity)

