# Syanape Discussion Project

## Overview

This Django project, Syanape Discussion, facilitates social interactions through posts, comments, and user management features. Users can create accounts, post content, interact with posts via likes and comments, and more.

## Features

- **User Management:**
  - Create, update, delete user accounts.
  - Login and logout functionalities.
  - Profile management (update user details).

- **Post Management:**
  - Create, update, delete posts.
  - View posts sorted by creation time.
  - Filter posts by hashtags.

- **Interactions:**
  - Like posts.
  - Comment on posts.
  - Like comments.

- **Search:**
  - Search users by name.
  - Filter posts by text query.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ashuanant10/Discussion.git
   cd Discussion
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup:**
   - Ensure SQLite is installed.
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the application:**
   Open your web browser and go to `http://localhost:8000` to view the application.

## Usage

- **Creating a User:**
  - Navigate to `/create_user` to create a new user account.

- **Logging In:**
  - Access `/login` to authenticate and log into the application.

- **Posting Content:**
  - Create new posts at `/create_post`.

- **Managing Posts:**
  - Edit or delete posts via `/update_post/<post_id>` and `/delete_post/<post_id>` respectively.

- **Searching Users:**
  - Use `/search_user` to find users by name.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- This project was developed as part of learning Django and web development techniques.
- Thanks to the Django community for their excellent documentation and resources.
