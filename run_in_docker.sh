#!/usr/bin/bash

docker run \
-e BROWSER=headlesschrome \
-e ENV=prod \
ecommerce \
/bin/bash -c pytest