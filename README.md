# React-Talent

**React-Talent** is a job site built using React that connects employers with potential talent. The platform allows users to add, view, edit, and delete job listings.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **View Jobs**: Users can view a list of job openings.
- **Add Jobs**: Employers can add new job listings.
- **Edit Jobs**: Employers can edit existing job listings.
- **Delete Jobs**: Employers can delete job listings.
- **Responsive Design**: The site is mobile-friendly and adjusts to different screen sizes.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/react-talent.git
   cd react-talent
   ```

2. **Install dependencies:**
   - For the frontend (React):
     ```bash
     npm install
     ```
   - For the backend (Django):
     ```bash
     cd server-side
     python -m venv myvenv
     source myvenv/bin/activate  # On Windows use `myvenv\Scripts\activate`
     pip install -r requirements.txt
     ```

3. **Set up environment variables:**
   Create a `.env` file in the root of the backend directory with necessary environment variables (e.g., database configuration).

4. **Run the backend server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Run the frontend server:**
   ```bash
   npm run dev
   ```

## Usage
Once the servers are running:

- Access the frontend at `http://localhost:3000`.
- The backend API will be accessible at `http://localhost:8080/api/`.

### Proxy Setup
The frontend uses a proxy to route API calls to the Django backend. This is configured in the `package.json` file of the React project:

```json
"proxy": "http://localhost:8080"
```

## API Endpoints
The backend provides the following API endpoints:

- **GET /api/jobs/**: Retrieve all job listings.
- **POST /api/jobs/**: Add a new job listing.
- **PUT /api/jobs/:id/**: Update an existing job listing.
- **DELETE /api/jobs/:id/**: Delete a job listing.

## Project Structure

```
react-talent/
│
├── backend/                 # Django project directory
│   ├── jobs/                # Django app for job-related models and views
│   └── jobsite/             # Django project settings and configurations
│
├── src/                     # React source files
│   ├── components/          # Reusable React components
│   ├── layouts/             # Layout components like MainLayout
│   ├── pages/               # React pages (e.g., Homescreen, AddJobPage)
│   └── App.js               # Main app component
│
├── .gitignore               # Files to ignore in Git
├── package.json             # Node.js dependencies and scripts
└── README.md                # Project documentation
```

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

-