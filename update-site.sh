#!/bin/sh

now="$(date): update site: dgyblog.com setup"

git add -A

git commit -m "$now"
git push origin master

jekyll build --destination ../duguyue100.github.io

cd ../duguyue100.github.io/

site_now="$(date): update site: site update"

git add -A

git commit -m "$site_now"

git push origin master
