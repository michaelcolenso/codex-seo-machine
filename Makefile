.PHONY: task tree test

task:
	@python scripts/run_task.py $(TASK) $(TOPIC)

tree:
	@find . -maxdepth 3 -type d | sort

test:
	@python -m unittest discover -s tests -p 'test_*.py' -v
