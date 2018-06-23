========================
RST Primer for AguaClara
========================

What is RST?
------------
RST stands for restructured text. It is the standard markup language
used for documenting python packages. Sphinx_
is the Python package that can generate an html website from the rst files. To read more
about why we chose RST over markdown or Latex, read the section `Why RST?`_.

Setting up RST for Development on Atom
--------------------------------------
If you are using the Atom IDE to write rst, you can use the `rst-preview-pandoc <https://atom.io/packages/rst-preview-pandoc>`__
plugin to auto-generate a live rst preview within atom (much like the markdown-preview-plus preview page.) To get rst-preview
working, you'll need to install `language-restructuredtext <https://atom.io/packages/language-restructuredtext>`_ and Pandoc_. If everything
worked, you can use ctrl-shift-e to toggle a display window for the live-updated
rst preview.

Building RST Locally
--------------------
We use Sphinx_ to build rst locally. To get Sphinx_, run locally, and see the
result, follow these steps:

#. Install Sphinx_ using pip: :code:`pip install sphinx --user -U`
#. To generate all the html, run the make file with :code:`make html`
#. View the html generated in the _build directory by opening it in your favorite editor.

Brief Best Practices
--------------------
When writing rst, there are often many ways to write the same thing. Almost always,
the way with the fewest number of characters is the best way. Ideally, never copy and paste.

How do I write RST?
-------------------
RST is friendly to learn and powerful. There are `many useful cheatsheets<https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#inserting-code-and-literal-blocks>`_.
When you start writing rst, look at the cheat sheets all the time. Use :code:`ctrl-f` all the time to find
whatever you need. Things not covered in the cheat sheets:

* Writing inline code snippet: :code:`:code:'your code'`. Learn how to syntax highlight `here <https://stackoverflow.com/questions/10870719/inline-code-highlighting-in-restructuredtext>`_
* A document is referred to by its title, as defined between the ==== signs at the
  top of the page... NOT the filename. So it is critical to have a title.
* Always run :code:`make html` before pushing to ensure you can make your changes without errors.
* Anything else you'd like to add for the future...

Converting Markdown to RST
--------------------------
Ideally, use pandoc to do the conversion: :code:`pandoc --from=markdown --to=rst --output=my_file.rst my_file.md`.
Raw html will not be converted (because it is not actually markdown).

Example to Start From
---------------------
This file is written in rst. You can start there! Also, there's a rich example
where we try to implement all AguaClara best practices here. I recommend looking
at the raw rst and the rendered html side by side. 

Why RST?
--------
In the beginning, we used markdown. As we tried to add different features to markdown (colored words, image sizes, citations),
we were forced to use raw html and various pre-processors. With these various band-aid
solutions came added complexity. Adding sections became cumbersome and awkward as it required
ill-defined html. Additionally, providing site-wide style updates was prohibitively time-consuming and
complex. Essentially, we were trying to pack too much functionality into markdown.
In the search for an alternative, restructured text provided several advantages.
Out of the box, rst supports globally-defined styles, figure numbering and referencing,
Latex function rendering, image display customization and more. Furthermore,
restructured text was already the language of choice for the AIDE ecosystem's
documentation.

.. _Sphinx: <http://www.sphinx-doc.org/en/master/>
.. _Pandoc: <https://pandoc.org/installing.html>
