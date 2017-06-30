SETTINGS={{ project_name }}.settings
TEST_SETTINGS={{ project_name }}.test_settings

# target: test - calls the "test" django command
test:
	python3 manage.py test 

# target: run - runs local server for django application
run:
	python3 manage.py runserver
