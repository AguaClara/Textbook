************************
RST Primer for AguaClara
************************

What is RST?
============
RST stands for restructured text. It is the standard markup language
used for documenting python packages. Sphinx_
is the Python package that can generate an html website from the rst files. To read more
about why we chose RST over markdown or Latex, read the section `Why RST?`_.

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

Setting up RST for Development
==============================
There are two ways to quickly view an RST file. The first is using an Atom plugin
that renders the view alongside the source code. This is a good initial test to
make sure the rst is proper rst and *mostly* looks correct. However, some functionality,
such as any extensions provided by Sphinx_ won't run in the preview. In order to
see the final html that will display on the website, you'll need to run sphinx to fully
generate the html code. Finally, to push the code so it is available on the textbook,
you'll need to incorporate it to the master branch.

Installing the Atom Plugins
---------------------------
If you are using the Atom IDE to write rst, you can use the `rst-preview-pandoc <https://atom.io/packages/rst-preview-pandoc>`__
plugin to auto-generate a live rst preview within atom (much like the markdown-preview-plus preview page.) To get rst-preview
working, you'll need to install `language-restructuredtext <https://atom.io/packages/language-restructuredtext>`_ and Pandoc_. If everything
worked, you can use ctrl-shift-e to toggle a display window for the live-updated
rst preview.

Building RST Locally with Sphinx_
---------------------------------
We use Sphinx_ to build rst locally. Follow these steps to get Sphinx_ and run locally:

#. Install Sphinx_ using pip: :code:`pip install sphinx --user -U`
#. To generate all the html, run the make file with :code:`make html`
#. View the html generated in the _build directory by opening it in your favorite editor.

Publishing Online
-----------------
To publish online, you need to submit a pull request to master and merge it in. Then
Travis will build the site using Sphinx_, and if there aren't any errors, upload
it to the gh_pages branch. We used `this guide <https://gist.github.com/brenns10/f48e1021e8befd2221a2>`_ to set up Travis.

**PUBLISHING NOTE**: If your changes to the master branch aren't pushing to gh-pages,
then check the status of the `Travis build here <https://travis-ci.org/AguaClara/Textbook>`_.


Brief Best Practices
====================
When writing rst, there are often many ways to write the same thing. Almost always,
the way with the fewest number of characters is the best way. Ideally, never copy and paste.

How do I write RST?
-------------------
RST is friendly to learn and powerful. There are many useful `cheatsheets <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#inserting-code-and-literal-blocks>`_.
When you start writing rst, look at the cheat sheets all the time. Use :code:`ctrl-f` all the time to find
whatever you need. Things not covered in the cheat sheets:

* Writing inline code snippet: :code:`:code:'your code'`. Learn how to syntax highlight `here <https://stackoverflow.com/questions/10870719/inline-code-highlighting-in-restructuredtext>`_
* A document is referred to by its title, as defined between the ==== signs at the
  top of the page... NOT the filename. So it is critical to have a title.
* Always run :code:`make html` before pushing to ensure you can make your changes without errors.
* Anything else you'd like to add for the future...

Example to Start From
---------------------
This file is written in rst. You can start there! Just click on "View page source"
at the top of the page.

Also, here's a rich example where we try to implement all AguaClara best
practices: :ref:`example_aguaclara_rst`. I recommend looking
at the raw rst and the rendered html side by side.

Converting Markdown to RST
==========================
Ideally, use pandoc to do the conversion: :code:`pandoc --from=markdown --to=rst --output=my_file.rst my_file.md`.
Raw html will not be converted (because it is not actually markdown), and tables are converted poorly.
You'll need to carefully review any page converted with pandoc.

.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _Pandoc: https://pandoc.org/installing.html
