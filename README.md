# Django To-Do List Application

This is a Django-based To-Do list application that allows users to manage tasks and tags. Users can create, update, delete, and toggle the completion status of tasks, as well as manage tags associated with tasks.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/todo_list.git
    cd todo_list
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Configuration

1. **Create a `.env` file** to configure your environment variables (optional but recommended):

    ```env
    DEBUG=True
    SECRET_KEY=your_secret_key
    ```

2. **Update `settings.py`** to include your environment variables.

## Usage

1. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

2. **Manage tasks and tags:**

    - Navigate to the task list view to see all tasks.
    - Use the provided forms to create, update, and delete tasks and tags.
    - Toggle the completion status of tasks by clicking on them.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.
