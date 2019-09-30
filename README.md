# `pronto` [![starme](https://img.shields.io/github/stars/althonos/pronto.svg?style=social&label=Star)](https://github.com/althonos/pronto)

*A Python frontend to ontologies.*

[![TravisCI](https://img.shields.io/travis/althonos/pronto/master.svg?&maxAge=600&style=flat-square)](https://travis-ci.org/althonos/pronto/branches)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square&maxAge=2678400)](https://choosealicense.com/licenses/mit/)
[![Source](https://img.shields.io/badge/source-GitHub-303030.svg?maxAge=2678400&style=flat-square)](https://github.com/althonos/pronto/)
[![Docs](https://img.shields.io/readthedocs/pronto?style=flat-square&maxAge=3600)](http://pronto.readthedocs.io/en/latest/?badge=latest)
[![Coverage](https://img.shields.io/codecov/c/gh/althonos/pronto?style=flat-square&maxAge=3600)](https://www.codecov.com/gh/althonos/pronto/)
[![Sanity](https://img.shields.io/codacy/grade/157b5fd24e5648ea80580f28399e79a4.svg?style=flat-square&maxAge=3600)](https://codacy.com/app/althonos/pronto)
[![PyPI](https://img.shields.io/pypi/v/pronto.svg?style=flat-square&maxAge=3600)](https://pypi.python.org/pypi/pronto)
[![Bioconda](https://img.shields.io/conda/vn/bioconda/pronto?style=flat-square&maxAge=3600)](https://anaconda.org/bioconda/pronto)
[![Versions](https://img.shields.io/pypi/pyversions/pronto.svg?style=flat-square&maxAge=3600)](https://pypi.org/project/pronto/#files)
[![Wheel](https://img.shields.io/pypi/wheel/pronto?style=flat-square&maxAge=3600)](https://pypi.org/project/pronto/#files)
[![Changelog](https://img.shields.io/badge/keep%20a-changelog-8A0707.svg?maxAge=2678400&style=flat-square)](https://github.com/althonos/pronto/blob/master/CHANGELOG.md)
[![GitHub issues](https://img.shields.io/github/issues/althonos/pronto.svg?style=flat-square&maxAge=600)](https://github.com/althonos/pronto/issues)
[![DOI](https://img.shields.io/badge/doi-10.5281%2Fzenodo.595572-green?style=flat-square&maxAge=3600)](https://doi.org/10.5281/zenodo.595572)

## 🚩 Table of Contents

- [Overview](#-overview)

## 🗺️ Overview

Pronto is a Python library to parse, browse, create, and export
ontologies, supporting several ontology languages and formats. It
implement the specifications of the [Open Biomedical Ontologies 1.4](http://owlcollab.github.io/oboformat/doc/obo-syntax.html)
in the form of an safe high-level interface.

## 🏳️ Supported Languages

- [Open Biomedical Ontologies 1.4](http://owlcollab.github.io/oboformat/doc/GO.format.obo-1_4.html).
  *Because this format is fairly new, not all OBO ontologies can be parsed at the
  moment. See the [OBO Foundry roadmap](https://github.com/orgs/fastobo/projects/2)
  listing the compliant ontologies, and don't hesitate to contact their developers
  to push adoption forward.*
- [OBO Graphs](https://github.com/geneontology/obographs) in [JSON](http://json.org/)
  format. *The format is not yet stabilized to the results may change from file
  to file.*
- [Ontology Web Language 2](https://www.w3.org/TR/owl2-overview/>)
  in [RDF/XML format](https://www.w3.org/TR/2012/REC-owl2-mapping-to-rdf-20121211/).
  *OWL2 ontologies are reverse translated to OBO using the mapping defined in the
  [OBO 1.4 Semantics](http://owlcollab.github.io/oboformat/doc/obo-syntax.html).*

## 🔧 Installing


Installing with `pip` is the easiest:
```console
# pip install pronto          # if you have the admin rights
$ pip install pronto --user   # install it in a user-site directory
```

There is also a `conda` recipe in the `bioconda` channel:
```console
$ conda install -c bioconda pronto
```

Finally, a development version can be installed from GitHub
using `setuptools`, provided you have the right dependencies
installed already:
```console
$ git clone https://github.com/althonos/pronto
$ cd pronto
# python setup.py install
```

## 💡 Examples

If you're only reading ontologies, you'll only use the `Ontology`
class, which is the main entry point.

```python
>>> from pronto import Ontology
```

It can be instantiated from a path to an ontology in one of the supported
formats, even if the file is compressed:
```python
>>> go = Ontology("tests/data/go.obo.gz")
```

Loading a file from a persistent URL is also supported:
```python
>>> cl = Ontology("http://purl.obolibrary.org/obo/cl.obo")
```

### 🏷️ Get a term by accession

`Ontology` objects can be used as mappings to access any entity
they contain from their identifier in compact form:
```python
>>> cl['CL:0002116']
Term('CL:0002116', name='B220-low CD38-positive unswitched memory B cell')
```

<!-- ### Export an ontology in OBO format -->

<!-- ### Get all the subclasses of a term -->

### 🌿 Find ontology terms without subclasses

The `terms` method of `Ontology` instances can be used to
iterate over all the terms in the ontology (including the
ones that are imported). We can then use the `subclasses`
method of `Term` objects that returns an iterator over the
subclasses of

```python
>>> ms = Ontology("ms.obo")
>>> for term in ms.terms():
...     if term.is_leaf():
...         print(term.id)
MS:0000000
MS:1000001
...
```

<!-- ### 🤝 Merging several ontologies -->



## 📖 API Reference

A complete API reference can be found in the [online documentation]


## 📜 License

This library is provided under the open-source
[MIT license](https://choosealicense.com/licenses/mit/).
Please cite this library if you are using it in a scientific
context using the following DOI:
[**10.5281/zenodo.595572**](https://doi.org/10.5281/zenodo.595572)