# Managing Sales

## Install Python 

Download and install [Python3](https://www.python.org/downloads/). 

## Create a virtual environment 

```
python3 -m venv venv

source venv/bin/activate
```

## Install the requirements

```
pip3 install --upgrade pip

pip3 install -r requirements.txt
```

## Run 

```
python3 main.py rank_sellers_by_item <SALE_ITEM_NAME>

# Ex.: python3 main.py rank_sellers_by_item 'Product 1'
```
