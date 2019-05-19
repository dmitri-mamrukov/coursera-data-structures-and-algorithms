INPUT_FILES := $(shell find . \
	-maxdepth 1 -mindepth 1	-type f -name 'input*.txt' | sort)

all: build_and_test

MAIN1 = connecting_points_kruskal.py
MAIN2 = connecting_points_prim.py
MAIN_TEST = test.py

permission:
	chmod +x $(MAIN_TEST) $(MAIN1) $(MAIN2)

build_and_test:
	./$(MAIN_TEST)

demo:
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN1) < $$file; \
	done
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN2) < $$file; \
	done

clean:
	rm -f *~
	rm -rf __pycache__
