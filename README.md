# CodeLeap Test Project

This project is a solution to the CodeLeap test. It implements a Django backend with Django REST Framework (DRF) to create API endpoints for managing posts.

## Features

- CRUD operations for posts
- Integration with an external API for post management

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/on-ferreira/codeleap_test.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the development server:

    ```bash
    python manage.py runserver
    ```

4. Access the API endpoints in your browser or via API client.

## API Endpoints

- `GET /`: Retrieve a list of posts.
- `POST /`: Create a new post.
- `GET /<post_id>/`: Retrieve a specific post.
- `PATCH /<post_id>/`: Update a specific post.
- `DELETE /<post_id>/`: Delete a specific post.

## External API

The project interacts with an external API hosted at `https://dev.codeleap.co.uk/careers/` for managing posts.

## Deployment

The project is deployed and accessible at [http://my-env.eba-r3pfmfk6.us-west-2.elasticbeanstalk.com/](http://my-env.eba-r3pfmfk6.us-west-2.elasticbeanstalk.com/).

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
