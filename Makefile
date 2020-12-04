generate-proto:
	cd protos && ./gen.sh

mypy:
	cd py && mypy foundation