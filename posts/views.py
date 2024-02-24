from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['GET', 'POST'])
def get_or_create_post(request):
    """
    View function to handle GET and POST requests for fetching existing posts
    or creating a new post respectively.

    :param request: The HTTP request object.
    :return: Response containing JSON data of posts or newly created post.
    """
    if request.method == 'GET':
        # Send a GET request to fetch existing posts
        response = requests.get('https://dev.codeleap.co.uk/careers/')
        # Extract JSON data from the response
        posts = response.json()
        return Response(posts)
    elif request.method == 'POST':
        # Extract data from the request
        data = request.data
        # Send a POST request to create a new post
        response = requests.post('https://dev.codeleap.co.uk/careers/', json=data)
        # Extract JSON data from the response
        return Response(response.json())

@api_view(['GET', 'PATCH', 'DELETE'])
def get_update_or_delete_post(request, post_id):
    """
    View function to handle GET, PATCH, and DELETE requests for fetching, updating,
    or deleting a specific post respectively.

    :param request: The HTTP request object.
    :param post_id: The ID of the post to be fetched, updated, or deleted.
    :return: Response containing JSON data of the post, updated post, or status code.
    """
    if request.method == 'GET':
        # Send a GET request to fetch a specific post
        response = requests.get(f'https://dev.codeleap.co.uk/careers/{post_id}/')
        # Extract JSON data from the response
        posts = response.json()
        return Response(posts)
    elif request.method == 'PATCH':
        # Extract data from the request
        data = request.data
        # Send a PATCH request to update the specified post
        response = requests.patch(f'https://dev.codeleap.co.uk/careers/{post_id}/', json=data)
        # Extract JSON data from the response
        return Response(response.json())
    elif request.method == 'DELETE':
        # Send a DELETE request to delete the specified post
        response = requests.delete(f'https://dev.codeleap.co.uk/careers/{post_id}/')
        # Return the status code of the response
        return Response(status=response.status_code)
