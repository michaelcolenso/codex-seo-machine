.PHONY: task tree

task:
	@python scripts/run_task.py $(TASK) $(TOPIC)

tree:
	@find . -maxdepth 3 -type d | sort
