#!/bin/sh
VERSION="4"

echo "\nStart..."
git add ./*
git commit -m "$VERSION"
git push --all

echo "\n[^_^]\n"

