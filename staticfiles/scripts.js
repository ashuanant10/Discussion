// document.addEventListener("DOMContentLoaded", () => {
//   // Search Form Validation
//   const searchForm = document.querySelector("nav form");
//   const searchInput = document.querySelector('nav input[type="text"]');

//   searchForm.addEventListener("submit", (e) => {
//     if (searchInput.value.trim() === "") {
//       e.preventDefault();
//       alert("Please enter a search term.");
//     }
//   });

//   // Create User Form Validation
//   const createUserForm = document.getElementById("createUserForm");

//   if (createUserForm) {
//     createUserForm.addEventListener("submit", (e) => {
//       const inputs = createUserForm.querySelectorAll("input");
//       let valid = true;

//       inputs.forEach((input) => {
//         if (input.value.trim() === "") {
//           valid = false;
//           alert(`Please fill in the ${input.name} field.`);
//         }
//       });

//       if (!valid) {
//         e.preventDefault();
//       }
//     });
//   }

//   // Login Form Validation
//   const loginForm = document.getElementById("loginForm");

//   if (loginForm) {
//     loginForm.addEventListener("submit", (e) => {
//       const username = document.getElementById("username").value.trim();
//       const password = document.getElementById("password").value.trim();

//       if (!username || !password) {
//         e.preventDefault();
//         alert("Username and password are required.");
//       }
//     });
//   }

//   // Example of generic JS content
//   console.log("Page loaded");
// });
// document.addEventListener("DOMContentLoaded", () => {
//   const createPostForm = document.getElementById("createPostForm");

//   if (createPostForm) {
//     createPostForm.addEventListener("submit", (e) => {
//       const text = createPostForm
//         .querySelector('textarea[name="text"]')
//         .value.trim();
//       const hashtags = createPostForm
//         .querySelector('input[name="hashtags"]')
//         .value.trim();

//       if (!text) {
//         e.preventDefault();
//         alert("Please enter text for your post.");
//       }

//       if (hashtags && !hashtags.match(/^#[\w]+(, #[\w]+)*$/)) {
//         e.preventDefault();
//         alert(
//           "Please enter hashtags in the correct format (e.g., #tag1, #tag2)."
//         );
//       }
//     });
//   }
// });
// document.addEventListener("DOMContentLoaded", () => {
//   const userListItems = document.querySelectorAll(".user-list li");

//   userListItems.forEach((item) => {
//     item.addEventListener("mouseover", () => {
//       item.style.backgroundColor = "#f5efe6";
//     });

//     item.addEventListener("mouseout", () => {
//       item.style.backgroundColor = "#ffffff";
//     });
//   });
// });
// document.addEventListener("DOMContentLoaded", () => {
//   const searchForm = document.querySelector("form");
//   const searchInput = document.getElementById("text_query");

//   searchForm.addEventListener("submit", (e) => {
//     if (searchInput.value.trim() === "") {
//       e.preventDefault();
//       alert("Please enter a search term.");
//     }
//   });

//   const discussionItems = document.querySelectorAll(".discussion-item");

//   discussionItems.forEach((item) => {
//     item.addEventListener("mouseenter", () => {
//       item.style.backgroundColor = "#f5efe6";
//     });

//     item.addEventListener("mouseleave", () => {
//       item.style.backgroundColor = "#ffffff";
//     });
//   });
// });
// document.addEventListener("DOMContentLoaded", () => {
//   const form = document.querySelector("form");

//   form.addEventListener("submit", (e) => {
//     const name = document.getElementById("name").value.trim();
//     const mobile = document.getElementById("mobile").value.trim();
//     const email = document.getElementById("email").value.trim();

//     if (!name || !mobile || !email) {
//       e.preventDefault();
//       alert("All fields are required.");
//     }
//   });
// });
// document.addEventListener("DOMContentLoaded", () => {
//   console.log("Profile updated page loaded");
//   // Additional interactivity can be added here if needed
// });
// document.addEventListener("DOMContentLoaded", () => {
//   const deleteForm = document.querySelector("form");

//   deleteForm.addEventListener("submit", (e) => {
//     const confirmation = confirm("Are you sure you want to delete this user?");
//     if (!confirmation) {
//       e.preventDefault();
//     }
//   });
// });
// function logout() {
//   fetch("{% url 'logout' %}", {
//     method: "POST",
//     headers: {
//       "X-CSRFToken": "{{ csrf_token }}",
//       "Content-Type": "application/json",
//     },
//   })
//     .then((response) => {
//       if (response.ok) {
//         window.location.href = "/logout_success/";
//       } else {
//         alert("Error: Only POST requests are allowed");
//       }
//     })
//     .catch((error) => console.error("Error:", error));
// }
