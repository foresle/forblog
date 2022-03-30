source ../venv/bin/activate
pelican content -o output -s pelicanconf.py
cp CNAME output/
ghp-import output -b gh-pages -m "Update"
git push origin gh-pages
