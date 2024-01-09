
from cookies import Cookies


def test_bake_project(cookies: Cookies):
    # Create a new Cookiecutter project instance using the template
    result = cookies.bake(extra_context={'project_slug': 'my_test_project'})
