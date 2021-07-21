#!/usr/bin/env bash
cd /usr/src/app
uvicorn --host 0.0.0.0 --log-level debug --app-dir .. app.main:app