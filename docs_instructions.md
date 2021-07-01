## Documentation Creation
```bash
pip install sphinx sphinx-markdown-builder;
```
```bash
sphinx-apidoc -o Sphinx-docs . sphinx-apidoc --full -A 'Saiem Gilani';
cd Sphinx-docs;
```

### Conf.py
```bash
echo "import os
import sys
sys.path.insert(0,os.path.abspath('../'))
def skip(app, what, name, obj,would_skip, options):
    if name in ( '__init__',):
        return False
    return would_skip
def setup(app):
    app.connect('autodoc-skip-member', skip)
" >> conf.py;
```

```bash
make markdown;
```