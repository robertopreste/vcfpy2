======
vcfpy2
======

.. image:: https://www.repostatus.org/badges/latest/wip.svg
    :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
    :target: https://www.repostatus.org/#wip

.. image:: https://travis-ci.com/robertopreste/vcfpy2.svg?branch=master
    :target: https://travis-ci.com/robertopreste/vcfpy2

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/robertopreste


Python 3 VCF library, based on vcfpy_.

This module is only intended to be used by HmtNote_; it is an exact clone of the vcfpy_ module, where a couple of lines of code were changed to better suit my needs.

I found an issue_ in the original vcfpy module and made a related `pull request`_ to fix it. However, it takes some time to accept my changes, while I need them implemented right now for my software to work properly, so I built this parallel module with the edits I need.

As soon as the issue gets fixed in the original module, I will delete this one.


Credits
-------

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template. All credits, however, go to bihealth_ that created the original vcfpy_ package.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
.. _vcfpy: https://github.com/bihealth/vcfpy
.. _HmtNote: https://github.com/robertopreste/HmtNote
.. _issue: https://github.com/bihealth/vcfpy/issues/130
.. _`pull request`: https://github.com/bihealth/vcfpy/pull/131
.. _bihealth: https://github.com/bihealth
