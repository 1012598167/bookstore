#!/bin/sh
export PATHONPATH=`pwd`
#coverage run --timid --branch --source fe,be --concurrency=thread -m pytest -v  -k fe/test/test_new_order.py --ignore=fe/data
#coverage run --timid --branch --source fe,be --concurrency=thread -m pytest -v  -k fe/test/test_search.py --ignore=fe/data
coverage run --timid --branch --source fe,be --concurrency=thread -m pytest -v  --ignore=fe/data
#coverage run --timid --branch --source fe,be --concurrency=thread -m pytest -v -k fe/test/test_login.py --ignore=fe/data
#-k fe/test/test_add_book.py 指定跑其中某个test
coverage combine
coverage report
coverage html
