# Netway
Large Network library for python.


## Installation
```bash
pip install netway
```

## Usage

Simple **GET** Request :
```python
import netway 

nw = netway.get("https://google.com/")
print(nw.headers)

# Avaliable GET Modules : 

# .domain
# .url
# .http
# .ip 
# .tld

# .text 
# .headers
# .status_code
```
