ifeq ($(firstword $(MAKECMDGOALS)),test)
  FILENAME := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(FILENAME):;@:)
endif

test: $(FILENAME)
	@py test/$(FILENAME).py
