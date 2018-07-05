.. _example_aguaclara_rst:

***********************************************
Functionality in RST and AguaClara Convention
***********************************************
This file will explain how to use RST functionality including images, tables, code, equations, and both internal and cross-document refereces. Additionally, this document is intended to define convention for this textbook project. Any syntax included in this document should be used when contributing to the textbook project. If you come across a function for which there is no convention, please edit this file to include it here.



.. _how_to_use_this_file:

How to use this file:
======================
Open the source code of the file next to the rendered code. The source code is found by clicking "View page source" at the top of the page. Follow along with the source code and rendered code, using the source code as a reference for the proper syntax.

You will often see this format ``.. word::``. The 'word' in this case is called a directive. Directives are what RST uses to format text. Directives allow the inclusion of figures, math, tables, references, color, and much more.

.. important:: **Proper indentation and line spacing is extremely important when writing in RST**


.. _headings_bullets_and_lists:

Headings, Bullet Points, and Numbered Lists
---------------------------------------------

Headings
^^^^^^^^^
Headings are defined by an underline consisting of one of the following characters: ``*,  =,  -,  ^, and "``. RST does not give any particular character hierarchy over another for defining titles, sections, subsections, or so on. The user indicates character hierarchy for headings and can use whatever order they want, and the order can change between documents. However, it is better to stick to the same convention throughout a project. This is the convention for the AguaClara textbook:

* `*` with overline, for document titles
* `=`, for sections
* `-`, for subsecti ons
* `^`, for subsubsections
* `"`, for subsubsubsections

Each title, section and subsection should have a label before it, formatted like this ``.. _headings:``. There should always be a blank line between the label and the actual heading, else references to the label will not work. For the sake of document readability, include 3 blank lines before the section label and 2 blank lines before the subsection label. Lesser headings (subsubsections and beyond) do not need to have labels, and there should be one blank line between lower headings and the preceeding content. Here is an example. Note the amount and location of blank lines::

  .. _example_document_title:

  ****************
  Document Title
  ****************
  Words go here



  .. _example_section:

  Section
  =========
  Words also go here


  .. _example_subsection:

  Subsection
  ------------
  and here

  Subsubsection
  ^^^^^^^^^^^^^^
  Even more words

Two rules:

* If under and overline are used, their length must be identical
* The length of the underline must be at least as long as the title itself

Lists and Bullets
^^^^^^^^^^^^^^^^^^^
This section is lifted from `this rst cheatsheet <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#inserting-code-and-literal-blocks>`_.
The following code::

    * This is a bulleted list.
    * It has two items, the second
      item uses two lines. (note the indentation)

    1. This is a numbered list.
    2. It has two items too.

    #. This is a numbered list.
    #. It has two items too.

gives:

* This is a bulleted list.
* It has two items, the second
  item uses two lines. (note the indentation)

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

.. note:: if two lists are separated by a blanck line only, then the two lists are not differentiated as you can see above.


.. _figures:

Figures
-------
Every figure should have a label, alternative text, and a caption. The label is used to reference a figure and is written before the figure directive. Below, the two figures are labelled ``fluffy_cat`` and ``mountain_figure``. The alternative text is a very short desciption of the figure. A caption is written below all of the figure specifications, with a blank line to separate the specs from the caption.

Use the following syntax for including figures from online sources::

  .. _fluffy_cat:
  .. figure:: https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg
      :width: 200px
      :align: center
      :height: 100px
      :alt: external figure

      This is a caption.

Use this syntax for figures located within the /Textbook repository on GitHub::

  .. _mountain_figure:
  .. figure:: mountain.jpg
      :width: 300px
      :align: center
      :alt: internal figure

      Here is a figure labeled ``mountain``. Specify the figure location with folder/image.jpg.
      The base directory for figure location is the directory of the file you are writing.
      In this case, that is Textbook/Textbook_Creation_Help.

Displayed below are the two figures generated using the code above.

.. _fluffy_cat:
.. figure:: https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg
    :width: 200px
    :align: center
    :height: 100px
    :alt: external figure

    This is a caption.

.. _mountain_figure:
.. figure:: mountain.jpg
    :width: 300px
    :align: center
    :alt: internal figure

    Here is a figure labeled ``mountain``. Specify the figure location with folder/image.jpg.
    The base directory for figure location is the directory of the file you are writing.
    In this case, that is Textbook/Textbook_Creation_Help.


.. _math_and_equations:

Math and Equations
-------------------
Math is very cool, and works natively in RST using LaTeX math syntax. In-line math can be written with the following syntax: ``:math:`y = ax^2 + bx + c``` which displays :math:`y = ax^2 + bx + c`. To display equations in their own line, use the following syntax::

  .. math::
    :label: quadratic

      y = ax^2 + bx + c

Which displays as:

  .. math::
    :label: quadratic

      y = ax^2 + bx + c

Complex equations can be generated as well, since RST uses LaTeX math.

  .. math::

      n_{\rm{offset}} = \sum_{k=0}^{N-1} \frac{s_k}{n_k} \ln \left( \frac{k}{k!} \right)

When introducing a new equation, Make sure to specify what the parameters in the equation mean. Once the equation has been introduced, its parameters do not need to be explained when displayed in the future. Use the following syntax for introducing equations::

  .. math::
    :label: continuity_equation

      \bar v_1 \frac{\pi D_1^2}{4} = \bar v_2 \frac{\pi D_2^2}{4}

  | Such that:
  | :math:`Q =` fluid flow rate
  | :math:`\bar v =` fluid average velocity
  | :math:`A =` pipe area
  | :math:`r =` pipe radius
  | :math:`D =` pipe diameter

All equations that appear on their own are automatically numbered. If you wish to call an equation in a later section of the document or in another document, give it a label. In the example equation above, the label is given with the ``:label: continuity_equation`` line. The equation below uses the code from the block above.

.. math::
  :label: continuity_equation

    \bar v_1 \frac{\pi D_1^2}{4} = \bar v_2 \frac{\pi D_2^2}{4}

| Such that:
| :math:`Q =` fluid flow rate
| :math:`\bar v =` fluid average velocity
| :math:`A =` pipe area
| :math:`r =` pipe radius
| :math:`D =` pipe diameter


.. _tables:

Tables
------
Tables should be made using csv for compatibility with excel::

  .. _an_example_table:
  .. csv-table:: This table has a title
     :header: "name", "firstname", "age"
     :widths: 20, 20, 10
     :align: center

     "Smith", "John", 40
     "Smith", "John, Junior", 20

The code block above generates the following table:

.. _an_example_table:
.. csv-table:: This table has a title
   :header: "name", "firstname", "age"
   :widths: 20, 20, 10
   :align: center

   "Smith", "John", 40
   "Smith", "John, Junior", 20

Every table should have a label, shown in the example above as ``an_example_table``


.. _links_and_references:

Links and References for Documents, Figures, and Tables
--------------------------------------------------------
Links are fairly straightforward, use the following syntax, ```hyperlink word display <aguaclarareach.org>`_``, and look like this `hyperlink word display <https://www.aguaclarareach.org/>`_. If you will be using the same link many times in a document, you can place this line at the end of the document::

  .. _AguaClara: http://aguaclara.cornell.edu/

Now, the syntax ``AguaClara_`` will link to the specified site: AguaClara_

References work by calling any "target. There are two types of references, internal and external. All types of call-able references can be accessed using their labels.

Internal References
^^^^^^^^^^^^^^^^^^^^^
Internal references link to figures, tables, or headings that are in the same document as the reference itself. They all follow the same syntax. Equations don't appear to be referencable by this syntax.

* Figures: ```fluffy_cat`_`` gives `fluffy_cat`_
* Tables: ```an_example_table`_`` gives `an_example_table`_
* Headings: ```How to use this file:`_`` gives `How to use this file:`_
    * For this heading reference method, make sure that the heading string is identical to the call string.

External References
^^^^^^^^^^^^^^^^^^^^
These are references to documents, equations, figures, tables, or headings in another file in the textbook. Note that clicking these references will take you away from this document, necessarily.

* Documents: ``:ref:`rst_intro``` gives :ref:`rst_intro`
* Equations: ``:eq:`orifice_equation``` only generates a number in parentheses. Thus, this reference should be preceeded by the word: 'equation.' Like this: equation :eq:`orifice_equation`
* Figures: ``:numref:`continuity_pipes``` gives :numref:`continuity_pipes`
* Tables: ``:numref:`dimension_table``` gives :numref:`dimension_table`
* Headings: ``:ref:`what_is_rst``` gives :ref:`what_is_rst`
    * To reference a heading in an external document, you must call the heading's label two lines above the heading itself. For example, if you view the source code for this file, you will see that the heading for this section, **Links and References for Documents, Figures, and Tables** is labelled ``links_and_references``.


.. _writing_code_blocks:

Writing Code Blocks (not actual, executable code)
---------------------------------------------------
You can write code in-line or as a code block. Note that these ways of showing code *only display code*, they do not generate a code block that actually runs. There are two ways of doing each. For in-line code, use ````this syntax```` or ``:code:`this syntax```. For code blocks, use this syntax:

.. code::

  .. code::

    This is my code block.

Or this syntax::

    This two colons at the end of this line indicate that the text below, which is separated by a blank line and indented, is a code block::

      This is my code block.


.. _python_and_doctests:

Writing Python and Including Doctests
-----------------------------------------

Doctests
^^^^^^^^^^^^

When writing code for the textbook, some sections will be written in execuatable code to demonstrate functions or run calculations. They will not, however, run automatically in the webpage, so to ensure that they are correct before they are pubished they are tested with doctests. Doctests compare the written code with the expected result typed manually below it. In the Anaconda Prompt, simply run the :code:`make doctest` in the correct directory and branch. When run, you see where your excutable code doesn't match up with the "answer" provided by you, the contributor. One reason this is important is because if functions in aide_design change, their outputs might alter from old versions. Doctests will show where this happens. Additonally, typos and other mistakes can be seen. Further documentation on running doctest can be found `here <http://docs.sphinxdocs.com/en/latest/step-3.html>`_.

The way to ensure a doctest will run is to precede each line of code with '>>>', the default Python prompt. When a doctest is run, every line of code with '>>>' in front of it will be run within a directory. The testing becomes relevant for lines which do not have '>>>' in front of them. Any line that is directly below a line beginnning with '>>>' is assumed to be an output of the line of code just above it. In the example below, :code:`19` is the expected output of the line :code:`>>> print(5+14)`. If the output of that line did not match the line below, doctests would alert you! Below are some examples of doctestable code.

    >>> python="code"
    >>> print(5+14)
    19

* You can even print and test tables in doctests:

    >>> import pandas as pd
    >>> names_male = pd.Series(['Barack', 'Monroe', 'Jack'])
    >>> names_female = pd.Series(['Michelle', 'Juanita', 'Jill'])
    >>> var_names = dict( female_names = names_female, male_names = names_male)
    >>> df = pd.DataFrame(var_names)
    >>> print(df)
      female_names male_names
    0     Michelle     Barack
    1      Juanita     Monroe
    2         Jill       Jack

* To get doctests to pass through Travis, you'll have to add any packages you use to the install step in ".travis.yml". Under install, add a line that says :code:`pip install my_package==0.0.0`. When doing this, make sure to specify the version as functionality can change!

Though there are other ways to include code in an RST document, this method makes doctesting possible, and will make it easy to change the documents should aide_design functions change, therefore this is the best way to include code! Additionally it makes it easy to see the difference between the code and the output, whereas other methods are less clear in this distinction.


.. _assorted_convention:

Assorted Other Convention
-------------------------
* Colored :red:`text`. Add colors/styles by using roles defined in /conf.py and /_static/css/custom.css.

.. _AguaClara: http://aguaclara.cornell.edu/

  .. disqus::
