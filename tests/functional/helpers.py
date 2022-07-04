import logging
import time

import pytest

import gitlab.base

SLEEP_INTERVAL = 0.5
TIMEOUT = 60  # seconds before timeout will occur


def delete_object(
    *, object: gitlab.base.RESTObject, index: int, hard_delete: bool = False
):
    if index:
        logging.info(f"Attempt {index+1} to delete {object!r}.")
    try:
        if hard_delete:
            object.delete(hard_delete=True)
        else:
            object.delete()
    except gitlab.exceptions.GitlabDeleteError:
        logging.info(f"{object!r} already deleted.")
        pass


def safe_delete(
    *,
    manager: gitlab.base.RESTManager,
    object_id: int,
    description: str,
    hard_delete: bool = False,
) -> None:
    """Ensure the object specified can not be retrieved. If object still exists after
    timeout period, fail the test"""
    max_iterations = int(TIMEOUT / SLEEP_INTERVAL)
    for index in range(max_iterations):
        try:
            object = manager.get(object_id)
        except gitlab.exceptions.GitlabGetError:
            return
        delete_object(object=object, index=index, hard_delete=hard_delete)
        time.sleep(SLEEP_INTERVAL)
    pytest.fail(f"{description} {object!r} was not deleted")
