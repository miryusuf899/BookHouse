EXAM №1 ON DJANGO MVT
Topics:
Django Template
Static
Media
CRUD operations with FBV (Function Based Views)
Create function
View function
Update function
Delete function
Detail View
Redirect
Project Name:

BookHouse — Online Library

Time:

2 hours

Grading:

100 points

TASK DESCRIPTION

You must create a small website using Django MVT architecture called BookHouse.

This website is designed to store and manage information about books.

Requirements:

The project must contain 4 models, and for each model you must implement full CRUD operations:

Create (add new data)
Read/List (view all objects)
Detail (view full information of one object)
Update (edit data)
Delete (remove object)

⚠️ All operations must be implemented only using Function Based Views (FBV).

You must correctly use the following topics:
Templates
Static files
Media files
CRUD with FBV
Detail View
Redirect

❗ Do NOT go beyond these topics.

MODELS
1) Category

Used to classify books.

Fields:

name — category name
description — short description
2) Author

Stores author information.

Fields:

full_name — full name
email — email address
photo — author image
bio — short biography
3) Publisher

Stores publishing company information.

Fields:

name — publisher name
address — address
phone — phone number
logo — logo image
4) Book (Main Model)

Fields:

title — book title
category — category (FK)
author — author (FK)
publisher — publisher (FK)
price — price
pages — number of pages
cover — book image
description — book description
RELATIONSHIPS BETWEEN MODELS

In the Book model:

One book belongs to one category
One book belongs to one author
One book belongs to one publisher

👉 Use proper ForeignKey relationships.

REQUIRED PAGES
Home Page
Main page of the site
Category Pages
Category list
Category detail
Category create
Category update
Category delete
Author Pages
Author list
Author detail
Author create
Author update
Author delete
Publisher Pages
Publisher list
Publisher detail
Publisher create
Publisher update
Publisher delete
Book Pages
Book list
Book detail
Book create
Book update
Book delete
CRUD REQUIREMENTS

For each model, implement:

1. Create

User can add new data

2. List/View

User can see all objects

3. Detail

User can view full information of one object

4. Update

User can edit object data

5. Delete

User can delete an object

⚠️ All must be done using FBV only.

TEMPLATES

You must use template inheritance.

Requirements:
Create base.html
All pages must extend base.html
base.html must include:
Website name
Navigation menu
Main content block
Menu must include links:
Home
Categories
Authors
Publishers
Books
STATIC FILES

You must use static files.

Requirements:
Connect a CSS file
Style the menu
Style buttons
Make list and detail pages visually clean

👉 The site should be clean, readable, and well-structured.

MEDIA FILES

Media must work properly.

Images should be used in:

Author.photo
Publisher.logo
Book.cover
Rules:
Display images on pages
If no image exists → show fallback text
DETAIL VIEW

Create detail pages for all 4 models.

Each detail page must display full information:

Category: name, description
Author: name, email, bio, photo
Publisher: name, address, phone, logo
Book: title, category, author, publisher, price, pages, description, cover
Buttons on detail page:
Update
Delete
Back to list
REDIRECT

Redirect must be used after:

Create
Update
Delete

👉 After an action, the user must be redirected to the appropriate page.

WORKFLOW

You must:

Create a project
Create an app
Create 4 models
Set up relationships correctly
Run migrations
Create templates
Connect static files
Configure media files
Implement CRUD with FBV
Create detail pages
Use redirect correctly
Finish the site cleanly and logically
IMPORTANT REQUIREMENTS
Use only FBV
Full CRUD for all 4 models
Template inheritance is required
Static is required
Media is required
Detail view is required
Redirect is required
The site must work without logical errors
Naming must be clear
Pages must be well-structured