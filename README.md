# docker_mini_project
Project to create a simple webpage to check the timetable using local PostgreSQL and Docker.

## To-Do List

1. **Set Up PostgreSQL Database**:
   - Ensure PostgreSQL is installed and running on your local machine.
   - Create a new database named `timetable_abdulaziz` using pgAdmin or psql.

2. **Create and Populate Database Table**:
   - Create the `timetable` table:
     ```sql
     CREATE TABLE timetable (
         id SERIAL PRIMARY KEY,
         course_name VARCHAR(100),
         level VARCHAR(20),
         day VARCHAR(20),
         time VARCHAR(20)
     );
     ```
   - Insert real course data from Webster University:
     ```sql
     INSERT INTO timetable (course_name, level, day, time)
     VALUES
         ('COSC 1550 - Computer Programming I', 'Undergraduate', 'Monday', '09:00 AM - 10:40 AM'),
         ('COSC 2810 - Systems Analysis and Design', 'Undergraduate', 'Tuesday', '02:00 PM - 03:40 PM'),
         ('COSC 3100 - Data Structures and Algorithms', 'Undergraduate', 'Wednesday', '11:00 AM - 12:40 PM'),
         ('COSC 4110 - Database Management Systems', 'Graduate', 'Thursday', '04:00 PM - 05:40 PM'),
         ('COSC 5150 - Advanced Software Engineering', 'Graduate', 'Friday', '01:00 PM - 02:40 PM'),
         ('COSC 1560 - Computer Programming II', 'Undergraduate', 'Monday', '10:00 AM - 11:40 AM'),
         ('COSC 1570 - Math for Computer Science', 'Undergraduate', 'Tuesday', '01:00 PM - 02:40 PM'),
         ('COSC 2610 - Operating Systems', 'Undergraduate', 'Wednesday', '09:00 AM - 10:40 AM'),
         ('COSC 2670 - Network Principles', 'Undergraduate', 'Thursday', '02:00 PM - 03:40 PM'),
         ('COSC 3410 - Computer and Information Security', 'Graduate', 'Friday', '11:00 AM - 12:40 PM'),
         ('COSC 3510 - Computer Architecture', 'Graduate', 'Monday', '02:00 PM - 03:40 PM'),
         ('COSC 3810 - Principles of Programming Languages', 'Graduate', 'Tuesday', '04:00 PM - 05:40 PM');
     ```

3. **Create Project Directory and Flask Application**:
   - Create the project directory and Python file:
     ```bash
     mkdir my_project
     cd my_project
     touch app.py
     ```
   - Edit `app.py` and implement the Flask application with PostgreSQL connection.

4. **Create `index.html` and `timetable.html` Templates**:
   - Create and populate `index.html` to display the form for selecting the level.
   - Create and populate `timetable.html` to display the timetable.

5. **Create `requirements.txt` File**:
   - Create a `requirements.txt` file with the following content:
     ```txt
     Flask==2.2.2
     Werkzeug==2.2.2
     Jinja2==3.1.2
     pg8000
     ```

6. **Create Dockerfile**:
   - Create a `Dockerfile` with the following content:
     ```Dockerfile
     # Use the official Python image from the Docker Hub
     FROM python:3.8-slim

     # Set the working directory in the container
     WORKDIR /app

     # Copy the requirements file into the container
     COPY requirements.txt requirements.txt

     # Install the dependencies
     RUN pip install --no-cache-dir -r requirements.txt

     # Copy the rest of the application code into the container
     COPY . .

     # Expose the port the app runs on
     EXPOSE 8000

     # Define the command to run the application
     CMD ["python", "app.py"]
     ```

7. **Create `docker-compose.yml` File**:
   - Create a `docker-compose.yml` file with the following content:
     ```yaml
     version: '3.8'

     services:
       web:
         build: .
         ports:
           - "8000:8000"
         environment:
           FLASK_ENV: development
           POSTGRES_USER: postgres
           POSTGRES_PASSWORD: 2134
           POSTGRES_DB: timetable_abdulaziz
           POSTGRES_HOST: host.docker.internal
           POSTGRES_PORT: 5432
     ```

8. **Build and Run Docker Containers**:
   - Run the following commands to build and start the Docker containers:
     ```bash
     docker-compose build
     docker-compose up
     ```

9. **Access the Application**:
   - Open the browser and access the web application at `http://localhost:8000`.

This sequence now includes the steps to set up a local PostgreSQL database with pgAdmin, create and populate the `timetable` table with real courses from Webster University, and dockerize the Flask application. 