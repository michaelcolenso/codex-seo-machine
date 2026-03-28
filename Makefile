.PHONY: task tree test check full-run

task:
	@python scripts/run_task.py $(TASK) $(TOPIC)

tree:
	@find . -maxdepth 3 -type d | sort

test:
	@python -m unittest discover -s tests -p 'test_*.py' -v

full-run:
	@python scripts/full_run.py

check: test full-run
	@python scripts/validate_article.py workspace/drafts/seo-workflow-implementation-for-small-teams.md
