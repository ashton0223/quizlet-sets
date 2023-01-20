# quizlet-sets - A library to download Quizlet study sets

### Usage:
Install using pip: `pip3 install quizlet-sets`.

### Example:

```py
from quizlet_sets import sets

URL = "https://quizlet.com/686459638/test-set-flash-cards/?new" # Sample study set

set = sets.get_terms(URL) # Returns a TermList object

name = "Sample set"

# There are a few different ways to export study sets.
# The file extension is not added automatically, and should be added to the name.
set.txt(name + '.txt')
set.xls(name + '.xls')
set.csv(name + '.csv')
set.anki(name + '.apkg', "deck name")
```
