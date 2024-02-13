from fabric import task

@task
def test(c):
    """run the tests"""
    cmd = "PYTHONPATH=src pytest ."

    c.run(cmd)
