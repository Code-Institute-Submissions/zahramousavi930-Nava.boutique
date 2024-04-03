
# Welcome to Nava Boutique Online Shop

Discover the world of fashion at Nava Boutique, where style meets convenience. Our user-friendly platform offers a seamless and enjoyable shopping experience for clothing and accessories enthusiasts. Whether you're planning a wardrobe refresh or looking for the perfect accessory, Nava Boutique has you covered.

We value your feedback and strive to enhance your shopping experience. If you have any questions or suggestions, feel free to reach out to our customer support team.

Happy shopping at Nava Boutique Online Shop!
![Am I Responsive Image](img/1.png)

## Visit the Live Site

Experience the Nava Boutique magic by visiting our live site deployed on Heroku. Click [here](https://nova-shop-ea4ad33fa8c5.herokuapp.com/) to explore the latest trends and shop with ease.

## Features

- **Responsive Design**: Our website is fully responsive, ensuring a smooth and enjoyable shopping experience across various devices, from desktops to smartphones.

- **Built with Django**: Nava Boutique is powered by the Django framework in Python, providing a robust and secure foundation for our platform.

## Table of Contents

- [Live Site](https://nova-shop-ea4ad33fa8c5.herokuapp.com/)
- [Overview](#overview)
- [Key Features](#key-features)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
- [Features](#features)
- [Product Catalog](#product-catalog)
- [Design](#design)
- [About Us](#about-us)
- [Forms](#forms)
- [Custom 404 Error](#custom-404-error)
- [Custom Models](#custom-models)
- [Other Features](#other-features)
- [Deployment](#deployment)
- [Testing](#testing)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Overview

Nava Boutique Online Shop is a fashion-forward platform built on the Django framework using Python. With a robust and secure foundation, our site offers a user-friendly interface, making online shopping a delightful experience.

## Key Features

- **Product Catalog**: Explore our extensive product catalog featuring the latest fashion trends, from clothing to accessories.
- **Secure Online Shopping**: Enjoy secure online shopping with user-friendly features for account management, order placement, and tracking.
- **Responsive Design**: Access the site seamlessly on desktops, tablets, and mobile devices.
- **User-Friendly Interface**: Navigate through our platform effortlessly, ensuring a hassle-free shopping process.

## User Experience (UX)

### User Stories

- #### Navigation

  - As a user, I want to navigate around the site easily to locate the products I want.
  - As a user, I want to view a list of all available products.
  - As a user, I want to be able to view more details on a product, such as price, ingredients, and reviews.
  - As a user, I want to be able to refine my search with categories.
  - As a user, I want to be able to sort products by price, review, or name.
  - As a user, I want to be able to easily contact the site owner if needed.
  - As a user, I want to be able to see all ingredients contained within the product, including any allergens.

- #### Accounts

  - As a user, I want the option to register for an account, allowing me to save my details and see previous orders.
  - As a user, I want to receive confirmation emails to confirm my registration.
  - As a user, I want the ability to be able to log in and out and be able to easily work out my current login status.
  - As a user, I want to be able to recover my account information in the event that I forget it.


- #### Admin

  - As an admin, I want to be able to add products easily in a format consistent with the rest of the site.
  - As an admin, I want to be able to edit products easily to ensure the customer is being shown the most up-to-date information
  - As an admin, I want to be able to delete discontinued products or mark seasonal products out of stock when not available.
  - As an admin, I want to be able to easily manage the images in the gallery, and update the site policies.
  - As an admin, I want to be able to add and update the ingredients for products and mark any allergens appropriately.

- #### Purchasing

  - As a user, I want to be able to add items to my cart, allowing me to store things until I'm ready to complete my purchase.
  - As a user, I want to be able to view my cart so I can see the current running total of my potential purchases.
  - As a user, I want the ability to update the quantity of the items in my cart easily.
  - As a user, I want an easily viewable total to allow me to monitor my overall spending.
  - As a user, I want to be able to complete the purchasing journey, without the need to register if I do not wish to.
  - As a user, I want to receive confirmation of my order so I know my order was placed successfully.
  - As a user, I want to be able to view my order history so I can review past purchases.

- #### Interaction

  - As a user, I want to be able to leave a review of products to share my experience with other customers
  - As a user, I want to be able to easily connect to the business's social media pages to keep up to date.
  - As a user, I want to be able to easily contact the site owner if needed.

#
## Design

- ### Colours

  The decision was made to keep the colors as simple as possible for the website, with the main content being either black text on a white background, or vice versa.

  This is due to cakes and confectionary being inherently colorful. Reducing the color palette to the most basic possible helps draw attention to the products displayed, and the colors within.

  ![Colours Image](img/colours.png)

- ### Fonts

  The [Verdana](https://www.cufonfonts.com/font/verdana) font from Google Fonts is used throughout the site on all content.

  This font was chosen due to its readability, popularity, and familiarity, with it being the chosen font for some products produced by Google.


- ### Wireframes

- ### Database Schema

  The database schema for the project was:

  ![Database Schema](img/schema.png)

  The full image can be viewed [here](img/schema.png)

#
## Features

### User Authentication and Account Management

- Registration, login, and password reset functionalities.
- User-friendly forms for signup, login, password reset, and order placement.

### Shopping Cart

- Add products to the shopping cart.
- Manage the shopping cart by updating quantities and removing items.
- Checkout and place orders with order history tracking for users.

### Admin Dashboard

- Admin dashboard for managing products, orders, and users.
- Admin approval required for new product listings before they appear on the main page.

### User Comments

- Users can leave comments on products.
- Admin can review and approve comments before displaying them on the main page.

### Custom Models

- Users can create and manage their orders, adding, removing, or editing their selections.
- Users can leave comments and like products in the catalog.
- Users can track the status of their orders.

### Product Catalog

- A curated product catalog showcasing the latest fashion trends.
- Each product includes detailed descriptions, size options, and high-quality images.
- Dynamic filtering options to help users easily find desired products.

### Design

The Nava Boutique Online Shop follows a clean and intuitive design:

- **Color Scheme**: Utilizes a modern and inviting color palette to enhance the visual appeal.
- **Typography**: Employs easy-to-read fonts for a comfortable browsing experience.
- **Responsive Layout**: Adapts seamlessly to different screen sizes, ensuring accessibility across devices.
- **Intuitive Navigation**: Provides clear and logical navigation paths for a user-friendly experience.

### About Us

At Nava Boutique Online Shop, we are passionate about delivering a delightful shopping experience. Our team is dedicated to providing you with a seamless and user-friendly platform to make your online shopping hassle-free. We believe in the joy of discovering new fashion trends and creating your unique style. Thank you for choosing us for your fashion needs.

### Forms

Users can leave comments, sign up, log in, reset passwords, and make orders with forms. They can also access their order information in the shopping cart or user panel.

### Custom 404 Error

A custom 404 error page is implemented to provide a user-friendly experience when a page is not found.

### Custom Models

1. Users can create and manage their orders, adding, removing, or editing their selections.
2. Users can leave comments and like products in the catalog.
3. Users can track the status of their orders.

### Other Features

- Social media marketing through platforms like Facebook and Instagram to reach and engage with the target audience.
- Influencer collaborations and partnerships to increase brand visibility and generate sales.
- The HTML templates include descriptive meta tags that enhance search engine visibility and provide meaningful information about the website's pages.
- Search engine optimization (SEO) techniques to improve organic visibility and attract potential customers.

### Deployment

I deployed this website using GitPod, Heroku, and following the below steps:

1. Log in to GitHub.
2. Log in to Heroku.
3. Use GitPod to deploy and commit changes to GitHub.
4. Add Procfile and Gunicorn for running code on Heroku.

### Testing

- Comprehensive testing using the Django test framework.
- Users must log in first to access all features of the site.

## Screenshots

### 1. Add Products
![Add Products](img/products.png)
**Description:** This screenshot showcases the "Add Products" interface, where administrators can add new food items to the menu.

### 2. Comments Section
![Comments Section](img/comment.png)
**Description:** Users can leave comments on food items, fostering user interaction. Admins have the ability to review and approve comments before they appear on the main page, ensuring content quality.

### 3. Header Section
![Header Section](img/header.png)
**Description:** The header is a crucial component of the website, offering clear and intuitive navigation. It typically includes the restaurant's logo, navigation links, and may feature a search bar or other relevant elements.

### 4. Login Page
![Login Page](img/login.png)
**Description:** Users access their accounts securely through the login page. This is essential for user authentication, enabling registered users to manage reservations, orders, and preferences.

### 5. Teller
![Teller](img/tailr.png)
**Description:** The Teller section allows users to subscribe to email notifications for new arrivals. Users can enter their email address to receive updates about the latest additions to the menu.

### 6. Admin Section - Add Products
![Admin Section - Add Products](img/add%20products.png)
**Description:** Admins have the ability to add new products to the menu through a dedicated interface, ensuring seamless management of the restaurant's offerings.

### 7. Admin Section - Change Password
![Admin Section - Change Password](img/change%20pasword.png)
**Description:** Admins can change their password securely through a designated page, enhancing account security and access control.

### 8. Admin Section - Accept Comments and Edit Users
![Admin Section - Accept Comments and Edit Users](img/admin.png)
**Description:** Admins can review and accept comments from users, ensuring content quality. Additionally, they have the capability to edit user profiles, providing comprehensive control over user management.

### 9. Checkout Section
![Checkout Section](img/checktout.png)
**Description:** The Checkout section allows users to review their selected items, enter shipping information, and proceed to payment. This step-by-step process ensures a smooth and secure completion of the order.

### 10. Order Details and Receipt
![Order Details and Receipt](img/order%20detils.png)
**Description:** After completing the checkout process, users receive a detailed order summary and a receipt. This includes information about the items purchased, total cost, and any relevant order details. Enhances user experience by providing a clear record of their transaction.

## Databases (PostgreSQL)

### Database Structure
* The project uses PostgreSQL as the relational database management system.
* Schemas and tables are organized to store information about products, users, comments, and orders.

### Database Connection
* The application connects to the PostgreSQL database to retrieve and store data.
* Database connection details such as host, port, username, and password are configured in the application's settings.

### Database Interaction
* CRUD operations are implemented to interact with the database.
* SQL queries are used to insert, retrieve, update, and delete data based on user actions and system requirements.

### Data Security
* The application ensures data security by using parameterized queries and prepared statements to prevent SQL injection attacks.
* Passwords are securely hashed before storing them in the database to enhance user authentication security.

## Testing

All parts of views and forms were tested using the inner framework of Django test. Users must log in first to use all features of the site.

### HTML

- HTML validation was carried out using the [Nu HTML Checker tool](https://validator.w3.org/) by W3C.
- Links are provided where the page could be tested using the URL.

#

- #### Home Page Validation

  - [Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnova-shop-ea4ad33fa8c5.herokuapp.com)

  ![Home Page Validation Image](img/html%20test.png)

...

### Lighthouse

- Lighthouse, using Chrome Dev Tools, was used to ensure best practices were followed on the site.

  ![Lighthouse Test Image](img/seo.png)


## Contributing

We welcome contributions from the community! If you find ways to improve the website or have suggestions for enhancements, please feel free to open an issue or create a pull request. Your input is valuable to the continued development and improvement of the Restaurant Booking System.

## License

This project is licensed under the [MIT License](LICENSE).

Thank you for choosing the Restaurant Booking System! We hope you enjoy your dining experience with us.
