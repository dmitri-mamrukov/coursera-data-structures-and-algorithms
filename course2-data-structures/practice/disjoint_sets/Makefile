all: build_and_test

MAIN_TEST = test.py

permission:
	chmod +x $(MAIN_TEST) demo_union_find.py

build_and_test:
	./$(MAIN_TEST)

demo:
	./demo_union_find.py

clean:
	rm -f *~
	rm -rf __pycache__
