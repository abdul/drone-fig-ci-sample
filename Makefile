run-tests:
	@nosetests $(TESTS) -s

test-unit:
	@$(MAKE) PYTHONPATH=$(PYTHONPATH) TESTS="./test/*.py" run-tests
