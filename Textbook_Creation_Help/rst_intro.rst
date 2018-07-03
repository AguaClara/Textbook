.. _rst_intro:

*********************************************************
Introduction to RST and Sphinx for Textbook Contributors
*********************************************************



.. _what_is_rst:

What is RST?
============

RST stands for ReStructured Text. It is the standard markup language used for documenting python packages. Sphinx_ is the Python package that generates an html website from RST files, and it is what we are using to generate this site. To read more about why we chose RST over markdown or Latex, read the following section, `why_rst`_.


.. _why_rst:

Why RST?
--------
In the beginning, we used markdown. As we tried to add different features to markdown (:red:`colored words`, image sizes, citations), we were forced to use raw html and various pre-processors. With these various band-aid solutions came added complexity. Adding sections became cumbersome and awkward as it required ill-defined html. Additionally, providing site-wide style updates was prohibitively time-consuming and complex. Essentially, we were trying to pack too much functionality into markdown. In the search for an alternative, restructured text provided several advantages. Out of the box, RST supports globally-defined styles, figure numbering and referencing, Latex function rendering, image display customization and more. Furthermore, restructured text was already the language of choice for the AIDE ecosystem's documentation.



.. _setting_up_rst:

Setting up RST for Development
==============================
There are two ways to *quickly* view an RST file. The first is using an Atom_ plugin that renders the view alongside the source code. This is a good initial test to make sure the RST is proper RST and looks *mostly* correct. However, some functionality, such as any extensions provided by Sphinx_ won't run in the preview. In order to see the final html that will display on the website, you'll need to use the second method, running sphinx locally to fully generate the html code. Once you are satisfied with your work and want to push it to the textbook, you'll need to incorporate it to the master branch. To do so, refer to `Publishing online`_.


.. _installing_atom:

Installing the Atom Plugins
---------------------------
If you are using the Atom IDE to write RST, you can use the `rst-preview-pandoc <https://atom.io/packages/rst-preview-pandoc>`_ plugin to auto-generate a live RST preview within atom (much like the markdown-preview-plus preview page.) To get rst-preview working, you'll need to install `language-restructuredtext <https://atom.io/packages/language-restructuredtext>`_ and Pandoc_ (``pip install pandoc``). If everything worked, you can use ``ctrl + shift + e`` to toggle a display window for the live-updated RST preview.


.. _building_rst_locally:

Building RST Locally with Sphinx_
---------------------------------
We use Sphinx_ to build RST locally and remotely. Follow these steps to get Sphinx_ and run it locally:

#. Install Sphinx_ and disqus for sphinx using pip: ``pip install sphinx --user -U`` and ``pip install git+https://github.com/rmk135/sphinxcontrib-disqus``.
#. Generate all the html by navigating in the command line to the source directory /Textbook and creating the build in that directory with the command line :code:`make html`.
#. View the html generated in the /Textbook/_build directory by copying the full file path of /Textbook/_build/html/index.html and pasting it into your browser.

.. note:: Regarding **1.** the master branch for the package implementing disqus in sphinx `is broken <https://github.com/Robpol86/sphinxcontrib-disqus/pull/7>`_, which is why we use a non-standard pip/online installation. If you already have the incorrect sphinx-disqus version installed, uninstall it with ``pip uninstall sphinxcontrib-disqus`` before installing the functioning version.


.. _publishing_online:

Publishing Online
-----------------
We use Travis_ to ensure this site will always contain functional builds. To publish online, you need to:

#. Submit a `pull request to master <https://github.com/AguaClara/Textbook/pulls>`_. You'll need to ask for someone else to review your work at this stage- "request reviewers". Every pull request **must** be reviewed by at least one other person.
#.  Travis_ will build the site using Sphinx_, and if there aren't any errors, Travis will report success to GitHub on the "checks" part of the pull request.
#. All your requested reviewers must now approve and comment on  your commit before the merge is allowed.
#. Once the PR passes Travis and is approved by another author, feel free to "merge to master."
#. To release the master branch, (build the html, pdf, and latex, and upload the pdf to Pages) you'll need to publish a `GitHub release <https://github.com/AguaClara/Textbook/releases/new>`_. Include a `semver <https://semver.org/>`_ version number as the tag (under "Tag: Choose or create"), and a brief description of the updates under "Release Title". Finally, for the description, detail the changes as much as you see fit and when ready, hit "Publish release". Example:
    * Tag name: 0.1.5
    * Release title: Filtration section maintenance
    * Description: Added filter code from aide_design 0.2.6. Also updated all broken external links.
#. Travis will rebuild the site and push the html to Pages, and the PDF and LaTeX to GitHub Releases under the tag name.

.. important:: If your changes to the master branch aren't pushing to gh-pages, then check the status of the `Travis build here <https://travis-ci.org/AguaClara/Textbook>`_.



.. _brief_best_practices:

Brief Best Practices
====================
When writing RST, there are often many ways to write the same thing. Almost always, the way with the fewest number of characters is the best way. Ideally, never copy and paste.


.. _how_do_i_write_rst:

How do I write RST?
-------------------
RST is friendly to learn and powerful. There are many useful cheatsheets, like `this one <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#inserting-code-and-literal-blocks>`_ and the next page on this site: :ref:`example_aguaclara_rst`, which is specifically for AguaClara and this textbook project. When you start writing RST, look at the cheat sheets all the time. Use :code:`ctrl-f` all the time to find whatever you need.

**Things not covered in most cheat sheets which are of critical importance:**

* A document is referred to by its title, as defined between the ``*****`` signs at the top of the page, **NOT** the filename. So it is critical to have a title.
* In addition to a title, every RST document in this book should have a refernce so that it can be linked to in other, external documents. If you view the source code of this document and scroll to the top, you'll see this document is labeled as ``rst_intro`` with the following code ``.. _rst_intro``. Call this document in another textbook RST file with ``:ref:`rst_intro```
* Always run :code:`make html` before pushing to ensure you can make your changes without errors.
* Anything else you'd like to add for the future...


.. _Example_to_start_from:

Example to Start From
---------------------
This file is written in RST. You can start there! Just click on "View page source" at the top of the page.

Also, the next page is specifies convention where we document all AguaClara best practices: :ref:`example_aguaclara_rst`. I recommend looking at the raw RST and the rendered html side by side.



.. _converting_md_to_rst:

Converting Markdown to RST
==========================
Ideally, use pandoc to do the conversion in the command line: :code:`pandoc --from=markdown --to=rst --output=my_file.rst my_file.md`.
Raw html will not be converted (because it is not actually markdown), and tables are converted poorly.
You'll need to carefully review any page converted with pandoc.

.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _Pandoc: https://pandoc.org/installing.html
.. _Atom: https://ide.atom.io/
.. _Travis: https://travis-ci.org/
