import os
import pytest
from src.app import add_task, list_tasks, remove_task

FILE = "tasks.json"

def setup_function():
    if os.path.exists(FILE):
        os.remove(FILE)

def test_add_task():
    add_task("Estudar")
    tasks = list_tasks()
    assert "Estudar" in tasks

def test_add_empty_task():
    with pytest.raises(ValueError):
        add_task("")

def test_remove_task():
    add_task("Teste")
    remove_task(0)
    assert list_tasks() == []