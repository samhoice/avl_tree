from fabric import task

@task
def test(c):
    """run the tests"""
    cmd = "pytest ."

    c.run(cmd)
