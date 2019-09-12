# Encode signed 64bit value using VLQ
## Installation
Just install python of 3rd version.

## vlq Script
### Usage
```bash
python3 vlq.py <int64 number>
```

### Command Line Options
- `-h`, `--help`- show this help message and exit

### How it works
- receives `int64 number` value as required params
- convert input value uses ZigZag encoding
- encode value using VLQ
- convert to Base16-string.

### Examples
```bash
python3 vlq.py 500
```
Output result
```
05e807
```
