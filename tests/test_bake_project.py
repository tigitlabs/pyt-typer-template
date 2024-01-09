
def test_bake_project(cookies):
    result = cookies.bake(extra_context={"repo_name": "helloworld"})
    assert result.exit_code == 0
    # Replace result.project with result.project_path
    assert result.project_path.is_dir()
