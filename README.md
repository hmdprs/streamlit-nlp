# Streamlit Sample
*Simple Streamlit App + Deployment on Heroku*

## Local Run

```sh
pipenv install
```

or

```sh
pipenv install --skip-lock streamlit spacy textblob gensim sklearn numpy matplotlib
pipenv run spacy download en_core_web_sm
pipenv lock
```

then

```sh
pipenv run streamlit run app.py
```

## Deployment Required Files

### requirements.txt

```sh
pipenv run pip freeze > requirements.txt
```

### setup.sh

```sh
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

or

```sh
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

### Procfile

```sh
web: sh setup.sh && streamlit run app.py
```

## heroku-cli

ref: https://github.com/heroku/cli/issues/369#issuecomment-396047253

```sh
$ curl https://cli-assets.heroku.com/install.sh | sh
```

```sh
heroku login
heroku create [app-name]
git push heroku master
```
