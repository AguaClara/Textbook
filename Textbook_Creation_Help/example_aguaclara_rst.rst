.. _example_aguaclara_rst:

***********************************************
Functionality in RST and AguaClara Convention
***********************************************
This file will explain how to use rst functionality including images, tables, code, equations, and both internal and cross-document refereces. Additionally, this document is intended to define convention for this textbook. Any syntax included in this document should be used when contributing to the textbook project. If you come across a function for which there is no convention, please include it here.



.. _how_to_use_this_file:

How to use this file:
=====================
Open the source code of the file next to the rendered code. The source code is found by clicking "View page source" at the top of the page. Follow along with the source code and rendered code, using the source code as a reference for the proper syntax.

.. important:: **Proper indentation and line spacing is extremely important**

You will often see a format like this ``.. word::``. The 'word' in this case is called a directive. Directives are what rst uses to format text.


.. _code:

Code
----
You can write code in-line or as a code block. There are two ways of doing each. For inline code, use ````this syntax```` or ``:code:`this syntax```. For code blocks, use this syntax:

  .. code::

    .. code::

      This is my code block.

Or this syntax::

  This text is not a code block, the code block is below::

    This is my code block.


.. _headings:

Headings
-----------

In order to write a title, you can either underline it or under and overline it. The following examples are correct titles.::

  ******
  Title
  ******

  subtitle
  =========

  subsubtitle
  ------------
  and so on

Two rules:

* If under and overline are used, their length must be identical
* The length of the underline must be at least as long as the title itself

Normally, there are no heading levels assigned to certain characters as the
structure is determined from the succession of headings. However, it is better to stick to the same convention throughout a project. For instance, this is the convention for the AguaClara textbook:

* `*` with overline, for document titles
* `=`, for sections
* `-`, for subsections
* `^`, for subsubsections
* `"`, for subsubsubsections

Each section and subsection should have a call reference before it, formatted like this::

    .. _headings:

    Headings
    -----------

There should always be a blank line between the call reference and the actual heading, else the reference will not work. For the sake of document readability, include 3 blank lines before the reference to a section and 2 blank lines before the reference to a subsection. All lower headers should not have references, and there should be one blank line between lower headings and the preceeding content.


.. _figures:

Figures
-------
Every figure should have a label, alternative text, and a caption. The label is used to reference a figure and is written before the figure directive. Below, the two figures are labelled ``fluffy_cat`` and ``mountain_figure``. The alternative text is a desciption of the figure with few words. A caption is written below all of the figure specifications, with a blank line to separate the specs from the caption.

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
Math is very cool, and works natively in rst using LaTeX math syntax. In-line math can be written with the following syntax: ``:math:`y = ax^2 + bx + c``` which displays :math:`y = ax^2 + bx + c`. To display equations in their own line, use the following syntax::

  .. math::
     :label: quadratic

        y = ax^2 + bx + c

Which displays as:

  .. math::
     :label: quadratic

        y = ax^2 + bx + c

Complex equations can be generated as well, since rst uses LaTeX math.

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

All equations that appear on their own are automatically numbered. If you wish to call an equation in a later section of the document or in another document, give it a label. In the example equation above, the label is given with the ``:label: continuity_equation`` line. The equation below uses the code from the block above except for this label, since this equation is too minor to be referenced later on.

  .. math::

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
  .. csv-table:: a title
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

Every table should have a reference, shown above as ``an_example_table``


.. _links_and_references:

Links and References for Documents, Figures, and Tables
--------------------------------------------------------
Links are fairly straightforward, use the following syntax, ```hyperlink word display <aguaclarareach.org>`_``, and look like this `hyperlink word display <https://www.aguaclarareach.org/>`_. References work by referencing any "target." If you will be using the same link many times in a document, you can place this line at the end of the document::

  .. _AguaClara Reach: aguaclarareach.org

Now, the syntax ``AguaClara_`` will link to the specified site: AguaClara_

There are two types of references, internal and external.

Internal References
^^^^^^^^^^^^^^^^^^^^^
Internal references link to figures, tables, or headers that are in the same document as the reference itself. All types of call-able references can be accessed using their labels, and they all follow the same syntax. Equations don't appear to be referencable by this syntax.

* Figures: ```fluffy_cat`_`` gives `fluffy_cat`_
* Tables: ```an_example_table`_`` gives `an_example_table`_
* Headers: ```How to use this file:`_`` gives `How to use this file:`_
  * For this header reference, make sure that the header title is identical to the string of the link used in the reference call.

External References
^^^^^^^^^^^^^^^^^^^^
These are references to documents, equations, figures, tables, or headers in another file in the textbook. Note that clicking these references will take you away from this document, necessarily.

* Documents: ``:ref:`rst_intro``` gives :ref:`rst_intro`
* Equations: ``:eq:`orifice_equation``` only generates a number in parentheses. Thus, this reference should be preceeded by the word: 'equation.' Like this: equation :eq:`orifice_equation`
* Figures: ``:numref:`continuity_pipes``` gives :numref:`continuity_pipes`
* Tables: ``:numref:`dimension_table``` gives :numref:`dimension_table`
* Headers: ``:ref:`what_is_rst``` gives :ref:`what_is_rst`
  * This method of referencing headers uses a different call than the internal reference. To reference a header in an external document, you must call the reference directly before the header itself. For example, if you view the source code for this file, you will see that the header for this section, **Links and References for Documents, Figures, and Tables** is referenced by ``links_and_references``.

This can be a figure :numref:`mountain_figure`, equation :eq:`quadratic`, or table :numref:`an_example_table`.


.. _python_and_doctests:

Python and Doctests
--------------------
* Test some python code with doctests. To test the code, run :code:`make doctest` as described `here <http://docs.sphinxdocs.com/en/latest/step-3.html>`_. In the linked document, there are many more options for controlling doctest behavior.

    >>> python="code"
    >>> print(5+14)
    19

* You can even print and test tables in doctests:

    >>> import pandas as pd
    >>> names_male = pd.Series(['Obama', 'Monroe', 'Jack'])
    >>> names_female = pd.Series(['Michelle', 'Juanita', 'Jill'])
    >>> var_names = dict( female_names = names_female, male_names = names_male)
    >>> df = pd.DataFrame(var_names)
    >>> print(df)
      female_names male_names
    0     Michelle      Obama
    1      Juanita     Monroe
    2         Jill       Jack

* To get doctests to pass through Travis, you'll have to add any packages you use to the install step in ".travis.yml". Under install, add a line that says :code:`pip install my_package==0.0.0`. When doing this, make sure to specify the version as functionality can change!

.. _assorted_convention:

Assorted Other Convention
-------------------------
* Colored :red:`text`. Add colors/styles by using roles defined in /conf.py and /_static/css/custom.css.

.. _AguaClara: http://aguaclara.cornell.edu/

  .. disqus::
