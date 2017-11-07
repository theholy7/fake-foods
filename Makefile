.PHONY: bbc_start_urls requirements

## StartUrl spider for BBC Good Food (This takes a while)
bbc_start_urls:
	scrapy crawl bbc-good-food-starturls

## Create User in Postgres for the project according to connection.py
create_user:
	createuser -e -P -s fake_foodie

## Create database and tables in Postgres for the project according to connection.py and database.py
create_db:
	createdb fake_foods

## Create tables in Postgres for the project according to database.py
create_tables:
	python creator.py

## Use psql to check database
navigate_db:
	psql -U fake_foodie -d fake_foods -h 127.0.0.1

## Install Python Dependencies
requirements:
	pip install -r requirements.txt

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := show-help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
#     * save line in hold space
#     * purge line
#     * Loop:
#         * append newline + line to hold space
#         * go to next line
#         * if line starts with doc comment, strip comment character off and loop
#     * remove target prerequisites
#     * append hold space (+ newline) to line
#     * replace newline plus comments by `---`
#     * print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
		}" ${MAKEFILE_LIST} \
		| LC_ALL='C' sort --ignore-case \
		| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
		'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
		    line_length -= length(words[i]) + 1; \
		    if (line_length <= 0) { \
		        line_length = ncol - indent - length(words[i]) - 1; \
		        printf "\n%*s ", -indent, " "; \
		    } \
		    printf "%s ", words[i]; \
		} \
		printf "\n"; \
		}' \
		| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')