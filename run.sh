#!/bin/bash
exec gunicorn live_hackery_site:app -b 0.0.0.0:80
