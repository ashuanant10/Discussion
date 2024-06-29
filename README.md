
# Synape Discussion Project

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

### Low-Level Design (LLD) Flow Diagram

1. **User Interaction Flow:**

   - **Home Page (`home`):** Displays all posts ordered by creation time.
   - **Create User (`create_user`):** Handles user creation based on form input.
   - **Login (`login`):** Authenticates users based on credentials.
   - **Search User (`search_user`):** Allows searching for users by name.
   - **User Home (`user_home/<int:user_id>`):** Shows user-specific details and actions.
   - **Logout (`logout`):** Logs out the current user session.
   - **Update User (`update_user/<int:user_id>`):** Allows updating user profile details.
   - **Delete User (`delete_user/<int:user_id>`):** Allows deleting a user account.
   - **Show User List (`show_user_list`):** Displays a list of all users.
   - **Create Post (`create_post`):** Creates a new post with text, image, and hashtags.
   - **List Posts (`list_post`):** Lists all posts created by the logged-in user.
   - **Update Post (`update_post/<int:post_id>`):** Allows updating an existing post.
   - **Delete Post (`delete_post/<int:post_id>`):** Allows deleting a post.
   - **Like Post (`like_post/<int:post_id>`):** Handles liking/unliking a post.
   - **Comment on Post (`comment_on_post/<int:post_id>`):** Allows commenting on a post.
   - **Like Comment (`like_comment/<int:comment_id>`):** Handles liking/unliking a comment.
   - **Delete Comment (`delete_comment/<int:comment_id>`):** Allows deleting a comment.
   - **Update Comment (`update_comment/<int:comment_id>`):** Allows updating a comment.
   - **List Discussions by Tags (`list_discussions_by_tags`):** Lists posts filtered by tags.
   - **List Discussions by Text (`list_discussions_by_text`):** Lists posts filtered by text query.

2. **Data Flow:**

   - **Models (`User`, `Post`, `HashTag`, `Comment`, `Like`, `Follow`):** Define the structure and relationships of data entities.
   - **Views (`views.py`):** Handle HTTP requests, interact with models, and return responses (HTML templates or JSON).
   - **Templates (`*.html` files):** Render HTML pages with dynamic content from views.

3. **Session Management:**

   - **Session Variables:** Use `request.session` to store and retrieve user session data like `user_id`.
   - **Login/Logout Flow:** Manage user authentication and session handling to control access to protected views.

4. **Error Handling:**

   - **Exception Handling (`try-except`):** Catch and handle exceptions, displaying appropriate error messages to users.
   - **HTTP Method Handling (`HttpResponseNotAllowed`):** Ensure correct HTTP method usage for each view function.

5. **Security Considerations:**

   - **CSRF Protection (`@csrf_exempt`, `csrf_token`):** Protect against Cross-Site Request Forgery (CSRF) attacks.
   - **User Authentication (`custom_login_required`):** Restrict access to authenticated users for specific views.
   - **Password Storage:** Securely store passwords using Django's hashing mechanisms (`password = models.CharField(max_length=255)`).

### Microservices Architecture for Syanape Discussion

1. **User Service**
   - Responsible for user management operations:
     - User creation, update, deletion.
     - Authentication and authorization.
     - Profile management.
   - Technology stack: Django with User model, authentication middleware.

2. **Post Service**
   - Manages all operations related to posts:
     - Create, update, delete posts.
     - Like and comment functionalities.
     - Retrieval of posts by various criteria (e.g., user, hashtags).
   - Technology stack: Django with Post, Comment, Like models.

3. **Search Service**
   - Handles search functionalities across users and posts:
     - User search by name.
     - Post search by text query and hashtags.
   - Technology stack: Django with search APIs or a dedicated search engine integration like Elasticsearch.

4. **Analytics Service**
   - Provides analytical insights into user behavior and post interactions:
     - Post view counts.
     - User activity tracking.
     - Trending posts based on likes and comments.
   - Technology stack: Python/Django with analytics libraries, database for storing aggregated data.

5. **Notification Service**
   - Sends notifications to users for activities like:
     - New followers.
     - Post likes and comments.
     - System updates.
   - Technology stack: Django with message queue integration (e.g., Celery and Redis).

6. **Gateway Service (API Gateway)**
   - Acts as a single entry point for clients to interact with the system.
   - Routes requests to appropriate microservices based on functionality.
   - Implements security, rate limiting, and authentication.
   - Technology stack: Django with Django Rest Framework or a lightweight API gateway like Kong or Ambassador.

### Communication Between Microservices

- **RESTful APIs:** Each microservice exposes REST endpoints for communication.
- **Message Brokers:** Use message brokers like RabbitMQ or Kafka for asynchronous communication, especially useful for notification and analytics services.
- **Shared Database vs. Separate Databases:** Considerations for data consistency and scalability. Each microservice might have its own database or share a database with others, depending on the data access patterns and requirements.

### Deployment and Scalability

- **Containerization:** Dockerize each microservice for consistency and portability.
- **Orchestration:** Deploy using Kubernetes or Docker Swarm for orchestration, ensuring scalability and resilience.
- **Monitoring and Logging:** Implement monitoring solutions like Prometheus and Grafana, and centralized logging with ELK stack or similar.

### Benefits of Microservices

- **Scalability:** Scale each microservice independently based on demand.
- **Flexibility:** Allows teams to work independently on different services.
- **Resilience:** Failure in one service doesn’t affect the entire system.
- **Technology Diversity:** Choose appropriate technology stacks for each microservice based on its requirements.

### Challenges

- **Complexity:** Distributed systems bring added complexity in terms of deployment, communication, and data consistency.
- **Testing:** End-to-end testing becomes challenging due to service dependencies.
- **Operational Overhead:** Requires monitoring, logging, and managing multiple services.

By adopting a microservices architecture, Syanape Discussion can achieve greater flexibility, scalability, and maintainability, aligning with modern software development practices.
