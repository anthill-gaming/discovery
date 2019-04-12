#!/usr/bin/env bash

# Setup postgres database
createuser -d anthill_discovery -U postgres
createdb -U anthill_discovery anthill_discovery