# Using this plugin:
# https://github.com/hackebrot/pytest-cookies


def test_bake_project_default(cookies):
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.project_path.is_dir()
    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "typer-cli-template"
    assert result.project_path.is_dir()


def test_bake_project(cookies):
    result = cookies.bake(extra_context={"project_name": "helloworld"})
    assert result.exit_code == 0
    assert result.project_path.is_dir()
    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "helloworld"
    assert result.project_path.is_dir()
