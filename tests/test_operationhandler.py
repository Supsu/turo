import time
import pytest

from ..fuzzer.operationhandler import OperationHandler

@pytest.fixture
def handler():
    """This function is a pytest fixture,
    that initializes an usable operationhandler object.

    For traditional unit testing, fixtures compare to the test setup&teardown"""
    yield OperationHandler(None, None)

    #Possible teardown code here

def test_operationhandler_start(handler):
    """The start function should spawn the thread and return immediately."""
    start_time = time.time()
    handler.start()
    end_time = time.time()

    assert end_time-start_time < 0.01
