# quizlet-sets - A library to download Quizlet study sets

### Usage:
Install it useing `pip3 install quizlet-sets`. [WIP, only have example code]

```py
from quizlet_sets import sets

URL = "https://quizlet.com/686459638/test-set-flash-cards/?new" # Sample study set

set = sets.get_terms(URL) # Returns a TermList object

name = "Sample set"

# There are a few different ways to export study sets.
set.txt(name)
set.xls(name)
set.csv(name)
set.anki(name)
```
