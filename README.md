# Office_Management

<h2><b>REPORT</b></h2> <br>
<h3><b>OBJECTIVE</b> </h3>
To develop an office management system using Django and PostgreSQL, providing CRUD functionality for employee records with secure, role-based access control. <br>
<h4><b>Tools and Libraries Used</h4></b>
•	Django: A high-level Python web framework used for building the web application. It provides an organized structure for managing the project, handling HTTP requests, and interacting with the database. <br>
•	PostgreSQL: An open-source relational database management system used to store and manage the data in the project. PostgreSQL is known for its robustness and scalability. <br>
•	psycopg2: A PostgreSQL adapter for Python, used to connect the Django application to the PostgreSQL database. <br>
•	Django's Built-in Authentication System: Utilized for managing user authentication, including role-based access control. <br>
<h4><b>Methodology</h4></b>
<b>1.	Set Up the Django Project:</b> <br>
o	The project began by installing Django and the necessary dependencies for PostgreSQL integration. A new Django project was created, serving as the main structure for the office management system. Within this project, an application specifically for handling employee-related data was set up. This modular approach allows for better organization and management of the project components. <br> <br>
<b>2.	Configure PostgreSQL:</b> <br>
o	The next step involved configuring the Django project to use PostgreSQL as its database backend. The database connection details, such as the database name, user credentials, and host information, were added to the project settings. Following the configuration, database migrations were run to set up the initial schema, preparing the database for data storage and retrieval. <br> <br>
<b>3.	Define Models:</b> <br>
o	In this phase, the data model for the Employee entity was defined. This model included fields for storing employee details such as first name, last name, designation, and role. The Employee model was also linked to Django’s built-in user authentication system, enabling each employee to have a corresponding user account. After defining the model, it was included in the project’s settings, and migrations were created and applied to update the database schema. <br> <br>
<b>4. Set Up Role-Based Authentication:</b> <br>
o	Role-based authentication was implemented to ensure that only authorized users could perform specific actions within the system. User roles such as Admin and Manager were created using Django’s built-in Group model. These roles were then assigned permissions that determined their level of access to the CRUD operations. The views in the application were updated to enforce these role checks, ensuring that only users with the appropriate permissions could access or modify employee data. <br> <br>
<b>5. Set Up URLs and Templates:</b> <br>
<h2><b>URLs (Uniform Resource Locators) </h2></b>
In Django, the urls.py files play a crucial role in mapping incoming HTTP requests to the appropriate views, which handle the logic and return the corresponding responses. There are typically two urls.py files involved in a Django project: <br>
<b>1. Project-level urls.py:</b> <br>
   - This file is located in the main project directory (e.g., office_management/urls.py). It serves as the entry point for all incoming requests to the Django project. <br>
   - The project-level urls.py includes global URL patterns and usually directs requests to the urls.py files of individual apps (e.g., the employees app). <br>
   - For example, a URL pattern might route all requests starting with /employees/ to the employees app’s urls.py file, where more specific routes are defined. <br> <br>
<b>2. App-level urls.py:</b>  <br>
   - This file resides within each app (e.g., employees/urls.py) and defines the URL patterns specific to that app. <br>
   - Each URL pattern is linked to a view that handles the request. For instance, the URL pattern /employees/create/ might link to a view that handles creating a new employee. <br>
   - Typical URL patterns include paths for listing all employees, creating a new employee, updating an existing employee, and deleting an employee. These patterns make it easy for users to navigate through the web application and perform CRUD operations. <br> <br>
<h4><b>VIEWS</b></h4>
Views in Django are Python functions or classes that handle requests and return responses. They are the core of the business logic in a Django application. Views interact with the data models to retrieve, process, and present data to the user via templates. Here’s how views work in the context of this project: <br> 
<b>1. List View (Read Operation):</b> <br>
   - The list view is responsible for displaying all employee records stored in the database. When a user navigates to the URL associated with the list view, the view queries the database for all employee entries and passes this data to the corresponding template (e.g., employee_list.html). <br> 
   - The template then renders the data in a structured format, typically a table, allowing users to see all employees at a glance. <br> <br>
<b>2. Create View (Create Operation):</b> <br>
   - The create view handles the addition of new employees to the system. When a user accesses the create URL, the view presents a form for inputting employee details. <br>
   - Upon submission, the view validates the input data, saves the new employee record to the database, and redirects the user to another page (often the employee list) to confirm that the new entry has been added. <br> <br>
<b>3. Update View (Update Operation):</b> <br>
   - The update view allows users to modify the details of an existing employee. When the corresponding URL is accessed, the view retrieves the specific employee’s data and pre-populates a form with it. <br>
   - After the user submits the changes, the view validates and updates the record in the database. The user is then redirected to a confirmation page or back to the list of employees. <br> <br>
<b>4. Delete View (Delete Operation):</b> <br>
   - The delete view manages the removal of employee records. When the user navigates to the delete URL, the view presents a confirmation page to ensure the user wants to proceed with the deletion. <br>
   - Upon confirmation, the view deletes the employee record from the database and redirects the user to the employee list or a confirmation page indicating the record has been successfully removed. <br> <br>
<h4><b>How URLs and Views Work Together</b></h4>
- URL Routing: When a user visits a URL, Django uses the patterns defined in urls.py to determine which view should handle the request. The URL pattern acts as a bridge between the user’s request and the view that processes it. <br>
- View Execution: Once the appropriate view is identified, it executes the necessary logic, which may involve querying the database, processing data, or rendering a template. <br>
- Response Generation: The view then generates an HTTP response, which could be an HTML page, JSON data, or a redirection to another URL, depending on the logic implemented in the view. <br> <br>

<h4><b>TEMPLATES</b></h4>
Templates are used by views to render the data and create the HTML pages that users interact with. Each view passes data to a corresponding template, which then formats and displays it. The relationship between URLs, views, and templates forms the backbone of Django’s Model-View-Template (MVT) architecture, ensuring a clean separation between data management, business logic, and presentation layers. <br> <br>
<b>6.	Create Superuser and Assign Permissions:</b> <br>
o	A superuser was created to manage the application through Django’s admin panel. This user had full access to the system and could create and manage other user roles and permissions. Using the admin interface, the necessary roles were created, and specific permissions were assigned to ensure that the application’s access control was in place. <br>

<h4><b>CONCLUSION</b></h4>
The project successfully created a secure office management system with role-based authentication, enabling efficient management of employee records through a scalable and adaptable web application.
