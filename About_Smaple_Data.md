**Sample Data**
The project includes the following sample data to demonstrate and test the functionality of the search application effectively. 
These data entries represent various courses, each with a unique name and detailed description, providing a realistic dataset for testing search and filtering features.

1. **name** : Python Programming

**Description**: A comprehensive course designed to teach the basics of Python programming. This entry helps test queries related to general programming topics.

2. **name** : Django Web Development

**Description**: A detailed course on building web applications using the Django framework. Useful for testing searches related to web development.

3. **name** : Frontend Development
   
**Description**: An introductory course covering HTML, CSS, and JavaScript, focused on creating visually appealing and responsive websites. This entry is ideal for testing searches involving UI/UX and frontend-related keywords.

4. **name** : Data Science with Python

**Description**: A beginner's guide to data science, featuring Python libraries like Pandas and NumPy for data manipulation and analysis. Helps in testing searches related to data analysis and science.

5. **name** : Machine Learning Basics

**Description**: A fundamental course on machine learning, covering core algorithms and their applications. This entry ensures the search functionality works for AI and ML-related queries.

**Purpose of Sample Data**
**Demonstrates Functionality**: Provides a realistic dataset to validate the search and filtering features.
**Testing Versatility**: Covers a range of topics to test partial and full-text search capabilities.
**Error Handling**: Allows for robust testing of the application's behavior when no results are found.


**Steps to Add Sample Data Through Django Admin Panel**

**Step 1 : Ensure the Item Model is Migrated**
Before adding data, ensure the database reflects your model structure. Run the following commands:

      **python manage.py makemigrations**
      
      **python manage.py migrate**
This creates and applies the necessary database migrations for the Item model.

**Step 2 : Start the Django Development Server**

Run the following command in your project directory:

    **python manage.py runserver**
    
Open your web browser and navigate to the admin panel at http://127.0.0.1:8000/admin/.

**Step 3 : Log in to the Admin Panel**

Use the admin username and password you created during the superuser setup.

**Step 4 : Access the Item Model in Admin**

Locate your app section (e.g., Search App) in the admin panel.
Click on the Item model to manage the entries.

**Step 5 : Add a New Item**

Click the Add Item button.
Fill out the fields for Name and Description using the sample data provided.

**Example Entry:**

Name: Python Programming

Description: A comprehensive course designed to teach the basics of Python programming.

Click Save to add the item.

**Step 6 : Repeat for All Sample Data Entries**

**Step 7 : Verify the Data**

Once all entries are added, visit the application's search page. Test the search functionality to ensure the data displays and filters correctly.
